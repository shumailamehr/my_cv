from django.contrib import admin

# Register your models here.
from.models import User_details

class AdminControl (admin.ModelAdmin):
    list_display = ('Name','Email','message')

admin.site.register(User_details,AdminControl)