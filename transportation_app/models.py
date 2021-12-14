from django.db import models

class MainCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)

class SubCategory(models.Model):
    parent = models.ForeignKey(MainCategory, on_delete=models.CASCADE, related_name="sub")
    child_name = models.CharField(max_length=80)

    def __str__(self):
        return str(self.child_name )

class Color (models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)

class TransportItem (models.Model):
    name = models.CharField(max_length=200)
    transportModel = models.CharField(max_length=200)
    colors = models.ManyToManyField(Color, related_name="item", blank=True)
    subCategory = models.ForeignKey(
        SubCategory, on_delete=models.CASCADE, related_name="item")

    def __str__(self):
        return str(self.name)





