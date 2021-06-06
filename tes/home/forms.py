from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, TextAreaField
from wtforms.validators import InputRequired, Email, Optional
import models

class ContactForm(FlaskForm):
    """Form for a contact submission on the homepage."""
    
    first_name = StringField("First Name", validators=[
                                InputRequired(message="Please enter your first name here.")
                                ], render_kw={'class': 'form-control'})
    last_name = StringField("Last Name", validators=[
                                InputRequired(message="Please enter your last name here.")
                                ], render_kw={'class': 'form-control'})
    email = StringField("Email", validators=[
                            InputRequired(message="Please enter your email address here.")
                                ], render_kw={'class': 'form-control'})                      
    message = TextAreaField("Message", validators=[
                            InputRequired(message="Please type your message in this field.")],
                            render_kw={'class': 'form-control', 'rows': 3})