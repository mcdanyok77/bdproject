from django.shortcuts import render, redirect
from .models import Outlet, Client, Rent, MonthlyPayment
from django.db.models import Q
from django.db.utils import IntegrityError
from django.http import HttpResponseRedirect



def main_page(request):
    return render(request, 'main.html')

# Представления для страницы торговых точек
def outlets_page(request):
    if request.method == 'POST':
        keyword = request.POST.get('keyword')
        if 'cancel' in request.POST:
            data = Outlet.objects.all()
        else:
            data = Outlet.objects.filter(Q(floor=keyword) | Q(id=keyword))
    else:
        data = Outlet.objects.all()
    return render(request, 'outlets.html', {'data': data})

# Добавление торговых точек
def add_outlet(request):
    if request.method == 'POST':
        new_floor = request.POST['new_floor']
        new_area = request.POST['new_area']
        new_price = request.POST['new_priceDay']
        new_outlets_id = request.POST['new_outletsID']

        try:
            outlet = Outlet.objects.create(
                floor=new_floor,
                area=new_area,
                priceDay=new_price,
                outletsID=new_outlets_id
            )
            outlet.save()
        except IntegrityError as e:
            # Обработка ошибки IntegrityError
            return HttpResponse('Ошибка: ' + str(e))
        
        return redirect('outlets')
    else:
        return render(request, 'add_outlet.html')

# Изменение торговых точек
def edit_outlet(request, outlet_id):
    if request.method == 'POST':
        new_floor = request.POST['new_floor']
        new_area = request.POST['new_area']
        new_price = request.POST['new_priceDay']

        outlet = Outlet.objects.get(id=outlet_id)
        outlet.floor = new_floor
        outlet.area = new_area
        outlet.priceDay = new_price
        outlet.save()

        return redirect('outlets')
    else:
        outlet_data = Outlet.objects.get(id=outlet_id)
        return render(request, 'edit_outlet.html', {'outlet_data': outlet_data})

# Удаление торговых точек
def delete_outlet(request, outlet_id):
    try:
        outlet = Outlet.objects.get(id=outlet_id)
        outlet.delete()
        return HttpResponseRedirect('/outlets/')  # Перенаправление на страницу торговых точек
    except Outlet.DoesNotExist:
        raise Http404("Торговая точка не найдена")

# Представления для страницы клиентов
def clients_page(request):
    if request.method == 'POST':
        keyword = request.POST.get('keyword')
        data = Client.objects.filter(Q(name=keyword) | Q(phoneNumber=keyword))
    else:
        data = Client.objects.all()
    return render(request, 'clients.html', {'data': data})

# Добавление клиентов
def add_client(request):
    if request.method == 'POST':
        new_name = request.POST['new_name']
        new_phoneNumber = request.POST['new_phoneNumber']
        new_adres = request.POST['new_adres']
        new_client_id = request.POST['new_clientID']

        try:
            client = Client.objects.create(
                name=new_name,
                phoneNumber=new_phoneNumber,
                adres=new_adres,
                clientID=new_client_id
            )
            client.save()
        except IntegrityError as e:
            # Обработка ошибки IntegrityError
            return HttpResponse('Ошибка: ' + str(e))
        
        return redirect('clients')
    else:
        return render(request, 'add_client.html')

# Изменение клиентов
def edit_client(request, client_id):
    if request.method == 'POST':
        new_name = request.POST['new_name']
        new_phoneNumber = request.POST['new_phoneNumber']
        new_adres = request.POST['new_adres']

        client = Client.objects.get(id=client_id)
        client.name = new_name
        client.phoneNumber = new_phoneNumber
        client.adres = new_adres
        client.save()

        return redirect('clients')
    else:
        client_data = Client.objects.get(id=client_id)
        return render(request, 'edit_client.html', {'client_data': client_data})

# Удаление клиентов
def delete_client(request, outlet_id):
    try:
        outlet = Client.objects.get(id=outlet_id)
        outlet.delete()
        return HttpResponseRedirect('/clients/')  # Перенаправление на страницу торговых точек
    except Client.DoesNotExist:
        raise Http404("Торговая точка не найдена")
    
# Представление для страницы аренды
def rent_page(request):
    if request.method == 'POST':
        keyword = request.POST.get('keyword')
        data = Rent.objects.filter(Q(client__name=keyword) | Q(outlet__id=keyword))
    else:
        data = Rent.objects.all()
    return render(request, 'rent.html', {'data': data})

# Добавление аренды
def add_rent(request):
    if request.method == 'POST':
        new_client = request.POST['new_client']
        new_outlet = request.POST['new_outlet']
        new_rentalPeriod = request.POST['new_rentalPeriod']
        new_rent_id = request.POST['new_rentID']

        try:
            rent = Rent.objects.create(
                client=new_client,
                outlet=new_outlet,
                rentalPeriod=new_rentalPeriod,
                rentID=new_rent_id
            )
            rent.save()
        except IntegrityError as e:
            # Обработка ошибки IntegrityError
            return HttpResponse('Ошибка: ' + str(e))
        
        return redirect('rent')
    else:
        return render(request, 'add_rent.html')

# Изменение аренды
def edit_rent(request, rent_id):
    if request.method == 'POST':
        new_client = request.POST['new_client']
        new_outlet = request.POST['new_outlet']
        new_rentalPeriod = request.POST['new_rentalPeriod']

        rent = Rent.objects.get(id=rent_id)
        rent.client = new_client
        rent.outlet = new_outlet
        rent.rentalPeriod = new_rentalPeriod
        rent.save()

        return redirect('rent')
    else:
        rent_data = Rent.objects.get(id=rent_id)
        return render(request, 'edit_rent.html', {'rent_data': rent_data})

# Представление для страницы ежемесячных платежей
def monthlypayment_page(request):
    if request.method == 'POST':
        keyword = request.POST.get('keyword')
        data = MonthlyPayment.objects.filter(Q(rent__id=keyword) | Q(sumPayment=keyword))
    else:
        data = MonthlyPayment.objects.all()
    return render(request, 'monthlypayment.html', {'data': data})
