from django.contrib.auth import get_user_model
from applications.booking.tests.test_setup import TestSetUp

User = get_user_model()


class TestViews(TestSetUp):
    def test_get_booking_list(self):
        """Get booking list"""
        res = self.client.get(self.booking_list_url)
        self.assertEqual(res.status_code, 200)

    def test_user_can_booking_time(self):
        """Auth user can booking time"""
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.user_token)
        res = self.client.post(self.booking_create_url, self.data_for_booking, format="json")
        self.assertEqual(res.status_code, 201)

    def test_cannot_booking_same_time(self):
        """Different or the same user cannot book the same time on the same day"""
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.user_token)
        res = self.client.post(self.booking_create_url, self.data_for_booking, format="json")
        self.assertEqual(res.status_code, 201)
        res_2 = self.client.post(self.booking_create_url, self.data_for_booking, format="json")
        self.assertEqual(res_2.status_code, 400)
