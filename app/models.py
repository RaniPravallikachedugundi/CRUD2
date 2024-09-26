from django.db import models

# Create your models here.
class Student(models.Model):
    Name=models.CharField(max_length=50);
    Register_Number=models.CharField(max_length=19);
    Mail_id=models.CharField(max_length=20);
    Age=models.IntegerField();


    def __str__(self):
        return self.Name