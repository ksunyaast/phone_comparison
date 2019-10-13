from django.db import models

# Create your models here.
class Phone(models.Model):
    name = models.CharField(
        max_length = 30
    )
    price = models.PositiveIntegerField()
    os = models.CharField(
        max_length = 30
    )
    ram = models.PositiveIntegerField()
    camera = models.PositiveIntegerField()
    cpu = models.TextField()
    screen = models.TextField()

class Digma(models.Model):
    model = models.ForeignKey('Phone', on_delete=models.CASCADE)
    max_memory = models.TextField()
    fm_radio = models.BooleanField()

class Xiaomi(models.Model):
    model = models.ForeignKey('Phone', on_delete=models.CASCADE)
    sim = models.CharField(
        max_length = 15
    )
    screen_protection = models.TextField()
    dual_camera = models.BooleanField()

class Samsung(models.Model):
    model = models.ForeignKey('Phone', on_delete=models.CASCADE)
    max_memory = models.TextField()
    sim = models.CharField(
        max_length = 15
    )