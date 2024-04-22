from .models import User, WorkerGrade, GOST
from rest_framework import serializers


class WorkerGradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkerGrade
        fields = ['salary', 'accessLevel', 'gradeName']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'userName', 'userSurname', 'userMiddleName', 'WorkerGrade', 'creationDate',"lastModified"]

class GOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = GOST
        fields = ['gostName','file', 'idCreator', 'creationDate', 'lastModified']


