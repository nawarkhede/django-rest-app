from django.http import JsonResponse, Http404
from django.shortcuts import render
from firstapp.serializers import (
    EmployeeSerializer,
    OrganizationSerializer,
    StudentSerializer,
)
from firstapp.models import Employee, Organization, Student

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics, mixins


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


#  class based views examples


class OrganizationList(APIView):
    def get(self, request):
        serializer = OrganizationSerializer(Organization.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrganizationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrganizationDetail(APIView):
    def get_object(self, pk):
        try:
            return Organization.objects.get(id=pk)
        except Organization.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        org = self.get_object(pk=pk)
        serializer = OrganizationSerializer(org)
        return Response(serializer.data)

    def put(self, request, pk):
        org = self.get_object(pk)
        serializer = OrganizationSerializer(org, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        org = self.get_object(pk)
        org.delete()
        return Response(status.HTTP_204_NO_CONTENT)


class StudentList(
    mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class StudentDetail(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, reqyest, pk):
        return self.retrieve(reqyest, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)
