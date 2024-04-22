from .models import User, WorkerGrade
from rest_framework import serializers


class WorkerGradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkerGrade
        fields = ['salary', 'accessLevel', 'gradeName']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['userName', 'userSurname', 'userMiddleName', 'WorkerGrade', 'creationDate',"lastModified"]


