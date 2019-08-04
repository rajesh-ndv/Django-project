from django.shortcuts import render,get_object_or_404
from .models import Listing
from realtors.models import Realtor
from .choices import bedroom_choices,price_choices,state_choices
# Create your views here.
def index(request):
    listings=Listing.objects.all()
    return render(request,'listings/listings.html',{'listings':listings})
def listing(request,listing_id):
    listing=get_object_or_404(Listing,pk=listing_id)
    return render(request,'listings/listing.html',{'context':listing})
def search(request):
    queryset_list=Listing.objects.order_by('-list_date')
    if 'city' in request.GET:
        city=request.GET['city']
        if city:
            queryset_list=queryset_list.filter(city__iexact=city)

    return render(request,'listings/search.html',{'bedroom':bedroom_choices,'price':price_choices,'state':state_choices,'listings':queryset_list})
