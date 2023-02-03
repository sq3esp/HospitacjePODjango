from django.test import Client, TestCase
from .models import AcademicTeacher, Hospitation, Classes

class WZHZAddMemberTestCase(TestCase):
    def test_add_to_WZHZ(self):
        teacher = AcademicTeacher.objects.create(
            first_name='Adam',
            last_name='Nowak',
            belongs_to_WZHZ=False,
        )

        self.assertFalse(teacher.belongs_to_WZHZ)

        client = Client()
        response = client.post('/wzhz/add', {'id': teacher.id})

        teacher.refresh_from_db()

        self.assertTrue(teacher.belongs_to_WZHZ)

    def test_add_to_WZHZ_with_wrong_id(self):
        client = Client()
        response = client.post('/wzhz/add', {'id': 1})

        self.assertEqual(response.status_code, 404)


class WZHZDetailsTestCase(TestCase):
    def test_details(self):
        teacher = AcademicTeacher.objects.create(
            first_name='Adam',
            last_name='Nowak',
            belongs_to_WZHZ=True,
        )

        client = Client()
        response = client.get(f'/wzhz/details/{teacher.id}')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, teacher.first_name)
        self.assertContains(response, teacher.last_name)

    def test_details_with_wrong_id(self):
        client = Client()
        response = client.get('/wzhz/details/1')

        self.assertEqual(response.status_code, 404)
