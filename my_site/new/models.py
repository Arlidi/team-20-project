from django.db import models
# Create your models here.

class camera(models.Model):
    cam_id = models.CharField(verbose_name = 'Camera ID', unique = True,  db_index=True, max_length=64)
    cam_fire_danger = models.CharField(verbose_name='Fire danger', max_length=64)
    cam_time = models.CharField(verbose_name='Time', max_length=64)
