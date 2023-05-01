from django.shortcuts import render
from .models import Quote
# Create your views here.

def home(request):
    quotes = Quote.objects.order_by("?")[0]
    return render(request, 'index.html', {'quotes':quotes})