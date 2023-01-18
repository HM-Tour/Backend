from django.contrib import admin
from .models import CustomUser


from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    add_fieldsets=((
        'None',{
            'fields':('username','email','password1','password2'),
        }
    ),(
        'personal information',{
            'fields':('first_name','last_name'),
        }
    ),)



admin.site.register(CustomUser,CustomUserAdmin)