import streamlit as st
import detail
import navegation as navy

# Título do Dashboard
st.title("Gestão de armazém")

# Criar o botão
if st.button("Modo Navegação"):
    # Chamar a função quando o botão for clicado
    destino = st.text_input("Destino")
    #destino = "SalaB"
    atual = None

    while atual != destino:
        atual = navy.map(destino)
        st.write(atual)


if st.button("Modo Detalhamento"):

    pn = st.text_input("Part Number")
    sn = st.text_input("Serial Number")
    st.write("Enviado")
