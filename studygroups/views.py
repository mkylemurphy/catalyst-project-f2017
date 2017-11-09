from django.shortcuts import get_object_or_404, render
from .models import Event

def index(request):
    print(Event.objects.all())
    return render(request, 'studygroups/index.html', {'events': Event.objects.all()})
