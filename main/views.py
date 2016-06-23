from django.shortcuts import render
from main.models import *
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.template.loader import render_to_string
from django.shortcuts import render
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from datetime import *
import random
import string
from django.core.mail import send_mail
from django.core.mail import EmailMessage

# Create your views here.

def home(request):
    category = Category.objects.all()
    context = {
        'sitename': 'INVIDIA CLOTHES',
        'categories': category,
    }
    return HttpResponse(render_to_string('home.html', context))


def item(request, alias):
    try:
        product = Item.objects.get(alias=alias)
    except:
        raise Http404('Объект не найден')
    context = {
        'product': product,
    }
    return HttpResponse(render_to_string('item.html', context))


def get_category(request, alias):
    try:
        category = Category.objects.get(alias=alias)
        products = Item.objects.filter(category=category)
    except:
        raise Http404('Объекты не найден')
    context = {
        'products': products,
        'category': category,
    }
    return HttpResponse(render_to_string('index.html', context))

def order(request):
    context = {
    }
    return HttpResponse(render_to_string('basket.html', context))

# def new_order(request):
#     if request.method == "POST":
#         form = OrderCreateForm(request.POST)
#         if form.is_valid():
#             order = form.save()
#             order.order = 


#     form = OrderCreateForm()
#     return render(request, 'basket.html', {'form' : form})