from flask import Blueprint, request, render_template
import requests
import sys
sys.path.append("C:/Users/12392/Desktop/.vscode/Springboard/Projects/capstones/capstone-1/tes")
from ..models import *

alumni = Blueprint('alumni', __name__)