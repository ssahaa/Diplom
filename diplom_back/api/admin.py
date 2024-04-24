from django.contrib import admin
from .models import User, WorkerGrade, GOST, TP, oldTP, Agreement, oldAgreement, GOST_DOCK
# Register your models here.

admin.site.register(User)
admin.site.register(WorkerGrade)
admin.site.register(GOST)
admin.site.register(TP)
admin.site.register(oldTP)
admin.site.register(Agreement)
admin.site.register(oldAgreement)
admin.site.register(GOST_DOCK)




