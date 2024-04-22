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