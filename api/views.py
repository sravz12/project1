from django.shortcuts import render
#
# # Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Books,Reviews
from api.serializers import BookSerializer,ReviewSerializer,UserSerializer
from rest_framework.viewsets import ViewSet,ModelViewSet
from django.contrib.auth.models import User
from rest_framework import authentication,permissions

# class ProductView(APIView):
#     def get(self,request,*args,**kwargs):
#         return Response({"msg":"inside products get"})
# class MorningView(APIView):
#     def get(self,request,*args,**kwargs):
#         return Response({"msg":"GOOD MORNING"})
# class AddView(APIView):
#     def post(self,request,*args,**kwargs):
#         n1=request.data
#
#         res=A+B
#         return Response({"msg":res})
# class MulView(APIView):
#     def get(self,request,*args,**kwargs):
#         A=int(input("num1"))
#         B=int(input("num2"))
#         res=A*B
#         return Response({"msg":res})
#
# class CubeView(APIView):
#     def post(self,request,*args,**kwargs):
#         n=int(request.data.get("num1"))
#         res=n**3
#         return Response({"result":res})
# class NumcheckView(APIView):
#     def post(self,request,*args,**kwargs):
#         n=int(request.data.get("num1"))
#         res=""
#         if n%2==0:
#             res="num is even"
#         else:
#             res="num is odd"
#         return Response({"result":res})
# class FactView(APIView):
#     def post(self,request,*args,**kwargs):
#         n=int(request.data.get("num1"))
#         res=1
#         for i in range(1,n+1):
#             res=res*i
#         return Response({"result":res})
# class WordcountView(APIView):
#     def post(self,request,*args,**kwargs):
#         txt=request.data.get("txt")
#         words=txt.split(" ")
#         wc={}
#         for w in words:
#             if w in wc:
#                 wc[w]+=1
#             else:
#                 wc[w]=1
#         return Response({"count":wc})
# class ArmstrongView(APIView):
#     def post(self,request,*args,**kwargs):
#         n=int(request.data.get("n"))
#         count=0
#         s=0
#         num=num1=n
#         res=""
#         while n>0:
#             d=n%10
#             count=count+1
#             n=n//10
#         while num>0:
#             d=n%10
#             s=s+d**count
#             n=num//10
#         if num1==s:
#             res="arm"
#         else:
#             res='not armstrong'
#         return Response({"result":res})
# class PaliandromeView(APIView):
#     def post(self,request,*args,**kwargs):
#         s=request.data.get("txt")
#         s1=s[::-1]
#         res=''
#         if s1 == s:
#             res='it is palindrome'
#         else:
#             res='not palindrome'
#         return Response({"result":res})

class ProductsView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Books.objects.all()
        serializer=BookSerializer(qs,many=True)
        return Response(data=serializer.data)


    def post(self,request,*args,**kwargs):
       serializer=BookSerializer(data=request.data)
       if serializer.is_valid():
           Books.objects.create(**serializer.validated_data)
           return Response(data=serializer.data)
       else:
           return Response(data=serializer.errors)


class ProductDetailView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        book=Books.objects.get(id=id)
        serializer=BookSerializer(book,many=False)
        return Response(data=serializer.data)
    def delete(self,request,*arg,**kwargs):
        id=kwargs.get("id")
        Books.objects.get(id=id).delete()
        return Response(data="deleted")
    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            Books.objects.filter(id=id).update(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)


class ReviewView(APIView):
    def get(self,request,*args,**kwargs):
        reviews=Reviews.objects.all()
        serialiser=ReviewSerializer(reviews,many=True)
        return Response(data=serialiser.data)

    def post(self,request,*args,**kwargs):
        serializer=ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class ReviewDetailsView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Reviews.objects.get(id=id)
        serializer=ReviewSerializer(qs,many=False)
        return Response(data=serializer.data)
    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        object=Reviews.objects.get(id=id)
        serializer=ReviewSerializer(instance=object,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        Reviews.objects.get(id=id).delete()
        return Response(data="deleted")

class ProductviewsetView(ViewSet):
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]



    def list(self,request,*args,**kwargs):
        qs=Books.objects.all()
        serializer=BookSerializer(qs,many=True)
        return Response(data=serializer.data)
    def create(self,request,*args,**kwargs):
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        book=Books.objects.get(id=id)
        serializer=BookSerializer(book,many=False)
        return Response(data=serializer.data)
    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        book=Books.objects.get(id=id)
        serializer=BookSerializer(instance=book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    def destroy(self,request,*arg,**kwargs):
        id=kwargs.get("pk")
        Books.objects.get(id=id).delete()
        return Response(data="deleted")

class ProductModelViewsetView(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Books.objects.all()

class ReviewModelViewsetView(ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Reviews.objects.all()
    def list(self,request,*args,**kwargs):
        all_reviews=Reviews.objects.all()
        if 'user' in request.query_params:
            all_reviews=all_reviews.filter(user=request.query_params.get("user"))
        serializer=ReviewSerializer(all_reviews,many=True)
        return Response(data=serializer.data)

class UsersView(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()



