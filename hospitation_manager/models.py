from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext as _

class AcademicTeacher(models.Model):
    last_hospitation_date = models.DateField(verbose_name="last hospitation Date", blank=True, null=True)
    academic_title = models.TextField(verbose_name="academic Title", blank=True)
    specialization = models.TextField(verbose_name="specialization", blank=True)
    first_name = models.TextField(verbose_name="first Name")
    last_name = models.TextField(verbose_name="last Name")
    belongs_to_WZHZ = models.BooleanField(verbose_name="belongs to WZHZ", default=False)
    appointment_to_WZHZ_date = models.DateField(verbose_name="appointment to WZHZ Date", blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.academic_title} {self.first_name} {self.last_name}"

class Classes(models.Model):
    required_specialization = models.TextField(verbose_name="required Specialization", blank=True)
    code = models.TextField(verbose_name="code")
    class_type = models.TextField(verbose_name="class Type")
    name = models.TextField(verbose_name="name")
    time_and_location = models.TextField(verbose_name="time and Location")
    ECTS = models.IntegerField(verbose_name="ECTS")
    teaching_method = models.TextField(verbose_name="teaching Method", blank=True)
    study_program = models.TextField(verbose_name="study Program", blank=True)
    teacher = models.ForeignKey(AcademicTeacher, on_delete=models.SET_NULL, verbose_name="teacher", blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.code} : {self.name}"

class HospitationTeam(models.Model):
    number = models.BigAutoField(verbose_name="number", primary_key=True)
    created_at = models.DateField(verbose_name="creation Date", auto_now=False, auto_now_add=True)
    academic_teacher1 = models.ForeignKey(AcademicTeacher, on_delete=models.CASCADE, verbose_name="academic Teacher 1", related_name="academic_teacher1")
    academic_teacher2 = models.ForeignKey(AcademicTeacher, on_delete=models.CASCADE, verbose_name="academic Teacher 2", related_name="academic_teacher2")

    def __str__(self) -> str:
        return f"{self.number} : {self.created_at} | {self.academic_teacher1.last_name}, {self.academic_teacher2.last_name}"

class ProtocolAppeal(models.Model):
    STATUS_CHOICES = [
        ('OD', 'odrzucone'),
        ('ZA', 'zatwierdzone'),
        ('OC', 'oczekuje')]
    issuer = models.ForeignKey(AcademicTeacher, verbose_name="issuer", on_delete=models.CASCADE)
    created_at = models.DateField(verbose_name="lodging date", auto_now=False, auto_now_add=True)
    reason = models.TextField(verbose_name="reason")
    status = models.CharField(verbose_name="status", max_length=2, choices=STATUS_CHOICES, default='OC')
    dean_response = models.TextField(verbose_name="dean response", blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.issuer.last_name} : {self.reason}, {self.status}"

