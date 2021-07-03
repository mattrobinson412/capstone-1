from flask import Blueprint, request, render_template
from flask import current_app as app
import requests
import sys
sys.path.append("C:/Users/12392/Desktop/.vscode/Springboard/Projects/capstones/capstone-1/tes")
from models import *

classes = Blueprint('classes', __name__, 
                    template_folder='templates',  
                    # static_url_path='static',  ----- fix in UI stage!!!
                    static_folder='static')


####### General '/classes/' routes ######################################
@classes.route('/')
def show_classes():
    """Show authorized user a list of all classes."""

    courses = Class.query.all()

    return render_template("/classes/classes.html", courses=courses)


@classes.route('/<int:class_id>')
def show_class(class_id):
    """Show authorized user the info pertaining to a certain class."""

    course = Class.query.get(class_id)
    lectures = Lecture.query.filter_by(class_id=class_id)
    syllabi = Syllabus.query.filter_by(class_id=class_id)
    docs = Document.query.filter_by(class_id=class_id)

    return render_template("/classes/class.html", course=course, lectures=lectures, syllabi=syllabi, docs=docs)


@classes.route('/<int:class_id>/lectures/<int:lecture_id>')
def show_class_lecture(class_id, lecture_id):
    """Show authorized user a lecture for a class."""

    course = Class.query.get(class_id)
    lecture = Lecture.query.get(lecture_id)

    return render_template("/classes/class-lecture.html", course=course, lecture=lecture)


# @classes.route('/<int:class_id>/syllabi/<int:syllabus_id>')
# def show_class_syllabus(class_id, syllabus_id):
#     """Show authorized user a syllabus for a class."""

#     course = Class.query.get(class_id)
#     syl = Syllabus.query.get(syllabus_id)

#     return render_template("/classes/class-syllabus.html", course=course, syl=syl)


# @classes.route('/<int:class_id>/documents/<int:doc_id>')
# def show_class_doc(class_id, doc_id):
#     """Show authorized user a document for a class."""

#     course = Class.query.get(class_id)
#     doc = Document.query.get(doc_id)

#     return render_template("/classes/class-doc.html", course=course, doc=doc)