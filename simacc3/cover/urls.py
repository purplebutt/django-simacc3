from django.urls import path
from . import views as vw

app_name='cover'

urlpatterns = [
    path('', vw.homepage, name="homepage"),
]
