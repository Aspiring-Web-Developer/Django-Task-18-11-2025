from django.shortcuts import render,get_object_or_404,HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny
from django.http import JsonResponse
from django.db.models import F,Q,Min,Max,Count,Sum,Avg

    
class Department_view(APIView):
       permission_classes=[IsAuthenticated]
       
       def post(self,request):
           serialize=Department_serializers(data=request.data)
           print(serialize)
           if serialize.is_valid():
            print("valid")
            serialize.save()
           return Response({"msg":"datasaved","data":serialize.data})
       def get(self,request):
           dep=Department_Model.objects.all()
           serialize=Department_serializers(dep,many=True)
           print(serialize)
           return Response(serialize.data)
    
class Department_Edit(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request,dep_id):
        dep=get_object_or_404(Department_Model,id=dep_id)
        serialize=Department_serializers(dep)
        print(serialize)
        return Response(serialize.data)
    
    def delete(self,request,dep_id):
        try:
           dep=get_object_or_404(Department_Model,dep_id)
           dep.delete()
           return Response("The given data Deleted")
        except  Department_Model.DoesNotExist:
            return Response("The data deleted")
        

    def put(self,request,dep_id):
        dep=get_object_or_404(Department_Model,id=dep_id)
        serialize=Department_serializers(instance=dep,data=request.data)
        print(serialize)
        return Response({"msg":"Data Ubdated","data":serialize.data})


class Employe_view(APIView):
    def post(self,request):
        serialize=Employe_Serializers(data=request.data)
        print(serialize)
        if serialize.is_valid():
            print("valid")
            serialize.save()
        return Response({"msg":"datasaved","data":serialize.data})
    def get(self,request):
        Emp=Employe_Model.objects.all()
        serialize=Employe_Serializers(Emp,many=True)
        print(serialize)
        return Response(serialize.data)
    
class Employe_Edit(APIView):
    def get(self,request,Emp_id):
        Emp=get_object_or_404(Employe_Model,id=Emp_id)
        serialize=Employe_Serializers(Emp)
        print(serialize)
        return Response(serialize.data)
    
    def delete(self,request,Emp_id):
        try:
           Emp=get_object_or_404(Employe_Model,Emp_id)
           Emp.delete()
           return Response("The given data Deleted")
        except  Employe_Model.DoesNotExist:
            return Response("The data deleted")
        

    def put(self,request,Emp_id):
        Emp=get_object_or_404(Employe_Model,id=Emp_id)
        serialize=Employe_Serializers(instance=Emp,data=request.data)
        print(serialize)
        return Response({"msg":"Data Ubdated","data":serialize.data})



class Profile_view(APIView):
    def post(self,request):
        serialize=Profile_Serializers(data=request.data)
        print(serialize)
        if serialize.is_valid():
            print("valid")
            serialize.save()
        return Response({"msg":"datasaved","data":serialize.data})
    def get(self,request):
        Pro=Profile_Model.objects.all()
        serialize=Profile_Serializers(Pro,many=True)
        print(serialize)
        return Response(serialize.data)
    
class Profile_Edit(APIView):
    def get(self,request,Pro_id):
        Pro=get_object_or_404(Profile_Model,id=Pro_id)
        serialize=Profile_Serializers(Pro)
        print(serialize)
        return Response(serialize.data)
    
    def delete(self,request,Pro_id):
        try:
           Pro=get_object_or_404(Profile_Model,id=Pro_id)
           Pro.delete()
           return Response("The given data Deleted")
        except  Profile_Model.DoesNotExist:
            return Response("The data deleted")
        

    def put(self,request,Pro_id):
        Pro=get_object_or_404(Profile_Model,id=Pro_id)
        serialize=Profile_Serializers(instance=Pro,data=request.data)
        print(serialize)
        return Response({"msg":"Data Ubdated","data":serialize.data})


from rest_framework.decorators import api_view,permission_classes
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(["POST"])
@permission_classes([AllowAny]) 
def Login_view(request):
    username=request.data.get("username")
    password=request.data.get("password")

    user=authenticate(username=username,password=password)
    data={}
    if user:
        token=RefreshToken.for_user(user)

        data['user']=user.username
        data['token']={
             'refresh': str(token),
             'access' : str(token.access_token)
        }
        return Response({"msg":"Login Successful","data":data})
    
    else:
        return Response({"msg":"Given Username or Password Invalid"},status=400)
    
def departments(self):
    depart=Department_Model.objects.filter(name='Services')
    serialize=Department_serializers(depart,many=True)
    return JsonResponse (serialize.data,safe=False)

def find(Self):
    min_salary=Employe_Model.objects.aggregate(Min('salary'))['salary__min']
    salar=Employe_Model.objects.filter(salary=min_salary)
    serialize=Employe_Serializers(salar,many=True)
    return JsonResponse (serialize.data,safe=False)

def high_salary(self):
    max_salary=Employe_Model.objects.aggregate(Max('salary'))['salary__max']
    high=Employe_Model.objects.filter(salary=max_salary)
    serialize=Employe_Serializers(high,many=True)
    return JsonResponse (serialize.data,safe=False)

def Search(self,Sname):
    filt=Employe_Model.objects.filter(name__icontains=Sname)
    serialize=Employe_Serializers(filt,many=True)
    return JsonResponse(serialize.data,safe=False)

def Dep_Search(self,Sname):
    filt=Department_Model.objects.filter(name__icontains=Sname)
    serialize=Department_serializers(filt,many=True)
    return JsonResponse(serialize.data,safe=False)

def ord_salary(self):
    salar=Employe_Model.objects.order_by('salary')
    serialize=Employe_Serializers(salar,many=True)
    return JsonResponse (serialize.data,safe=False)

def name_sort(self):
    Emp=Employe_Model.objects.order_by("name")
    serialize=Employe_Serializers(Emp,many=True)
    return JsonResponse (serialize.data,safe=False)

def depname(self):
    dep=Department_Model.objects.order_by('-name')
    serialize=Department_serializers(dep,many=True)
    return JsonResponse (serialize.data,safe=False)

def TotalE(self):
    emp=Employe_Model.objects.aggregate(count=Count('id'))
    return HttpResponse (emp['count'])

def ToSal(self):
    emp=Employe_Model.objects.aggregate(salary=Sum('salary'))
    return HttpResponse(emp['salary'])

def Avrg_sal(self):
    emp=Employe_Model.objects.aggregate(Avrg=Avg('salary'))
    return HttpResponse(emp['Avrg'])

def High_sal(self):
    emp=Employe_Model.objects.aggregate(High=Max('salary'))
    return JsonResponse(emp['High'],safe=False)

def low_sal(self):
    emp=Employe_Model.objects.aggregate(Low=Min('salary'))
    return JsonResponse (emp['Low'],safe=False)

def Each(self):
    emp=Department_Model.objects.annotate(employees_count=Count('employee'))
    serialize=Department_serializers(emp,many=True)
    return JsonResponse(serialize.data,safe=False)

def salaryP(self):
    emp=Department_Model.objects.values('name').annotate(salary=Sum('salary'))
    return JsonResponse(list(emp),safe=False)
    




