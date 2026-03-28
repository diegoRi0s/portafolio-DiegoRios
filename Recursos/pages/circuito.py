import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import os
from PIL import Image


st.set_page_config(page_title="AHR Interactive Map", layout="wide")


st.markdown("""
    <style>
    /* Fondo principal blanco */
    .main, html, body, [data-testid="stAppViewContainer"] { 
        background-color: #FFFFFF !important; 
    }
    
    /* FORZAR TEXTO NEGRO EN TODO EL DOCUMENTO */
    h1, h2, h3, h4, h5, h6, p, label, .stMarkdown, [data-testid="stText"], .stMetric label { 
        color: #000000 !important; 
    }

    /* Diseño de la Tarjeta (Card) */
    .telemetry-card {
        background-color: #FBFBFB;
        border: 1px solid #E0E0E0;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 4px 4px 15px rgba(0,0,0,0.05);
        height: 100%;
        color: #000000 !important;
    }

    /* Ajuste de métricas para que no hereden gris */
    [data-testid="stMetricValue"] { 
        color: #007BFF !important; 
        font-weight: bold;
    }
    
    /* Forzar color negro en el selectbox */
    .stSelectbox div[data-baseweb="select"] > div {
        color: black !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("ANÁLISIS INTERACTIVO: AUTÓDROMO HNOS. RODRÍGUEZ")
st.subheader("Configuración Formula E | Mapeo de Telemetría")
st.divider()

# --- CARGA DEL MAPA ---
directorio_actual = os.path.dirname(os.path.abspath(__file__))
ruta_imagen = os.path.join(directorio_actual, "circuito_ahr.png")

if os.path.exists(ruta_imagen):
    img = Image.open(ruta_imagen)
    st.image(img, caption="Trazado Local - Autódromo Hermanos Rodríguez", use_container_width=True)
else:
    st.error("Imagen 'circuito_ahr.png' no encontrada en la carpeta 'pages'.")

st.divider()

puntos_control = {
    "Recta Principal": {"V": "79 km/h", "THR": "100%", "BRK": "0%", "Regen": "0 kW", "Tip": "Máxima potencia en recta."},
    "Curva 1 (Moises S.)": {"V": "32 km/h", "THR": "5%", "BRK": "95%", "Regen": "350 kW", "Tip": "Frenado fuerte y regeneración."},
    "S de Alta Velocidad": {"V": "65 km/h", "THR": "85%", "BRK": "15%", "Regen": "45 kW", "Tip": "Mantener inercia constante."},
    "Entrada Foro Sol": {"V": "28 km/h", "THR": "0%", "BRK": "100%", "Regen": "350 kW", "Tip": "Zona técnica de baja velocidad."},
    "Curva Peraltada": {"V": "74 km/h", "THR": "95%", "BRK": "0%", "Regen": "10 kW", "Tip": "Aceleración hacia meta."}
}

st.write("### Panel de Telemetría por Sector")
seleccion = st.selectbox("Selecciona un sector para ver los detalles:", list(puntos_control.keys()))
datos = puntos_control[seleccion]


col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="telemetry-card">
        <h4 style="margin-top:0;">Rendimiento</h4>
        <p style="margin-bottom:0;">Velocidad: <b>{datos['V']}</b></p>
        <p>Regeneración: <b>{datos['Regen']}</b></p>
        <hr>
        <p style="font-size:0.9em;"><i>{datos['Tip']}</i></p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="telemetry-card">
        <h4 style="margin-top:0;"> Pedales (Inputs)</h4>
        <p style="color:green; font-weight:bold; margin-bottom:5px;"> Acelerador (THR): {datos['THR']}</p>
        <p style="color:red; font-weight:bold;"> Freno (BRK): {datos['BRK']}</p>
        <p style="color:black; font-size:0.85em; margin-top:15px;">Datos capturados a 3ms a 80km/h max.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    # Esta tarjeta contiene la gráfica de Plotly
    st.markdown('<div class="telemetry-card"><h4 style="margin-top:0;"> Gráfica de Inputs</h4>', unsafe_allow_html=True)
    
    fig = go.Figure(go.Bar(
        x=['THR', 'BRK'],
        y=[int(datos['THR'].replace('%','')), int(datos['BRK'].replace('%',''))],
        marker_color=['#28A745', '#DC3545'],
        text=[datos['THR'], datos['BRK']],
        textposition='auto',
    ))
    fig.update_layout(
        height=180, 
        template="plotly_white", 
        yaxis_range=[0,105], 
        margin=dict(l=0, r=0, t=10, b=0),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color="black")
    )
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.divider()
st.caption("F.E. Autodromo Hermanos Rodriguez. | Diego Ríos | Lobos UPJR Racing | 2025")