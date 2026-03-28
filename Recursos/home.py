import streamlit as st

# 1. CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(
    page_title="Lobos UPJR - Dashboard Hub",
    page_icon="🐺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. ESTILO PERSONALIZADO (CSS)
st.markdown("""
    <style>
    /* Fondo y texto general */
    .main { background-color: #FFFFFF; }
    
    /* Estilo de los botones */
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 4em;
        background-color: #f0f2f6;
        color: #1e1e1e;
        border: 2px solid #007BFF;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #007BFF;
        color: white;
        border: 2px solid #0056b3;
    }
    
    /* Contenedor de bienvenida */
    .welcome-box {
        padding: 30px;
        border-radius: 15px;
        background: linear-gradient(135deg, #007BFF 0%, #00d4ff 100%);
        color: white;
        margin-bottom: 25px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. CABECERA DE BIENVENIDA
st.markdown("""
    <div class="welcome-box">
        <h1>🐺 LOBOS UPJR | Proyectos de Ingeniería</h1>
        <p>Hub Centralizado de Telemetría, Control e IoT Industrial</p>
    </div>
    """, unsafe_allow_html=True)

# 4. COLUMNAS PRINCIPALES
col_intro, col_nav = st.columns([1.5, 1])

with col_intro:
    st.subheader("🚀 Sobre este Portafolio")
    st.write("""
    Bienvenido a mi ecosistema de aplicaciones de ingeniería. Aquí integro soluciones reales 
    que van desde la **Agricultura de Precisión** hasta la **Telemetría de Alta Competición**.
    
    **Tecnologías implementadas:**
    - **Python & Streamlit:** Interfaz de usuario y lógica de datos.
    - **IoT (LoRa & MQTT):** Comunicación entre nodos y sistemas maestros.
    - **Data Visualization:** Análisis de rendimiento en tiempo real con Plotly.
    """)
    
    st.image("https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&q=80&w=1000", 
             caption="Sistemas Embebidos e Ingeniería Electrónica", use_container_width=True)

with col_nav:
    st.info("### 📂 Selecciona una Terminal")
    st.write("Haz clic en un botón para saltar directamente al dashboard:")
    
    # BOTÓN PROYECTO 1: AGRO-IOT
    if st.button("🌱 Monitor de Cultivo (Agro-IoT)"):
        st.switch_page("C:\\Users\\dieco\\Documents\\Proyectos\\Portafolio\\portafolio-DiegoRios\\Recursos\\Proyectos\\pages\\Nodosv1.py") # Asegúrate que el nombre coincida
        
    # BOTÓN PROYECTO 2: MAESTRO
    if st.button("🖥️ Sistema Maestro de Control"):
        st.switch_page("C:\Users\dieco\Documents\Proyectos\Portafolio\portafolio-DiegoRios\Recursos\Proyectos\pages\ControlMaestro.py")
        
    # BOTÓN PROYECTO 3: FORMULA E
    if st.button("🏎️ Telemetría Formula E (AHR)"):
        st.switch_page("C:\\Users\\dieco\\Documents\\Proyectos\\Portafolio\\portafolio-DiegoRios\\Recursos\\Proyectos\\pages\\Telemetria.py")

    # BOTÓN PROYECTO 4: CIRCUITO
    if st.button("🗺️ Telemetría sobre Circuito (AHR)"):
        st.switch_page("C:\\Users\\dieco\\Documents\\Proyectos\\Portafolio\\portafolio-DiegoRios\\Recursos\\Proyectos\\pages\\Circuito.py")


st.divider()

# 5. ESTADO DEL SISTEMA (FOOTER INTERACTIVO)
st.subheader("🛠️ Status Global del Hardware")
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.success("**Gateway:** ONLINE 🟢")
with c2:
    st.success("**Nodos LoRa:** 12 ACTV")
with c3:
    st.warning("**Batería UPS:** 88%")
with c4:
    st.info("**Ubicación:** Irapuato, Gto.")

st.caption("Developed by Diego Ríos | IRT - UPJR | 2025")