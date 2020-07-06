from django.urls import path
from . import views

urlpatterns = [
    path('',views.home ),
    path('fun1/',views.fun1),
    path('count123/',views.count,name='count'),
]
