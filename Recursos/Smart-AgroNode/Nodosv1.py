import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime, timedelta

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
# Subheader con información del Nodo y la Siembra
st.subheader("Nodo 01 - Irapuato, Gto.           Siembra: Maíz🌾")
st.divider()

# --- SIMULACIÓN DE DATOS ACTUALES ---
# Simulamos valores comunes en campo abierto (marzo/abril en el Bajío)
temp_aire = np.random.uniform(24.0, 32.0)
hum_aire = np.random.uniform(15.0, 35.0)
temp_tierra = np.random.uniform(18.0, 22.0)
hum_tierra = np.random.uniform(40.0, 60.0)
caudal = np.random.uniform(1.5, 3.0) # Litros por minuto
tiempo_riego = "45 min"
dias_siembra = 42 # Días desde que se plantó

# --- DASHBOARD: SECCIÓN DE CUADRADOS DE COLORES (Métricas Actuales) ---
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

st.divider()

# --- SIMULACIÓN DE HISTORIAL MENSUAL (Día a Día) ---
st.subheader("📊 Histórico Mensual de Humedad del Suelo (Día a Día)")

# 1. Generar fechas para los últimos 30 días
today = datetime.now()
dates = [today - timedelta(days=x) for x in range(30)]
dates.reverse() # Ordenar de la más antigua a la más reciente

# 2. Generar datos simulados de humedad (entre 40% y 70%) con una tendencia
# Simulamos una tendencia ligeramente decreciente al principio, luego un riego
base_hum = np.linspace(65, 50, 20) # Primeros 20 días secándose
after_irrigation = np.linspace(75, 60, 10) # 10 días después de un riego
monthly_hum_values = np.concatenate((base_hum, after_irrigation))
# Añadir un poco de ruido aleatorio para que se vea real
monthly_hum_values += np.random.normal(0, 2, 30) 

# 3. Crear el DataFrame
history_data = pd.DataFrame({
    'Fecha': dates,
    'Humedad del Suelo (%)': monthly_hum_values
})
# Establecer la fecha como índice para que Streamlit la use en el eje X
history_data.set_index('Fecha', inplace=True)

# 4. Graficar
st.line_chart(history_data)


st.write(f"Última actualización de datos actuales: {datetime.now().strftime('%H:%M:%S')}")
st.write("Nota: Los datos históricos son simulados para el último mes.")