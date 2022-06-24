from django.contrib import admin
from .models import TC_profile, TC_user, Follow

admin.site.register(TC_user)
admin.site.register(TC_profile)
admin.site.register(Follow)

# Register your models here.
