from django.db import models
from django.utils.translation import gettext_lazy as _


class Leverancier(models.Model):
    leverancier = models.CharField(max_length=256)
    # TODO: Icon misschien later toevoegen

    def __str__(self):
        return self.leverancier


class Category(models.Model):
    class CategoryChoices(models.TextChoices):
        BRONNEN = 'BR', _('Bronnen')
        LAGEOPWEKKING = 'LO', _('Lage opwekking')
        HOGEOPWEKKING = 'HO', _('Hoge opwekking')
        LAGEAFGIFTE = 'LA', _('Lage afgifte')
        HOGEAFGIFTE = 'HA', _('Hoge afgifte')

    category = models.CharField(max_length=2, choices=CategoryChoices.choices)
    sub_category = models.CharField(max_length=64) #TODO: Unique in combination with category.

    def __str__(self):
        return f'{self.category} {self.sub_category}'


class Product(models.Model):
    productnr = models.CharField(max_length=256)
    leverancier_id = models.ForeignKey('Leverancier', models.CASCADE)
    type = models.CharField(max_length=64)  # TODO: product line item type!

    sub_category = models.ForeignKey('Category', models.CASCADE)

    vermogen = models.FloatField()
    belasting = models.FloatField()
    rendement = models.FloatField()  # TODO: Misschien berekenbaar met vermogen/belasting*100

    def __str__(self):
        return f'{self.leverancier_id.leverancier} {self.type} {self.productnr}'
# class KeuzeSchema(models.Model):
#     pass
# class KeuzeSchemaItems(models.Model):
#     pass
# class Gebouw(models.Model):
#     pass
