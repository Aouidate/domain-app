from django.urls import path
from domain import views
urlpatterns = [
path('calculate_domain',views.calculate_domain,)
     ]
# inside the app1 application urls.py file
#// same for app2