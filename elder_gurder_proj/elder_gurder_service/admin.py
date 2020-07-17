from django.contrib import admin

from .models import CustomUser , LonelyPeople , Visitis


# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Visitis)
admin.site.register(LonelyPeople)

