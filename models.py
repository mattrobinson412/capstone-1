"""Model classes for Expositors Library app."""

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import UserMixin

db = SQLAlchemy()

bcrypt = Bcrypt()

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class User(UserMixin, db.Model):
    """class representing an individual user on the app."""

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    password = db.Column(db.String, nullable=False, unique=True)
    phone_number = db.Column(db.String(13), nullable=True, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    status_id = db.Column(db.Integer, db.ForeignKey('status.id'))

    status = db.relationship('Status', backref='user')

    @classmethod
    def register(cls, first_name, last_name, pwd, phone_number, email, status_id):
        """Register user w/hashed password & return user."""

        hashed = bcrypt.generate_password_hash(pwd)
        # turn bytestring into normal (unicode utf8) string
        hashed_utf8 = hashed.decode("utf8")

        # return instance of user w/first_name and hashed pwd
        return cls(first_name=first_name, 
                    last_name=last_name,
                    password=hashed_utf8,
                    phone_number=phone_number,
                    email=email,
                    status_id=status_id)
    # end_register

    # start_authenticate
    @classmethod
    def authenticate(cls, email, pwd):
        """Validate that user exists & password is correct.

        Return user if valid; else return False.
        """

        u = User.query.filter_by(email=email).first()

        if u and bcrypt.check_password_hash(u.password, pwd):
            # return user instance
            return u
        else:
            return False
    # end_authenticate    

    def __repr__(self):
        u = self
        return f"<User {u.id} {u.first_name} {u.last_name} {u.password} {u.phone_number} {u.email} {u.status_id}>"

    def serialize(self):
        """Returns a dict representation of a 'User' instance that can be turned into JSON."""

        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'password': self.password,
            'phone_number': self.phone_number,
            'email': self.email,
            'status_id': self.status_id
        }


class Status(db.Model):
    """class representing a user's status in the app."""

    __tablename__ = 'status'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    status = db.Column(db.String, nullable=False)

    def __repr__(self):
        s = self
        return f"<Status {s.id} {s.status}>"

    def serialize(self):
        """Returns a dict representation of a 'Status' instance that can be turned into JSON."""

        return {
            'id': self.id,
            'status': self.status
        }


