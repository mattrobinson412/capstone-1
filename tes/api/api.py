"""External API calls for TES catalog application."""

from flask import Blueprint, request, jsonify, g
import requests
import sys
sys.path.append("C:/Users/12392/Desktop/.vscode/Springboard/Projects/capstones/capstone-1/tes")
from ..models import *

api = Blueprint('api', __name__)


# REST routes for USERS ======================================================>
@api.route('/users')
def get_users():
    """Returns JSON w/ all users."""

    # TO-DO: Restrict access to '/api' routes!

    #  =====================================>
    users = [user.serialize() for user in User.query.all()]
    return jsonify(users=users)


@api.route('/users/<int:id>')
def get_user(id):
    """Returns JSON for one particular user."""

     # TO-DO: Restrict access to '/api' routes!

    #  =====================================>

    user = User.query.get_or_404(id)
    return jsonify(user=user.serialize())


@api.route('/users', methods=['POST'])
def create_user():
    """Creates a new user and returns JSON of that created user."""

     # TO-DO: Restrict access to '/api' routes!

    #  =====================================>

    new_user = User(first_name=request.json["first_name"],
                    last_name=request.json["last_name"],
                    password=request.json["password"],
                    phone_number=request.json["phone_number"],
                    email=request.json["email"],
                    status_id=request.json["status_id"])
    db.session.add(new_user)
    db.session.commit()
    response_json = jsonify(user=new_user.serialize())
    return (response_json, 201)


@api.route('/users/<int:id>', methods=["PATCH"])
def update_user(id):
    """Updates a particular user and responds w/ JSON of that user."""

     # TO-DO: Restrict access to '/api' routes!

    #  =====================================>

    user = User.query.get_or_404(id)
    user.first_name = request.json.get('first_name', user.first_name)
    user.last_name = request.json.get('last_name', user.last_name)
    user.password = request.json.get('password', user.password)
    user.phone_number = request.json.get('phone_number', user.phone_number)
    user.email = request.json.get('email', user.email)
    user.status_id = request.json.get('status_id', user.status_id)
    db.session.commit()
    return jsonify(user=user.serialize())


@api.route('/users/<int:id>', methods=["DELETE"])
def delete_user(id):
    """Deletes a particular user."""

     # TO-DO: Restrict access to '/api' routes!

    #  =====================================>

    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify(message="Deleted!")


# REST routes for STATUSES ======================================================>
@api.route('/statuses')
def get_statuses():
    """Returns JSON w/ all statuses."""

    # TO-DO: Restrict access to '/api' routes!

    #  =====================================>
    statuses = [status.serialize() for status in Status.query.all()]
    return jsonify(statuses=statuses)


@api.route('/statuses/<int:id>')
def get_status(id):
    """Returns JSON for one particular status."""

     # TO-DO: Restrict access to '/api' routes!

    #  =====================================>

    status = Status.query.get_or_404(id)
    return jsonify(status=status.serialize())


@api.route('/statuses', methods=['POST'])
def create_status():
    """Creates a new status and returns JSON of that created status."""

     # TO-DO: Restrict access to '/api' routes!

    #  =====================================>

    new_status = Status(status=request.json["status"])
    db.session.add(new_status)
    db.session.commit()
    response_json = jsonify(status=new_status.serialize())
    return (response_json, 201)


@api.route('/statuses/<int:id>', methods=["PATCH"])
def update_status(id):
    """Updates a particular status and responds w/ JSON of that status."""

     # TO-DO: Restrict access to '/api' routes!

    #  =====================================>

    status = Status.query.get_or_404(id)
    status.status = request.json.get('status', status.status)
    db.session.commit()
    return jsonify(status=status.serialize())


@api.route('/statuses/<int:id>', methods=["DELETE"])
def delete_status(id):
    """Deletes a particular status."""

     # TO-DO: Restrict access to '/api' routes!

    #  =====================================>

    status = Status.query.get_or_404(id)
    db.session.delete(status)
    db.session.commit()
    return jsonify(message="Deleted!")


