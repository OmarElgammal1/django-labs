"""
Seed script — run with: python manage.py seed_data
Creates sample Instructors, Students, and Courses with M2M relationships.
"""
from django.core.management.base import BaseCommand
from students.models import Student
from instructors.models import Instructor
from courses.models import Course


class Command(BaseCommand):
    help = 'Seed the database with sample instructors, students, and courses'

    def handle(self, *args, **options):
        # ---------- Instructors ----------
        i1 = Instructor.objects.get_or_create(first_name='Ahmed', last_name='Hassan', defaults={'bio': 'Machine Learning expert'})[0]
        i2 = Instructor.objects.get_or_create(first_name='Sara', last_name='Ali', defaults={'bio': 'Web Development specialist'})[0]
        i3 = Instructor.objects.get_or_create(first_name='Mohamed', last_name='Youssef', defaults={'bio': 'Data Engineering instructor'})[0]

        # ---------- Students ----------
        s1 = Student.objects.get_or_create(first_name='Omar', last_name='Elgammal')[0]
        s2 = Student.objects.get_or_create(first_name='Nour', last_name='Ibrahim')[0]
        s3 = Student.objects.get_or_create(first_name='Layla', last_name='Mahmoud')[0]
        s4 = Student.objects.get_or_create(first_name='Youssef', last_name='Khaled')[0]
        s5 = Student.objects.get_or_create(first_name='Mona', last_name='Saeed')[0]

        # ---------- Courses ----------
        c1 = Course.objects.get_or_create(title='Python Programming', defaults={'description': 'Learn Python from scratch'})[0]
        c2 = Course.objects.get_or_create(title='Django Web Development', defaults={'description': 'Build web apps with Django'})[0]
        c3 = Course.objects.get_or_create(title='Machine Learning', defaults={'description': 'Intro to ML algorithms'})[0]

        # ---------- M2M relationships ----------
        c1.instructors.add(i1, i2)
        c1.students.add(s1, s2, s3)

        c2.instructors.add(i2)
        c2.students.add(s1, s4, s5)

        c3.instructors.add(i1, i3)
        c3.students.add(s2, s3, s4, s5)

        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))
