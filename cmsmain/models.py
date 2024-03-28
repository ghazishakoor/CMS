from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Subject(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    


# Term ------------------------------
class Term(models.Model):
    term_code = models.CharField(max_length=20, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.term_code



# Location ---------------------------
class Location(models.Model):
    location_code = models.CharField(max_length=10, unique=True, null=True, blank=True)
    building = models.CharField(max_length=20, null=True, blank=True)
    room = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f'{self.building} - {self.room}'



# Student -----------------------------------
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subjects  = models.ManyToManyField(Subject, related_name='students')
    student_number = models.PositiveIntegerField(unique=True, null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, null=True, blank=True)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=50)
    passport_number = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    enrolment_date = models.DateField()
    picture = models.ImageField(upload_to='uploads/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'



# Contact ----------------------------------------
class Contact(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, default=None)
    full_name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    relationship = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.full_name



# Teacher ---------------------------------------------
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject, related_name='teachers')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=100)
    date_joined = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'


# CourseClass -------------------------------------------
class CourseClass(models.Model):
    class_code = models.CharField(max_length=20)
    class_name = models.CharField(max_length=30)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='classes')
    term = models.ForeignKey(Term, on_delete=models.CASCADE, related_name='classes')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='classes')
    students = models.ManyToManyField(Student, related_name='classes', blank=True)

    def __str__(self):
        return f"{self.class_name}"


# Assignment ----------------------------------------------
class Assignment(models.Model):
    course_class = models.ForeignKey(CourseClass, on_delete=models.CASCADE, related_name='assignments', null=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()

    def __str__(self):
        return self.name


# Assignmark ------------------------------------------------
class AssignMark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='assignmarks', null=True, blank=True)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    mark = models.DecimalField(max_digits=5, decimal_places=2)
    remark = models.TextField(null=True, blank=True)
    
    class Meta:
        # Add a unique constraint on the combination of student and assignment
        constraints = [
            models.UniqueConstraint(fields=['student', 'assignment'], name='unique_student_assignment')
        ]
    
    def __str__(self):
        return f'{self.student} - {self.assignment}'


# Exam -----------------------------------------------------
class Exam(models.Model):
    course_class = models.ForeignKey(CourseClass, on_delete=models.CASCADE, related_name='exams', null=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='exams', null=True, blank=True)
    date = models.DateField()

    def __str__(self):
        return self.name


# Exam Mark ----------------------------------------------------
class ExamMark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='exammarks', null=True, blank=True)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='exammarks')
    mark = models.DecimalField(max_digits=5, decimal_places=2)
    remark = models.TextField(null=True, blank=True)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['student', 'exam'], name='unique_student_exam')
        ]
    
    def __str__(self):
        return f"{self.student} - {self.exam}"


# Test ---------------------------------------------------------
class Test(models.Model):
    course_class = models.ForeignKey(CourseClass, on_delete=models.CASCADE, related_name='tests', null=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField()

    def __str__(self):
        return self.name


# TestMark ----------------------------------------------------
class TestMark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='testmarks', null=True, blank=True)
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='testmarks')
    mark = models.DecimalField(max_digits=5, decimal_places=2)
    remark = models.TextField(null=True, blank=True)
    
    class Meta:
        # Add a unique constraint on the combination of student and test
        constraints = [
            models.UniqueConstraint(fields=['student', 'test'], name='unique_student_test')
            ]


    def __str__(self):
        return f"{self.student} - {self.test}"


# Report ------------------------------------------------------
class Report(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    grade = models.DecimalField(max_digits=5, decimal_places=2)
    remarks = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.student} {self.grade}'

# Program ----------------------------------------------------
class Program(models.Model):
    program_code = models.CharField(max_length=20)
    program_name = models.CharField(max_length=50)
    subjects = models.ManyToManyField(Subject)
    
    def __str__(self):
        return self.program_name



    
