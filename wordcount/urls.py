from django.urls import path
from . import views
urlpatterns = [
    # path('',views.intro),
    path('', views.homepage),
    path('count', views.count, name='count'),
]