# REST routes for DONATIONS ======================================================>
@api.route('/donations')
def get_donations():
    """Returns JSON w/ all donations."""

    # TO-DO: Restrict access to '/api' routes!

    #  =====================================>
    donations = [donation.serialize() for donation in Donation.query.all()]
    return jsonify(donations=donations)


@api.route('/donations/<int:id>')
def get_donation(id):
    """Returns JSON for one particular donation."""

     # TO-DO: Restrict access to '/api' routes!

    #  =====================================>

    donation = Donation.query.get_or_404(id)
    return jsonify(donation=donation.serialize())


@api.route('/donations', methods=['POST'])
def create_donation():
    """Creates a new donation and returns JSON of that created donation."""

     # TO-DO: Restrict access to '/api' routes!

    #  =====================================>

    donation = Donation(user_id=request.json["user_id"],
                    first_name=request.json["first_name"],
                    last_name=request.json["last_name"],
                    date=request.json["date"],
                    amount=request.json["amount"],
                    payment_type=request.json["payment_type"])
    db.session.add(donation)
    db.session.commit()
    response_json = jsonify(donation=donation.serialize())
    return (response_json, 201)


@api.route('/donations/<int:id>', methods=["PATCH"])
def update_donation(id):
    """Updates a particular donation and responds w/ JSON of that donation."""

     # TO-DO: Restrict access to '/api' routes!

    #  =====================================>

    donation = Donation.query.get_or_404(id)
    donation.user_id = request.json.get('user_id', donation.user_id)
    donation.first_name = request.json.get('first_name', donation.first_name)
    donation.last_name = request.json.get('last_name', donation.last_name)
    donation.date = request.json.get('date', donation.date)
    donation.amount = request.json.get('amount', donation.amount)
    donation.payment_type = request.json.get('payment_type', donation.payment_type)
    db.session.commit()
    return jsonify(donation=donation.serialize())


@api.route('/donations/<int:id>', methods=["DELETE"])
def delete_donation(id):
    """Deletes a particular donation."""

     # TO-DO: Restrict access to '/api' routes!

    #  =====================================>

    donation = Donation.query.get_or_404(id)
    db.session.delete(donation)
    db.session.commit()
    return jsonify(message="Deleted!")


# REST routes for LECTURES ======================================================>
@api.route('/lectures')
def get_lectures():
    """Returns JSON w/ all lectures."""

    # TO-DO: Restrict access to '/api' routes!

    #  =====================================>
    lectures = [lecture.serialize() for lecture in Lecture.query.all()]
    return jsonify(lectures=lectures)


@api.route('/lectures/<int:id>')
def get_lecture(id):
    """Returns JSON for one particular lecture."""

     # TO-DO: Restrict access to '/api' routes!

    #  =====================================>

    lecture = Lecture.query.get_or_404(id)
    return jsonify(lecture=lecture.serialize())


@api.route('/lectures', methods=['POST'])
def create_lecture():
    """Creates a new lecture and returns JSON of that created lecture."""

     # TO-DO: Restrict access to '/api' routes!

    #  =====================================>

    new_lecture = Lecture(class_id=request.json["class_id"],
                    name=request.json["name"],
                    link=request.json["link"],
                    date=request.json["date"],
                    staff_id=request.json["staff_id"])
    db.session.add(new_lecture)
    db.session.commit()
    response_json = jsonify(lecture=new_lecture.serialize())
    return (response_json, 201)


@api.route('/lectures/<int:id>', methods=["PATCH"])
def update_lecture(id):
    """Updates a particular lecture and responds w/ JSON of that lecture."""

     # TO-DO: Restrict access to '/api' routes!

    #  =====================================>

    lecture = Lecture.query.get_or_404(id)
    lecture.class_id = request.json.get('class_id', lecture.class_id)
    lecture.name = request.json.get('name', lecture.name)
    lecture.link = request.json.get('link', lecture.link)
    lecture.date = request.json.get('date', lecture.date)
    lecture.staff_id = request.json.get('staff_id', lecture.staff_id)
    db.session.commit()
    return jsonify(lecture=lecture.serialize())


