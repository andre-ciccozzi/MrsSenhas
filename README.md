# MrsSenhas

MrsSenhas é um software simples e moderno para geração de senhas seguras, desenvolvido com Python e Streamlit. O objetivo é facilitar a criação de senhas fortes para proteger suas contas e dados pessoais, oferecendo uma interface visual intuitiva e personalizável.

## Funcionalidades

- Interface gráfica amigável e responsiva (usando Streamlit)
- Geração de senhas personalizadas com opções de:
  - Tamanho da senha (de 6 a 32 caracteres)
  - Inclusão de letras maiúsculas
  - Inclusão de letras minúsculas
  - Inclusão de números
  - Inclusão de símbolos
- Exibição da senha gerada de forma segura
- Log simples de cada geração de senha (útil para depuração)

## Como funciona

O software separa a lógica de geração de senha (arquivo `generate.py`) da interface visual (arquivo `main.py`). O usuário escolhe as opções desejadas na interface, clica em "Gerar Senha" e recebe uma senha forte de acordo com as preferências selecionadas.

