# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
from json import JSONEncoder
from django.views.decorators.csrf import csrf_exempt
from web.models import User, Token,  Expense, Income
from datetime import datetime
# Create your views here.




@csrf_exempt

def submit_expense(request):
    """ user submit an expenese """

    #TODO; validate date, usr might be fake, token might be fake, amount might be ...

    this_token = request.POST['token']
    this_user = User.objects.filter(token__token = this_token).get()

    if 'date' not in request.POST:
        date = datetime.now()
    Expense.objects.create(user = this_user , amount = request.POST['amount'], text = request.POST['text'], date = date)
    print ("Submet Expense")
    print(request.POST)

    return JsonResponse({
        'status': 'OK',
        }, encoder = JSONEncoder)
    

@csrf_exempt

def submit_income(request):
    """ user submit an income """

    #TODO; validate date, usr might be fake, token might be fake, amount might be ...

    this_token = request.POST['token']
    this_user = User.objects.filter(token__token = this_token).get()

    if 'date' not in request.POST:
        date = datetime.now()
    Income.objects.create(user = this_user , amount = request.POST['amount'], text = request.POST['text'], date =date)
    print ("Submet Income")
    print(request.POST)

    return JsonResponse({
        'status': 'OK',
        }, encoder = JSONEncoder)

