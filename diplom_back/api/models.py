from django.db import models

# Create your models here.

class WorkerGrade(models.Model):
    salary = models.IntegerField(blank=False, db_column='slary', default=0, null=False)
    accessLevel = models.IntegerField(blank=False, db_column='accessLevel', default=0, null=False)
    gradeName = models.CharField(blank=False, db_column='gradeName', default="No name", unique=False,null=False, max_length=128)

    def __str__(self):
        return f"{self.gradeName}"


class User(models.Model):
    userName = models.CharField(blank=False, db_column='userName', default="No name", unique=False, null=False, max_length=128)
    userSurname = models.CharField(blank=False, db_column='userSurname', default="No surname", unique=False, null=False, max_length=128)
    userMiddleName = models.CharField(blank=False, db_column='userMiddleName', default="No middlename", unique=False, null=False, max_length=128)
    WorkerGrade = models.ForeignKey(WorkerGrade, on_delete=models.CASCADE, null=False, blank=False)
    creationDate = models.DateField(null=False, blank=False, auto_now_add=True)
    lastModified = models.DateField(auto_now=True, null=False, blank=False)

    def __str__(self):
        return f"{self.userSurname}, {self.userName},  {self.userMiddleName}"
