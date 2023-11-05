from django.contrib import admin
from myapp import models

admin.site.register([models.Outlet, models.Client, models.Rent, models.MonthlyPayment])

# Register your models here.
