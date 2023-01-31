from django.db import models

class AcademicTeacher(models.Model):
    last_observation_date = models.DateField(verbose_name="Last Observation Date")
    academic_title = models.TextField(verbose_name="Academic Title")
    specialization = models.TextField(verbose_name="Specialization")
    first_name = models.TextField(verbose_name="First Name")
    last_name = models.TextField(verbose_name="Last Name")
    belongs_to_WZHZ = models.BooleanField(verbose_name="Belongs to WZHZ")
    appointment_to_WZHZ_date = models.DateField(verbose_name="Appointment to WZHZ Date")