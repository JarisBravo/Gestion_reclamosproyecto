# gestionar_reclamos/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from gestionar_reclamos import views
from gestionar_reclamos.views import reclamo_enviado, solicitud_enviada
from django.views.i18n import set_language
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('nuevo_reclamo/', views.nuevo_reclamo, name='nuevo_reclamo'),
    path('nueva_solicitud/', views.nueva_solicitud, name='nueva_solicitud'),
    path('solicitud_quincho/', views.solicitud_quincho, name='solicitud_quincho'),
    path('solicitud_gimnasio/', views.solicitud_gimnasio, name='solicitud_gimnasio'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('admin/', admin.site.urls),
    path('reclamo_enviado/', reclamo_enviado, name='reclamo_enviado'),
    path('solicitud_enviada/', solicitud_enviada, name='solicitud_enviada'),
    path('i18n/', set_language, name='set_language'),
    
    # Cambia esta línea para usar el método POST en el logout
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    
]

# Añade la configuración para servir archivos media solo si DEBUG está activado
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
