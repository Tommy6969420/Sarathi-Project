from django.db import models
class Teacher(models.Model):
    teacher_name=models.CharField(max_length=30)
    subject=models.CharField(max_length=25)
    email=models.EmailField()
    contact_number=models.CharField(max_length=15)
    image=models.ImageField(upload_to='teachers/')
    def __str__(self):
        return f"{self.teacher_name} {self.contact_number}"
class Class(models.Model):
    name=models.CharField(max_length=10)
    def __str__(self):
        return f'{self.name}'
class Student(models.Model):
    name=models.CharField(max_length=64)
    for_class=models.ForeignKey(Class,on_delete=models.CASCADE)
    date_of_birth=models.DateField()
    parents_name=models.CharField(max_length=64)
    address=models.CharField(max_length=64)
    contact=models.CharField(max_length=10)
    def __str__(self):
        return f"{self.name} {self.for_class} "