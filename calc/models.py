from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Class(models.Model):
    user = models.ForeignKey( User ,on_delete=models.DO_NOTHING)
    classname = models.CharField(max_length=50)
    section = models.CharField(max_length=50)
    shift = models.CharField(max_length=50)
    total_students = models.models.PositiveIntegerField()
    
class Subject(models.Model):
    user = models.ForeignKey( User ,on_delete=models.DO_NOTHING)
    # image = models.ImageField(upload_to='pics', height_field=None, width_field=None, max_length=None)
    subject = models.CharField(max_length=50)
    classid = models.ForeignKey(Class , on_delete=models.DO_NOTHING)
class Student(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ForeignKey( User ,on_delete=models.DO_NOTHING)
    c_class = models.ForeignKey(Class , on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50)
    f_Name = models.CharField(max_length=50)
    cnic =  models.CharField(max_length=50)
    contact1 = models.CharField( max_length=50)
    contact2 = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    religion = models.CharField(max_length=50)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=50)
    admit_date = models.DateField(auto_now=False, auto_now_add=True)
    admit_class = models.CharField(max_length=50)
    current_class = models.CharField(max_length=50)
    section = models.CharField(max_length=50)
    shift = models.CharField(max_length=50)
    last_school = models.TextField()
    image =models.ImageField(upload_to='pics/', height_field=None, width_field=None, max_length=None)
    age = models.CharField(max_length=50)
    gr = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    image_counter = models.CharField(max_length=100)

class mystudent:
    name : str
    address : str
    cnic : str  

class Professor(models.Model):
    user = models.ForeignKey( User ,on_delete=models.DO_NOTHING)
    class_id = models.ForeignKey(Class , on_delete=models.DO_NOTHING)
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50)
    f_Name = models.CharField(max_length=50)
    cnic =  models.CharField(max_length=50)
    contact1 = models.CharField( max_length=50)
    contact2 = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    religion = models.CharField(max_length=50)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=50)
    joining_date = models.DateField(auto_now=False, auto_now_add=False)
    shift = models.CharField(max_length=50)
    image = models.ImageField(upload_to='pics/', height_field=None, width_field=None, max_length=None)
    age = models.IntegerField()
    status = models.CharField(max_length=50)
    education_level = models.CharField(max_length=50)
    email = models.EmailField( max_length=254)
    experience =models.IntegerField()
    #Account Detail
    bank_name = models.CharField(max_length=50)
    branch_code = models.IntegerField()
    account_number = models.CharField(max_length=50)
    image_counter = models.CharField(max_length=100)




class Others(models.Model):
    user = models.ForeignKey( User ,on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50)
    f_Name = models.CharField(max_length=50)
    cnic =  models.CharField(max_length=50)
    contact1 = models.CharField( max_length=50)
    contact2 = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    religion = models.CharField(max_length=50)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=50)
    joining_date = models.DateField(auto_now=False, auto_now_add=False)
    shift = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='pics/', height_field=None, width_field=None, max_length=None)
    age = models.IntegerField()
    status = models.CharField(max_length=50)
    education_level = models.CharField(max_length=50)
    email = models.EmailField( max_length=254)
    experience =models.IntegerField()
    #Account Detail
    bank_name = models.CharField(max_length=50)
    branch_code = models.IntegerField()
    account_number = models.CharField(max_length=50)
    image_counter = models.CharField(max_length=100)

class Salary(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    professor = models.ForeignKey(Professor, on_delete=models.DO_NOTHING,null=True)
    other = models.ForeignKey(Others, on_delete=models.DO_NOTHING,null=True)
    name = models.CharField(max_length=50)
    salary = models.IntegerField()
    month = models.CharField(max_length=50)
    payment_date = models.DateField(auto_now=False, auto_now_add=False)
    person = models.IntegerField()

    # shift2 = models.CharField(max_length=50)

class Expenses(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    exp_amount = models.IntegerField()
    exp_date = models.DateField(auto_now=False, auto_now_add=False)
    exp_description = models.TextField()
    exp_mon = models.CharField(max_length=50)

    # pass
    