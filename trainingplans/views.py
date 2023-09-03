from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from trainingplans.models import TrainingPlans

# Create your views here.
def trainingDetails(request,pk):
    plan = get_object_or_404(TrainingPlans,pk=pk)
    context = {
        'planDetail': plan,
    }
    return render(request, "selectedplan.html", context)