from django.contrib import admin
from .models import PickupSlot, Item, Commande

class PickupSlotAdmin(admin.ModelAdmin):
    list_display = ['time_slot', 'remaining_capacity', 'max_capacity']  # Afficher les champs dans le panneau admin

admin.site.register(PickupSlot, PickupSlotAdmin)
admin.site.register(Item)
admin.site.register(Commande)