from django.shortcuts import render
from .models import Name
# Create your views here.
def home(request):
    names=Name.objects.all()
    return render(request,"home.html",{"names":names})
