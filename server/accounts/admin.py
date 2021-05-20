from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# admin을 User model 이용해서 등록 
admin.site.register(User, UserAdmin)
