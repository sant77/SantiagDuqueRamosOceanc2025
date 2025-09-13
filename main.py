import streamlit as st
import pandas as pd
from data.data_manager import fetch_and_store_weather, DB_PATH
from agent.mars_agent import get_mars_weather_agent
from config.settings import GOOGLE_API_KEY

# Configuración de la página
st.set_page_config(page_title="Chatbot de Clima en Marte", page_icon="🚀")
st.title("🚀 Chatbot de Clima en Marte")
st.markdown("Pregúntame sobre el clima marciano: temperaturas, vientos, presiones... ¡Todo basado en datos reales de InSight!")

# Inicializar sesión
if "messages" not in st.session_state:
    st.session_state.messages = []
if "agent" not in st.session_state:
    st.session_state.agent = get_mars_weather_agent()

# Botón para actualizar datos
if st.button("Actualizar datos de Marte (últimos Sols)"):
    with st.spinner("Obteniendo datos de NASA..."):
        fetch_and_store_weather()

# Mostrar chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input del usuario
if prompt := st.chat_input("¿Cómo está el clima hoy en Marte?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            response = st.session_state.agent.invoke({"input": prompt, "chat_history": st.session_state.messages[-10:]})
            ai_reply = response["output"]
            st.markdown(ai_reply)
            st.session_state.messages.append({"role": "assistant", "content": ai_reply})

# Sidebar con datos recientes
with st.sidebar:
    st.header("Datos actualizados")
    if st.button("Ver últimos Sols en DB"):
        conn = sqlite3.connect(DB_PATH)
        df = pd.read_sql_query("SELECT * FROM weather ORDER BY sol DESC LIMIT 5", conn)
        st.dataframe(df)
    st.info("Datos crudos de InSight API, sin vectorización.")