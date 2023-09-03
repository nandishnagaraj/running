from django.shortcuts import get_object_or_404

from trainingplans.models import TrainingPlans

# Create your views here.
def trainingplans(request,pk):
    plan = get_object_or_404(TrainingPlans,pk)
    print(plan)
    