from django.db import models

class Outlet(models.Model):
    outletsID = models.AutoField(primary_key=True)
    floor = models.IntegerField()
    area = models.FloatField()
    priceDay = models.FloatField()

    def __str__(self):
        return str(self.outletsID)

class Client(models.Model):
    clientID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=222)
    adres = models.CharField(max_length=255)
    
    def __str__(self):
        return str(self.clientID)

class Rent(models.Model):
    rentID = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    outlet = models.ForeignKey(Outlet, on_delete=models.CASCADE)
    rentalPeriod = models.IntegerField()
    
    def __str__(self):
        return str(self.rentID)

class MonthlyPayment(models.Model):
    paymentID = models.AutoField(primary_key=True)
    sumPayment = models.FloatField()
    datePayment = models.DateField()
    rent = models.ForeignKey(Rent, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.paymentID)