class HospitationProtocol(models.Model):
    issuer = models.ForeignKey(AcademicTeacher, on_delete=models.CASCADE, verbose_name="issuer")
    created_at = models.DateField(verbose_name="lodging date", auto_now=False, auto_now_add=True)
    protocol_content = models.TextField(verbose_name="content of protocol")
    is_appeal_lodged = models.BooleanField(verbose_name="is appeal lodged?", default=False)
    appeal = models.OneToOneField(ProtocolAppeal, verbose_name="appeal", on_delete=models.SET_NULL, blank=True, null=True)

    preparation_date = models.DateField(_("data sporządzenia"), auto_now=False, auto_now_add=False)
    confirmation_date = models.DateField(_("data potwierdzenia"), auto_now=False, auto_now_add=False)
    final_evaluation = models.IntegerField(_("ocena końcowa"), validators=[MaxValueValidator(5), MinValueValidator(2)])
    did_classes_started_in_time = models.BooleanField(_("czy zajęcia rozpoczęły się punktualnie"))
    delay_in_starting_classes = models.IntegerField(_("opóźnienie rozpoczęcia zajęć"))
    was_presence_checked = models.BooleanField(_("czy sprawdzono obecność studentów"))
    enrolled_number = models.IntegerField(_("liczba zapisanych"))
    is_room_prepared = models.BooleanField(_("czy sala jest dostosowana"))
    is_room_prepared_cause = models.TextField(_("czy sala jest dostosowana przyczyna"), blank=True, null=True)
    is_content_consistent_with_program = models.BooleanField(_("czy treść zgodna z programem kursu"))
    other_remarks = models.TextField(_("inne uwagi"), blank=True, null=True)
    subject = models.IntegerField(_("temat"), validators=[MaxValueValidator(5), MinValueValidator(2)])
    explanation = models.IntegerField(_("wyjaśnienie"), validators=[MaxValueValidator(5), MinValueValidator(2)])
    engagement = models.IntegerField(_("zaangażowanie"), validators=[MaxValueValidator(5), MinValueValidator(2)])
    inspiration = models.IntegerField(_("inspiracja"), validators=[MaxValueValidator(5), MinValueValidator(2)])
    valid_answers = models.IntegerField(_("poprawne odpowiedzi"), validators=[MaxValueValidator(5), MinValueValidator(2)])
    didactic_resources = models.IntegerField(_("środki dydaktyczne"), validators=[MaxValueValidator(5), MinValueValidator(2)])
    appropriate_language = models.IntegerField(_("poprawny język"), validators=[MaxValueValidator(5), MinValueValidator(2)])
    group_dynamics = models.IntegerField(_("dynamika grupy"), validators=[MaxValueValidator(5), MinValueValidator(2)])
    atmosphere = models.IntegerField(_("atmosfera"), validators=[MaxValueValidator(5), MinValueValidator(2)])
    technical_means_of_passing_knowledge = models.IntegerField(_("techniczne środki przekazania wiedzy"), validators=[MaxValueValidator(5), MinValueValidator(2)])
    up_to_date_knowledge = models.IntegerField(_("aktualna wiedza"), validators=[MaxValueValidator(5), MinValueValidator(2)])
    content = models.IntegerField(_("materiał"), validators=[MaxValueValidator(5), MinValueValidator(2)])
    teaching_skills = models.IntegerField(_("umiejętności nauczania"), validators=[MaxValueValidator(5), MinValueValidator(2)])
    examples = models.IntegerField(_("przykłady"), validators=[MaxValueValidator(5), MinValueValidator(2)])
    tempo = models.IntegerField(_("tempo"), validators=[MaxValueValidator(5), MinValueValidator(2)])
    preparation = models.IntegerField(_("przygotowanie"), validators=[MaxValueValidator(5), MinValueValidator(2)])
    exercises = models.IntegerField(_("zadania"), validators=[MaxValueValidator(5), MinValueValidator(2)])
    planning = models.IntegerField(_("planowanie"), validators=[MaxValueValidator(5), MinValueValidator(2)])
    comments = models.IntegerField(_("komentarze"), validators=[MaxValueValidator(5), MinValueValidator(2)])
    documentation = models.IntegerField(_("dokumentacja"), validators=[MaxValueValidator(5), MinValueValidator(2)])

    def __str__(self) -> str:
        return f"{self.issuer.last_name} : {self.protocol_content}, is appeal lodged?: {self.is_appeal_lodged}"

class Hospitation(models.Model):
    STATUS_CHOICES = [
        ('Z', 'Przeprowadzona'),
        ('O', 'Odwołana'),
        ('P', 'Planowana'),
        ('W', 'Oczekuje na przeprowadzenie')]
    number = models.BigAutoField(verbose_name="number", primary_key=True)
    hospitation_date = models.DateField(verbose_name="hospitation Date", blank=True, null=True)
    created_at = models.DateField(verbose_name="date", auto_now=False, auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name="status", default='W')
    hospitation_team = models.ForeignKey(HospitationTeam, on_delete=models.SET_NULL, verbose_name="hospitation Team", blank=True, null=True)
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE, verbose_name="classes")
    associated_protocol = models.OneToOneField(HospitationProtocol, on_delete=models.SET_NULL, verbose_name="associated protocol", blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.number} : {self.hospitation_date}, {self.status}, {self.classes.name}"