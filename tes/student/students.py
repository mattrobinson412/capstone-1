from flask import Blueprint, request, render_template
import requests
import models

student = Blueprint('student', __name__)