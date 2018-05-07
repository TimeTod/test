from django.db import models

# Create your models here.
class Todo(models.Model):
    is_active = models.BooleanField(default=True)

    title = models.CharField(max_length=256)
    finish = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Employee(models.Model):
    '''雇员'''
    name = models.CharField(max_length=64)
    email = models.EmailField()

    todo = models.ForeignKey(Todo,on_delete=models.CASCADE)

    def __str__(self):
        return "{}-{}".format(self.todo_id,self.email)