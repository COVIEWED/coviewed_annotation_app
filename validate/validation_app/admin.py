from django.contrib import admin

from .models import claim, user_validation

admin.site.register(claim)
admin.site.register(user_validation)
# Register your models here.
