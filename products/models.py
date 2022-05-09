from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = "menu"

class Categorys(models.Model):
    name = models.CharField(max_length=45)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    class Meta:
        db_table = "categories"


class Allergy(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = "allergy"


class Drinks(models.Model):
    korean_name = models.CharField(max_length=45)
    english_name = models.CharField(max_length=45)
    description = models.TextField()
    category = models.ForeignKey(Categorys, on_delete=models.CASCADE)
    allergydrink = models.ManyToManyField(Allergy, through="Allergy_Drink")

    class Meta:
        db_table = "drinks"


class Allergy_Drink(models.Model):
    allergy = models.ForeignKey(Allergy, on_delete=models.CASCADE)
    drink = models.ForeignKey(Drinks, on_delete=models.CASCADE)

    class Meta:
        db_table = "allergy_drinks"


class Nutritions(models.Model):
    one_serving_kca = models.DecimalField(max_digits = 10, decimal_places = 2)
    sodium_mg = models.DecimalField(max_digits = 10, decimal_places = 2)
    saturated_gat_g = models.DecimalField(max_digits = 10, decimal_places = 2)
    drink = models.OneToOneField(Drinks, on_delete=models.CASCADE)

    class Meta:
        db_table = "nutritions"

class Images(models.Model):
    image_url = models.CharField(max_length=2000)        
    drink = models.ForeignKey(Drinks, on_delete=models.CASCADE)

    class Meta:
        db_table = "images"

