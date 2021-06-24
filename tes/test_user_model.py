"""User Model tests."""

import os

from unittest import TestCase
from sqlalchemy import exc
from models import *
os.environ['DATABASE_URL'] = "postgresql:///tes_lib_test"

# Now we can import app

from app import app

# Create our tables 

db.create_all()


class UserTestCase(TestCase):
    """Unit tests for User methods."""

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

    def test_register(self):
        new_user = User.register(
                'Matt',
                'Samuels',
                'garble',
                '234234',
                'new@gmail.com',
                2
            )
        self.assertIsInstance(new_user, User)
    

    def test_authenticate(self):
        user_check = User.authenticate('calm@gmail.com', 'nag')
        self.assertTrue(user_check)