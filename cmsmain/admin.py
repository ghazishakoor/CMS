from django.contrib import admin
from .models import *

# Register your models here.
tables = [Student, Subject, Teacher, Program, Contact, Term, Exam,
          Assignment, Test, ExamMark, AssignMark, TestMark, Report, CourseClass, Location]
admin.site.register(tables)
