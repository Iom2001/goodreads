from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class RegistrationTestCase(TestCase):

    def test_user_account_is_created(self):
        self.client.post(
            reverse("users:register"),
            data = {
                "username": "testuser",
                "first_name": "Test",
                "last_name": "User",
                "email": "test@gmail.com",
                "password": "samoPassword",
            }
        )

        user = User.objects.get(username="testuser")

        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.first_name, "Test")
        self.assertEqual(user.last_name, "User")
        self.assertEqual(user.email, "test@gmail.com")
        self.assertNotEqual(user.password, "samoPassword")
        self.assertTrue(user.check_password("samoPassword"))

    def test_required_fields(self):
        response = self.client.post(
            reverse("users:register"),
            data = {
                "first_name": "Test",
                "email": "test@gmail.com",
            }
        )

        user_count = User.objects.count()
        self.assertEqual(user_count, 0)

        self.assertFormError(response.context["form"], "username", "This field is required.")
        self.assertFormError(response.context["form"], "password", "This field is required.")

    def test_invalid_email(self):
        response = self.client.post(
            reverse("users:register"),
            data={
                "username": "testuser",
                "first_name": "Te  st",
                "last_name": "User",
                "email": "invalid_email",
                "password": "samoPassword",
            }
        )

        user_count = User.objects.count()
        self.assertEqual(user_count, 0)

        self.assertFormError(response.context["form"], "email", "Enter a valid email address.")

    def test_unique_username(self):
        self.client.post(
            reverse("users:register"),
            data={
                "username": "testuser",
                "first_name": "Test",
                "last_name": "User",
                "email": "test@gmail.com",
                "password": "samoPassword",
            }
        )

        user_count = User.objects.count()
        self.assertTrue(user_count > 0)
        user = User.objects.get(username="testuser")
        self.assertEqual(user.username, "testuser")

        response = self.client.post(
            reverse("users:register"),
            data={
                "username": "testuser",
                "first_name": "Test",
                "last_name": "User",
                "email": "test@gmail.com",
                "password": "samoPassword",
            }
        )

        self.assertFormError(response.context["form"], "username", "A user with that username already exists.")