@api.route('/lectures/<int:id>', methods=["DELETE"])
def delete_lecture(id):
    """Deletes a particular lecture."""

     # TO-DO: Restrict access to '/api' routes!

    #  =====================================>

    lecture = Lecture.query.get_or_404(id)
    db.session.delete(lecture)
    db.session.commit()
    return jsonify(message="Deleted!")


# REST routes for SYLLABI ======================================================>
@api.route('/syllabi')
def get_syllabi():
    """Returns JSON w/ all syllabi."""

    # TO-DO: Restrict access to '/api' routes!

    #  =====================================>
    syllabi = [syllabus.serialize() for syllabus in Syllabus.query.all()]
    return jsonify(syllabi=syllabi)


@api.route('/syllabi/<int:id>')
def get_syllabus(id):
    """Returns JSON for one particular syllabus."""

     # TO-DO: Restrict access to '/api' routes!

    #  =====================================>

    syllabus = Syllabus.query.get_or_404(id)
    return jsonify(syllabus=syllabus.serialize())


@api.route('/syllabi', methods=['POST'])
def create_syllabus():
    """Creates a new syllabus and returns JSON of that created syllabus."""

     # TO-DO: Restrict access to '/api' routes!

    #  =====================================>

    new_syllabus = Syllabus(class_id=request.json["class_id"],
                    name=request.json["name"],
                    link=request.json["link"])
    db.session.add(new_syllabus)
    db.session.commit()
    response_json = jsonify(syllabus=new_syllabus.serialize())
    return (response_json, 201)


@api.route('/syllabi/<int:id>', methods=["PATCH"])
def update_syllabus(id):
    """Updates a particular syllabus and responds w/ JSON of that syllabus."""

     # TO-DO: Restrict access to '/api' routes!

    #  =====================================>

    syllabus = Syllabus.query.get_or_404(id)
    syllabus.class_id = request.json.get('class_id', syllabus.class_id)
    syllabus.name = request.json.get('name', syllabus.name)
    syllabus.link = request.json.get('link', syllabus.link)
    db.session.commit()
    return jsonify(syllabus=syllabus.serialize())


@api.route('/syllabi/<int:id>', methods=["DELETE"])
def delete_syllabus(id):
    """Deletes a particular syllabus."""

     # TO-DO: Restrict access to '/api' routes!

    #  =====================================>

    syllabus = Syllabus.query.get_or_404(id)
    db.session.delete(syllabus)
    db.session.commit()
    return jsonify(message="Deleted!")


# REST routes for DOCUMENTS ======================================================>
@api.route('/documents')
def get_documents():
    """Returns JSON w/ all documents."""

    # TO-DO: Restrict access to '/api' routes!

    #  =====================================>
    documents = [document.serialize() for document in Document.query.all()]
    return jsonify(documents=documents)


@api.route('/documents/<int:id>')
def get_document(id):
    """Returns JSON for one particular document."""

     # TO-DO: Restrict access to '/api' routes!

    #  =====================================>

    document = Document.query.get_or_404(id)
    return jsonify(document=document.serialize())


@api.route('/documents', methods=['POST'])
def create_document():
    """Creates a new document and returns JSON of that created document."""

     # TO-DO: Restrict access to '/api' routes!

    #  =====================================>

    new_document = Document(class_id=request.json["class_id"],
                    name=request.json["name"],
                    link=request.json["link"])
    db.session.add(new_document)
    db.session.commit()
    response_json = jsonify(document=new_document.serialize())
    return (response_json, 201)


@api.route('/documents/<int:id>', methods=["PATCH"])
def update_document(id):
    """Updates a particular document and responds w/ JSON of that document."""

     # TO-DO: Restrict access to '/api' routes!

    #  =====================================>

    document = Document.query.get_or_404(id)
    document.class_id = request.json.get('class_id', document.class_id)
    document.name = request.json.get('location', document.name)
    document.link = request.json.get('link', document.link)
    db.session.commit()
    return jsonify(document=document.serialize())


@api.route('/documents/<int:id>', methods=["DELETE"])
def delete_document(id):
    """Deletes a particular document."""

     # TO-DO: Restrict access to '/api' routes!

    #  =====================================>

    document = Document.query.get_or_404(id)
    db.session.delete(document)
    db.session.commit()
    return jsonify(message="Deleted!")


