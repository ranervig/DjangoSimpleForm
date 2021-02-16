from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    school = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"First Name: {self.first_name} Last Name: {self.last_name} School: {self.school}"

