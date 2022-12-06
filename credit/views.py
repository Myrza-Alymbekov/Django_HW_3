from django.shortcuts import render
from django.views import generic

from.models import Client, Account


class ClientsView(generic.ListView):
    model = Client
    context_object_name = 'client_list'
    template_name = 'index.html'


class ClientDetailView(generic.DetailView):
    model = Client
    context_object_name = 'client'
    pk_url_kwarg = 'id'


class AccountDetailView(generic.DetailView):
    model = Account
    context_object_name = 'account'
    pk_url_kwarg = 'id'
