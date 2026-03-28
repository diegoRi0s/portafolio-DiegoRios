import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import plotly.express as px # Para gráficas más interactivas

# Configuración Pro
st.set_page_config(page_title="Master Control System", layout="wide")

# Estilo "Cyber-Industrial"
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    div[data-testid="stMetricValue"] { color: #00FF00; font-family: 'Courier New'; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER MAESTRO ---
col_logo, col_text = st.columns([1, 4])
with col_text:
    st.title("🖥️ SISTEMA MAESTRO DE CONTROL | AGRO-NET v1.0")
    st.write(f"**Estado General del Sistema:** `OPERACIONAL` | **Último Sync:** {datetime.now().strftime('%H:%M:%S')}")

st.divider()

# --- FILA 1: ESTADO DE INFRAESTRUCTURA ---
st.subheader("📡 Estado de la Red y Energía")
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Nodos Activos", "12/12", "Online", delta_color="normal")
with c2:
    st.metric("Latencia Media (LoRa)", "142 ms", "-12ms")
with c3:
    st.metric("Nivel Batería Gateway", "88%", "Cargando ⚡")
with c4:
    st.metric("Uso CPU RPi 5", "12%", "Estable")

st.divider()

# --- FILA 2: CONTROL DE ACTUADORES (INTERACTIVO) ---
st.subheader("🕹️ Control de Actuadores y Riego")
col_ctrl, col_map = st.columns([1, 2])

with col_ctrl:
    st.write("🛰️ **Comandos Remotos**")
    bomba_principal = st.toggle("Bomba Principal (Sector A)", value=True)
    valvula_lora = st.toggle("Válvula Solenoide LoRa (Sector B)", value=False)
    
    if bomba_principal:
        st.success("✅ Bomba enviando 22 L/min")
    else:
        st.error("🛑 Bomba en STANDBY")
        
    st.info("💡 *Nota: Los cambios tardan ~2s en propagarse vía MQTT.*")

with col_map:
    # Simulamos un mapa de calor de humedad en el campo
    st.write("🗺️ **Mapa de Humedad por Sector**")
    map_data = pd.DataFrame(
        np.random.uniform(30, 90, size=(5, 5)),
        columns=[f"Sector {i}" for i in range(1, 6)]
    )
    st.dataframe(map_data.style.background_gradient(cmap='Blues'))

st.divider()

# --- FILA 3: LOG DE EVENTOS CRÍTICOS ---
st.subheader("📝 Log de Eventos del Sistema")
logs = {
    "Timestamp": [datetime.now() - pd.Timedelta(minutes=i*15) for i in range(5)],
    "Evento": ["Sync Exitoso", "Nodo 04: Batería Baja", "Riego Automático Iniciado", "Gateway Reboot", "Cambio de IP"],
    "Prioridad": ["Alta", "Media", "Baja", "Alta", "Baja"]
}

df_logs = pd.DataFrame(logs)
st.dataframe(df_logs, use_container_width=True)

st.divider()

# --- FILA 4: ESTADÍSTICAS Y TENDENCIAS ---
st.subheader("📊 Tendencias de Sensores")
col_chart1, col_chart2 = st.columns(2)

with col_chart1:
    # Gráfica de temperatura
    temp_data = pd.DataFrame({
        "Hora": pd.date_range("00:00", periods=24, freq="h"),
        "Temperatura (°C)": np.random.uniform(18, 35, 24)
    })
    fig_temp = px.line(temp_data, x="Hora", y="Temperatura (°C)", title="Temperatura en últimas 24h")
    st.plotly_chart(fig_temp, use_container_width=True)

with col_chart2:
    # Gráfica de humedad
    humidity_data = pd.DataFrame({
        "Hora": pd.date_range("00:00", periods=24, freq="h"),
        "Humedad (%)": np.random.uniform(40, 85, 24)
    })
    fig_humidity = px.line(humidity_data, x="Hora", y="Humedad (%)", title="Humedad en últimas 24h")
    st.plotly_chart(fig_humidity, use_container_width=True)