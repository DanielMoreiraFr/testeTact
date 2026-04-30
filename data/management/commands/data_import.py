import pandas as pd
from django.core.management.base import BaseCommand
from data.models import DataModels

class Command(BaseCommand):
    def handle(self, *args, **options):
        try:    
            df = pd.read_csv('student_performance_finalscore.csv') 
            df = df.fillna(0) # substitui NaN por 0 para evitar erros
            
            objetos_para_salvar = [] 

            for indice, linha in df.iterrows():
                novo_registro = DataModels(
                    idade = linha['Age'],
                    genero = linha['Gender'],
                    horas_estudadas = linha['Hours_Studied'],
                    frequencia = linha['Attendance'],
                    horas_sono = linha['Sleep_Hours'],
                    nivel_estresse = linha['Stress_Level'],
                    tempo_tela = linha['Screen_Time'],
                    ultimo_gpa = linha['Previous_GPA'],
                    trabalho=True if str ( linha['Part_Time_Job']).lower() == 'yes' else False,
                    metodo_estudo = linha['Study_Method'],
                    dieta = linha['Diet_Quality'],
                    internet = linha['Internet_Quality'],
                    extracurricular=True if str ( linha['Extracurricular']).lower() == 'yes' else False,
                    quant_aulas_partic = linha['Tutoring_Sessions_Per_Week'],
                    renda_familiar = linha['Family_Income_Level'],
                    ansiedade = linha['Exam_Anxiety_Score'],
                    pontos_final = linha['Final_Score']
                )
                objetos_para_salvar.append(novo_registro)

            DataModels.objects.bulk_create(objetos_para_salvar) # uso de bulk para melhorar a performance ao salvar objts
        except Exception as erro:
            print(f'ERRO: {erro}')
        else:
            print(f'Sucesso! {len(objetos_para_salvar)} linhas importadas')