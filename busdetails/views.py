from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from busdetails.models import BusCompany


class BusCompaniesListView(ListView):
    model = BusCompany
    template_name = 'buses/list.html'
    context_object_name = 'buses'

class BusCompaniesCreateView(CreateView):
    model = BusCompany
    template_name = 'buses/create.html'
    fields = ('name','head_office','staff_count')
    success_url = '/'

class BusCompaniesUpdateView(UpdateView):
    model = BusCompany
    template_name = 'buses/forms.html'
    fields = ('name','head_office','staff_count')
    success_url = '/'

class BusCompaniesDeleteView(DeleteView):
    model = BusCompany
    template_name = 'buses/forms.html'
    success_url = '/'

# def list_bus_companies(request: HttpRequest):
#     buses= BusCompany.objects.all().order_by("name")
#     return render(request,'buses/list.html',{'buses':buses})
