from .views import index, documentation, DC_3, DC_6, Catalina, Junkers_87_Stuka
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='home'),
    path('documentation', documentation, name='documentation'),
    path('DC_3', DC_3, name='DC_3'),
    path('DC_6', DC_6, name='DC_6'),
    path('Catalina', Catalina, name='Catalina'),
    path('Junkers_87_Stuka', Junkers_87_Stuka, name='Junkers_87_Stuka'),
]
