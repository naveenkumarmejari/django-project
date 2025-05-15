from django.db import models

# Create your models here.
class task_details(models.Model):
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=300)
    email=models.EmailField( max_length=254)
    uername=models.CharField(max_length=200)
    mobilenum=models.BigIntegerField()
    password=models.CharField(max_length=100)
    cpassword=models.CharField(max_length=200)


# class todoapp(models.Model):
#     todotitel=models.CharField(max_length=200)
#     status=models.CharField(max_length=100,choices=[("Not started","Not started"),("IN progeress","IN progeress"),("completed","completed")])  
#     defalul="NOt started"
#     due=models.TextField()   



class Task(models.Model):
     title = models.CharField(max_length=255)
     status = models.CharField(
    max_length=20,
    choices=[("Not started", "Not started"), ("In progress", "In progress"), ("Completed", "Completed")],
    default="Not started"
)
     due_date = models.DateField()
     def _str_(self):
          return self.title