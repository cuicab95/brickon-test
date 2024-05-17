from django.db import models
import uuid
from django.utils import timezone

# Create your models here.


class BasicMixin(models.Model):
    """
    Datos básicos para los models, se puede heredar para no repetir los fields
    ejemplo: class Product(BasicMixin)
    """
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SoftDeleteManager(models.Manager):
    """
    Listado de los registros:
    Por default te excluye los eliminados, para obtener solo los eliminados puedes hacer
    Modelo.objects.deleted()

    En caso de querer ver todos los registros puede hacer lo sig:
    Modelo.all_objects.all()
    """
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

    def deleted(self):
        return super().get_queryset().filter(is_deleted=True)


class SoftDeleteMixin(models.Model):
    """
    Eliminado de registros, puede ser de 2 maneras:
    lógico: que exista en la BD y tenga la bandera is_deleted=True
    ejemplo: instance.delete()

    Fisíco: que se elimine permanente de la BD
    ejemplo: instance.delete(force_delete=True)
    """
    is_deleted = models.BooleanField(default=False)

    def delete(self, force_delete=False, **kwargs):
        if force_delete:
            return super().delete(**kwargs)
        if not self.is_deleted:
            self.is_deleted = True
            self.save(update_fields=["is_deleted"])
        return self.is_deleted

    objects = SoftDeleteManager()
    all_objects = models.Manager()

    class Meta:
        abstract = True


class Product(BasicMixin, SoftDeleteMixin):
    """"
    Modelo para almacenar los productos
    NOTA: Podría extenderse más, agregar categorías, proveedor etc..
    """
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.FloatField()
    sku = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)




