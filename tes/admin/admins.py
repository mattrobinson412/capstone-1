from flask import Blueprint, request, render_template, flash, session, g, redirect
from sqlalchemy.exc import IntegrityError
import requests
import sys
sys.path.append("C:/Users/12392/Desktop/.vscode/Springboard/Projects/capstones/capstone-1/tes")
from models import *
from secret import *
from .forms import *
import app

admin = Blueprint('admin', __name__, template_folder='templates', static_folder='static')



CURR_USER_KEY = "curr_user"


##################### @admin.before_request functions ############################
# NEED TO DO! ==========================>




# Admin login/logout ROUTES =====================================> NEED TO DO! #######
@admin.route("/login", methods=["GET", "POST"])
def handle_admin_login():
    """Handle login function for an admin user."""

    form = LoginForm()

    if form.validate_on_submit():
        user = User.authenticate(form.email.data,
                                    form.password.data)

        if user:
            # IMPLEMENT authentication! ##############
    
            ##########################################
            flash(f"Hello, {user.first_name}!", "success")
            return redirect("/admin/home")

        flash("Invalid credentials. Please try again.", 'danger')
        
    return render_template('/admin/login.html', form=form)


# @admin.route('/logout')
# def handle_admin_logout():
#     """Handle logout of user."""

#     # PLEASE IMPLEMENT THIS! ===========>
#     session.pop(CURR_USER_KEY)
#     flash("Successful logout! Come back soon!", 'success')
#     return redirect("/home/login")


#################################################################################
# Admin general routes:

@admin.route('/home')
def show_admin_home():
    """Show dashboard for Admin user."""

    # IMPLEMENT authentication! ##############
    
    ##########################################

    return render_template("/admin/home.html")


@admin.route('/add')
def admin_add_options():
    """Allow Admin user to choose to create a new 'Resource' or 'Class' instance."""

    # IMPLEMENT authentication!!! ######################

    ####################################################

    return render_template("admin/add.html")


@admin.route('/contact')
def admin_handle_inquiries():
    """Allow Admin user to see and handle contact forms from the homepage."""

    contacts = Contact.query.all()
    
    return render_template("admin/contact.html", contacts=contacts)


#################################################################################
# Admin 'add/' routes:

@admin.route("/add/class", methods=["GET", "POST"])
def admin_add_class():
    """Allow Admin user to create a new 'Class' instance."""

    # IMPLEMENT authentication!!! ######################

    ####################################################
    form = CreateClassForm()

    if form.validate_on_submit():
        name = form.name.data
        date = form.date.data
        staff_id = form.staff_id.data

        course = Class(name=name, date=date, staff_id=staff_id)
        db.session.add(course)
        db.session.commit()
        return redirect(f"/admin/edit/classes/{course.id}")

    else:
        flash("Sorry! Something went wrong with your addition. Please try again.")
        return render_template("admin/addclass.html", form=form)
    

@admin.route("/add/resource", methods=["GET", "POST"])
def admin_add_resource():
    """Allow Admin user to create a new 'Resource' instance."""

    # IMPLEMENT authentication!!! ######################

    ####################################################
    form = CreateResourceForm()

    if form.validate_on_submit():
        title = form.title.data
        link = form.link.data
        category = form.category.data
        staff_id = form.staff_id.data

        res = Resource(title=title, link=link, category=category, staff_id=staff_id)
        db.session.add(res)
        db.session.commit()
        return redirect(f"/admin/edit/resources")

    else:
        flash("Sorry! Something went wrong with your addition. Please try again.")
        return render_template("admin/addresource.html", form=form)
    

@admin.route("/add/classes/<int:class_id>/syllabus", methods=["GET", "POST"])
def admin_add_class_syllabus(class_id):
    """Allow Admin user to add a new syllabus to a specific class."""

    course = Class.query.get_or_404(class_id)
    form = AddSyllabusForm()

    if form.validate_on_submit():
        class_id = form.class_id.data
        name = form.name.data
        link = form.link.data

        syl = Syllabus(class_id=class_id, name=name, link=link)
        db.session.add(syl)
        db.session.commit()
        return redirect(f"/admin/edit/classes/{course.id}")

    else:
        flash("Sorry! Something went wrong with your addition. Please try again.")
        return render_template("admin/add-syllabus.html", form=form, course=course)


@admin.route("/add/classes/<int:class_id>/document", methods=["GET", "POST"])
def admin_add_class_doc(class_id):
    """Allow Admin user to add a new document to a specific class."""

    course = Class.query.get_or_404(class_id)
    form = AddDocumentForm()

    if form.validate_on_submit():
        class_id = form.class_id.data
        name = form.name.data
        link = form.link.data

        doc = Document(class_id=class_id, name=name, link=link)
        db.session.add(doc)
        db.session.commit()
        return redirect(f"/admin/edit/classes/{course.id}")

    else:
        flash("Sorry! Something went wrong with your addition. Please try again.")
        return render_template("admin/add-document.html", form=form, course=course)


