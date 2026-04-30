# 📊 TesteTact

![Django](https://img.shields.io/badge/Django-4.x-green)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow)

---

## 📖 Descrição

O **TesteTact** é uma plataforma web para análise de dados acadêmicos, focada em fornecer insights sobre o desempenho e bem-estar de estudantes. A aplicação permite correlacionar métricas como GPA, níveis de estresse, qualidade do sono e frequência, auxiliando na tomada de decisões baseada em dados.

O sistema combina backend com Django e Django Rest Framework, junto a uma interface interativa utilizando Bootstrap 5 e visualizações dinâmicas com Chart.js.

---

## 🏗️ Arquitetura

O projeto segue uma arquitetura modular baseada em Django Apps, separando responsabilidades entre API, lógica de negócio e apresentação:

- **Backend (Django + DRF):**
  - Gerenciamento de dados acadêmicos
  - Exposição de endpoints REST
  - Processamento estatístico

- **Frontend (Templates + Bootstrap + Chart.js):**
  - Interface responsiva
  - Dashboards interativos
  - Visualização gráfica dos dados

- **Pipeline de Dados:**
  - Importação via comando customizado (`data_import`)
  - Modelagem estruturada para análise

---

## ⚙️ Funcionalidades

- 📈 Análise de GPA (média acadêmica)
- 😓 Monitoramento de níveis de estresse
- 😴 Avaliação de qualidade do sono
- 📅 Controle de frequência
- 📊 Dashboards interativos com gráficos dinâmicos
- 🔗 API REST para integração externa
- 📥 Importação automatizada de dados

---

## 📁 Estrutura de Pastas

```bash
TesteTact/
│
├── api/                # Endpoints e serializers (DRF)
├── dashboards/         # Lógica estatística e análises
├── data/               # Models e comando data_import
├── static/             # Arquivos estáticos (CSS, JS)
├── templates/          # Templates HTML
├── testeTact/          # Configurações principais do Django
│
└── manage.py

````

---

## 🚀 Como Executar

**1. Clonar o repositório**

```bash
git clone https://github.com/seu-usuario/testetact.git
cd testetact
````

**2. Criar e ativar ambiente virtual**

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

**3. Instalar dependências**

```bash
pip install -r requirements.txt
```

**4. Aplicar migrações**

```bash
python manage.py migrate
```

**5. Importar dados iniciais (opcional)**

```bash
python manage.py data_import
```

**6. Executar o servidor**

```bash
python manage.py runserver
```

**7. Acessar a aplicação**

```bash
http://127.0.0.1:8000/
```

---

```
```
