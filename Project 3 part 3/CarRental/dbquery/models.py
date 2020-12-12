# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Customer(models.Model):
    custid = models.AutoField(db_column='CustID', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=15)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=14)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customer'


class Rate(models.Model):
    type = models.IntegerField(db_column='Type')  # Field name made lowercase.
    category = models.IntegerField(db_column='Category')  # Field name made lowercase.
    weekly = models.IntegerField(db_column='Weekly')  # Field name made lowercase.
    daily = models.IntegerField(db_column='Daily')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rate'


class Rental(models.Model):
    custid = models.ForeignKey(Customer, models.DO_NOTHING, db_column='CustID')  # Field name made lowercase.
    vehicleid = models.ForeignKey('Vehicle', models.DO_NOTHING, db_column='VehicleID')  # Field name made lowercase.
    startdate = models.CharField(db_column='StartDate', max_length=10)  # Field name made lowercase.
    orderdate = models.CharField(db_column='OrderDate', max_length=10)  # Field name made lowercase.
    rentaltype = models.IntegerField(db_column='RentalType', blank=True, null=True)  # Field name made lowercase.
    qty = models.IntegerField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    returndate = models.CharField(db_column='ReturnDate', max_length=10)  # Field name made lowercase.
    totalamount = models.TextField(db_column='TotalAmount')  # Field name made lowercase. This field type is a guess.
    paymentdate = models.CharField(db_column='PaymentDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    returned = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rental'


class Vehicle(models.Model):
    vehicleid = models.CharField(db_column='VehicleID', primary_key=True, max_length=17, blank=True, null=False)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=15)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type')  # Field name made lowercase.
    category = models.IntegerField(db_column='Category', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vehicle'
