TesteTact
📝 Descrição

O TesteTact é uma plataforma desenvolvida para gerenciar e analisar o desempenho de estudantes através de métricas comportamentais e acadêmicas. O sistema correlaciona variáveis como horas de sono, nível de ansiedade e frequência escolar com o desempenho acadêmico, fornecendo insights através de um dashboard interativo.
🏗️ Arquitetura do Sistema

O projeto utiliza uma estrutura modular no Django para separar responsabilidades:

    api/: Gerencia os serializadores e endpoints que alimentam os gráficos via JSON.

    dashboards/: Contém a lógica de processamento de dados e os scripts para visualização estatística.

    data/: Responsável pela persistência de dados e comandos de sistema, como o script de importação de CSV.

    testeTact/: Diretório principal com as configurações de sistema, URLs e WSGI.

    static/: Centraliza arquivos CSS e JS organizados por contexto.

    templates/: Armazena os arquivos HTML estruturados por aplicação.

🚀 Funcionalidades Principais

    Ingestão de Dados: Comando administrativo customizado para carregar dados de arquivos CSV diretamente no banco de dados.

    Dashboards Interativos: Visualização de dados dinâmica utilizando Chart.js (Gráficos de Barras, Linhas e Pizza).

    Consumo Assíncrono: Uso de JavaScript fetch para atualização de dados sem recarregamento de página.

📂 Estrutura de Pastas
Plaintext

Bash

TESTETACT/
├── api/                  # Endpoints REST
├── dashboards/           # Lógica de Dashboards e Estatísticas
├── data/                 # Modelagem e Comandos (management/commands)
├── static/               # Assets (CSS/JS modulares)
├── templates/            # Arquivos HTML (organizados por app)
├── testeTact/            # Configurações globais do Django
├── student_performance_finalscore.csv  # Dataset original
└── manage.py             # CLI do Django

🛠️ Como Executar o Projeto

    Instalar Dependências:

Bash

pip install django djangorestframework

    Preparar o Banco de Dados:

Bash

python manage.py migrate

    Importar Dados do CSV:

Bash

python manage.py data_import

    Iniciar Servidor:

Bash

python manage.py runserver

Acesse: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)