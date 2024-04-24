from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets
# Create your views here.


class WorkerGradeViewSet(viewsets.ModelViewSet):
    queryset = WorkerGrade.objects.all().order_by('id')
    serializer_class = WorkerGradeSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer


class GOSTViewSet(viewsets.ModelViewSet):
    queryset = GOST.objects.all().order_by('id')
    serializer_class = GOSTSerializer

class GOSTDOCViewSet(viewsets.ModelViewSet):
    queryset = GOST_DOCK.objects.all().order_by('id')
    serializer_class = GOSTDOCKSerializer

class TPViewSet(viewsets.ModelViewSet):
    queryset = TP.objects.all().order_by('id')
    serializer_class = TPSerializer

class OldTPViewSet(viewsets.ModelViewSet):
    queryset = oldTP.objects.all().order_by('id')
    serializer_class = oldTPSerializer

class AgreementTPViewSet(viewsets.ModelViewSet):
    queryset = Agreement.objects.all().order_by('id')
    serializer_class = AgreemdetSerializer

class oldAgreementTPViewSet(viewsets.ModelViewSet):
    queryset = oldAgreement.objects.all().order_by('id')
    serializer_class = OldAgreemdetSerializer


