from django.db.models import Avg
from django.db.models.functions import Round
from data.models import DataModels

def get_media_nota(campo, valor):
    res = DataModels.objects.filter(**{campo: valor}).aggregate(Avg('pontos_final'))['pontos_final__avg']
    return round(float(res), 2) if res else 0


def get_dados_perfil():
    return {
        'labels_genero': ['Masculino', 'Feminino', 'Não-Binário'],
        'dados_genero': [get_media_nota('genero', 'Male'), get_media_nota('genero', 'Female'), get_media_nota('genero', 'Non-Binary')],
        'l_ansiedade': ['Baixa', 'Média', 'Alta'],
        'd_ansiedade': [get_media_nota('ansiedade', 1), get_media_nota('ansiedade', 2), get_media_nota('ansiedade', 3)],
        'l_renda': ['Baixa', 'Média', 'Alta'],
        'd_renda': [get_media_nota('renda_familiar', 'Low'), get_media_nota('renda_familiar', 'Middle'), get_media_nota('renda_familiar', 'High')],
    }

def get_dados_tendencias():
    dados_sono = DataModels.objects.annotate(h=Round('horas_sono')).values('h').annotate(m=Avg('pontos_final')).order_by('h')
    dados_tela = DataModels.objects.annotate(h=Round('tempo_tela')).values('h').annotate(m=Avg('pontos_final')).order_by('h')
    dados_freq = DataModels.objects.annotate(f=Round('frequencia')).values('f').annotate(m=Avg('pontos_final')).order_by('f')
    
    return {
        'l_sono': [f"{int(i['h'])}h" for i in dados_sono], 'd_sono': [round(float(i['m']), 2) for i in dados_sono],
        'l_tela': [f"{int(i['h'])}h" for i in dados_tela], 'd_tela': [round(float(i['m']), 2) for i in dados_tela],
        'l_freq': [f"{int(i['f'])}%" for i in dados_freq], 'd_freq': [round(float(i['m']), 2) for i in dados_freq],
    }

def get_dados_idade_pizza():
    estudantes = DataModels.objects.values('idade', 'pontos_final')
    grupos = {}
    for e in estudantes:
        if e['idade']:
            faixa = (e['idade'] // 2) * 2
            label = f"{faixa}-{faixa+1} anos"
            if label not in grupos: grupos[label] = {'soma': 0, 'cnt': 0}
            grupos[label]['soma'] += e['pontos_final']
            grupos[label]['cnt'] += 1
    
    labels = sorted(grupos.keys())
    dados = [round(grupos[l]['soma'] / grupos[l]['cnt'], 2) for l in labels]
    return {'l_idade': labels, 'd_idade': dados}

def get_dados_sono_vs_ansiedade():
    dados = DataModels.objects.annotate(
        h_sono=Round('horas_sono')
    ).values('h_sono').annotate(
        media_ansiedade=Avg('ansiedade')
    ).order_by('h_sono')

    return {
        'l_sono_ans': [f"{int(i['h_sono'])}h" for i in dados],
        'd_sono_ans': [round(float(i['media_ansiedade']), 2) for i in dados]
    }

def get_dados_trabalho_vs_desempenho():
    medias = DataModels.objects.values('trabalho').annotate(
        media_nota=Avg('pontos_final')
    ).order_by('-trabalho')

    labels = []
    valores = []
    
    for item in medias:
        status = "Trabalha" if item['trabalho'] else "Não Trabalha"
        labels.append(status)
        valores.append(round(item['media_nota'], 2))

    return {
        'l_trabalho_nota': labels,
        'd_trabalho_nota': valores
    }