# REST routes for GRADUATES ======================================================>
@api.route('/graduates')
def get_graduates():
    """Returns JSON w/ all graduates."""

    # TO-DO: Restrict access to '/api' routes!

    #  =====================================>
    graduates = [graduate.serialize() for graduate in Graduate.query.all()]
    return jsonify(graduates=graduates)


@api.route('/graduates/<int:id>')
def get_graduate(id):
    """Returns JSON for one particular graduate."""

     # TO-DO: Restrict access to '/api' routes!

    #  =====================================>

    graduate = Graduate.query.get_or_404(id)
    return jsonify(graduate=graduate.serialize())


@api.route('/graduates', methods=['POST'])
def create_graduate():
    """Creates a new graduate and returns JSON of that created graduate."""

     # TO-DO: Restrict access to '/api' routes!

    #  =====================================>

    new_graduate = Graduate(first_name=request.json["first_name"],
                    last_name=request.json["last_name"],
                    grad_year=request.json["grad_year"],
                    church_id=request.json["church_id"],
                    role=request.json["role"])
    db.session.add(new_graduate)
    db.session.commit()
    response_json = jsonify(graduate=new_graduate.serialize())
    return (response_json, 201)


@api.route('/graduates/<int:id>', methods=["PATCH"])
def update_graduate(id):
    """Updates a particular graduate and responds w/ JSON of that graduate."""

     # TO-DO: Restrict access to '/api' routes!

    #  =====================================>

    graduate = Graduate.query.get_or_404(id)
    graduate.first_name = request.json.get('first_name', graduate.first_name)
    graduate.last_name = request.json.get('last_name', graduate.last_name)
    graduate.grad_year = request.json.get('grad_year', graduate.grad_year)
    graduate.church_id = request.json.get('church_id', graduate.church_id)
    graduate.role = request.json.get('role', graduate.role)
    db.session.commit()
    return jsonify(graduate=graduate.serialize())


@api.route('/graduates/<int:id>', methods=["DELETE"])
def delete_graduate(id):
    """Deletes a particular graduate."""

     # TO-DO: Restrict access to '/api' routes!

    #  =====================================>

    graduate = Graduate.query.get_or_404(id)
    db.session.delete(graduate)
    db.session.commit()
    return jsonify(message="Deleted!")


# REST routes for STAFF ======================================================>
@api.route('/staff')
def get_staff():
    """Returns JSON w/ all staff."""

    # TO-DO: Restrict access to '/api' routes!

    #  =====================================>
    staff = [member.serialize() for member in Staff.query.all()]
    return jsonify(staff=staff)


@api.route('/staff/<int:id>')
def get_staff_member(id):
    """Returns JSON for one particular staff member."""

     # TO-DO: Restrict access to '/api' routes!

    #  =====================================>

    staff_memeber = Staff.query.get_or_404(id)
    return jsonify(staff_member=staff_member.serialize())


@api.route('/staff', methods=['POST'])
def create_staff_member():
    """Creates a new staff_member and returns JSON of that created staff_member."""

     # TO-DO: Restrict access to '/api' routes!

    #  =====================================>

    new_staff_member = Staff(first_name=request.json["first_name"],
                    last_name=request.json["last_name"],
                    join_date=request.json["join_date"],
                    church_id=request.json["church_id"],
                    role=request.json["role"])
    db.session.add(new_staff_member)
    db.session.commit()
    response_json = jsonify(staff_member=new_staff_member.serialize())
    return (response_json, 201)


@api.route('/staff/<int:id>', methods=["PATCH"])
def update_staff_member(id):
    """Updates a particular staff_member and responds w/ JSON of that staff_member."""

     # TO-DO: Restrict access to '/api' routes!

    #  =====================================>

    staff_member = Staff.query.get_or_404(id)
    staff_member.first_name = request.json.get('first_name', staff_member.first_name)
    staff_member.last_name = request.json.get('last_name', staff_member.last_name)
    staff_member.join_date = request.json.get('join_date', staff_member.join_date)
    staff_member.church_id = request.json.get('church_id', staff_member.church_id)
    staff_member.role = request.json.get('role', staff_member.role)
    db.session.commit()
    return jsonify(staff_member=staff_member.serialize())


