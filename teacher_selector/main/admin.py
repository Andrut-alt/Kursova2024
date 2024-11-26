from django.contrib import admin
from .models import Teacher, Interest, Departament

class InterestAdmin(admin.ModelAdmin):
    list_display = ('name',)
    

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'departament')
    filter_horizontal = ('interests',)
    search_fields = ('name', 'email')
    list_filter = ('departament',)
    ordering = ('interests',)
   
    

class DepartamentAdmin(admin.ModelAdmin):
    list_display = ('departament',)

admin.site.register(Interest, InterestAdmin)
admin.site.register(Departament, DepartamentAdmin)
admin.site.register(Teacher, TeacherAdmin)