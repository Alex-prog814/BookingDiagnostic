from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient, APITestCase

User = get_user_model()


class TestSetUp(APITestCase):
    def setUp(self):
        self.login_url = reverse("login")
        self.booking_create_url = reverse("booking-create")
        self.booking_list_url = reverse("booking-list")

        self.user_data = {
            "email": "email@gmail.com",
            "password": "test123",
            "password_confirmation": "test123"
        }

        self.client = APIClient()
        self.user = User(
            email="test1@gmail.com",
            is_active=True,
        )
        self.user.set_password("test1test")

        self.user.save()

        self.master = User(
            email="test2@gmail.com",
            is_active=True,
            is_master=True
        )
        self.master.set_password("test2test")

        self.master.save()

        self.data_for_booking = {
            "master": self.master.id,
            "date": "2022-02-22",
            "time": "15:00-16:00"
        }

        res = self.client.post(
            self.login_url,
            data={"email": "test1@gmail.com", "password": "test1test"},
            format="json",
        )
        self.user_token = res.data["access"]

        return super().setUp()

    def tearDown(self):
        return super().tearDown()