class Donation(db.Model):
    """class representing a single donation in the app."""

    __tablename__ = 'donation'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    date = db.Column(db.String(8), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    payment_type = db.Column(db.String, nullable=False)

    def __repr__(self):
        d = self
        return f"<Donation {d.id} {d.user_id} {d.first_name} {d.last_name} {d.date} {d.amount} {d.payment_type}>"

    def serialize(self):
        """Returns a dict representation of a 'Donation' instance that can be turned into JSON."""

        return {
            'id': self.id,
            'user_id': self.user_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'date': self.date,
            'amount': self.amount,
            'payment_type': self.payment_type
        }


class Class(db.Model):
    """class representing a single class in the app."""

    __tablename__ = 'class'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    date = db.Column(db.String, nullable=False)
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'), nullable=True)

    staff = db.relationship('Staff', backref='class')

    def __repr__(self):
        c = self
        return f"<Class {c.id} {c.name} {c.date} {c.staff_id}>"
    
    def serialize(self):
        """Returns a dict representation of a 'Class' instance that can be turned into JSON."""

        return {
            'id': self.id,
            'name': self.name,
            'date': self.date,
            'staff_id': self.staff_id
        }




class Lecture(db.Model):
    """class representing a single class lecture in the app."""

    __tablename__ = 'lecture'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    class_id = db.Column(db.Integer, db.ForeignKey('class.id'), nullable=False)
    name = db.Column(db.String, nullable=True)
    link = db.Column(db.String, nullable=False)
    date = db.Column(db.String, nullable=False)
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'), nullable=False)

    course = db.relationship('Class', backref='lecture')
    staff = db.relationship('Staff', backref='lecture')

    def __repr__(self):
        l = self
        return f"<Lecture {l.id} {l.class_id} {l.name} {l.link} {l.date} {l.staff_id}>"

    def serialize(self):
        """Returns a dict representation of a 'Lecture' instance that can be turned into JSON."""

        return {
            'id': self.id,
            'class_id': self.class_id,
            'name': self.name,
            'link': self.link,
            'date': self.date,
            'staff_id': self.staff_id
        }


class Syllabus(db.Model):
    """class representing a single class syllabus in the app."""

    __tablename__ = 'syllabi'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    class_id = db.Column(db.Integer, db.ForeignKey('class.id'), nullable=False)
    name = db.Column(db.String, nullable=False)
    link = db.Column(db.String, nullable=False)

    course = db.relationship('Class', backref='syllabus')

    def __repr__(self):
        s = self
        return f"<Syllabus {s.id} {s.class_id} {s.name} {s.link}>"

    def serialize(self):
        """Returns a dict representation of a 'Syllabus' instance that can be turned into JSON."""

        return {
            'id': self.id,
            'class_id': self.class_id,
            'name': self.name,
            'link': self.link
        }


class Document(db.Model):
    """class representing a single class document in the app."""

    __tablename__ = 'document'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    class_id = db.Column(db.Integer, db.ForeignKey('class.id'), nullable=False)
    name = db.Column(db.String, nullable=False)
    link = db.Column(db.String, nullable=False)

    course = db.relationship('Class', backref='document')

    def __repr__(self):
        d = self
        return f"<Document {d.id} {d.class_id} {d.name} {d.link}>"

    def serialize(self):
        """Returns a dict representation of a 'Document' instance that can be turned into JSON."""

        return {
            'id': self.id,
            'class_id': self.class_id,
            'name': self.name,
            'link': self.link
        }


class Church(db.Model):
    """class representing a single TES-affiliated church in the app."""

    __tablename__ = 'church'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)
    phone_number = db.Column(db.String(13), nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    website = db.Column(db.String, nullable=False)

    def __repr__(self):
        c = self
        return f"<Church {c.id} {c.name} {c.location} {c.phone_number} {c.email} {c.website}>"

    def serialize(self):
        """Returns a dict representation of a 'Church' instance that can be turned into JSON."""

        return {
            'id': self.id,
            'name': self.name,
            'location': self.location,
            'phone_number': self.phone_number,
            'email': self.email,
            'website': self.website
        }


class Graduate(db.Model):
    """class representing a single TES graduate in the app."""

    __tablename__ = 'graduate'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    grad_year = db.Column(db.Integer, nullable=False)
    church_id = db.Column(db.Integer, db.ForeignKey('church.id'), nullable=False)
    role = db.Column(db.Text, nullable=True)

    church = db.relationship('Church', backref='graduate')

    def __repr__(self):
        g = self
        return f"<Graduate {g.id} {g.first_name} {g.last_name} {g.grad_year} {g.church_id}"

    def serialize(self):
        """Returns a dict representation of a 'Graduate' instance that can be turned into JSON."""

        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'grad_year': self.grad_year,
            'church_id': self.church_id,
            'role': self.role
        }


class Staff(db.Model):
    """Class representing an individual staff member/professor at TES."""

    __tablename__ = 'staff'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    join_date = db.Column(db.String(8), nullable=False)
    church_id = db.Column(db.Integer, db.ForeignKey('church.id'), nullable=False)
    role = db.Column(db.Text, nullable=True)

    church = db.relationship('Church', backref='staff')

    def __repr__(self):
        s = self
        return f"<Staff {s.id} {s.first_name} {s.last_name} {s.join_date} {s.church_id} {s.role}>"

    def serialize(self):
        """Returns a dict representation of a 'Staff' instance that can be turned into JSON."""

        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'join_date': self.join_date,
            'church_id': self.church_id,
            'role': self.role
        }


class Resource(db.Model):
    """class representing a single TES-affiliated resource in the app."""

    __tablename__ = 'resource'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    link = db.Column(db.String, nullable=False)
    category = db.Column(db.Text, nullable=False)
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'), nullable=True)

    staff = db.relationship('Staff', backref='resource')

    def __repr__(self):
        r = self
        return f"<Resource {r.id} {r.title} {r.category} {r.staff_id}>"
    
    def serialize(self):
        """Returns a dict representation of a 'Resource' instance that can be turned into JSON."""

        return {
            'id': self.id,
            'title': self.title,
            'link': self.link,
            'category': self.category,
            'staff_id': self.staff_id
        }


class Contact(db.Model):
    """Class representing a single contact from the homepage."""

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    email = db.Column(db.String, nullable=False)
    message = db.Column(db.Text, nullable=False)

    def __repr__(self):
        c = self
        return f"<Contact {c.id} {c.first_name} {c.last_name} {c.email} {c.message}>"

    def serialize(self):
        """Returns a dict representation of a 'Contact' instance that can be turned into JSON."""

        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'message': self.message
        }