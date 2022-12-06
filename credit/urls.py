from django.urls import path

from . import views

urlpatterns = [
    path('', views.ClientsView.as_view(), name='index'),
    path('<int:id>/detail/', views.ClientDetailView.as_view(template_name='detail.html'), name='detail'),
    path('<int:id>/account/', views.AccountDetailView.as_view(template_name='detail_account.html'), name='detail_account'),
]

