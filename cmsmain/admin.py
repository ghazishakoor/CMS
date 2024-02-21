from django.contrib import admin
from .models import *

# Register your models here.
tables = [Student, Subject, Teacher, Program, Contact, Term, Exam, Assignment, ExamMark, AssignMark, Report]
admin.site.register(tables)
