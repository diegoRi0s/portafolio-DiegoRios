import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime, timedelta

st.set_page_config(page_title="Agro-Node Dashboard", layout="wide")


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

st.subheader("Nodo 01 - Irapuato, Gto.           Siembra: Maíz🌾")
st.divider()


temp_aire = np.random.uniform(24.0, 32.0)
hum_aire = np.random.uniform(15.0, 35.0)
temp_tierra = np.random.uniform(18.0, 22.0)
hum_tierra = np.random.uniform(40.0, 60.0)
caudal = np.random.uniform(1.5, 3.0) 
tiempo_riego = "45 min"
dias_siembra = 42 

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


st.subheader("📊 Histórico Mensual de Humedad del Suelo (Día a Día)")


today = datetime.now()
dates = [today - timedelta(days=x) for x in range(30)]
dates.reverse() 


base_hum = np.linspace(65, 50, 20) 
after_irrigation = np.linspace(75, 60, 10)
monthly_hum_values = np.concatenate((base_hum, after_irrigation))
monthly_hum_values += np.random.normal(0, 2, 30) 


history_data = pd.DataFrame({
    'Fecha': dates,
    'Humedad del Suelo (%)': monthly_hum_values
})
history_data.set_index('Fecha', inplace=True)

st.line_chart(history_data)


st.write(f"Última actualización de datos actuales: {datetime.now().strftime('%H:%M:%S')}")
