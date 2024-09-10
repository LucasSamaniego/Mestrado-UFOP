import streamlit as st
import detail
import navegation as navy
import display

# Título do Dashboard
st.title("Gestão de armazém")
destino = st.text_input("Destino")

if st.button("Sair Modo Navegação"):
    sair = True

# Criar o botão
if st.button("Modo Navegação"):
    # Chamar a função quando o botão for clicado
    atual = None
    sair == False

    while atual != destino and sair == False:
        atual = navy.map(destino)
        st.write(atual)
    
    st.write("Chegou ao destino!")


if st.button("Modo Detalhamento"):

    pn = st.text_input("Part Number")
    sn = st.text_input("Serial Number")
    st.write("Enviado")


if st.button("Ligar display"):

    display.show("Direita")
    st.write("Enviado")
