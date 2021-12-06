from django.db import models


class test1(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=50)
    #THIS 6-12-2021 test