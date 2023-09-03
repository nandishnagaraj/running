from django.http import HttpResponse
from django.shortcuts import render

from trainingplans.models import TrainingPlans

def home(request):
    plans = TrainingPlans.objects.all()    
    context = {
        'plans': plans,
    }
    return render(request, "home.html", context)

