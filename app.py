import streamlit as st
from fpdf import FPDF

st.set_page_config(page_title="App Economia Teste")
st.title('ECONOMIA - APLICAÇÃO')

# Função para gerar o PDF
def generate_pdf(name, age):
    # Verifica se a idade é válida
    if (65 - age) < 0:
        message = "Você já pode se aposentar"
    else:
        message = f"Faltam {65 - age} anos para você se aposentar"

    # Cria um objeto PDF
    pdf = FPDF()
    pdf.add_page()
    
    # Define a fonte e o tamanho do texto
    pdf.set_font("Arial", size = 12)
    
    # Adiciona o texto ao PDF
    pdf.cell(200, 10, txt = "Nome: " + name, ln = True)
    pdf.cell(200, 10, txt = "Idade: " + str(age), ln = True)
    pdf.cell(200, 10, txt = message, ln = True)

    # Salva o PDF com o nome "relatorio.pdf"
    pdf.output("relatorio.pdf")

# Entrada para configurar o host e a porta
# Nome COMPLETO
name = st.text_input("Nome Completo", placeholder="Digite seu nome completo")
age = st.number_input("Idade", min_value=0, max_value=200)

button = st.button("Gerar")

if button:
    # Chama a função para gerar o PDF
    generate_pdf(name, age)
    st.success("PDF gerado com sucesso!")
