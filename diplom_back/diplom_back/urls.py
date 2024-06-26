"""
URL configuration for diplom_back project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from rest_framework import routers
from api.views import WorkerGradeViewSet, UserViewSet, GOSTViewSet, GOSTDOCViewSet, TPViewSet, OldTPViewSet, AgreementTPViewSet, oldAgreementTPViewSet
from django.conf import settings
from django.conf.urls.static import static
router = routers.DefaultRouter()

router.register(r'Должности', WorkerGradeViewSet)
router.register(r'Пользователи', UserViewSet)
router.register(r'ГОСТ', GOSTViewSet)
router.register(r'Связь ГОСТ и ТП', GOSTDOCViewSet)
router.register(r'ТП', TPViewSet )
router.register(r'Старые ТП', OldTPViewSet)
router.register(r'Согласование ТП', AgreementTPViewSet )
router.register(r'Старые согласования', oldAgreementTPViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
