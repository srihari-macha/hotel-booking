# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def get_data(request):
    price=request.POST.get('price')
    return price

def hotel_home(request):
    return render(request,'hotels_home.html')

def hotel_price_home(request):
    if request.method=='POST':
        price=request.POST.get('price')
        print price
    return render(request,'hotels_price.html',{'price':price})


def hotel_price(request):
    if request.method=='POST':
        num_days=request.POST['days']
        num_rooms=request.POST['rooms']
        price=4500
        num_days1=int(num_days)
        num_rooms1=int(num_rooms)
        total_price=num_days1*num_rooms1*price
        return HttpResponse(total_price)
