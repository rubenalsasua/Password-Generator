from django.urls import path
from App import views

urlpatterns = [
    path('', views.PasswordListView.as_view(), name='lista'),
    path('crear/', views.PasswordCreateView.as_view(), name='crear_contraseña'),
    path('eliminar/<int:pk>/', views.PasswordDeleteView.as_view(), name='eliminar_contraseña'),

]
