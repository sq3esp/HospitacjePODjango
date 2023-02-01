from django.contrib import admin

# Register your models here.

from .models import AcademicTeacher
from .models import Classes
from .models import HospitationTeam
from .models import ProtocolAppeal
from .models import HospitationProtocol
from .models import Hospitation


admin.site.register(AcademicTeacher)
admin.site.register(Classes)
admin.site.register(HospitationTeam)
admin.site.register(HospitationProtocol)
admin.site.register(ProtocolAppeal)
admin.site.register(Hospitation)

