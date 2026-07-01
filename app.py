import streamlit as st
import google.generativeai as genai

# Configuração da página do Streamlit
st.set_page_config(page_title="Painel Astrológico Pro", page_icon="🔮", layout="centered")

# Estilização mística (Roxo e Ouro)
st.markdown("""
    <style>
    .main { background-color: #0f0c1b; color: #f3e6ff; }
    h1, h2, h3 { color: #ffd700 !important; font-family: 'Georgia', serif; }
    .stButton>button { background-color: #4b0082; color: #ffd700; border: 1px solid #ffd700; border-radius: 10px; }
    .stButton>button:hover { background-color: #ffd700; color: #4b0082; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔮 Colegiado Autoconhecimento & Espiritualidade")
st.subheader("Assistente de Previsões e Atendimentos")

# Campo para colocar a chave da API com segurança dentro do app
api_key = st.sidebar.text_input("Insira sua Chave de API do Google:", type="password")

if api_key:
    genai.configure(api_key=api_key)
else:
    st.warning("⚠️ Por favor, insira sua Chave de API na barra lateral para começar.")

# --- SEÇÃO 1: PREVISÃO SEMANAL ---
st.markdown("---")
st.header("🌌 1. Previsão Semanal Geral")
transitos = st.text_area("Digite os trânsitos marcantes da semana:", placeholder="Ex: Sol em sextil com Urano, Marte em Leão...")
foco_semana = st.text_input("Qual o foco ou tom espiritual da semana?", placeholder="Ex: Inovação com os pés no chão, inteligência emocional...")

if st.button("Gerar Texto Semanal"):
    if not api_key:
        st.error("Insira a Chave de API primeiro!")
    elif not transitos:
        st.error("Por favor, digite os trânsitos da semana.")
    else:
        with st.spinner("Sintonizando com os astros..."):
            model = genai.GenerativeModel('gemini-1.5-flash')
            prompt = f"""
            Você é um astrólogo sênior e terapeuta esotérico focado em autoconhecimento de alta performance. 
            Com base nos seguintes trânsitos: {transitos}, e com o foco semanal em: {foco_semana}, 
            escreva um texto de orientação semanal magnético, profundo e místico, mas com conselhos muito práticos.
            Use os seguintes subtópicos no texto:
            - 🔮 Mensagem dos Astros: O Céu da Semana
            - O Clima Geral (Análise profunda dos aspectos)
            - O Impulso para Ação (Como direcionar a energia)
            - 💡 Conselhos Práticos para a Semana (No Trabalho e Nas Relações)
            O tom deve ser acolhedor, maduro e transformador.
            """
            response = model.generate_content(prompt)
            st.markdown("### ✨ Sua Previsão Semanal")
            st.write(response.text)

# --- SEÇÃO 2: ANÁLISE PERSONALIZADA ---
st.markdown("---")
st.header("👤 2. Direcionamento Personalizado por Cliente")
nome_cliente = st.text_input("Nome do Cliente:")
dados_cliente = st.text_area("Dados do Mapa do Cliente e Momento Atual:", placeholder="Ex: Sol em Touro, Asc em Escorpião. Passando por transição de carreira...")

if st.button("Gerar Relatório do Cliente"):
    if not api_key:
        st.error("Insira a Chave de API primeiro!")
    elif not transitos or not dados_cliente:
        st.error("Preencha os trânsitos da semana e os dados do cliente.")
    else:
        with st.spinner("Cruzando dados do mapa com o céu atual..."):
            model = genai.GenerativeModel('gemini-1.5-flash')
            prompt = f"""
            Como um astrólogo profissional, cruze o céu atual que tem estes trânsitos: {transitos}, 
            com o mapa e momento deste cliente: Nome: {nome_cliente}. Detalhes: {dados_cliente}.
            Gere um relatório personalizado mostrando como os trânsitos da semana afetam diretamente a vida dele(a).
            Inclua:
            - Uma introdução personalizada e profunda direcionada ao cliente.
            - Pontos de atenção no céu da semana para o mapa dele(a).
            - 🧭 Diretrizes de orientação: Tópicos rápidos para guiar o astrólogo no atendimento ou na gravação de um áudio.
            Mantenha o tom de alta performance espiritual e acolhimento.
            """
            response = model.generate_content(prompt)
            st.markdown(f"### ✨ Relatório: {nome_cliente}")
            st.write(response.text)
