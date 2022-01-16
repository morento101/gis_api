from django.db import models


class MapModel(models.Model):
    name_of_territory = models.CharField(verbose_name="Карта", max_length=90)
    scale = models.CharField(verbose_name="Масштаб", max_length=20)

    def __str__(self):
        return f"Map: {self.name_of_territory}"


class ChainModel(models.Model):
	name = models.CharField(verbose_name="Назва ходу", max_length=40)
	type = models.CharField(verbose_name="Тип ходу", max_length=20)
	accuracy = models.CharField(verbose_name="Точність/класс ходу", max_length=20)
	map = models.ForeignKey(verbose_name="Карта", to="MapModel", on_delete=models.CASCADE)
	line = models.ManyToManyField(to="LineModel")
	point = models.ManyToManyField(to="PointModel")

	def __str__(self):
		return f"Chain: {self.name}"


class LineModel(models.Model):
	length = models.FloatField(verbose_name="Довжина", blank=True)
	elevation = models.FloatField(verbose_name="Перевищення", blank=True)
	point = models.ManyToManyField(to="PointModel") # maybe remove this line


class PointModel(models.Model):
	name = models.CharField(verbose_name="Назва точки", max_length=10)
	z_coord = models.FloatField(verbose_name="Координата X", blank=True)
	y_coord = models.FloatField(verbose_name="Координата Y", blank=True)
	abs_height = models.FloatField(verbose_name="Абсолютна висота", blank=True)
