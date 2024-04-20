from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import ActionsForm
from . import models

# Create your views here.
def home_view(request):
    
    if request.method == 'POST':
        form = ActionsForm(request.POST)

        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect(reverse('tracker:show'))
        
    else:
        form = ActionsForm()

    return render(request,'perform/home.html',context={'form':form})

def show_view(request):
    all_task = models.Actions.objects.all()
    context = {'all_task':all_task}
    return render(request,'perform/show.html',context=context)

def delete_tasks_view(request, date):
    if request.method == 'POST':
        # Get tasks associated with the given date
        tasks_to_delete = models.Actions.objects.filter(date=date)
        # Delete the tasks
        tasks_to_delete.delete()
        # Redirect back to the show page
        return redirect('tracker:show')
    # If the request method is not POST, render an error page or handle