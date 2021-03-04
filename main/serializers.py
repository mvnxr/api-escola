from rest_framework import serializers

from .models import Aluno


class AlunoUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = (
            'id',
            'nome',
            'is_student',
            'turma',
        )

