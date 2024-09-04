from django.shortcuts import render
from . models import Address
from . serializer import AddressSerilizer
from django.http import JsonResponse
from rest_framework.decorators import api_view


@api_view(["GET","POST"])
def index(request):
    if request.method=='GET':
        data=Address.objects.all()
        ser=AddressSerilizer(data, many=True)
        return JsonResponse(ser.data, safe=False)
    if request.method=='POST':
        ser=AddressSerilizer(data=request.data)
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data,status=201)
    return JsonResponse()
@api_view(["GET","DELETE"])
def detail(request,id):
    try:
        data=Address.objects.get(id=id)
    except Address.DoesNotExist:
        return JsonResponse({'error':"data not"})
    if request.method=='GET':
        ser=AddressSerilizer(data)
        return JsonResponse(ser.data, safe=False)
    if request.method=='DELETE':
        data.delete()
        return JsonResponse({'delete':'success'})
    return JsonResponse({})