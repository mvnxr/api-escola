from django.urls import path

# from grade.views import GradeSerializerApiView, GradesSerializerApiView
from main.views import AlunoUserCreate, AlunoUserUpdate, AlunoUserDelete, AlunoUserList, AlunoUserDetail, generate_token

urlpatterns = [
    path('generate_token', generate_token),
    path('alunos', AlunoUserList.as_view(), name='list_alunos'),
    path('alunos/create', AlunoUserCreate.as_view(), name='create_aluno'),
    path('alunos/<int:pk>', AlunoUserDetail.as_view(), name='read_aluno'),
    path('alunos/<int:pk>/update', AlunoUserUpdate.as_view(), name='update_aluno'),
    path('alunos/<int:pk>/delete', AlunoUserDelete.as_view(), name='delete_aluno'),
]