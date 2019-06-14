from django.shortcuts import render
# Create your views here.
from .forms import companyform
from .models import companymodel
from django.views.generic import TemplateView,ListView,CreateView,DetailView,UpdateView

from django.http import HttpResponse
class home_view(TemplateView):
   template_name = 'home.html'
class create_view(CreateView):

    model=companymodel
    fields = ('name','loc','ceo')
    template_name = 'companymodel_form.html'

class list_view(ListView):
    model = companymodel
    template_name = 'companymodel_list.html'
class details_view(DetailView):
    model = companymodel
    template_name = 'companymodel_detail.html'
class update_view(UpdateView):
    model = companymodel
    fields = ('name','ceo')
    # template_name = ""