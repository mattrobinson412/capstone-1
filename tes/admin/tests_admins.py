"""Admin View tests."""

import os
from unittest import TestCase

from models import *

os.environ['DATABASE_URL'] = "postgresql:///tes_lib_test"

from app import *

db.create_all()

app.config['WTF_CSRF_ENABLED'] = False
# Make Flask errors be real errors, not HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class AdminViewTestCase(TestCase):
    """Test views for admins."""

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
                1
            )
        db.session.add(u)
        db.session.commit()

        self.client = app.test_client()

    def tearDown(self):
        res = super().tearDown()
        db.session.rollback()
        return res
    
    # ===============================================#

    def test_handle_admin_login(self):
        with app.test_client() as client:
            