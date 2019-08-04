from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import bedroom_choices,price_choices,state_choices

# Create your views here.
def index(request):
    listings=Listing.objects.order_by('-list_date')[:3]
    return render(request,'pages/index.html',{'listings':listings,'state':state_choices,'bedroom':bedroom_choices,'price':price_choices})
def about(request):
    realtors=Realtor.objects.all()
    mvp_realtors=Realtor.objects.all().filter(is_mvp=True)
    return render(request,'pages/about.html',{'realtors':realtors,'mvp':mvp_realtors})
