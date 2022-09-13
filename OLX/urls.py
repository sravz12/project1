"""OLX URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
# from api.views import ProductView,MorningView,AddView,MulView
from api.views import CubeView,NumcheckView,FactView,WordcountView,ArmstrongView,PaliandromeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cube',CubeView.as_view()),
    path('numcheck',NumcheckView.as_view()),
    path('fact',FactView.as_view()),
    path('word',WordcountView.as_view()),
    path('armstrong',ArmstrongView.as_view()),
    path('paliandrome',PaliandromeView.as_view())

    # path("products",ProductView.as_view()),
    # path("morning",MorningView.as_view()),
    # path("add",AddView.as_view()),
    # path("mul",MulView.as_view())
]
