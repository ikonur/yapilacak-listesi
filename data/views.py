from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import render
from django.utils import timezone


from .models import todolist


# Create your views here.

class todolistListView(ListView):

  model = todolist
  paginate_by = 10 


class todolistDetailView(DetailView):

    model = todolist
