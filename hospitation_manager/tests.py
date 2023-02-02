from django.test import TestCase
from .models import ProtocolAppeal, AcademicTeacher, HospitationTeam

# Create your tests here.

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
    