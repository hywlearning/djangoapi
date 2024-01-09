from django.db import IntegrityError
from django.http import HttpRequest
from django.shortcuts import render
from .models import TbMenu,Category
from .serializers import MenuSerializer,CateogrySerializer,UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework import status,generics,viewsets
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.


class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class=UserSerializer
    
    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.validated_data['password'] = make_password(serializer.validated_data.get('password'))
            self.perform_create(serializer)
            return Response(serializer.data,status=status.HTTP_200_OK)
            # Call the parent class's create method to handle object creation
            '''
            mutable_post_data = request.POST.copy()
            print("request",mutable_post_data['password'])
            mutable_post_data['password']=make_password(mutable_post_data['password'])
            response = super().create(mutable_post_data, *args, **kwargs)
            return response
            '''
        except IntegrityError as e:
            return Response(f"Error: {e}", status=status.HTTP_400_BAD_REQUEST)

class menu_singleinfo(generics.RetrieveUpdateDestroyAPIView):
    queryset = TbMenu.objects.all()
    serializer_class= MenuSerializer
    permission_classes=[IsAuthenticated]
    
    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            return Response({"detail":"no data"},status=status.HTTP_404_NOT_FOUND)
    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response({"detail":"deleted"},status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({"detail":"no data"},status=status.HTTP_404_NOT_FOUND)   
    def update(self, request, *args, **kwargs):
        serializeditem= MenuSerializer(data=request.data)
        if serializeditem.is_valid(raise_exception=True):
            try:
                serializeditem.save()
            except IntegrityError as e:
                return Response(f"Error: {e}",status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializeditem.error_messages,status=status.HTTP_400_BAD_REQUEST)
            

class menuv2(viewsets.ViewSet):  
    queryset = TbMenu.objects.all()
    serializer_class= MenuSerializer 
    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
    def create(self, request):
        serializeditem= MenuSerializer(data=request.data)
        if serializeditem.is_valid(raise_exception=True):
            try:
                serializeditem.save()
            except IntegrityError as e:
                 return Response(f"Error: {e}",status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializeditem.error_messages,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def menu_items(request):
    if request.method=='GET':
        try:
            limit = request.GET.get('limit', 10)
            print(f"limit={limit}")
        except:
            limit=10
        try:
            s_query=f"select * from tb_menu"
            s_query=f"{s_query} limit {limit}"
            items=TbMenu.objects.raw(s_query) 
        except:
            items=[]
        serializedItems= MenuSerializer(items,many=True)
        return Response(serializedItems.data)
    if request.method=='POST':
        serializeditem= MenuSerializer(data=request.data)
        if serializeditem.is_valid(raise_exception=True):
            try:
                serializeditem.save()
            except IntegrityError as e:
                 return Response(f"Error: {e}",status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializeditem.error_messages,status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET','POST'])
def category_items(request):
    if request.method=='GET':
        try:
            limit = request.GET.get('limit', 10)
            print(f"limit={limit}")
        except:
            limit=10
        try:
            items=Category.objects.raw(f'SELECT * FROM tb_category LIMIT {limit}') 
           
        except:
            items=[]
        serializedItems= CateogrySerializer(items,many=True)
        return Response(serializedItems.data)
    if request.method=='POST':
        serializeditem= CateogrySerializer(data=request.data)
        print("getdata",request.data)
        if serializeditem.is_valid(raise_exception=True):
            try:
                serializeditem.save()
            except IntegrityError as e:
                 return Response(f"Error: {e}",status=status.HTTP_400_BAD_REQUEST)
            return Response(serializeditem.data,status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
