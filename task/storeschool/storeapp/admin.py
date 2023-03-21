from .models import Department, Purpose, Details, Course
from django.contrib import admin

# Register your models here.
admin.site.register(Department)
admin.site.register(Details)
admin.site.register(Course)
admin.site.register(Purpose)
