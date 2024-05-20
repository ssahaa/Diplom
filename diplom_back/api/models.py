from django.db import models

# Create your models here.

class WorkerGrade(models.Model):
    salary = models.IntegerField(blank=False, db_column='slary', default=0, null=False, verbose_name='Зарплата')
    accessLevel = models.IntegerField(blank=False, db_column='accessLevel', default=0, null=False, verbose_name='Уровень прав')
    gradeName = models.CharField(blank=False, db_column='gradeName', default="No name", unique=False,null=False, max_length=128, verbose_name='Наименование должности')

    def __str__(self):
        return f"{self.gradeName}"


class User(models.Model):
    userName = models.CharField(blank=False, db_column='userName', default="No name", unique=False, null=False, max_length=128, verbose_name='Имя')
    userSurname = models.CharField(blank=False, db_column='userSurname', default="No surname", unique=False, null=False, max_length=128, verbose_name='Фамилия')
    userMiddleName = models.CharField(blank=False, db_column='userMiddleName', default="No middlename", unique=False, null=False, max_length=128, verbose_name='Отчество')
    WorkerGrade = models.ForeignKey(WorkerGrade, on_delete=models.CASCADE, null=False, blank=False, verbose_name='id должности')
    creationDate = models.DateField(null=False, blank=False, auto_now_add=True, verbose_name='Дата создания')
    lastModified = models.DateField(auto_now=True, null=False, blank=False, verbose_name='Дата последнего изменения')
    password = models.CharField(blank=False, db_column='password', default="pass123", unique=False, null=False, max_length=128, verbose_name='Пароль')
    login = models.CharField(blank=False, db_column='Login', default="Login123", unique=False, null=False, max_length=128, verbose_name='Логин')

    def __str__(self):
        return f"{self.userSurname} {self.userName} {self.userMiddleName}"



class GOST(models.Model):
    gostName = models.CharField(blank=False, db_column='GostName', default="No name", unique=False, null=False, max_length=128, verbose_name='Наименование')
    creationDate = models.DateField(null=False, blank=False, auto_now_add=True, verbose_name='Дата создания')
    lastModified = models.DateField(auto_now=True, null=False, blank=False, verbose_name='Дата последнего изменения')
    file = models.FileField(upload_to ='GOST', verbose_name='Файл ГОСТ')
    idCreator = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='id Создателя')

    def __str__(self) -> str:
        return self.gostName




class TP(models.Model):
    currentVersionTP = models.FileField(upload_to ='TP', null=False, blank=False, verbose_name='Текущая версия ТП')
    TpName = models.CharField(blank=False, db_column='TpName', default="No name", unique=False, null=False, max_length=128, verbose_name='Наименование ТП')
    creationDate = models.DateField(null=False, blank=False, auto_now_add=True, verbose_name='Дата создания')
    lastModified = models.DateField(auto_now=True, null=False, blank=False, verbose_name='Дата последнего изменения')
    needForChange = models.BooleanField(default=False, null=False, blank=False, verbose_name='Необходимость корректировки')
    idCreator = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='id создателя')
    comment = models.CharField(blank=False, db_column='comment', default="No name", unique=False, null=False, max_length=256, verbose_name='Комментарий')
    newDockVersion = models.FileField(upload_to ='TP', null=True, blank=True, verbose_name='Несогласованная версия ТП')
    def __str__(self) -> str:
        return f"{self.TpName}"

class oldTP(models.Model):
    creationDate = models.DateField(null=False, blank=False, auto_now_add=True, verbose_name='Дата создания')
    dock = models.FileField(upload_to ='TPold', null=False, blank=False, verbose_name='ТП документ')
    idTP = models.ForeignKey(TP, on_delete=models.CASCADE, null=False, blank=False, verbose_name='id ТП')

    def __str__(self) -> str:
        return f" ТП на {self.idTP.TpName} от {self.creationDate}"

class Agreement(models.Model):
   # class Meta:
        # делает уникальным направление обмена
    #    unique_together = ("creator", "inspector")

    idTP = models.ForeignKey(TP, on_delete=models.CASCADE, null=True, verbose_name='id ТП')
    creationDate = models.DateField(null=False, blank=False, auto_now_add=True, verbose_name='Дата создания')
    lastModified = models.DateField(auto_now=True, null=False, blank=False, verbose_name='Дата последнего изменения')
    result = models.BooleanField(default=False, null=False, blank=False, verbose_name='Результата согласования')
    comment = models.CharField(blank=False, db_column='comment', default="No comment", unique=False, null=False, max_length=256, verbose_name='Комментарий')
    AdminComment = models.CharField(blank=False, db_column='adminComment', default="No old comment", unique=False, null=False, max_length=256, verbose_name='Причина отказа администратором')
    dock = models.FileField(upload_to ='Agreement', null=False, blank=False, verbose_name='Документ для рассмотрения')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=False,blank=False, related_name="creatorARG", verbose_name='id Создателя документа')
    #inspector = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="inspectorARG", verbose_name='id Согласующего')
    isActual = models.BooleanField(default=True, null=False, blank=False, verbose_name='Актуальность')
    idTpStringNew = models.CharField(blank=False, db_column='TPAllGostId', default="-", unique=False, null=False, max_length=256, verbose_name='Все Id Гостов')
    NewName = models.CharField(blank=False, db_column='NewName', unique=False, null=True, max_length=256, verbose_name='Новое наименование')
    IsNewTP = models.BooleanField(default=False, null=False, blank=False, verbose_name='Явлется ли новым ТП')
    def __str__(self) -> str:
        return f"{f"Создание ТП {self.NewName}"  if self.idTP is None else f"Изменение ТП {self.idTP.TpName}"} от {self.creationDate}"

class oldAgreement(models.Model):
    idAgreement = models.ForeignKey(Agreement, on_delete=models.CASCADE, verbose_name='id согласования')
    creationDate = models.DateField(null=False, blank=False, auto_now_add=True, verbose_name='Дата создания')
    comment = models.CharField(blank=False, db_column='comment', default="No comment", unique=False, null=False, max_length=256, verbose_name='Комментарий')
    commentOLD = models.CharField(blank=False, db_column='commentOLD', default="No old comment", unique=False, null=False, max_length=256, verbose_name='Комментарий 2')

    def __str__(self) -> str:
        return f" Согласование  ТП: {self.idAgreement.idTP} от {self.idAgreement.creationDate}"

class GOST_DOCK(models.Model):
    idGOST = models.ForeignKey(GOST, on_delete=models.CASCADE, null=False, blank=False, verbose_name='id ГОСТ')
    idDOCK = models.ForeignKey(TP, on_delete=models.CASCADE, null=False, blank=False, verbose_name='id ТП')

    def __str__(self) -> str:
        return f" ГОСТ: {self.idGOST} ТП: {self.idDOCK}"