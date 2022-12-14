from django.db import models
from django.conf import settings



class Teacher(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.user
    

class Subject(models.Model):
    name = models.CharField(max_length=64)
    
    def __str__(self):
        return self.name

class School_Class(models.Model):
    level = models.IntegerField(default=1)
    name = models.CharField(max_length=2)
    course = models.ManyToManyField("Course")

    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    school_class = models.ForeignKey(School_Class, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    
class Course(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    level = models.IntegerField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    number_of_lesson_in_week = models.IntegerField()


    def __str__(self):
        return f"{self.subject}:{self.level}:{self.teacher.user}"

class Grade(models.Model):
    GRADES = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
    )
    
    grade = models.IntegerField(choices=GRADES)
    course = models.ManyToManyField(Course)
    student = models.ManyToManyField(Student)

# class Lesson(models.Model):
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
    
#     is_realized = models.BooleanField(default=False)
#     date = models.DateField()





    



