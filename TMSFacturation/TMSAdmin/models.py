from datetime import datetime

from django.db import models


# Create your models here.

class User(models.Model):
    email = models.CharField(max_length=30, primary_key=True)
    password = models.CharField(max_length=30)
    isAdmin = models.BooleanField(default=False)
    class Meta:
        db_table = "db_User"

class Service(models.Model):
    codeS = models.CharField(max_length=30,primary_key=True)
    descriptionS = models.TextField(max_length=1000,null=True)
    QteS = models.IntegerField()
    priceS = models.DecimalField(max_digits=5, decimal_places=2)
    unitS = models.CharField(max_length=5,default="")
    class  Meta:
        db_table = "db_Service"

class Client(models.Model):
    codeC = models.CharField(max_length=30,primary_key=True)
    nameC = models.CharField(max_length=30)
    class Meta:
        db_table = "db_Client"

class Operation(models.Model):
    operationID = models.AutoField(primary_key=True)
    # dateO = models.DateField(default=datetime.now().date())
    yearO = models.IntegerField(default=datetime.now().date().year)
    monthO = models.IntegerField(default=datetime.now().date().month)
    dayO = models.IntegerField(default=datetime.now().date().day)
    # timeO = models.TimeField(null=True)
    timeO = models.CharField(max_length=6)
    adresseO = models.CharField(max_length=30)
    destinationO = models.CharField(max_length=30)
    distanceO = models.IntegerField(default=0)
    clientO = models.ForeignKey(Client,on_delete=models.CASCADE)
    total_costO = models.DecimalField(max_digits=5, decimal_places=2,default=0)
    isCompleteO = models.BooleanField(default=False)
    isCanceledO = models.BooleanField(default=False)
    class Meta:
        db_table = "db_Operation"

class OperationInput(models.Model):
    operation_inputID = models.AutoField(primary_key=True)
    serviceOI = models.ForeignKey(Service,on_delete=models.CASCADE)
    QteOI = models.IntegerField()
    priceOI = models.DecimalField(max_digits=5, decimal_places=2,default=0)
    total_priceOI = models.DecimalField(max_digits=5, decimal_places=2,default=0)
    operationOI = models.ForeignKey(Operation,on_delete=models.CASCADE)

    class Meta:
        db_table = "db_OperationInput"



  # Service("S8002934P", "PRISE EN CHARGE DU PREMIER USAGER ALLER OU RETOUR, SEULEMENT - COUT FACTURABLE", 1,
    #         75.00).save()
    # Service("S8002935P", "PRISE EN CHARGE D'USAGER ADDITIONNEL - COUT FACTURABLE", 1 ,50.00).save()
    # Service("S8007316P", "PRISE EN CHARGE D'USAGER CONTAMINE OU SUSCEPTIBLE DE L'ETRE - COUT FACTURABLE", 1, 80).save()
    # Service("S8007318P", "PRISE EN CHARGE D'USAGER ADDITIONNEL CONTAMINE OU SUSCEPTIBLE DE L'ETRE - COUT FACTURABLE", 1,
    #         80).save()
    # Service("S8002945P", "SERVICE ACCOMPAGNATEUR DEUXIEME CHAUFFEUR - TARIF HORAIRE", 1, 55.00).save()
    # Service("S8002941P", "UTILISATION D'UN FAUTEUIL BARIATRIQUE - COUT FACTURABLE", 1, 75.00).save()
    # Service("S8002942P", "UTILISATION D'UN SIEGE SECURITAIRE POUR BEBE OU ENFANT - COUT FACTURABLE", 1, 0).save()
    # Service("S8007317P", "UTILISATION D'UN SIEGE ESCALIER - COUT FACTURABLE", 1, 300.00).save()
    # Service("S8002938P", "UTILISATION D'OXYGENE - COUT FACTURABLE TARIF HORAIRE", 1, 10.00).save()