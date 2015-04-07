from django.shortcuts import render
from django.shortcuts import render_to_response
from oper.models import Client, Operators
from django.contrib import auth
from django.core.context_processors import csrf


def enter(request):
    return render_to_response('enter.html', {'username': auth.get_user(request).username})


def operators(request):
    return render_to_response('Operators.html', {'Operators': Operators.objects.all(), 'username': auth.get_user(request).username})


def clients(request):
    return render_to_response('Clients.html', {'Clients': Client.objects.all(), 'username': auth.get_user(request).username})


def client(request, client_id=1):
    args = {}
    args.update(csrf(request))
    args['client'] = Client.objects.get(id=client_id)
    args['operator'] = Operators.objects.filter(id=client_id)
    args['username'] = auth.get_user(request).username
    return render_to_response('Client.html', args)


def operator(request, operator_id=1):
    args = {}
    args.update(csrf(request))
    args['operator'] = Operators.objects.get(id=operator_id)
    args['client'] = Client.objects.filter(id=operator_id)
    args['username'] = auth.get_user(request).username
    return render_to_response('Operator.html', args)
