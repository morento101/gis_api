from django.contrib import admin
from . import models

admin.site.register(models.MapModel)
admin.site.register(models.ChainModel)
admin.site.register(models.LineModel)
admin.site.register(models.PointModel)
