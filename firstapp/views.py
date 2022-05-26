from django.shortcuts import render
from .models import Order
from .forms import OrderForm
from cms.models import CmsSlider


# Create your views here.

def first_page(request):
    slider_list = CmsSlider.objects.all()
    return render(request, 'index.html', {'slider_list': slider_list,
                                          })