@api.route('/staff/<int:id>', methods=["DELETE"])
def delete_staff_member(id):
    """Deletes a particular staff member."""

     # TO-DO: Restrict access to '/api' routes!

    #  =====================================>

    staff_member = Staff.query.get_or_404(id)
    db.session.delete(staff_member)
    db.session.commit()
    return jsonify(message="Deleted!")


# REST routes for CLASSES ======================================================>
@api.route('/classes')
def get_classes():
    """Returns JSON w/ all classes."""

    # TO-DO: Restrict access to '/api' routes!

    #  =====================================>
    classes = [course.serialize() for course in Class.query.all()]
    return jsonify(classes=classes)


@api.route('/classes/<int:id>')
def get_class(id):
    """Returns JSON for one particular class."""

     # TO-DO: Restrict access to '/api' routes!

    #  =====================================>

    course = Class.query.get_or_404(id)
    return jsonify(course=course.serialize())


@api.route('/classes', methods=['POST'])
def create_class():
    """Creates a new class and returns JSON of that created class."""

     # TO-DO: Restrict access to '/api' routes!

    #  =====================================>

    new_class = Class(name=request.json["name"],
                    date=request.json["date"],
                    staff_id=request.json["staff_id"])
    db.session.add(new_class)
    db.session.commit()
    response_json = jsonify(course=new_class.serialize())
    return (response_json, 201)


@api.route('/classes/<int:id>', methods=["PATCH"])
def update_class(id):
    """Updates a particular class and responds w/ JSON of that class."""

     # TO-DO: Restrict access to '/api' routes!

    #  =====================================>

    course = Class.query.get_or_404(id)
    course.name = request.json.get('name', course.name)
    course.date = request.json.get('date', course.date)
    course.staff_id = request.json.get('staff_id', course.staff_id)
    db.session.commit()
    return jsonify(course=course.serialize())


@api.route('/classes/<int:id>', methods=["DELETE"])
def delete_class(id):
    """Deletes a particular class."""

     # TO-DO: Restrict access to '/api' routes!

    #  =====================================>

    course = Class.query.get_or_404(id)
    db.session.delete(course)
    db.session.commit()
    return jsonify(message="Deleted!")


# REST routes for CHURCHES ======================================================>
@api.route('/churches')
def get_churches():
    """Returns JSON w/ all churches."""

    # TO-DO: Restrict access to '/api' routes!

    #  =====================================>
    churches = [church.serialize() for church in Church.query.all()]
    return jsonify(churches=churches)


@api.route('/churches/<int:id>')
def get_church(id):
    """Returns JSON for one particular church."""

     # TO-DO: Restrict access to '/api' routes!

    #  =====================================>

    church = Church.query.get_or_404(id)
    return jsonify(church=church.serialize())


@api.route('/churches', methods=['POST'])
def create_church():
    """Creates a new church and returns JSON of that created church."""

     # TO-DO: Restrict access to '/api' routes!

    #  =====================================>

    new_church = Church(name=request.json["name"],
                    location=request.json["location"],
                    phone_number=request.json["phone_number"],
                    email=request.json["email"],
                    website=request.json["website"])
    db.session.add(new_church)
    db.session.commit()
    response_json = jsonify(church=new_church.serialize())
    return (response_json, 201)


@api.route('/churches/<int:id>', methods=["PATCH"])
def update_church(id):
    """Updates a particular church and responds w/ JSON of that church."""

     # TO-DO: Restrict access to '/api' routes!

    #  =====================================>

    church = Church.query.get_or_404(id)
    church.name = request.json.get('name', church.name)
    church.location = request.json.get('location', church.location)
    church.phone_number = request.json.get('phone_number', church.phone_number)
    church.email = request.json.get('email', church.email)
    church.website = request.json.get('website', church.website)
    db.session.commit()
    return jsonify(church=church.serialize())


@api.route('/churches/<int:id>', methods=["DELETE"])
def delete_church(id):
    """Deletes a particular church."""

     # TO-DO: Restrict access to '/api' routes!

    #  =====================================>

    church = Church.query.get_or_404(id)
    db.session.delete(church)
    db.session.commit()
    return jsonify(message="Deleted!")


