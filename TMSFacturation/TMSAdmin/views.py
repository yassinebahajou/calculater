from datetime import datetime, date

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader

# Create your views here.
from django.urls import reverse

from .dao import operationDAO
from .models import Client, Operation, Service, OperationInput


def services(request):
    instances = Service.objects.all().values()
    context = {
        'myServices': instances,
    }
    template = loader.get_template("services/index.html")
    return HttpResponse(template.render(context, request))

def operations(request):
    instances = Operation.objects.all()
    context = {
        'myOperations': instances,
        'myDays': range(1,32),
        'myMonth': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
        'myYears': range(2020,date.today().year+1),
    }
    template = loader.get_template("operations/index.html")
    return HttpResponse(template.render(context, request))

def filter_operations(request):
    day = int(request.POST.get('day'))
    month = int(request.POST.get('month'))
    year = int(request.POST.get('year'))
    if(day==0 and month  == 0 and year == 0):
        instances = Operation.objects.all()
    elif(day==0 and month ==0 and year !=0):
        instances = Operation.objects.filter(yearO=year)
    elif (day == 0 and month != 0 and year == 0):
        instances = Operation.objects.filter(monthO=month)
    elif (day == 0 and month != 0 and year != 0):
        instances = Operation.objects.filter(monthO=month,yearO=year)
    elif (day != 0 and month == 0 and year == 0):
        instances = Operation.objects.filter(dayO=day)
    elif (day != 0 and month == 0 and year != 0):
        instances = Operation.objects.filter(dayO=day,yearO=year)
    elif (day != 0 and month != 0 and year == 0):
        instances = Operation.objects.filter(dayO=day,monthO=month)
    elif (day != 0 and month != 0 and year != 0):
        instances = Operation.objects.filter(dayO=day,monthO=month,yearO=year)
    print("operation_filter:",instances)
    context = {
        'myOperations': instances,
        'myDays': range(1,32),
        'myMonth': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
        'myYears': range(2020,date.today().year+1),
        'filterValues': {"day":day,"month":month,"year":year}
    }
    template = loader.get_template("operations/index.html")
    return HttpResponse(template.render(context, request))

def to_update(request, codeS):
  instance = Service.objects.get(codeS=codeS)
  print("service",instance)
  template = loader.get_template('services/update.html')
  context = {
    'service': instance,

  }
  return HttpResponse(template.render(context, request))

def to_update_op(request, opid):
  print("updateop",opid)
  operation = Operation.objects.get(operationID=opid)
  inputs = OperationInput.objects.filter(operationOI=opid)
  services = Service.objects.all()
  print("operation",operation)
  template = loader.get_template('operations/update.html')
  context = {
    'operation': operation,
    'inputs': inputs,
    'services': services,

  }
  return HttpResponse(template.render(context, request))

def to_add(request):
  template = loader.get_template('services/ajouter.html')
  context = { }
  return HttpResponse(template.render(context, request))

def to_add_op(request):
    instances = Client.objects.all()
    template = loader.get_template('operations/ajouter.html')
    context = {
        "clients" : instances,
    }
    return HttpResponse(template.render(context, request))

def add(request):
    print("heyu")
    codeS = request.POST.get('codeS')
    descriptionS = request.POST.get('descriptionS')
    qteS = request.POST.get('QteS')
    priceS = request.POST.get('priceS')
    unitS = request.POST.get('unitS')
    instance = Service()
    instance.codeS = codeS
    instance.descriptionS = descriptionS
    instance.QteS = qteS
    instance.priceS = priceS
    instance.unitS = unitS
    instance.save()
    print(instance.priceS)
    return HttpResponseRedirect(reverse('services'))

def add_op(request):
    print("heyu")
    codeC = request.POST.get('client')
    client = Client.objects.get(codeC=codeC)
    adresse = request.POST.get('adresse')
    destination = request.POST.get('destination')
    distance = request.POST.get('distance')
    operationDAO.create_operation(client,adresse,destination,distance)
    return HttpResponseRedirect(reverse('operations'))

def add_op_in(request):
    print("add_op_in")
    codeS = request.POST.get('service')
    OperationID = request.POST.get('Operation')
    print("add op:",OperationID)
    service = Service.objects.get(codeS=codeS)
    operation = Operation.objects.get(operationID=OperationID)
    qte = request.POST.get('Qte')
    operationDAO.create_operation_input(operation,service,qte)
    return HttpResponseRedirect(reverse('to_update_op', kwargs={'opid':OperationID}))

def delete_op_in(request,opID,opinID):
    operationDAO.delete_operation_input(opID,opinID)
    return HttpResponseRedirect(reverse('to_update_op', kwargs={'opid':opID}))

def up_service_details(request):
    print("add_op_in")
    time = request.POST.get('time')
    distance = request.POST.get('distance')
    OperationID = request.POST.get('Operation')
    operation = Operation.objects.get(operationID=OperationID)
    operation.distanceO = distance
    operation.timeO = time
    operation.save()
    return HttpResponseRedirect(reverse('to_update_op', kwargs={'opid':OperationID}))

def update(request, codeS):
    print("heyu")
    codeE = request.POST.get('codeS')
    descriptionS = request.POST.get('descriptionS')
    qteS = request.POST.get('QteS')
    priceS = request.POST.get('priceS')
    unitS = request.POST.get('unitS')
    instance = Service.objects.get(codeS=codeS)
    print(instance.priceS)
    instance.codeS = codeE
    instance.QteS = qteS
    instance.descriptionS = descriptionS
    instance.priceS = priceS
    instance.unitS = unitS
    instance.save()
    print(instance.priceS)
    return HttpResponseRedirect(reverse('services'))