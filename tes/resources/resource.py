from flask import Blueprint, request, render_template
import requests
import models

resources = Blueprint('resources', __name__)