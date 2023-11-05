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

# Представление для страницы аренды
def rent_page(request):
    if request.method == 'POST':
        keyword = request.POST.get('keyword')
        data = Rent.objects.filter(Q(client__name=keyword) | Q(outlet__id=keyword))
    else:
        data = Rent.objects.all()
    return render(request, 'rent.html', {'data': data})

# Представление для страницы ежемесячных платежей
def monthlypayment_page(request):
    if request.method == 'POST':
        keyword = request.POST.get('keyword')
        data = MonthlyPayment.objects.filter(Q(rent__id=keyword) | Q(sumPayment=keyword))
    else:
        data = MonthlyPayment.objects.all()
    return render(request, 'monthlypayment.html', {'data': data})
