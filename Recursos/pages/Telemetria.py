import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# 1. Configuración de página
st.set_page_config(page_title="Formula E Live Telemetry", layout="wide")

# 2. 🎨 ESTILO CLEAN (SIN RECUADROS, SIN SOMBRAS)
st.markdown("""
    <style>
    /* Fondo blanco estándar de Streamlit */
    .main, html, body, [data-testid="stAppViewContainer"] { 
        background-color: #FFFFFF !important; 
    }
    
    /* Texto negro y gris oscuro para legibilidad */
    h1, h2, h3, h4, p, label, .stMarkdown, [data-testid="stText"] { 
        color: #31333F !important; 
        font-family: "Source Sans Pro", sans-serif;
    }

    /* Ajuste de métricas para que se vean como en tu captura */
    div[data-testid="stMetricValue"] { 
        color: #1F77B4 !important; 
        font-weight: 700;
        font-size: 2.5rem !important;
    }
    
    /* Quitar cualquier contenedor residual */
    div[data-testid="stVerticalBlock"] > div {
        background-color: transparent !important;
        border: none !important;
        box-shadow: none !important;
    }

    hr { border-top: 1px solid #e6eaf1 !important; }
    </style>
    """, unsafe_allow_html=True)

# Encabezado con el rayo naranja como en tu imagen
st.title("⚡ FORMULA E LIVE TELEMETRY | GEN3")
st.markdown("### **Driver:** Diego Rios | **Team:** Lobos UPJR Racing 🏎️")
st.divider()

# --- DATOS ---
speed = 78 
battery_soc = 42.5

# --- FILA 1: VELOCÍMETRO Y MÉTRICAS ---
col_gauge, col_m1, col_m2, col_m3 = st.columns([1.5, 1, 1, 1])

with col_gauge:
    fig_gauge = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = speed,
        domain = {'x': [0, 1], 'y': [0, 1]},
        gauge = {
            'axis': {'range': [None, 80], 'tickwidth': 1, 'tickcolor': "#31333F"},
            'bar': {'color': "#1F77B4"},
            'bgcolor': "white",
            'borderwidth': 1,
            'bordercolor': "#e6eaf1",
            'steps': [
                {'range': [0, 60], 'color': '#f0f2f6'},
                {'range': [60, 80], 'color': '#ff4b4b'}]
        }
    ))
    fig_gauge.update_layout(
        height=280, 
        margin=dict(l=30, r=30, t=50, b=20),
        paper_bgcolor='rgba(0,0,0,0)',
        font={'color': "#31333F", 'family': "Source Sans Pro"}
    )
    st.plotly_chart(fig_gauge, use_container_width=True)

with col_m1:
    st.metric("EST. LAP TIME (AHR)", "3:44.205")
    st.success("↑ Slow Track Mode")
    st.info("📍 **Location:** Autódromo Hermanos Rodríguez, MX")

with col_m2:
    st.metric("BATTERY (SOC)", f"{battery_soc}%", "-0.8% / LAP", delta_color="inverse")
    st.write("**DRIVE MODE**")
    st.success("ECO-REGEN ACTIVE")

# --- FILA 2: GRÁFICA DE PEDALES ---
st.divider()
st.subheader("Telemetría de Pedales (Acelerador vs Freno)")

t = np.linspace(0, 20, 100)
throttle = 50 + 40 * np.sin(t/2) + np.random.normal(0, 2, 100)
brake = (100 - throttle + np.random.normal(0, 5, 100)) * (throttle < 40)

fig_pedals = go.Figure()
fig_pedals.add_trace(go.Scatter(x=t, y=throttle, name='THROTTLE (Acc)', fill='tozeroy', line=dict(color='#00FF00', width=2.5)))
fig_pedals.add_trace(go.Scatter(x=t, y=brake, name='BRAKE', fill='tozeroy', line=dict(color='#FF0000', width=2.5)))

fig_pedals.update_layout(
    template="plotly_white",
    height=400,
    xaxis_title="Tiempo (Segundos)",
    yaxis_title="Porcentaje (%)",
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)
st.plotly_chart(fig_pedals, use_container_width=True)

# --- FILA 3: TABLA DE SECTORES ---
st.divider()
st.subheader("Análisis Detallado por Sector")
sectores = pd.DataFrame({
    "Sector": ["Recta Principal", "Curva 1 (Moises S.)", "S de alta velocidad", "Entrada al Foro Sol", "Curva Peraltada"],
    "Speed (km/h)": [79, 32, 55, 28, 74],
    "Acelerador %": [100, 5, 75, 0, 95],
    "Freno %": [0, 95, 10, 100, 0],
    "Regeneración": ["0 kW", "350 kW", "45 kW", "350 kW", "10 kW"]
})

# Estilo de tabla para resaltar colores como en tu imagen
def color_pedal_val(val):
    if val == 100 or val == 95: return 'color: #FF0000; font-weight: bold'
    if val == 5 or val == 0: return 'color: #00FF00;'
    return ''

st.table(sectores.style.set_properties(**{'text-align': 'left'}))

# --- FILA 4: TABLA DE TIEMPOS ---
st.divider()
st.subheader("🏁 Tiempos: Últimas 5 Vueltas")
laps_data = {
    "Lap": [24, 23, 22, 21, 20],
    "Lap Time": ["3:44.205", "3:44.118", "3:44.590", "3:43.902", "3:45.002"],
    "Status": ["VALID", "VALID", "VALID", "PERSONAL BEST", "VALID"]
}
st.table(pd.DataFrame(laps_data))

st.info("💡 **Análisis de Telemetría:** El Delta de tiempo entre la vuelta 21 y 20 se debe a un exceso de regeneración en el Sector 3.")

st.caption("F.E. Sistema de Telemetría | Diego Ríos | IRT - UPJR | 2025")