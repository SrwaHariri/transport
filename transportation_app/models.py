from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Category(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['-id']


class Color (models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['-id']


class TransportItem(models.Model):
    name = models.CharField(max_length=200)
    transport_model = models.CharField(max_length=200)
    colors = models.ManyToManyField(Color, )
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name="item", blank=True, null=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['-id']

    @receiver(post_save, sender='transportation_app.TransportItem')
    def set_default_color(**kwargs):

        # unpack kwargs:
        item = kwargs['instance']

        # check if its empty field

        if not item.colors.all().exists():

            pink, created = Color.objects.get_or_create(name='pink')

            # add to instance:
            item.colors.add(pink)
            item.save()
