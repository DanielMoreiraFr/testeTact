from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from data.models import DataModels
from dashboards import utils_dash
from .serializers import DataModelsSerializer

class AlunosPagination(PageNumberPagination): # endpoint para listar alunos
    page_size = 50 # Retorna 50 alunos por vez

class ListaAlunosAPI(APIView):
    def get(self, request):
        alunos = DataModels.objects.all().order_by('id')
        paginator = AlunosPagination()
        result_page = paginator.paginate_queryset(alunos, request)
        serializer = DataModelsSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

class DashboardStatsAPI(APIView): # endpoint pro dash
    def get(self, request):
        data = {
            "perfil": utils_dash.get_dados_perfil(),
            "tendencias": utils_dash.get_dados_tendencias(),
            "idade_distribuicao": utils_dash.get_dados_idade_pizza(),
            "sono_vs_ansiedade": utils_dash.get_dados_sono_vs_ansiedade(),
            "trabalho_vs_desempenho": utils_dash.get_dados_trabalho_vs_desempenho(),
            "total_geral": DataModels.objects.count()
        }
        return Response(data)