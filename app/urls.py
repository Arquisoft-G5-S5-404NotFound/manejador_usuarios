"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.app, name='app'),
    path('health-check/', views.health_check, name='health-check'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]

"""
path('crear/', views.crear_usuario, name='crear_usuario'),
path('actualizar/<int:user_id>/', views.actualizar_usuario, name='actualizar_usuario'),
path('eliminar/<int:user_id>/', views.eliminar_usuario, name='eliminar_usuario'),
path('activos/', views.lista_usuarios_activos, name='lista_usuarios_activos'),
path('<str:email>/', views.detalle_usuario_por_email, name='detalle_usuario_por_email')
"""
