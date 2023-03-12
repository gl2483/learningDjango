from django.db import models

class Personel(models.Model):
    fist_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.fist_name + " " + self.last_name

class Department(models.Model):
    dept_name = models.CharField(max_length=200)
    dept_head = models.ForeignKey(Personel, default=0, on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.dept_name

class Employee(Personel):  
    dept = models.ForeignKey(Department, default=0, on_delete=models.SET_DEFAULT)
    manager = models.ForeignKey(Personel, default=0, on_delete=models.SET_DEFAULT)

    def dept(self):
        return self.dept

    def manager(self):
        return self.manager
