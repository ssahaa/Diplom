from .models import User, WorkerGrade, GOST, GOST_DOCK, TP, oldTP, Agreement, oldAgreement
from rest_framework import serializers


class WorkerGradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkerGrade
        fields = ['id', 'salary', 'accessLevel', 'gradeName']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'userName', 'userSurname', 'userMiddleName', 'WorkerGrade', 'creationDate',"lastModified","password"]

class GOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = GOST
        fields = ['id', 'gostName','file', 'idCreator', 'creationDate', 'lastModified']

class GOSTDOCKSerializer(serializers.ModelSerializer):
    class Meta:
        model = GOST_DOCK
        fields = ['id', 'idGOST', 'idDOCK']

class TPSerializer(serializers.ModelSerializer):
    class Meta:
        model = TP
        fields = ['id','TpName', 'currentVersionTP', 'creationDate', 'lastModified', 'needForChange', 'idCreator', "comment", 'newDockVersion']

class oldTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = oldTP
        fields = ['id', 'creationDate', 'dock', 'idTP']

class AgreemdetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agreement
        fields = ['id', 'idTP', 'creationDate', 'lastModified','result','comment','commentOLD','dock','creator','inspector','idActual']

class OldAgreemdetSerializer(serializers.ModelSerializer):
    class Meta:
        model = oldAgreement
        fields = ['id', 'idAgreement', 'creationDate', 'comment','commentOLD']

