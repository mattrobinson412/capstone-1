from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, IntegerField, TextField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import InputRequired, Length, Optional, EqualTo, Email



class LoginForm(FlaskForm):
    """Form for logging a user in."""

    email = StringField("Email Address", validators=[InputRequired(message="Please enter your email here."), Email()])
    password = PasswordField('Password', [InputRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm  = PasswordField('Repeat Password')

class ContactForm(FlaskForm):
    """Form for a contact submission by an Alumni user."""
    
    first_name = StringField("First Name", validators=[
                                InputRequired(message="Please enter your first name here.")
                                ], render_kw={'class': 'form-control'})
    last_name = StringField("Last Name", validators=[
                                InputRequired(message="Please enter your last name here.")
                                ], render_kw={'class': 'form-control'})
    email = StringField("Email", validators=[
                            InputRequired(message="Please enter your email address here."), Email()
                                ], render_kw={'class': 'form-control'})                      
    message = TextAreaField("Message", validators=[
                            InputRequired(message="Please type your message in this field.")],
                            render_kw={'class': 'form-control', 'rows': 3})


class EditUserForm(FlaskForm):
    """Form for editing a user."""

    first_name = TextField("First Name", validators=[Optional()])
    last_name = TextField("Last Name", validators=[Optional()])
    phone_number = StringField("Phone Number", validators=[Optional()])
    email = StringField("Email", validators=[Optional(), Email()])
    password = PasswordField('Password', [InputRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm  = PasswordField('Repeat Password')
    