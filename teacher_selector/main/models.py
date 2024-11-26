from django.db import models
from django.contrib.auth.models import User


class Interest(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Departament(models.Model):
    DEPARTAMENT_CHOICES = [
        ('Cистемного проектування', 'Cистемного проектування'),
        ('Радіофізики та комп’ютерних технологій', 'Радіофізики та комп’ютерних технологій'),
        ('Радіоелектронних і комп’ютерних систем', 'Радіоелектронних і комп’ютерних систем'),
        ('Оптоелектроніки та інформаційних технологій', 'Оптоелектроніки та інформаційних технологій'),
    ]
    departament = models.CharField(max_length=50, null=True, choices=DEPARTAMENT_CHOICES)

    def __str__(self):
        return self.departament if self.departament else "Без назви"

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    interests = models.ManyToManyField(Interest, blank=True)
    departament = models.ForeignKey(Departament, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    thesis_topic = models.CharField(max_length=200, null=True)
    full_name = models.CharField(max_length=100, null=True)
    course = models.IntegerField(null=True)

    def __str__(self):
        return self.user.username