import requests
from django.test import TestCase, Client
from rest_framework.authtoken.admin import User

from main.models import Aluno
from rest_framework.authtoken.models import Token


class UserTest(TestCase):

    def setUp(self):
        self.superuser = User.objects.create(is_superuser=True)
        self.user = Aluno.objects.create(nome='aluno', is_student=True)
        self.headers = {
            'Content-type': 'application/json',}
        self.url_base = 'http://127.0.0.1:8000/api/'
        self.client = Client()
        self.token = Token.objects.create(user_id=self.superuser.id)
        print(self.token)


    def test_if_user_exists(self):
        filter_user = Aluno.objects.filter(nome=self.user.nome).exists()
        self.assertTrue(self.user)

    def test_user_role_is_student(self):
        filter_student = Aluno.objects.filter(nome=self.user.nome, is_student=True).exists()
        self.assertTrue(self.user.is_student)

    def test_list_students_requests(self):
        response = self.client.get(self.url_base + 'alunos')
        self.assertEqual(response.status_code, 200)

    def test_create_students_request(self):
        response = self.client.post(self.url_base + 'alunos/create', content_type="application/json", data={
            'nome': 'test_user',
            'is_student': True,
        },HTTP_AUTHORIZATION=f'Token {self.token}')
        self.assertEqual(response.status_code, 201)

    def test_read_students_request(self):
        response = self.client.get(self.url_base + f'alunos/{self.user.id}')
        self.assertEqual(response.status_code, 200)

    def test_update_students_request(self):
        response = self.client.put(self.url_base + f'alunos/{self.user.id}/update', content_type="application/json", data={
            'nome': 'updated_user',
        }, HTTP_AUTHORIZATION=f'Token {self.token}')
        self.assertEqual(response.data["nome"], 'updated_user')
        self.assertEqual(response.status_code, 200)

    def test_delete_students_request(self):
        response = self.client.delete(self.url_base + f'alunos/{self.user.id}/delete', HTTP_AUTHORIZATION=f'Token {self.token}')
        self.assertIsNone(response.data)