from django.db import models

# Create your models here.

class tbl_register(models.Model):
    uname=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    phone=models.IntegerField()
    
    class meta:
        db_table="tbl_register"
#tbl for user choice
class tbl_event(models.Model):
    plan_name=models.CharField(max_length=30)
    event_name=models.CharField(max_length=30)
    hotel_name=models.CharField(max_length=50)
    location=models.CharField(max_length=100)
    date=models.CharField(max_length=50)
    time=models.CharField(max_length=50)
    people_count=models.IntegerField()
    user_id=models.CharField(max_length=100)
    total_amount=models.IntegerField()
    status=models.CharField(max_length=100)

    class meta:
        db_table="tbl_event"
#table for plans
class tbl_category(models.Model):
    category_type=models.CharField(max_length=30)
    image=models.FileField()
    food=models.IntegerField()
    price=models.IntegerField()

    class meta:
        db_table="tbl_category"

class tbl_booking(models.Model):
    package_name=models.CharField(max_length=50)
    event_name=models.CharField(max_length=30)
    price=models.IntegerField()
    status=models.CharField(max_length=30)

    class meta:
        db_table="tbl_booking"

class tbl_payment(models.Model):
    booking_id=models.IntegerField()
    event_name=models.CharField(max_length=50)
    price=models.IntegerField()
    status=models.CharField(max_length=30)
    user_id=models.CharField(max_length=100)

    
    class meta:
        db_table="tbl_payment"
