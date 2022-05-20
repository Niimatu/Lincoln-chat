from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import s1,s2
from .models import stu

# Register your models here.
class sa(UserAdmin):
    add_form = s1
    form = s2
    list_display = ['student','username']
    model = stu
    
    
admin.site.register(stu,sa)  
#admin.site.register(sa)  