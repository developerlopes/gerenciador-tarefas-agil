# Gerenciador de Tarefas Ágil

Projeto desenvolvido como parte do portfólio de Engenharia de Software no Centro Universitário UNIFECAF.

## 📋 Descrição

Este projeto simula o desenvolvimento de um sistema de gerenciamento de tarefas utilizando práticas ágeis. O foco é permitir o controle visual do fluxo de trabalho, priorização de atividades e acompanhamento de desempenho da equipe.

O sistema implementa as funcionalidades básicas de um CRUD de tarefas e simula a aplicação do método Kanban no planejamento.

## 🚀 Funcionalidades

- ✅ Criar tarefas com título, descrição e status
- 📄 Visualizar todas as tarefas
- ✏️ Atualizar tarefas existentes
- 🗑️ Excluir tarefas

## 📌 Metodologia Ágil Utilizada

Utilização do **Kanban**, com organização em três colunas:
- A Fazer
- Em Progresso
- Concluído

## 📊 Requisitos

### Funcionais

- RF01: Criar tarefas com título, descrição e status
- RF02: Atualizar e remover tarefas
- RF03: Listar todas as tarefas

### Não Funcionais

- RNF01: O sistema deve responder em até 2 segundos
- RNF02: Deve possuir interface simples

## 🛠️ Tecnologias Utilizadas

- Python 3.x
- Flask (backend)
- HTML/CSS (simples)
- VS Code

## ▶️ Como Executar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/developerlopes/gerenciador-tarefas-agil
   cd gerenciador-tarefas-agil

2. Crie um ambiente virtual (opcional, mas recomendado):

python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows

3. Instale as dependências:

pip install -r requirements.txt

4. Execute o projeto:

python app.py

5. Acesse em:
http://localhost:5000
