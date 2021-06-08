from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, IntegerField, TextField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import InputRequired, Length, Optional, EqualTo, Email



class LoginForm(FlaskForm):
    """Form for logging a user in."""

    email = StringField("Email Address", validators=[InputRequired(message="Please enter your email here."), Email()])
    password = PasswordField('Password', [InputRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm  = PasswordField('Repeat Password')


class CreateClassForm(FlaskForm):
    """Form for creating a new class."""

    name = StringField("Name", validators=[InputRequired(message="Please enter the name of the class here.")])
    date = StringField("Date", validators=[InputRequired(message="Please enter the starting date of the class here.")])
    staff_id = IntegerField("Staff ID", validators=[InputRequired(message="Please enter the staff ID of the professor.")])


class CreateResourceForm(FlaskForm):
    """Form for creating a new resource."""

    title = StringField("Title", validators=[InputRequired(message="Please enter the title here.")])
    link = StringField("Link", validators=[InputRequired(message="Please enter the link to the resource here.")])
    category = StringField("Category", validators=[InputRequired(message="Please enter the category of the resource here.")])
    staff_id = IntegerField("Staff ID", validators=[InputRequired(message="Please enter the ID of the staff member who created the resource.")])


class EditClassForm(FlaskForm):
    """Form for editing an existing class."""

    name = StringField("Name", validators=[Optional()])
    date = StringField("Date", validators=[Optional()])
    staff_id = IntegerField("Staff ID", validators=[Optional()])


class EditResourceForm(FlaskForm):
    """Form for editing an existing resource."""

    title = StringField("Title", validators=[Optional()])
    link = StringField("Link", validators=[Optional()])
    category = TextField("Category", validators=[Optional()])
    staff_id = IntegerField("Staff ID", validators=[Optional()])


class AddSyllabusForm(FlaskForm):
    """Form for adding a syllabus to a class."""

    class_id = IntegerField("Class ID", validators=[InputRequired(message="Please enter the ID of the class this syllabus belongs to.")])
    name = StringField("Name", validators=[InputRequired(message="Please enter the name of the syllabus here.")])
    link = StringField("Link", validators=[InputRequired(message="Please enter the link to the syllabus here.")])


class AddDocumentForm(FlaskForm):
    """Form for adding a document to a class."""

    class_id = IntegerField("Class ID", validators=[InputRequired(message="Please enter the ID of the class this document belongs to.")])
    name = StringField("Name", validators=[InputRequired(message="Please enter the name of the document here.")])
    link = StringField("Link", validators=[InputRequired(message="Please enter the link to the document here.")])


class AddLectureForm(FlaskForm):
    """Form for adding a lecture to a class."""

    class_id = IntegerField("Class ID", validators=[InputRequired(message="Please enter the ID of the class this lecture belongs to.")])
    name = StringField("Name", validators=[InputRequired(message="Please enter the name of the lecture here.")])
    link = FileField("Link", validators=[FileRequired()])
    date = StringField("Date", validators=[InputRequired(message="Please enter the date of the lecture here.")])
    staff_id = IntegerField("Staff ID", validators=[InputRequired(message="Please enter the ID of the staff member who taugh this lecture.")])


class EditSyllabusForm(FlaskForm):
    """Form for editing a class syllabus."""

    class_id = IntegerField("Class ID", validators=[Optional()])
    name = StringField("Name", validators=[Optional()])
    link = StringField("Link", validators=[Optional()])


class EditDocumentForm(FlaskForm):
    """Form for editing a class document."""

    class_id = IntegerField("Class ID", validators=[Optional()])
    name = StringField("Name", validators=[Optional()])
    link = StringField("Link", validators=[Optional()])


class EditLectureForm(FlaskForm):
    """Form for editing a class lecture."""

    class_id = IntegerField("Class ID", validators=[Optional()])
    name = StringField("Name", validators=[Optional()])
    link = FileField("Link", validators=[Optional()])
    date = StringField("Date", validators=[Optional()])
    staff_id = IntegerField("Staff ID", validators=[Optional()])


class EditUserForm(FlaskForm):
    """Form for editing a user."""

    first_name = TextField("First Name", validators=[Optional()])
    last_name = TextField("Last Name", validators=[Optional()])
    phone_number = StringField("Phone Number", validators=[Optional()])
    email = StringField("Email", validators=[Optional(), Email()])
    password = PasswordField('Password', [InputRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm  = PasswordField('Repeat Password')
    