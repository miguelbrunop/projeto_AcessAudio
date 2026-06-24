import streamlit as st
from newspaper import Article
from gtts import gTTS
import pytesseract
from PIL import Image
import os

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

st.set_page_config(page_title="AcessAudio", layout="wide")

st.title("🎧 AcessAudio")

opcao = st.sidebar.selectbox("Escolha uma opção:", 
                             ["✍️ Texto manual", "🌐 Resumo de site", "🖼️ Texto em imagem"])

if opcao == "✍️ Texto manual":
    st.header("✍️ Texto manual")
    texto = st.text_area("Digite o texto:", height=200)
    if st.button("Gerar áudio"):
        tts = gTTS(text=texto, lang='pt')
        tts.save("saida.mp3")
        os.system("start saida.mp3")
        st.success("Áudio gerado e reproduzido!")

elif opcao == "🌐 Resumo de site":
    st.header("🌐 Resumo de site")
    url = st.text_input("Digite a URL da notícia/artigo:")
    if st.button("Gerar resumo e áudio"):
        artigo = Article(url, language="pt")
        artigo.download()
        artigo.parse()
        artigo.nlp()
        resumo = artigo.summary
        st.text_area("Resumo gerado:", resumo, height=200)
        tts = gTTS(text=resumo, lang='pt')
        tts.save("saida.mp3")
        os.system("start saida.mp3")
        st.success("Áudio gerado e reproduzido!")

elif opcao == "🖼️ Texto em imagem":
    st.header("🖼️ Texto em imagem")
    arquivo_imagem = st.file_uploader("Envie uma imagem", type=["jpg", "jpeg", "png"])
    if arquivo_imagem is not None:
        imagem = Image.open(arquivo_imagem)
        st.image(imagem, caption="Imagem enviada", width=500)
        if st.button("Reconhecer texto e gerar áudio"):
            texto = pytesseract.image_to_string(imagem, lang="por")
            st.text_area("Texto reconhecido:", texto, height=200)
            tts = gTTS(text=texto, lang='pt')
            tts.save("saida.mp3")
            os.system("start saida.mp3")
            st.success("Áudio gerado e reproduzido!")