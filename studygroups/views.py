from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from .models import Event
from .forms import *

def index(request):
    print(Event.objects.all())
    return render(request, 'studygroups/index.html', {'events': Event.objects.all()})

def create(request):
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            info  = form.cleaned_data['info']
            location  = form.cleaned_data['location']
            date  = form.cleaned_data['date']
            start_time  = form.cleaned_data['start_time']
            end_time  = form.cleaned_data['end_time']
            print(name, info, location)
            item = Event(name=name, info=info, location=location,
                         date=date, start_time=start_time, end_time=end_time)
            item.save()
        return HttpResponseRedirect(reverse('index'))
    else:
        form = CreateForm()
        context = {'form': form}
        return render(request, 'studygroups/create.html', context)
