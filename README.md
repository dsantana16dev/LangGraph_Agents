# 🤖 AI Agents Lab — LangGraph & LangChain

Este repositório é uma **série prática de estudos** focada na construção de **agentes de IA** utilizando:

* 🧠 LangChain
* 🔀 LangGraph

A ideia é evoluir progressivamente, construindo agentes cada vez mais sofisticados, indo do básico até arquiteturas mais próximas de aplicações reais.

---

## 📚 Estrutura do Projeto

Cada pasta representa um agente independente:

```
.
├── 01-reflection-agent/
├── 02-...
├── 03-...
└── ...
```

---

## 🚀 01. Reflection Agent

### 🧠 Conceito

O **Reflection Agent** implementa um dos padrões mais importantes em agentes de IA:

> **Self-Reflection Loop (Auto-refinamento)**

Ele funciona em um ciclo contínuo:

```
Gerar → Refletir → Melhorar → Repetir
```

---

### ⚙️ Como funciona

O agente possui dois nós principais:

#### ✍️ Generation Node

Responsável por gerar uma resposta inicial.

#### 🤔 Reflection Node

Responsável por analisar criticamente e sugerir melhorias.

---

### 🔁 Fluxo do agente

```
GENERATE → REFLECT → GENERATE → REFLECT → ...
```

O loop continua até atingir uma condição de parada (ex: número de iterações).

---

### 💡 Exemplo de uso

Entrada:

```
Make this tweet better:
@LangChainAI - newly Tool Calling feature is seriously underrated...
```

Saída:

👉 Uma versão refinada após múltiplas iterações de melhoria.

---

### 🧠 Por que isso é importante?

Esse padrão é amplamente utilizado em:

* Geração de conteúdo de alta qualidade
* Revisão automática de textos
* Code review com IA
* Agentes autônomos

---

## 🛠️ Tecnologias utilizadas

* Python 3.11+
* LangChain
* LangGraph
* python-dotenv

---

## ⚙️ Setup

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/ai-agents-lab.git
cd ai-agents-lab
```

---

### 2. Crie o ambiente virtual

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\\Scripts\\activate   # Windows
```

---

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

---

### 4. Configure as variáveis de ambiente

Crie um arquivo `.env`:

```bash
OPENAI_API_KEY=your_key_here
```

---

## 🧪 Roadmap da Série

A ideia é evoluir para agentes mais avançados:

* ✅ 01 - Reflection Agent
* 🔜 02 - Tool Calling Agent
* 🔜 03 - Multi-Agent Collaboration
* 🔜 04 - RAG Agent (Retrieval-Augmented Generation)
* 🔜 05 - Autonomous Agent
* 🔜 06 - AI Agents para negócios (use cases reais)

---

## 🎯 Objetivo

Construir conhecimento prático em:

* Arquitetura de agentes
* Orquestração com grafos
* Loops de decisão e controle
* Aplicações reais com IA

---

## 💡 Possíveis aplicações futuras

* SaaS de geração de conteúdo
* Assistentes corporativos
* Automação de processos
* Agentes especializados por indústria

---

## 👨‍💻 Autor

**Daniel Santana**

---

## ⭐ Contribuição

Sinta-se à vontade para:

* Abrir issues
* Sugerir melhorias
* Contribuir com novos agentes

---

## 📌 Observação

Este repositório faz parte de uma jornada de aprendizado contínuo em IA aplicada.
# 🤖 AI Agents Lab — LangGraph & LangChain

Este repositório é uma **série prática de estudos** focada na construção de **agentes de IA** utilizando:

* 🧠 LangChain
* 🔀 LangGraph

A ideia é evoluir progressivamente, construindo agentes cada vez mais sofisticados, indo do básico até arquiteturas mais próximas de aplicações reais.

---

## 📚 Estrutura do Projeto

Cada pasta representa um agente independente:

```
.
├── 01-reflection-agent/
├── 02-...
├── 03-...
└── ...
```

---

## 🚀 01. Reflection Agent

### 🧠 Conceito

O **Reflection Agent** implementa um dos padrões mais importantes em agentes de IA:

> **Self-Reflection Loop (Auto-refinamento)**

Ele funciona em um ciclo contínuo:

```
Gerar → Refletir → Melhorar → Repetir
```

---

### ⚙️ Como funciona

O agente possui dois nós principais:

#### ✍️ Generation Node

Responsável por gerar uma resposta inicial.

#### 🤔 Reflection Node

Responsável por analisar criticamente e sugerir melhorias.

---

### 🔁 Fluxo do agente

```
GENERATE → REFLECT → GENERATE → REFLECT → ...
```

O loop continua até atingir uma condição de parada (ex: número de iterações).

---

### 💡 Exemplo de uso

Entrada:

```
Make this tweet better:
@LangChainAI - newly Tool Calling feature is seriously underrated...
```

Saída:

👉 Uma versão refinada após múltiplas iterações de melhoria.

---

### 🧠 Por que isso é importante?

Esse padrão é amplamente utilizado em:

* Geração de conteúdo de alta qualidade
* Revisão automática de textos
* Code review com IA
* Agentes autônomos

---

## 🛠️ Tecnologias utilizadas

* Python 3.11+
* LangChain
* LangGraph
* python-dotenv

---

## ⚙️ Setup

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/ai-agents-lab.git
cd ai-agents-lab
```

---

### 2. Crie o ambiente virtual

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\\Scripts\\activate   # Windows
```

---

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

---

### 4. Configure as variáveis de ambiente

Crie um arquivo `.env`:

```bash
OPENAI_API_KEY=your_key_here
```

---

## 🧪 Roadmap da Série

A ideia é evoluir para agentes mais avançados:

* ✅ 01 - Reflection Agent
* 🔜 02 - Tool Calling Agent
* 🔜 03 - Multi-Agent Collaboration
* 🔜 04 - RAG Agent (Retrieval-Augmented Generation)
* 🔜 05 - Autonomous Agent
* 🔜 06 - AI Agents para negócios (use cases reais)

---

## 🎯 Objetivo

Construir conhecimento prático em:

* Arquitetura de agentes
* Orquestração com grafos
* Loops de decisão e controle
* Aplicações reais com IA

---

## 💡 Possíveis aplicações futuras

* SaaS de geração de conteúdo
* Assistentes corporativos
* Automação de processos
* Agentes especializados por indústria

---

## 👨‍💻 Autor

**Daniel Santana**

---

## ⭐ Contribuição

Sinta-se à vontade para:

* Abrir issues
* Sugerir melhorias
* Contribuir com novos agentes

---

## 📌 Observação

Este repositório faz parte de uma jornada de aprendizado contínuo em IA aplicada.

