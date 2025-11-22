from django.urls import path
from .views import *

urlpatterns =[
    path("department/",Department_view.as_view()),
    path("departmentedit/<int:dep_id>/",Department_Edit.as_view()),
    path("employe/",Employe_view.as_view()),
    path("employeedit/<int:Emp_id>/",Employe_Edit.as_view()),
    path("profile/",Profile_view.as_view()),
    path("profileedit/<int:Pro_id>/",Profile_Edit.as_view()),
    path("depart/login/",Login_view),
    path("speci/",departments),
    path("find/",find),
    path("high/",high_salary),
    path("search/<str:Sname>/",Search),
    path("dep/<str:Sname>/",Dep_Search),
    path("salary/",ord_salary),
    path("Empname/",name_sort),
    path("depname/",depname),
    path('count/',TotalE),
    path('countsal/',ToSal),
    path('Avrgsal/',Avrg_sal),
    path('Highsal/',High_sal),
    path('lowsal/',low_sal),
    path('each/',Each),
    path('salaryp/',salaryP)
]