from django.http import JsonResponse
from django.shortcuts import render
from firstapp.serializers import EmployeeSerializer
from firstapp.models import Employee

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


def index(request):
    return JsonResponse({"name": "nishant"})


@api_view(["GET", "POST"])
def employee_list(request):

    if request.method == "GET":
        serializer = EmployeeSerializer(Employee.objects.all(), many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def employee_details(request, pk):
    try:
        employee = Employee.objects.get(id=pk)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        employee.delete()
        return Response(status.HTTP_204_NO_CONTENT)
