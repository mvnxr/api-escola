from django.db import models


class Aluno(models.Model):
    nome = models.CharField('Nome', max_length=255)
    is_student = models.BooleanField('é estudante?', default=True)
    turma = models.CharField('Turma', blank=True, null=True, max_length=255)

    class Meta:
        verbose_name = 'Alunos'
        verbose_name_plural = 'Alunos'
        ordering = ['id']

    def __str__(self):
        return f'{self.name} {self.turma}'
