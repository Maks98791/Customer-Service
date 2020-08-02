from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.parsers import JSONParser

from api.models import Customer
from api.serializers import CustomerSerializer


@csrf_exempt
def customer_list(request):

    # GET all customers
    if request.method == 'GET':
        customers = Customer.objects.all()
        customers_serializer = CustomerSerializer(customers, many=True)
        return JsonResponse(customers_serializer.data, safe=False)

    # POST new customer
    elif request.method == 'POST':
        customer_data = JSONParser().parse(request)
        customer_serializer = CustomerSerializer(data=customer_data)
        if customer_serializer.is_valid():
            customer_serializer.save()
            return JsonResponse(customer_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE all customers
    elif request.method == 'DELETE':
        Customer.objects.all().delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
def customer_details(request, pk):

    try:
        customer = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    # GET customer details
    if request.method == 'GET':
        customer_serializer = CustomerSerializer(customer)
        return JsonResponse(customer_serializer.data)

    # PUT existing customer
    elif request.method == 'PUT':
        customer_data = JSONParser().parse(request)
        customer_serializer = CustomerSerializer(customer, data=customer_data)
        if customer_serializer.is_valid():
            customer_serializer.save()
            return JsonResponse(customer_serializer.data)
        return JsonResponse(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE existing customer
    elif request.method == 'DELETE':
        customer.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
def customer_list_by_age(request, age):

    customers = Customer.objects.filter(age=age)

    # GET all customers by age
    if request.method == 'GET':
        customers_serializer = CustomerSerializer(customers, many=True)
        return JsonResponse(customers_serializer.data, safe=False)
