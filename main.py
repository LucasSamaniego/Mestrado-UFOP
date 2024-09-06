import streamlit as st
import detail
import navegation as navy

# Título do Dashboard
st.title("Gestão de armazém")

# Criar o botão
if st.button("Clique aqui"):
    # Chamar a função quando o botão for clicado
    destino = SalaB
    atual = None

    while atual != destino:
        atual = navy.map(destino)
        st.write(msg)
