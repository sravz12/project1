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
from api.views import ProductsView,ProductDetailView,ReviewView,ReviewDetailsView,ProductviewsetView,ProductModelViewsetView,ReviewModelViewsetView,UsersView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import ObtainAuthToken
router=DefaultRouter()
router.register("api/v1/products",ProductviewsetView,basename="products")
router.register("api/v2/products",ProductModelViewsetView,basename="books")
router.register("api/v3/reviews",ReviewModelViewsetView,basename="review")
router.register("register",UsersView,basename="users")


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('cube',CubeView.as_view()),
    # path('numcheck',NumcheckView.as_view()),
    # path('fact',FactView.as_view()),
    # path('word',WordcountView.as_view()),
    # path('armstrong',ArmstrongView.as_view()),
    # path('paliandrome',PaliandromeView.as_view()),
    path('products',ProductsView.as_view()),
    path('products/<int:id>',ProductDetailView.as_view()),
    path('reviews',ReviewView.as_view()),
    path('reviews/<int:id>',ReviewDetailsView.as_view()),
    path("token/",ObtainAuthToken.as_view())



    # path("products",ProductView.as_view()),
    # path("morning",MorningView.as_view()),
    # path("add",AddView.as_view()),
    # path("mul",MulView.as_view())
]+router.urls
