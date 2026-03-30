import streamlit as st

from generate import generate_password

st.set_page_config(page_title="Gerador de Senhas", page_icon="🔒", layout="centered")

st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #e0e7ff 0%, #f0fdfa 100%);
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 4px 32px rgba(0,0,0,0.08);
    }
    .stButton>button {
        background: linear-gradient(90deg, #6366f1 0%, #06b6d4 100%);
        color: white;
        font-weight: bold;
        border-radius: 8px;
        border: none;
        padding: 0.5rem 2rem;
        font-size: 1.1rem;
    }
    .stTextInput>div>input {
        font-size: 1.2rem;
        font-weight: bold;
        color: #0f172a;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='main'>", unsafe_allow_html=True)
st.title("Gerador de Senhas")
st.write("Crie senhas fortes")

length = st.slider("Tamanho da senha", 6, 32, 12)
col1, col2, col3, col4 = st.columns(4)
with col1:
    use_upper = st.checkbox("Maiúsculas", value=True)
with col2:
    use_lower = st.checkbox("Minúsculas", value=True)
with col3:
    use_digits = st.checkbox("Números", value=True)
with col4:
    use_symbols = st.checkbox("Símbolos", value=True)


if st.button("Gerar Senha"):
    password = generate_password(
        length,
        use_upper=use_upper,
        use_lower=use_lower,
        use_digits=use_digits,
        use_symbols=use_symbols
    )
    st.text_input("Senha Gerada", value=password, key="senha", disabled=True)
else:
    st.text_input("Senha Gerada", value="", key="senha", disabled=True)

st.markdown("</div>", unsafe_allow_html=True)
