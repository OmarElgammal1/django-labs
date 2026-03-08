from django.contrib import admin

# Register your models here.
from .models import Author, Student
from courses.models import Course


class CourseInline(admin.TabularInline):
    model = Course.students.through
    extra = 1


class StudentAdmin(admin.ModelAdmin):
    inlines = [CourseInline]


admin.site.register(Author)
admin.site.register(Student, StudentAdmin)