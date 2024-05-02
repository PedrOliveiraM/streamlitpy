import streamlit as st
from fpdf import FPDF
import io

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
    
    # Salva o PDF em memória
    pdf_bytes = pdf.output(dest='S').encode('latin1')
    
    return pdf_bytes

# Entrada para configurar o host e a porta
# Nome COMPLETO
name = st.text_input("Nome Completo", placeholder="Digite seu nome completo")
age = st.number_input("Idade", min_value=0, max_value=200)

# Chama a função para gerar o PDF
pdf_bytes = generate_pdf(name, age)

# Exibe um botão para baixar o PDF
st.download_button(
    label="Baixar PDF",
    data=pdf_bytes,
    file_name="relatorio.pdf",
    mime="application/pdf"
)
st.success("PDF gerado com sucesso!")
