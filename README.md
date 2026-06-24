# AcessAudio

Protótipo multimídia que converte texto, páginas da web e imagens em áudio utilizando bibliotecas de processamento de dados em Python.

## Objetivo
O projeto tem como finalidade apoiar estudantes no aprendizado e promover acessibilidade para pessoas com deficiência visual, permitindo que diferentes formatos de informação sejam transformados em fala.

## Como funciona
1. O usuário pode inserir um texto manual, fornecer a URL de um site ou enviar uma imagem com texto.

2. O sistema processa a entrada:

- Texto → áudio (Text-to-Speech).

- Site → resumo automático → áudio.

- Imagem → OCR (reconhecimento de texto) → áudio.

3. O áudio é reproduzido e pode ser salvo em um arquivo .mp3.

## Estrutura do projeto
- `app.py` → código principal com interface em Streamlit
- `saida.mp3` → exemplo de áudio gerado

## Como executar
Instale as bibliotecas necessárias:
    pip install streamlit newspaper3k gtts pytesseract pillow

Execute a aplicação:
    streamlit run app.py

Acesse no navegador:

- Local: http://localhost:8501  
- Celular: se hospedado no Streamlit Cloud, abra o link público diretamente no navegador do celular.