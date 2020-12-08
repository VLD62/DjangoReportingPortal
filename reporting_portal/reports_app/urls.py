from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name="index"),
    # path('create/', views.create, name="create"),
    path('', views.IndexView.as_view(), name="index"),
    path('create/', views.ReportCreateView.as_view(), name="create"),
    path('<int:pk>/', views.ReportDetailsView.as_view(), name="report details"),
    path('edit/<int:pk>/', views.ReportEditView.as_view(), name='edit report'),
    path('delete/<int:pk>/', views.ReportDeleteView.as_view(), name='delete report'),
    # path('delete/<int:pk>/', views.delete_report, name='delete report'),
    # path('<int:pk>/', views.report_details, name="report details"),
    # path('edit/<int:pk>/', views.edit_report, name='edit report'),
]
