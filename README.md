

# Consulta de Municípios por Estado – IBGE

Este projeto consiste em uma aplicação desenvolvida em **Python** que realiza a consulta de municípios brasileiros a partir da **API pública do IBGE**, exibindo informações como microrregião e mesorregião.

##  Contexto do projeto

Este projeto é uma **extensão de um trabalho acadêmico desenvolvido anteriormente**, que já realizava toda a consulta e processamento dos dados via **terminal (CLI)**.

Nesta nova etapa, o foco foi **exclusivamente o desenvolvimento de uma interface gráfica**, reaproveitando a lógica já existente, com o objetivo de tornar a aplicação mais intuitiva, visual e amigável ao usuário.

Ou seja:
- ✔ A lógica de consumo da API já estava pronta
- ✔ A evolução foi a **criação da interface gráfica (GUI)**

## 🖥️ Funcionalidades

- Consulta de municípios por **UF**
- Exibição de:
  - Nome do município
  - Microrregião
  - Mesorregião
- Interface gráfica em **modo dark**
- Validação de entrada do usuário
- Tratamento de erros de conexão
- Conversão do projeto para **executável (.exe)**

## 🛠️ Tecnologias utilizadas

- Python
- Tkinter (interface gráfica)
- Requests
- API REST do IBGE
- PyInstaller

  ## ▶️ Como executar o projeto

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/seu-usuario/consulta-municipios-ibge.git
cd consulta-municipios-ibge
