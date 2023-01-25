from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404 

from laboratories.models import Laboratory
from laboratories.forms import LaboratoryForm

# Create your views here.
def index(request):
    context = {
        'laboratories': Laboratory.objects.all().order_by('-id')
    }

    return render(request, 'laboratories/index.html', context)


def create(request):
    form = LaboratoryForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        laboratory = Laboratory.objects.create(
            name=form.cleaned_data['name']
        )

        return redirect('laboratories:index')

    context = {
        'form': form
    }

    return render(request, 'laboratories/create.html', context)


def detail(request, pk):
    pass


def delete(request, pk):
    laboratory = get_object_or_404(Laboratory, pk=pk)
    laboratory.delete()

    return redirect('laboratories:index')


def update(request, pk):
    laboratory = get_object_or_404(Laboratory, pk=pk)
    form = LaboratoryForm(request.POST or None, initial={
        'name': laboratory.name
    })

    if request.method == 'POST' and form.is_valid():
        laboratory.name = form.cleaned_data['name']
        laboratory.save()

        return redirect('laboratories:index')

    context = {
        'form': form,
        'laboratory': laboratory
    }

    return render(request, 'laboratories/update.html', context)