# REST routes for RESOURCES ======================================================>
@api.route('/resources')
def get_resources():
    """Returns JSON w/ all resources."""

    # TO-DO: Restrict access to '/api' routes!

    #  =====================================>
    resources = [resource.serialize() for resource in Resource.query.all()]
    return jsonify(resources=resources)


@api.route('/resources/<int:id>')
def get_resource(id):
    """Returns JSON for one particular resource."""

     # TO-DO: Restrict access to '/api' routes!

    #  =====================================>

    resource = Resource.query.get_or_404(id)
    return jsonify(resource=resource.serialize())


@api.route('/resources', methods=['POST'])
def create_resource():
    """Creates a new resource and returns JSON of that created resource."""

     # TO-DO: Restrict access to '/api' routes!

    #  =====================================>

    new_resource = Resource(title=request.json["title"],
                    category=request.json["category"],
                    staff_id=request.json["staff_id"],
                    author=request.json["author"])
    db.session.add(new_resource)
    db.session.commit()
    response_json = jsonify(resource=new_resource.serialize())
    return (response_json, 201)


@api.route('/resources/<int:id>', methods=["PATCH"])
def update_resource(id):
    """Updates a particular resource and responds w/ JSON of that resource."""

     # TO-DO: Restrict access to '/api' routes!

    #  =====================================>

    resource = Class.query.get_or_404(id)
    resource.title = request.json.get('title', resource.title)
    resource.category = request.json.get('date', resource.category)
    resource.staff_id = request.json.get('staff_id', resource.staff_id)
    resource.author = request.json.get('author', resource.author)
    db.session.commit()
    return jsonify(resource=resource.serialize())


@api.route('/resources/<int:id>', methods=["DELETE"])
def delete_resource(id):
    """Deletes a particular resource."""

     # TO-DO: Restrict access to '/api' routes!

    #  =====================================>

    resource = Class.query.get_or_404(id)
    db.session.delete(resource)
    db.session.commit()
    return jsonify(message="Deleted!")


# REST routes for CONTACTS ======================================================>
@api.route('/contacts')
def get_contacts():
    """Returns JSON w/ all contacts."""

    # TO-DO: Restrict access to '/api' routes!

    #  =====================================>
    contacts = [contact.serialize() for contact in Contact.query.all()]
    return jsonify(contacts=contacts)


@api.route('/contacts/<int:id>')
def get_contact(id):
    """Returns JSON for one particular contact."""

     # TO-DO: Restrict access to '/api' routes!

    #  =====================================>

    contact = Contact.query.get_or_404(id)
    return jsonify(contact=contact.serialize())


@api.route('/contacts', methods=['POST'])
def create_contact():
    """Creates a new contact and returns JSON of that created contact."""

     # TO-DO: Restrict access to '/api' routes!

    #  =====================================>

    new_contact = Contact(first_name=request.json["first_name"],
                    last_name=request.json["last_name"],
                    email=request.json["email"],
                    message=request.json["message"])
    db.session.add(new_contact)
    db.session.commit()
    response_json = jsonify(contact=new_contact.serialize())
    return (response_json, 201)


@api.route('/contacts/<int:id>', methods=["PATCH"])
def update_contact(id):
    """Updates a particular contact and responds w/ JSON of that contact."""

     # TO-DO: Restrict access to '/api' routes!

    #  =====================================>

    contact = Contact.query.get_or_404(id)
    contact.first_name = request.json.get('first_name', contact.first_name)
    contact.last_name = request.json.get('last_name', contact.last_name)
    contact.email = request.json.get('email', contact.email)
    contact.message = request.json.get('message', contact.message)
    db.session.commit()
    return jsonify(contact=contact.serialize())


@api.route('/contacts/<int:id>', methods=["DELETE"])
def delete_contact(id):
    """Deletes a particular contact."""

     # TO-DO: Restrict access to '/api' routes!

    #  =====================================>

    contact = Contact.query.get_or_404(id)
    db.session.delete(contact)
    db.session.commit()
    return jsonify(message="Deleted!")