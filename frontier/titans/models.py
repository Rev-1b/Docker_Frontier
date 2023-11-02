from django.db import models


class SomeModel(models.Model):
    param1 = models.CharField(max_length=256)
    param2 = models.IntegerField()
    param3 = models.DateTimeField(auto_now_add=True)
    param4 = models.BooleanField(default=True)
