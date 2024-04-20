from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import AddShowForm
from . import models

# Create your views here.

def add_notes_view(request):

    if request.method == 'POST':
        form = AddShowForm(request.POST)

        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect(reverse('notes:show_notes'))
        
    else:
        form = AddShowForm()

    return render(request,'notes/add_notes.html',context={'form':form})


def show_notes_view(request):
    all_notes = models.AddShow.objects.all()
    context = {'all_notes':all_notes}
    return render(request,'notes/show_notes.html',context=context)