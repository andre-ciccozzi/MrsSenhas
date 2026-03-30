import streamlit as st
from generate import generate_password

st.set_page_config(page_title="Gerador de Senhas Automatizado", page_icon="🔒", layout="centered")


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
        width: 100%;
    }
    .stTextInput>div>input {
        font-size: 1.2rem;
        font-weight: bold;
        color: #0f172a;
        font-family: 'Courier New', Courier, monospace;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='main'>", unsafe_allow_html=True)
st.title("Gerador de Senhas")
st.write("Crie senhas fortes e seguras instantaneamente")


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


if 'senha_gerada' not in st.session_state:
    st.session_state['senha_gerada'] = ""
if 'erro' not in st.session_state:
    st.session_state['erro'] = ""


if st.button("Gerar Senha"):
    password = generate_password(
        length,
        use_upper=use_upper,
        use_lower=use_lower,
        use_digits=use_digits,
        use_symbols=use_symbols
    )
    
    if password.startswith("Erro"):
        st.session_state['erro'] = password
        st.session_state['senha_gerada'] = ""
    else:
        st.session_state['senha_gerada'] = password
        st.session_state['erro'] = ""
    
   
    st.rerun()


if st.session_state['erro']:
    st.error(st.session_state['erro'])

st.text_input(
    "Senha Gerada", 
    value=st.session_state['senha_gerada'], 
    key="senha_display", 
    disabled=True
)

st.markdown("</div>", unsafe_allow_html=True)