from django.contrib import admin

# Register your models 

from CSE.models import Student, GymMember

admin.site.register(Student)

admin.site.register(GymMember)