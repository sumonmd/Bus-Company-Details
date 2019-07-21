from django.urls import path,include

from busdetails import views

urlpatterns = [

    path('',views.BusCompaniesListView.as_view()),
    path('create/',views.BusCompaniesCreateView.as_view()),
    path('update/<int:pk>/',views.BusCompaniesUpdateView.as_view()),
    path('delete/<int:pk>/',views.BusCompaniesDeleteView.as_view()),
]