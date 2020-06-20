from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices, bedroom_choices, state_choices

from listings.models import Listing
from rltrs.models import Rltr 


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }
    return render(request,'pages/index.html', context )

def about(request):
    # Get all realtors
    rltrs = Rltr.objects.order_by('-hire_date')
    
    # Get MVP status
    mvp_rltrs = Rltr.objects.all().filter(is_mvp=True)

    context = {
        'rltrs': rltrs,
        'mvp_rltrs': mvp_rltrs 
    }
    return render(request,'pages/about.html', context )
