from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Tests if create user with email is successful"""
        email= 'testEmail@gmail.com'
        password= 'testPass123'
        user= get_user_model().objects.create_user(
            email= email,
            password= password
        )
        
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Tests if the second part of the email to converted to lower case"""
        email= 'testEmail@GMAIL.COM'
        user= get_user_model().objects.create_user(
            email = email
        )

        userEmail= user.email
        secondPart= userEmail.split('@')[-1]
        self.assertTrue(secondPart.islower())

    def test_user_with_invalid_email(self):
        """Tests that the email address passed is Valid"""
        email = None

        with self.assertRaises(ValueError):
            user= get_user_model().objects.create_user(email= email)

    def test_create_superuser(self):
        """Tests that a super user is created"""
        user= get_user_model().objects.create_superuser('testEmail@gmail.com', 'pass123')

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)