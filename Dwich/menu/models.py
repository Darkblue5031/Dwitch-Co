from typing import Any
from django.db import models
from food.models import Dwich, Burger, Frite
from drink.models import Soft


# Create your models here.


class DwichMenu(models.Model):
    nom = models.ForeignKey(Dwich, on_delete=models.CASCADE, null=False)
    frites = models.ForeignKey(Frite, on_delete=models.CASCADE, null=False)
    prix = models.DecimalField(max_digits=4, decimal_places=2)
    en_ligne = models.BooleanField(default = False)
    du_moment = models.BooleanField(default = False)

    def __str__(self) -> str:
        return self.nom.nom +" " + self.frites.nom
    
    def __dict__(self) -> dict:
        return {
            'nom': self.nom,
            'frites': self.frites,
            'prix': self.prix.__float__(),
            'en_ligne': self.en_ligne,
            'du_moment': self.du_moment
        }


class DwichMenuSoft(models.Model):
    nom = models.ForeignKey(Dwich, on_delete=models.CASCADE, null=False)
    frites = models.ForeignKey(Frite, on_delete=models.CASCADE, null=False)
    boisson = models.ForeignKey(Soft, on_delete=models.CASCADE, null=False)
    prix = models.DecimalField(max_digits=4, decimal_places=2)
    en_ligne = models.BooleanField(default = False)
    du_moment = models.BooleanField(default = False)

    def __str__(self) -> str:
        return self.nom.nom +" " + self.frites.nom +" " + self.boisson.nom
    
    def __dict__(self) -> dict:
        return {
            'nom': self.nom,
            'frites': self.frites,
            'boisson': self.boisson,
            'prix': self.prix.__float__(),
            'en_ligne': self.en_ligne,
            'du_moment': self.du_moment
        }


class BurgerMenu(models.Model):
    nom = models.ForeignKey(Burger, on_delete=models.CASCADE, null=False)
    frites = models.ForeignKey(Frite, on_delete=models.CASCADE, null=False)
    prix = models.DecimalField(max_digits=4, decimal_places=2)
    en_ligne = models.BooleanField(default = False)
    du_moment = models.BooleanField(default = False)

    def __str__(self) -> str:
        return self.nom.nom +" " + self.frites.nom
    
    def __dict__(self) -> dict:
        return {
            'nom': self.nom,
            'frites': self.frites,
            'prix': self.prix.__float__(),
            'en_ligne': self.en_ligne,
            'du_moment': self.du_moment
        }

class BurgerMenuSoft(models.Model):
    nom = models.ForeignKey(Burger, on_delete=models.CASCADE, null=False)
    frites = models.ForeignKey(Frite, on_delete=models.CASCADE, null=False)
    boisson = models.ForeignKey(Soft, on_delete=models.CASCADE, null=False)
    prix = models.DecimalField(max_digits=4, decimal_places=2)
    en_ligne = models.BooleanField(default = False)
    du_moment = models.BooleanField(default = False)

    def __str__(self) -> str:
        return self.nom.nom +" " + self.frites.nom +" " + self.boisson.nom
    
    def __dict__(self) -> dict:
        return {
            'nom': self.nom,
            'frites': self.frites,
            'boisson': self.boisson,
            'prix': self.prix.__float__(),
            'en_ligne': self.en_ligne,
            'du_moment': self.du_moment
        }


class KidCorner(models.Model):
    menu_type = models.TextChoices("Viande", "Cordon_Bleu Steak")
    nom = models.CharField(blank=False, choices=menu_type, max_length=11)
    frites = models.ForeignKey(Frite, on_delete=models.CASCADE, null=False)
    prix = models.DecimalField(max_digits=4, decimal_places=2)
    en_ligne = models.BooleanField(default = False)
    du_moment = models.BooleanField(default = False)

    def __str__(self) -> str:
        return self.nom +" " + self.frites.nom
    
    def __dict__(self) -> dict:
        return {
            'nom': self.nom,
            'frites': self.frites,
            'prix': self.prix.__float__(),
            'en_ligne': self.en_ligne,
            'du_moment': self.du_moment
        }


class KidCornerSoft(models.Model):
    menu_type = models.TextChoices("Viande", "Cordon_Bleu Steak")
    nom = models.CharField(blank=False, choices=menu_type, max_length=11)
    frites = models.ForeignKey(Frite, on_delete=models.CASCADE, null=False)
    boisson = models.ForeignKey(Soft, on_delete=models.CASCADE, null=False)
    prix = models.DecimalField(max_digits=4, decimal_places=2)
    en_ligne = models.BooleanField(default = False)
    du_moment = models.BooleanField(default = False)

    def __str__(self) -> str:
        return self.nom +" " + self.frites.nom +" " + self.boisson.nom
    
    def __dict__(self) -> dict:
        return {
            'nom': self.nom,
            'frites': self.frites,
            'boisson': self.boisson,
            'prix': self.prix.__float__(),
            'en_ligne': self.en_ligne,
            'du_moment': self.du_moment
        }
