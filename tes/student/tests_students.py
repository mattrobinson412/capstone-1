"""Student View tests."""

import os

from unittest import TestCase
from sqlalchemy import exc
from app import *
from models import *
from flask_login import login_required, login_user, logout_user, current_user

os.environ['DATABASE_URL'] = "postgresql:///tes_lib_test"
app.config['WTF_CSRF_ENABLED'] = False



db.create_all()

app.config['WTF_CSRF_ENABLED'] = False
# Make Flask errors be real errors, not HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class StudentViewTestCase(TestCase):
    """Test views for students."""

    def setUp(self):
        """Create test client, add sample data."""
        db.drop_all()
        db.create_all()

        admin = Status(status="Admin")
        alum = Status(status="Alumni")
        student = Status(status="Student")
        db.session.add(admin)
        db.session.add(alum)
        db.session.add(student)
        db.session.commit()

        u = User.register(
                'Sam',
                'Bam',
                'nag',
                '54321',
                'calm@gmail.com',
                3
            )
        u1 = User.register(
                'Bam',
                'Sam',
                'gan',
                '12345',
                'hype@gmail.com',
                1
            )

        db.session.add(u)
        db.session.add(u1)
        db.session.commit()
        self.client = app.test_client()

    def tearDown(self):
        res = super().tearDown()
        db.session.rollback()
        return res
    
    # ===============================================#

    def test_handle_student_login(self):
        with app.test_client() as client:
        
            resp = client.get('/student/login')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
    
    def test_handle_student_login(self):
        with app.test_client() as client:
        
            resp = client.post('/student/login', data={'email':'calm@gmail.com', 'password':'nag'})
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)

    