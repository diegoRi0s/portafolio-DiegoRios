import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime

# Configuración de la página estilo "Hacker/Dark"
st.set_page_config(page_title="Agro-Node Dashboard", layout="wide")

# Estilo personalizado para los contenedores de colores
st.markdown("""
    <style>
    .metric-container {
        background-color: #1e1e1e;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #00FF00;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🚜 Agro-Node IoT | Monitoreo de Cultivo a Campo Abierto")
st.subheader("Nodo 01 - Irapuato, Gto.")
st.divider()

# --- SIMULACIÓN DE DATOS ---
# Simulamos valores comunes en campo abierto (marzo/abril en el Bajío)
temp_aire = np.random.uniform(24.0, 32.0)
hum_aire = np.random.uniform(15.0, 35.0)
temp_tierra = np.random.uniform(18.0, 22.0)
hum_tierra = np.random.uniform(40.0, 60.0)
caudal = np.random.uniform(1.5, 3.0) # Litros por minuto
tiempo_riego = "45 min"
dias_siembra = 42 # Días desde que se plantó

# --- DASHBOARD: SECCIÓN DE CUADRADOS DE COLORES ---
col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)

with col1:
    st.metric(label="🌡️ Temp. Aire", value=f"{temp_aire:.1f} °C", delta="Normal")
    
with col2:
    st.metric(label="💧 Humedad Aire", value=f"{hum_aire:.1f} %", delta="-2%", delta_color="inverse")

with col3:
    # Color azul para riego
    st.info(f"**⏱️ Tiempo de Riego**\n\n{tiempo_riego}")

with col4:
    st.success(f"**🌱 Humedad Suelo**\n\n{hum_tierra:.1f} %")

with col5:
    st.warning(f"**🌊 Caudal de Riego**\n\n{caudal:.2f} L/min")

with col6:
    st.error(f"**📅 Días desde Siembra**\n\n{dias_siembra} días")

# --- GRÁFICA DE MONITOREO EN TIEMPO REAL ---
st.divider()
st.subheader("📊 Histórico de Humedad del Suelo (Últimas 24h)")

# Crear datos falsos para la gráfica
chart_data = pd.DataFrame(
    np.random.randn(24, 1) / 10 + 0.5,
    columns=['Humedad']
)
st.line_chart(chart_data)

st.write(f"Última actualización: {datetime.now().strftime('%H:%M:%S')}")