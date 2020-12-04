from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name="index"),
    # path('create/', views.create, name="create"),
    path('', views.IndexView.as_view(), name="index"),
    path('create/', views.ReportCreateView.as_view(), name="create"),
    path('<int:pk>/', views.report_details, name="report details"),
]
