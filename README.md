# TesteTact - Academic Data Analysis Platform

![Django](https://img.shields.io/badge/Framework-Django-092e20?style=for-the-badge&logo=django)
![JavaScript](https://img.shields.io/badge/Frontend-JS%20%2F%20Chart.js-f7df1e?style=for-the-badge&logo=javascript&logoColor=black)
![Python](https://img.shields.io/badge/Language-Python%203-3776ab?style=for-the-badge&logo=python&logoColor=white)

## 📝 Descrição
O **TesteTact** é uma plataforma desenvolvida para gerenciar e analisar o desempenho de estudantes através de métricas comportamentais e acadêmicas. O sistema correlaciona variáveis como horas de sono, nível de ansiedade e frequência escolar com o desempenho acadêmico, fornecendo insights através de um dashboard interativo.

## 🏗️ Arquitetura do Sistema
O projeto utiliza uma estrutura modular no Django para separar responsabilidades:

*   **`api/`**: Gerencia os serializadores e endpoints que alimentam os gráficos via JSON.
*   **`dashboards/`**: Contém a lógica de processamento de dados e os scripts para visualização estatística.
*   **`data/`**: Responsável pela persistência de dados e comandos de sistema, como o script de importação de CSV.
*   **`testeTact/`**: Diretório principal com as configurações de sistema, URLs e WSGI.
*   **`static/`**: Centraliza arquivos CSS e JS organizados por contexto.
*   **`templates/`**: Armazena os arquivos HTML estruturados por aplicação.

## 🚀 Funcionalidades Principais
*   **Ingestão de Dados**: Comando administrativo customizado para carregar dados de arquivos CSV diretamente no banco de dados.
*   **Dashboards Interativos**: Visualização de dados dinâmica utilizando **Chart.js** (Gráficos de Barras, Linhas e Pizza).
*   **Consumo Assíncrono**: Uso de JavaScript `fetch` para atualização de dados sem recarregamento de página.

## 📂 Estrutura de Pastas
```text
TESTETACT/
├── api/                  # Endpoints REST
├── dashboards/           # Lógica de Dashboards e Estatísticas
├── data/                 # Modelagem e Comandos (management/commands)
├── static/               # Assets (CSS/JS modulares)
├── templates/            # Arquivos HTML (organizados por app)
├── testeTact/            # Configurações globais do Django
├── student_performance_finalscore.csv  # Dataset original
└── manage.py             # CLI do Django
```

## 🛠️ Como Executar o Projeto

1. **Instalar Dependências**:
```bash
pip install django djangorestframework
```

2. **Preparar o Banco de Dados**:
```bash
python manage.py migrate
```

3. **Importar Dados do CSV**:
```bash
python manage.py data_import
```

4. **Iniciar Servidor**:
```bash
python manage.py runserver
```
Acesse: `http://127.0.0.1:8000/`

---
**Projeto desenvolvido para o processo de avaliação técnica da Tact.**
```