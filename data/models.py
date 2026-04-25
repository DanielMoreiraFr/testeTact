from django.db import models

# Create your models here.

class DataModels(models.Model):
    idade = models.IntegerField(default=0)
    genero = models.CharField(max_length=100, default='')
    horas_estudadas = models.FloatField(default=0.0)
    frequencia = models.FloatField(default=0.0)
    horas_sono = models.FloatField(default=0.0)
    nivel_estresse = models.FloatField(default=0.0)
    tempo_tela = models.FloatField(default=0.0)
    ultimo_gpa = models.FloatField(default=0.0)
    trabalho = models.BooleanField(default=False)
    metodo_estudo = models.CharField(max_length=100, default='')
    dieta = models.CharField(max_length=100, default='')
    internet = models.CharField(max_length=100, default='')
    extracurricular = models.BooleanField(default=False)
    quant_aulas_partic = models.IntegerField(default=0)
    renda_familiar = models.CharField(max_length=15, default='')
    ansiedade = models.FloatField(default=0.0)
    pontos_final = models.FloatField(default=0.0)

    def __str__(self):
        return f"Perfil {self.id}"