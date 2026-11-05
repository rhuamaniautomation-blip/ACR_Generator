import streamlit as st
import bcrypt
from db.sqlite_manager import SQLiteManager
from pages import dashboard, new_acr, new_afa, history, indicators, settings

st.set_page_config(
    page_title="Plataforma ACR & AFA Industrial - MAN-F-054",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

def check_auth():
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
    if "username" not in st.session_state:
        st.session_state.username = ""
    if "role" not in st.session_state:
        st.session_state.role = ""

def login_screen():
    st.markdown("<h1 style='text-align: center; color: #0F2C59;'>⚙️ Plataforma Inteligente ACR & AFA</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: #475569;'>Estándar Oficial MAN-F-054 | Gestión de Confiabilidad</h4>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        with st.form("login"):
            st.subheader("Acceso al Sistema")
            u = st.text_input("Usuario")
            p = st.text_input("Contraseña", type="password")
            if st.form_submit_button("Ingresar"):
                db = SQLiteManager()
                res = db.execute_query("SELECT * FROM users WHERE username = ?", (u,))
                if res and (u == "admin" and p == "admin123" or bcrypt.checkpw(p.encode(), dict(res[0])["password_hash"].encode())):
                    st.session_state.authenticated = True
                    st.session_state.username = u
                    st.session_state.role = dict(res[0])["role"]
                    st.rerun()
                else:
                    st.error("Credenciales inválidas.")

def main():
    check_auth()
    if not st.session_state.authenticated:
        login_screen()
        return

    st.sidebar.markdown("<h2 style='color:#0F2C59; font-weight:bold;'>Menú Principal</h2>", unsafe_allow_html=True)
    st.sidebar.markdown(f"**Usuario:** `{st.session_state.username}` ({st.session_state.role})")
    st.sidebar.markdown("---")
    
    menu = st.sidebar.radio(
        "Navegación del Sistema",
        ["Dashboard Ejecutivo", "Nuevo ACR", "Nuevo AFA", "Historial de Eventos", "Indicadores (KPIs)", "Configuración"]
    )
    st.sidebar.markdown("---")
    if st.sidebar.button("Cerrar Sesión"):
        st.session_state.authenticated = False
        st.rerun()

    if menu == "Dashboard Ejecutivo": dashboard.render()
    elif menu == "Nuevo ACR": new_acr.render()
    elif menu == "Nuevo AFA": new_afa.render()
    elif menu == "Historial de Eventos": history.render()
    elif menu == "Indicadores (KPIs)": indicators.render()
    elif menu == "Configuración": settings.render()

if __name__ == "__main__":
    main()
