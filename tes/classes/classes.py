from flask import Blueprint, request, render_template
import requests
import sys
sys.path.append("C:/Users/12392/Desktop/.vscode/Springboard/Projects/capstones/capstone-1/tes")
import models

classes = Blueprint('classes', __name__)