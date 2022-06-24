from django.contrib import admin
from .models import TC_profile, TC_user

admin.site.register(TC_user)
admin.site.register(TC_profile)

# Register your models here.
