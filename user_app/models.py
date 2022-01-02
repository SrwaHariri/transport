from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class BaseModel(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        'User',
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name='%(class)s_created_by'
    )
    updated_by = models.ForeignKey(
        'User',
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name='%(class)s_updated_by'
    )

    @staticmethod
    def update_instance(instance, data):
        for item in data.items():
            key = item[0]
            value = item[1]
            setattr(instance, key, value)
        instance.save()

    @classmethod
    def reorder_instance(cls, instance_ids: list, field: str, ):
        """
            A generic class method that is used to re-order a
            model field given an array of instance ids.

            :param instance_ids: An array of instance_ids of the model
            :param field: The model field that needs to be updated
        """

        objs = []
        for idx, instance_id in enumerate(instance_ids):
            instance = cls.objects.get(id=instance_id)
            setattr(instance, field, idx + 1)
            objs.append(instance)

        cls.objects.bulk_update(objs, fields=[field])


        class Meta:
            # This indicates that the model is abstract model and other models can inherit from it.
            abstract = True
            ordering = ['-id']