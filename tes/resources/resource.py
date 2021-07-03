from flask import Blueprint, request, render_template
from flask import current_app as app
import requests
from models import *

resources = Blueprint('resources', __name__,
                        template_folder='templates',  
                        # static_url_path='static',  ----- fix in UI stage!!!
                        static_folder='static')


####### General '/classes/' routes ######################################
@resources.route('/')
def show_resources():
    """Show authorized user a list of all resources."""

    resources = Resource.query.all()

    return render_template("/resources/resources.html", resources=resources)


# @resources.route('/<int:resource_id>')
# def show_resource(resource_id):
#     """Show authorized user the info pertaining to a certain class."""

#     resource = Class.query.get(resource_id)

#     return render_template("/resources/class.html", resource=resource)

