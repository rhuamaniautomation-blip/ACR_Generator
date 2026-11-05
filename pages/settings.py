import streamlit as st

def render():
    st.subheader("⚙️ Configuración y Credenciales de IA")
    st.selectbox("Proveedor de IA", ["Gemini 2.5 Flash", "Gemini 2.5 Pro", "GPT-5 Azure OpenAI", "Copilot API"])
    st.text_input("API Key", type="password")
    if st.button("Guardar"):
        st.success("Configuración guardada.")
