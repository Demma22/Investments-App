from django.shortcuts import render
from .models import *
from django.db.models import Sum
from decimal import Decimal

# Create your views here.




def index(request):
    # Query the database to get the required information
    total_deposit = Investment.objects.aggregate(Sum('deposit')).get('deposit__sum', 0)
    interest = Decimal('0.00324544') * total_deposit  # 10% interest on total_deposit
    running_investments = total_deposit + interest
   
    # Pass the data to the template for rendering
    return render(request, 'index.html', {
        'total_deposit': total_deposit,
        'interest': interest,
        'running_investments': running_investments,
    })
