from django.db import models
from students.models import Student
from instructors.models import Instructor

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    students = models.ManyToManyField(Student, related_name='courses')
    instructors = models.ManyToManyField(Instructor, related_name='courses')

    def __str__(self):
        return self.title
