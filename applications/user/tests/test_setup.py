from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient, APITestCase

from booking_diagnostic.settings import DOMAIN

User = get_user_model()


class TestSetUp(APITestCase):
    def setUp(self):
        self.register_url = reverse("register")
        self.login_url = reverse("login")
        self.profile_url = DOMAIN + "/user/profile/"

        self.user_data = {
            "email": "email@gmail.com",
            "password": "test123",
            "password_confirmation": "test123"
        }

        self.user_profile_data = {
            "full_name": "Example user",
            "auto": "Example car"
        }

        self.user_profile_data_update = {
            "full_name": "Example user updated",
            "auto": "Example car updated"
        }

        self.client = APIClient()
        self.user = User(
            email="test1@gmail.com",
            is_active=True,
        )
        self.user.set_password("test1test")

        self.user.save()

        res = self.client.post(
            self.login_url,
            data={"email": "test1@gmail.com", "password": "test1test"},
            format="json",
        )
        self.user_token = res.data["access"]

        return super().setUp()

    def tearDown(self):
        return super().tearDown()
