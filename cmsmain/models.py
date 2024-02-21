from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Subject(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subjects  = models.ManyToManyField(Subject)
    student_number = models.PositiveIntegerField(null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, null=True, blank=True)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=50)
    passport_number = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    enrolment_date = models.DateField()
    picture = models.ImageField(upload_to='uploads/', null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Contact(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, default=None)
    full_name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    relationship = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.full_name


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=100)
    date_joined = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Term(models.Model):
    term_code = models.CharField(max_length=20, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.term_code


class Assignment(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()

    def __str__(self):
        return self.name


class AssignMark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    mark = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return f'{self.student} - {self.assignment}'


class Exam(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name


class ExamMark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    mark = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.student} - {self.exam}"


class Report(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    grade = models.DecimalField(max_digits=5, decimal_places=2)
    remarks = models.TextField()

class Program(models.Model):
    program_code = models.CharField(max_length=20)
    program_name = models.CharField(max_length=50)
    subjects = models.ManyToManyField(Subject)
    
    def __str__(self):
        return self.program_name