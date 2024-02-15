from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Snack


class snackTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass"
        )

        self.Snack = Snack.objects.create(name="pickle",  description=1, purchaser=self.user)

    def test_string_representation(self):
        self.assertEqual(str(self.Snack), "pickle")

    def test_Snack_content(self):
        self.assertEqual(f"{self.Snack.name}", "pickle")
        self.assertEqual(f"{self.purchaser}", "tester")
        self.assertEqual(self. description, "1")

    def test__list_view(self):
        response = self.client.get(reverse("_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "pickle")
        self.assertTemplateUsed(response, "snack_list.html")

    def test__detail_view(self):
        response = self.client.get(reverse("_detail", args="1"))
        no_response = self.client.get("/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "purchaser: tester")
        self.assertTemplateUsed(response, "detail.html")

    def test__create_view(self):
        response = self.client.post(
            reverse("create"),
            {
                "name": "Rake",
                " description": 2,
                "purchaser": self.user.id,
            },
            follow=True,
        )

        self.assertRedirects(response, reverse("detail", args="2"))
        self.assertContains(response, "Rake")

    def test__update_view_redirect(self):
        response = self.client.post(
            reverse("update", args="1"),
            {"name": "Updated name", " description": 3, "purchaser": self.user.id},
        )

        self.assertRedirects(
            response, reverse("detail", args="1"), target_status_code=200
        )

    def test_Snack_update_bad_url(self):
        response = self.client.post(
            reverse("Snack_update", args="9"),
            {"name": "Updated name", " description": 3, "purchaser": self.user.id},
        )

        self.assertEqual(response.status_code, 404)

    def test_Snack_delete_view(self):
        response = self.client.get(reverse("delete", args="1"))
        self.assertEqual(response.status_code, 200)

   
    def test_model(self):
        Snack = Snack.objects.create(name="rake", purchaser=self.user)
        self.assertEqual(Snack.name, "rake")