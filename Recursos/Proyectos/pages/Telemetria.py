import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime

# Configuración de página
st.set_page_config(page_title="Formula E Telemetry", layout="wide")

# --- ESTILO "LIGHT & CLEAN" ---
st.markdown("""
    <style>
    .main { background-color: #FFFFFF; color: #1e1e1e; }
    div[data-testid="stMetricValue"] { color: #007BFF; font-family: 'Segoe UI', sans-serif; font-weight: bold; }
    hr { border-top: 1px solid #ddd; }
    </style>
    """, unsafe_allow_html=True)

st.title("⚡ FORMULA E LIVE TELEMETRY | GEN3")
st.subheader("Driver: Diego Rios | Team: Lobos UPJR Racing 🏎️")
st.divider()

# --- DATOS DE CARRERA ---
lap_current = 24
battery_soc = 42.5
speed = 78 # Velocidad cerca del límite solicitado

# --- FILA 1: VELOCÍMETRO Y TIEMPO ESTIMADO ---
col_gauge, col_time, col_batt = st.columns([1.5, 1, 1])

with col_gauge:
    fig_gauge = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = speed,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "SPEED (km/h)", 'font': {'size': 18}},
        gauge = {
            'axis': {'range': [None, 80]},
            'bar': {'color': "#007BFF"},
            'steps': [
                {'range': [0, 60], 'color': '#f0f2f6'},
                {'range': [60, 80], 'color': '#ff4b4b'}]
        }
    ))
    fig_gauge.update_layout(height=250, margin=dict(l=10, r=10, t=40, b=10))
    st.plotly_chart(fig_gauge, use_container_width=True)

with col_time:
    # Tiempo estimado a 80km/h con variaciones de frenado
    st.metric("EST. LAP TIME (AHR)", "3:44.205", "Slow Track Mode")
    st.info("**Location:** Autódromo Hermanos Rodríguez, MX")

with col_batt:
    st.metric("BATTERY (SOC)", f"{battery_soc}%", "-0.8% / LAP")
    st.write("**DRIVE MODE**")
    st.success("ECO-REGEN ACTIVE")

st.divider()

# --- FILA 2: GRÁFICA DE TELEMETRÍA DE PEDALES (THR vs BRK) ---
st.subheader("Telemetría de Pedales (Acelerador vs Freno)")

# Simulación de telemetría en una sección del circuito (Recta -> Curva 1 -> S'es)
t = np.linspace(0, 20, 100)
# Acelerador: Sube en rectas, baja en curvas
throttle = 50 + 40 * np.sin(t/2) + np.random.normal(0, 2, 100)
throttle = np.clip(throttle, 0, 100)
# Freno: Sube cuando el acelerador baja
brake = 100 - throttle + np.random.normal(0, 5, 100)
brake = np.clip(brake, 0, 100) * (throttle < 30) # Solo frena si el acelerador es bajo

fig_pedals = go.Figure()
fig_pedals.add_trace(go.Scatter(x=t, y=throttle, name='THROTTLE (Acc)', line=dict(color='#00FF00', width=2), fill='tozeroy'))
fig_pedals.add_trace(go.Scatter(x=t, y=brake, name='BRAKE', line=dict(color='#FF0000', width=2), fill='tozeroy'))

fig_pedals.update_layout(
    template="plotly_white",
    xaxis_title="Tiempo (Segundos)",
    yaxis_title="Porcentaje (%)",
    height=350,
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)
st.plotly_chart(fig_pedals, use_container_width=True)

st.divider()

# --- FILA 3: TABLA DE SECTORES ---
st.subheader("Análisis Detallado por Sector")
sectores_hermanos = pd.DataFrame({
    "Sector": ["Recta Principal", "Curva 1 (Moises S.)", "S de alta velocidad", "Entrada al Foro Sol", "Curva Peraltada"],
    "Speed (km/h)": [79, 32, 55, 28, 74],
    "Acelerador %": [100, 5, 75, 0, 95],
    "Freno %": [0, 95, 10, 100, 0],
    "Regeneración": ["0 kW", "350 kW", "45 kW", "350 kW", "10 kW"]
})

# Aplicamos colores a la tabla
def color_pedals(val):
    if isinstance(val, int):
        if val > 80: return 'color: red; font-weight: bold'
        if val < 10: return 'color: green;'
    return ''

st.table(sectores_hermanos.style.applymap(color_pedals, subset=['Acelerador %', 'Freno %']))

# --- FILA 4: TABLA DE CONSISTENCIA (ÚLTIMAS 5 VUELTAS) ---
st.divider()
st.subheader("🏁 Tiempos: Últimas 5 Vueltas")

# Generamos tiempos alrededor de los 3:44.xxx con variaciones realistas
laps_data = {
    "Lap": [24, 23, 22, 21, 20],
    "Lap Time": ["3:44.205", "3:44.118", "3:44.590", "3:43.902", "3:45.002"],
    "S1 (s)": [45.273765, 45.136647, 45.5654353, 45.653757, 45.754643],
    "S2 (s)": [92.412543235, 92.31543234, 92.63235452, 92.10023523, 92.5014325],
    "S3 (s)": [86.623523, 86.764323, 86.423543, 86.878543, 86.765434],
    "Status": ["PERSONAL BEST" if i == 3 else "VALID" for i in range(5)]
}

df_consistency = pd.DataFrame(laps_data)

# Función para resaltar la vuelta más rápida
def highlight_best(s):
    is_best = s == "3:43.902"
    return ['background-color: #D4EDDA; font-weight: bold' if is_best else '' for v in s]

# Mostramos la tabla con estilo
st.table(df_consistency.style.set_properties(**{'text-align': 'center'}))

st.info("💡 **Análisis de Telemetría:** El Delta de tiempo entre la vuelta 21 y 20 se debe a un exceso de regeneración en el Sector 3.")

st.caption("F.E. Sistema de Telemetría | Diego Ríos | IRT - UPJR | 2025")