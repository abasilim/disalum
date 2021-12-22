
from rest_framework import permissions
from rest_framework import response
from rest_framework import serializers
from rest_framework.serializers import Serializer
from alumniapp.models import School
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import SAFE_METHODS, AllowAny,  BasePermission, DjangoModelPermissions, IsAuthenticated
from .serializers import userSerializer,  schoolSerializer
from rest_framework.response import Response
from users.models import NewUser
from django_filters import rest_framework as filters

class PostUserWritePermission(BasePermission):
    message = 'Editing posts is restricted to the authr only.'
    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user

# class UserViewset(viewsets.ViewSet):
#     permissions_classes = [IsAuthenticated]
#     queryset = NewUser.objects.all()

#     def list(self, request):
#         serializer_class = userSerializer(self.queryset, many=True)
#         return Response(serializer_class.data)

#     def retrieve(self, request, pk=None):
#         user = get_object_or_404(self.queryset, pk=pk)
#         serializer_class = userSerializer(user)
#         return Response(serializer_class.data)
# viewsets
class UserViewset(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = userSerializer
    queryset = NewUser.objects.all()

    #class SchoolViewset(viewsets.ModelViewSet, PostUserWritePermission):
class SchoolViewset(viewsets.ModelViewSet):
    #permission_classes = [PostUserWritePermission]
    permission_classes = [AllowAny]
    serializer_class = schoolSerializer
    #queryset = School.schoolobj.all()

    def get_queryset(self):
        school = School.schoolobj.all()
        return school
    
    def retrieve(self, request, *args, **kwargs):
        param = kwargs
        print(param['pk'])
        school = School.schoolobj.filter(alumni_Name=param['pk'])
        serializer = schoolSerializer(school)
        return Response(serializer.data)

    # def get_object(self, queryset=None, **kwargs):
    #     item = self.kwargs.get('pk')
    #     return get_object_or_404(School, slug=item)

    # # Define a custom Queryset
    # def get_queryset(self):
    #     return School.schoolobj.all()