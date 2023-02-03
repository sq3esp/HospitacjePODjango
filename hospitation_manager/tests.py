from django.test import Client, TestCase
from .models import ProtocolAppeal, AcademicTeacher, HospitationTeam, Hospitation, Classes

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

>>>>>>> 41dd9d29531e6a90fc3c0c11cfa09204f7d93570

class ProtocolAppealTestCase(TestCase):
    def setUp(self) -> None:
        AcademicTeacher.objects.create(
            academic_title = "mgr",
            specialization = "test_spec",
            first_name = "test_name",
            last_name = "test_last_name"
        )

        ProtocolAppeal.objects.create(
            issuer = AcademicTeacher.objects.get(last_name="test_last_name"),
            reason = "test_reason"
        )
    
    def test_protocol_appeal_created_correctly(self):
        """Protocol appeal auto fields are correctly filled"""
        appeal = ProtocolAppeal.objects.get(issuer = AcademicTeacher.objects.get(last_name="test_last_name"))
        self.assertEqual(appeal.status, 'OC')
        self.assertIsNotNone(appeal.created_at)
        self.assertIsNone(appeal.dean_response)


class HospitationTeamTestCase(TestCase):
    def setUp(self) -> None:
        AcademicTeacher.objects.create(
            academic_title = "mgr1",
            specialization = "test_spec1",
            first_name = "test_name1",
            last_name = "test_last_name1"
        )

        AcademicTeacher.objects.create(
            academic_title = "mgr2",
            specialization = "test_spec2",
            first_name = "test_name2",
            last_name = "test_last_name2"
        )

        HospitationTeam.objects.create(
            academic_teacher1 = AcademicTeacher.objects.get(last_name="test_last_name1"),
            academic_teacher2 = AcademicTeacher.objects.get(last_name="test_last_name2")
        )
    
    def test_hospitation_team_created_correctly(self):
        """Hospitation team auto fields are correctly filled"""
        hospitationTeam = HospitationTeam.objects.get(academic_teacher1 = AcademicTeacher.objects.get(last_name="test_last_name1"))
        self.assertIsNotNone(hospitationTeam.created_at)
    
