🧠 **Real-Time Sales Analytics Platform**  
💡 Desenvolvido com paixão na **Impacta Tecnologia**

</div>

---

## 🌟 **Visão do Projeto**
Um sistema completo e em tempo real para análise de vendas da **SHEIN**, combinando o poder do **FastAPI** com a elegância do **Streamlit** e a robustez do **PostgreSQL**!

---

## ✨ **Funcionalidades Incríveis**

| 🔥 Feature | 🎁 Benefício |
|-------------|--------------|
| 📊 **Dashboard Interativo** | Visualizações dinâmicas e em tempo real |
| 🔗 **API RESTful Completa** | CRUD completo com Swagger automático |
| 🔄 **Dados em Tempo Real** | Atualizações instantâneas ao criar produtos |
| 📈 **Análises Inteligentes** | Insights por categoria e marca |
| 🐳 **Containerização** | Deploy simplificado com Docker |

---

## 🚀 **Comece em 3 Passos**

### ✅ **Pré-requisitos**
```bash

🎮 Passo 1: Clone e Execute
cd shein-sales-dashboard
docker-compose up --build

🌐 Passo 2: Acesse as Aplicações
🖥️ Serviço	🔗 URL	📖 Descrição
Dashboard	http://localhost:8501
	Interface visual incrível
API Docs	http://localhost:8000/docs
	Documentação interativa
Banco	localhost:5432	PostgreSQL robusto
🎉 Passo 3: Explore e Crie!

No Dashboard: adicione produtos pelo formulário lateral

Na API: teste endpoints via Swagger

Veja a mágica acontecer em tempo real! 🎯

🏗️ Arquitetura do Sistema
🎯 SHEIN SALES PLATFORM
├── 🐳 Docker Compose
│   ├── 🗄️ PostgreSQL (Banco de Dados)
│   ├── 🔗 FastAPI (API Backend)
│   └── 📊 Streamlit (Dashboard Frontend)

📁 Estrutura de Arquivos
shein-sales-dashboard/
├── 🐳 docker-compose.yml        # Orquestração dos containers
├── 📊 init.sql                  # Dados iniciais do banco
├── 📁 api/                      # Backend FastAPI
│   ├── 🐳 Dockerfile
│   ├── 🐍 main.py               # Aplicação FastAPI
│   └── 📋 requirements.txt      # Dependências da API
└── 📁 dashboard/                # Frontend Streamlit
    ├── 🐳 Dockerfile
    ├── 🐍 app.py               # Aplicação Streamlit
    └── 📋 requirements.txt     # Dependências do Dashboard

🎮 Como Usar - Guia Rápido
📊 No Dashboard (http://localhost:8501)

✅ Visualizar métricas em tempo real
✅ Adicionar produtos
✅ Ver gráficos dinâmicos
✅ Atualização automática

🔗 Na API (http://localhost:8000/docs)
GET    /produtos/           # Listar produtos
GET    /produtos/{id}       # Buscar produto específico
POST   /produtos/           # Criar produto
PUT    /produtos/{id}       # Atualizar produto
DELETE /produtos/{id}       # Remover produto
GET    /categorias/         # Análise por categoria
GET    /marcas/             # Análise por marca

🗄️ Banco de Dados
Host: localhost
Porta: 5432
Database: sheindb
Usuário: postgres
Senha: postgres

🛠️ Comandos Úteis
🐳 Docker
docker-compose up --build   # Iniciar tudo
docker-compose down         # Parar tudo
docker-compose logs -f      # Ver logs
docker-compose up db api    # Iniciar serviços específicos

🔧 Desenvolvimento (sem Docker)
# API
cd api
pip install -r requirements.txt
uvicorn main:app --reload

# Dashboard
cd dashboard
pip install -r requirements.txt
streamlit run app.py

📊 Exemplo de Dados
{
  "👗 Roupas": 29500,
  "👖 Calça": 19209,
  "👕 Camisa": 18200,
  "📱 Eletrônicos": 16500
}


🧩 Produtos em Destaque

Calça Jeans Feminina Skinny

Smartwatch SHEIN Fit

Vestido Midi Floral

Fone Bluetooth SHEIN Sound

👨‍💻 Equipe de Desenvolvimento
👤 Membro	🎯 Função	🔥 Contribuição
Jadson Porto	Full Stack Developer	Arquitetura & Backend
Michael Ramos	Full Stack Developer	Dashboard & Frontend

👨‍🏫 Orientação: Prof. Odair Gabriel da Silva
🏫 Instituição: Impacta Tecnologia
📘 Disciplina: Projeto Integrador

🌟 Destaques Técnicos
🚀 Performance

⚡ FastAPI com tipagem assíncrona

🎨 Streamlit: interface moderna e intuitiva

🗄️ PostgreSQL: banco robusto e escalável

🔒 Confiabilidade

✅ Containers isolados com Docker

📝 Documentação Swagger automática

🧪 Validação de dados com Pydantic

🎯 Inovações

🔄 Atualização em tempo real

📱 Interface responsiva

🛠️ Pronto para produção (DevOps Ready)

💫 Impacto do Projeto

“Este projeto demonstra o poder da integração entre backend moderno e frontend interativo, criando uma solução completa de análise de dados que pode ser aplicada em diversos contextos empresariais.”

<div align="center">

🎊 Implementação!
Desenvolvido com 💙 por Jadson Porto & Michael Ramos
Sob orientação do Prof. Odair Gabriel – Impacta Tecnologia

⭐ Se este projeto te inspirou, deixe uma estrela! ⭐

📞 Suporte

Em caso de dúvidas, consulte a documentação da API em
http://localhost:8000/docs

ou analise os logs do Docker.

🚀 Happy Coding!

🔗 Links Rápidos
📚 Documentação da API http://localhost:8000/docs
📊 Acessar Dashboard http://localhost:8501/
🐛 Reportar Bug

</div> ```
# Apenas Docker e Docker Compose necessários!
# ⚠️ Nenhuma instalação de Python necessária!
