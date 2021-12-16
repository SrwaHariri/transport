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


@receiver(post_save, sender=TransportItem)
def SetDefaultColor(**kwargs):
        # unpack kwargs:
        item = kwargs['instance']

        # set color if field is empty:
        if not item.color.all():
            # get the resource pool department:
            pink = Color.objects.get(name='pink')

            # add to instance:
            item.color.add(pink)
            item.save()
