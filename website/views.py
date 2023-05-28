from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def index(request):
    return render(request, "index.html")
'''Returns the index.html page'''


def contact(request):
    return render(request, "contact.html")
'''Returns the contact.html page'''



def shipping(request):
    return render(request, "shipping.html")
'''Returns the shipping.html page'''
