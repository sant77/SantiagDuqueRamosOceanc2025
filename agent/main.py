import streamlit as st
from mars_agent.mars_agent import get_mars_weather_agent

# Configuración de la página
st.set_page_config(page_title="Chatbot de Clima en Marte", page_icon="🚀")
st.title("🚀 Chatbot de Clima en Marte")
st.markdown("Pregúntame sobre el clima marciano: temperaturas, vientos, presiones... ¡Todo basado en datos reales de InSight!")

# Inicializar sesión
if "messages" not in st.session_state:
    st.session_state.messages = []
if "agent" not in st.session_state:
    st.session_state.agent = get_mars_weather_agent()

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

