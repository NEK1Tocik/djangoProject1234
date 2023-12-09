from django.db import models

class ModelNikita(models.Model):
    name = models.CharField(max_length=10)
    email = models.CharField(max_length=10)
    city = models.CharField(max_length=10)
    prof = models.CharField(max_length=10)


class ModelNikitaImg(models.Model):
    name = models.CharField(max_length=10)
    img = models.ImageField(upload_to='imgs')

class ModelReg(models.Model):
    login = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    email = models.CharField(max_length=10)