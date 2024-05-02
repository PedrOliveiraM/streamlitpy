import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

st.set_page_config(page_title="App Economia Teste")
st.title('ECONOMIA - APLICAÇÃO')

# Função para gerar o PDF
def generate_pdf(name, age):
    # Verifica se a idade é válida
    if (65 - age) < 0:
        message = "Você já pode se aposentar"
    else:
        message = f"Faltam {65 - age} anos para você se aposentar"

    # Cria o conteúdo do relatório
    nome = f"Nome: {name} "
    idade =  f"Idade {age}"
    result = message
    # Cria um arquivo PDF
    c = canvas.Canvas("relatorio.pdf", pagesize=letter)
      # Adiciona o texto ao PDF
    c.drawString(100, 750, f"Nome: {name}")
    c.drawString(100, 730, f"Idade: {age}")
    c.drawString(100, 710, message)

    c.save()

# Entrada para configurar o host e a porta
#Nome COMPLETO
name = st.text_input("Nome Completo",placeholder="Digite seu nome completo")
age = st.number_input("Idade", min_value=0, max_value=200)

button = st.button("Gerar")

if button:
    # Chama a função para gerar o PDF
    generate_pdf(name, age)
    st.success("PDF gerado com sucesso!")