# Add info for '/add/' lectures!!! Good luck :). ##############################
@admin.route("/add/classes/<int:class_id>/lecture", methods=["GET", "POST"])
def admin_add_class_lecture(class_id):
    """Allow Admin user to add a new lecture to a specific class."""

    form = AddLectureForm()
    course = Class.query.get_or_404(class_id)
    if form.validate_on_submit():
        class_id = form.class_id.data
        name = form.name.data
        link = form.link.data
        date = form.date.data
        staff_id = form.staff_id.data
        
        #    Vimeo API interaction! ===============>
        # v = vimeo.VimeoClient(
        #         token=f"{access_token}",
        #         key=f"{client_id}",
        #         secret=f"{client_secret}"
        #         )
        # vimeo_uri = v.upload(link, 
        #                 data={'name': name, 'description': date})



        doc = Lecture(class_id=class_id, name=name, link=link, date=date, staff_id=staff_id)
        db.session.add(doc)
        db.session.commit()
        return redirect(f"/admin/edit/classes/{course.id}")

    else:
        flash("Sorry! Something went wrong with your addition. Please try again.")
        return render_template("admin/add-lecture.html", form=form, course=course)



#################################################################################
# Admin 'edit/' routes:

@admin.route("/edit")
def admin_edit_options():
    """Allow Admin user to choose to create a new 'Resource' or 'Class' instance."""

    return render_template("admin/edit.html")


@admin.route("/edit/classes")
def admin_edit_classes():
    """Allow Admin user to choose a 'Class' instance to edit."""

    classes = Class.query.all()

    return render_template("/admin/edit-class-list.html", classes=classes)


@admin.route("/edit/resources")
def admin_edit_resources():
    """Allow Admin user to choose a 'Resource' instance to edit."""

    resources = Resource.query.all()
    return render_template("/admin/edit-resource-list.html", resources=resources)


@admin.route("/edit/classes/<int:class_id>")
def admin_edit_class(class_id):
    """Allow Admin user to edit everything pertaining to a 'Class' instance."""

    course = Class.query.get_or_404(class_id)
    lectures = Lecture.query.filter_by(class_id=class_id)
    syllabi = Syllabus.query.filter_by(class_id=class_id)
    docs = Document.query.filter_by(class_id=class_id)
    
    return render_template("/admin/edit-class.html", course=course, lectures=lectures, syllabi=syllabi, docs=docs)
    
    
@admin.route("/edit/classes/<int:class_id>/info", methods=["GET", "POST"])
def admin_edit_class_info(class_id):
    """Allows Admin user to edit a classes' general info."""

    course = Class.query.get_or_404(class_id)
    form = EditClassForm(obj=course)

    if form.validate_on_submit():
            name = form.name.data
            date = form.date.data
            staff_id = form.staff_id.data

            course.name = name
            course.date = date
            course.staff_id = staff_id
            db.session.commit()
            return redirect(f"/admin/edit/classes/{class_id}")

    else:
        flash("Sorry! Something went wrong with your edits. Please try again.")
        return render_template("/admin/edit-class-info.html", form=form, course=course)


@admin.route("/edit/classes/<int:class_id>/syllabi/<int:syllabus_id>", methods=["GET", "POST"])
def admin_edit_class_syllabus(class_id, syllabus_id):
    """Allow Admin user to edit a class syllabus."""

    course = Class.query.get_or_404(class_id)
    syl = Syllabus.query.get_or_404(syllabus_id)
    form = EditSyllabusForm(obj=syl)

    if form.validate_on_submit():
            class_id = form.class_id.data
            name = form.name.data
            link = form.link.data

            syl.class_id = class_id
            syl.name = name
            syl.link = link
            db.session.commit()
            return redirect(f"/admin/edit/classes/{class_id}")

    else:
        flash("Sorry! Something went wrong with your edits. Please try again.")
        return render_template("/admin/edit-syl.html", form=form, course=course)


@admin.route("/edit/classes/<int:class_id>/documents/<int:doc_id>", methods=["GET", "POST"])
def admin_edit_class_doc(class_id, doc_id):
    """Allow Admin user to edit a class document."""

    course = Class.query.get_or_404(class_id)
    doc = Document.query.get_or_404(doc_id)
    form = EditDocumentForm(obj=doc)

    if form.validate_on_submit():
            class_id = form.class_id.data
            name = form.name.data
            link = form.link.data

            doc.class_id = class_id
            doc.name = name
            doc.link = link
            db.session.commit()
            return redirect(f"/admin/edit/classes/{class_id}")

    else:
        flash("Sorry! Something went wrong with your edits. Please try again.")
        return render_template("/admin/edit-doc.html", form=form, course=course)




@admin.route("/edit/resources/<int:resource_id>", methods=["GET", "POST"])
def admin_edit_resource(resource_id):
    """Allows Admin user to edit the info of a 'Resource' instance."""

    res = Resource.query.get_or_404(resource_id)
    form = EditResourceForm(obj=res)

    if form.validate_on_submit():
            title = form.title.data
            link = form.link.data
            category = form.category.data
            staff_id = form.staff_id.data

            res.title = title
            res.link = link
            res.category = category
            res.staff_id = staff_id
            db.session.commit()
            return redirect(f"/admin/edit/resources")

    else:
        flash("Sorry! Something went wrong with your edits. Please try again.")
        return render_template("/admin/edit-res-info.html", form=form, res=res)
