from gtts import gTTS

texto = "O AcessAudio apoia estudantes e promove acessibilidade, convertendo textos em áudio para facilitar o aprendizado e a inclusão."

tts = gTTS(text=texto, lang='pt')

tts.save("saida.mp3")

print("Áudio gerado com sucesso! Verifique o arquivo saida.mp3 na pasta do projeto.")