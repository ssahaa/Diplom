from django.contrib import admin
from .models import User, WorkerGrade, GOST
# Register your models here.

admin.site.register(User)
admin.site.register(WorkerGrade)
admin.site.register(GOST)