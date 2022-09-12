from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
class ProductView(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"msg":"inside products get"})
class MorningView(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"msg":"GOOD MORNING"})
class AddView(APIView):
    def get(self,request,*args,**kwargs):
        A=int(input("first num"))
        B=int(input("second num"))
        res=A+B
        return Response({"msg":res})
