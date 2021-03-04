from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status, generics
from .models import Aluno
from .serializers import AlunoUserSerializer
from rest_framework.authtoken.models import Token

def generate_token(request):
    if request.user.is_superser:
        token = Token.objects.create(user_id=request.user)
        return HttpResponse(f'Token {token}')

class AlunoUserCreate(generics.CreateAPIView):
    queryset = Aluno.objects.all().filter(is_student=True)
    serializer_class = AlunoUserSerializer


class AlunoUserDetail(generics.RetrieveAPIView):
    queryset = Aluno.objects.all().filter(is_student=True)
    serializer_class = AlunoUserSerializer

    def get_object(self):
        if self.kwargs.get('pk'):
            return self.queryset.get(pk=self.kwargs.get('pk'))
        return self.queryset.all()


class AlunoUserUpdate(generics.UpdateAPIView):
    queryset = Aluno.objects.all().filter(is_student=True)
    serializer_class = AlunoUserSerializer


class AlunoUserDelete(generics.DestroyAPIView):
    queryset = Aluno.objects.all().filter(is_student=True)
    serializer_class = AlunoUserSerializer


class AlunoUserList(generics.ListCreateAPIView):
    queryset = Aluno.objects.all().filter(is_student=True)
    serializer_class = AlunoUserSerializer


class AlunoUsersApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Aluno.objects.all().filter(is_student=True)
    serializer_class = AlunoUserSerializer


class AlunoUserGradeApiView(generics.ListCreateAPIView):
    queryset = Aluno.objects.all().filter(is_student=True)
    serializer_class = AlunoUserSerializer

    def get_queryset(self):
        if self.kwargs.get('grade_pk'):
            return self.queryset.filter(turma=self.kwargs.get('grade_pk'))
        return self.queryset.all()
