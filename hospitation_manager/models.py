from django.db import models

class AcademicTeacher(models.Model):
    last_hospitatnion_date = models.DateField(verbose_name="Last hospitatnion Date")
    academic_title = models.TextField(verbose_name="Academic Title")
    specialization = models.TextField(verbose_name="Specialization")
    first_name = models.TextField(verbose_name="First Name")
    last_name = models.TextField(verbose_name="Last Name")
    belongs_to_WZHZ = models.BooleanField(verbose_name="Belongs to WZHZ")
    appointment_to_WZHZ_date = models.DateField(verbose_name="Appointment to WZHZ Date")


class Activities(models.Model):
    required_specialization = models.TextField(verbose_name="Required Specialization")
    code = models.TextField(verbose_name="Code")
    class_type = models.TextField(verbose_name="Class Type")
    name = models.TextField(verbose_name="Name")
    time_and_location = models.TextField(verbose_name="Time and Location")
    ECTS = models.IntegerField(verbose_name="ECTS")
    teaching_method = models.TextField(verbose_name="Teaching Method")
    study_program = models.TextField(verbose_name="Study Program")
    teacher = models.ForeignKey(AcademicTeacher, on_delete=models.CASCADE, verbose_name="Teacher")

class HospitationTeam(models.Model):
    number = models.IntegerField(verbose_name="Number")
    creation_date = models.DateField(verbose_name="Creation Date")
    academic_teacher1 = models.ForeignKey(AcademicTeacher, on_delete=models.CASCADE, verbose_name="Academic Teacher 1", related_name="academic_teacher1")
    academic_teacher2 = models.ForeignKey(AcademicTeacher, on_delete=models.CASCADE, verbose_name="Academic Teacher 2", related_name="academic_teacher2")

class Hospitation(models.Model):
    STATE_CHOICES = (
        ('Z', 'Przeprowadzona'),
        ('O', 'Odwołana'),
        ('W', 'Oczekuje na przeprowadzenie'),)
    number = models.IntegerField(verbose_name="Number")
    hospitation_date = models.DateField(verbose_name="Hospitation Date")
    creation_date = models.DateField(verbose_name="Date")
    state = models.CharField(max_length=1, choices=STATE_CHOICES, verbose_name="State")
    hospitation_team = models.ForeignKey(HospitationTeam, on_delete=models.CASCADE, verbose_name="Hospitation Team")
    activity = models.ForeignKey(Activities, on_delete=models.CASCADE, verbose_name="Activity")

