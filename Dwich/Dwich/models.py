from django.db import models
from django.contrib.auth.models import User


class PickupSlot(models.Model):
    time_slot = models.TimeField()
    remaining_capacity = models.IntegerField(default=3)
    max_capacity = models.IntegerField(default=3)

    def __str__(self) -> str:
        return str(self.time_slot.strftime("%H:%M")) + ", " + str(self.remaining_capacity)


class Commande(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    numero = models.CharField(max_length=60)
    prix = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    note = models.TextField(blank=True, null=True)
    pickup_slot = models.ForeignKey(PickupSlot, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.client) + ", " + str(self.pickup_slot)

class Item(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    nom = models.CharField(max_length=120)
    prix = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.nom}, {self.commande.pickup_slot.time_slot.strftime('%H:%M')}, {self.commande.client}"


