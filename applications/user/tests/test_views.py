from django.contrib.auth import get_user_model
from applications.user.tests.test_setup import TestSetUp

User = get_user_model()


class TestViews(TestSetUp):
    def test_user_cannot_register_with_no_data(self):
        """Registration without user data"""
        res = self.client.post(self.register_url)
        self.assertEqual(res.status_code, 400)

    def test_user_can_register_correctly(self):
        """Registration with user data"""
        res = self.client.post(self.register_url, self.user_data, format="json")
        self.assertEqual(res.status_code, 201)

    def test_user_crud_profile(self):
        """Auth user can create, read, update, delete, profile"""
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.user_token)
        res_create = self.client.post(self.profile_url, self.user_profile_data, format="json")
        self.assertEqual(res_create.status_code, 201)
        res_update = self.client.put(self.profile_url + f"{res_create.data.get('id')}/",
                                     self.user_profile_data_update, format="json")
        self.assertEqual(res_update.data.get('name'), self.user_profile_data_update.get('name'))
        res_delete = self.client.delete(self.profile_url + f"{res_create.data.get('id')}/")
        self.assertEqual(res_delete.status_code, 204)
