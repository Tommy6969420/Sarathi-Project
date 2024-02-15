from django.contrib import admin
from.models import Teacher,Class, Student 
# Register your models here.

class TeacherAdmin(admin.ModelAdmin):
    list_display=['teacher_name',"contact_number"]
    search_fields=['teacher_name']
    list_filter=['subject']

class StudentAdmin(admin.ModelAdmin):
    list_display=['name','for_class','parents_name','address']
    search_fields= ['name','for_class','parents_name','address']
    list_filter=['for_class','address',]

admin.site.register(Class)
admin.site.register(Student,StudentAdmin)
admin.site.register(Teacher,TeacherAdmin)