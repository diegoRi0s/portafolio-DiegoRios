import streamlit as st
import pandas as pd

# Configuración de página "Race Engineering Mode"
st.set_page_config(page_title="AHR Interactive Telemetry", layout="wide")

# --- ESTILO "PIT WALL" ---
# Forzamos una estética limpia para que resalte el mapa
st.markdown("""
    <style>
    .main { background-color: #F8F9FA; color: #1e1e1e; }
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 { color: #007BFF; font-family: 'Segoe UI', sans-serif; }
    div[data-testid="stExpander"] { border: 2px solid #007BFF; border-radius: 10px; background-color: white; }
    .data-label { font-weight: bold; color: #555; }
    .data-value { font-size: 1.2em; font-weight: bold; color: #007BFF; }
    .thr-val { color: #28A745; font-weight: bold; } /* Verde Acelerador */
    .brk-val { color: #DC3545; font-weight: bold; } /* Rojo Freno */
    </style>
    """, unsafe_allow_html=True)

st.title("🗺️ TELEMETRÍA INTERACTIVA SOBRE CIRCUITO")
st.subheader("Autódromo Hermanos Rodríguez | CDMX | Configuration: FE Gen3")
st.divider()

# --- DATOS DE TELEMETRÍA POR PUNTO CLAVE (Simulados a 80km/h max) ---
ahr_data = {
    "P1: Recta Principal": {"Speed": "79 km/h", "THR": "100%", "BRK": "0%", "Regen": "0 kW", "Time_Est": "0:45.2"},
    "P2: Curva 1 (Moises S.)": {"Speed": "32 km/h", "THR": "5%", "BRK": "95%", "Regen": "350 kW", "Time_Est": "1:15.8"},
    "P3: Zona de 'S'es": {"Speed": "65 km/h", "THR": "85%", "BRK": "15%", "Regen": "45 kW", "Time_Est": "2:10.1"},
    "P4: Entrada Foro Sol": {"Speed": "28 km/h", "THR": "0%", "BRK": "100%", "Regen": "350 kW", "Time_Est": "2:55.5"},
    "P5: Salida Peraltada": {"Speed": "74 km/h", "THR": "95%", "BRK": "0%", "Regen": "10 kW", "Time_Est": "3:20.9"}
}

# --- LAYOUT PRINCIPAL ---
col_map, col_info = st.columns([2, 1])

with col_map:
    st.subheader("📍 Mapa del Circuito y Puntos de Telemetría")
    
    # Imagen del Circuito (Usamos una URL pública limpia del AHR)
    # Nota: Si tienes una imagen local más limpia, úsala con st.image("imagen_local.png")
    st.image("https://raw.githubusercontent.com/u-beta-test/ahr-circuit/main/ahr_fe_map_clean.png", 
             caption="Autódromo Hermanos Rodríguez - Trazado FE", use_container_width=True)
    
    st.info("💡 **Instrucción:** Usa los paneles de la derecha para ver la telemetría detallada en cada uno de los puntos marcados en el mapa.")

with col_info:
    st.subheader("📊 Telemetría en Punto de Control")
    st.write("Selecciona un punto del circuito para ver los datos:")
    
    # Usamos st.expander para simular "pop-ups" interactivos sobre el mapa
    
    # --- PUNTO 1 ---
    with st.expander("🚩 P1: Recta Principal (Alta Velocidad)"):
        data = ahr_data["P1: Recta Principal"]
        c1, c2 = st.columns(2)
        c1.markdown(f"<span class='data-label'>SPEED:</span> <span class='data-value'>{data['Speed']}</span>", unsafe_allow_html=True)
        c1.markdown(f"<span class='data-label'>TIME EST:</span> <span class='data-value'>{data['Time_Est']}</span>", unsafe_allow_html=True)
        c2.markdown(f"<span class='data-label'>THR:</span> <span class='thr-val'>{data['THR']}</span>", unsafe_allow_html=True)
        c2.markdown(f"<span class='data-label'>BRK:</span> <span class='brk-val'>{data['BRK']}</span>", unsafe_allow_html=True)
        st.caption(f"⚡ Regen: {data['Regen']}")

    # --- PUNTO 2 ---
    with st.expander("🚩 P2: Curva 1 (Frenado Fuerte)"):
        data = ahr_data["P2: Curva 1 (Moises S.)"]
        c1, c2 = st.columns(2)
        c1.markdown(f"<span class='data-label'>SPEED:</span> <span class='data-value'>{data['Speed']}</span>", unsafe_allow_html=True)
        c1.markdown(f"<span class='data-label'>TIME EST:</span> <span class='data-value'>{data['Time_Est']}</span>", unsafe_allow_html=True)
        c2.markdown(f"<span class='data-label'>THR:</span> <span class='thr-val'>{data['THR']}</span>", unsafe_allow_html=True)
        c2.markdown(f"<span class='data-label'>BRK:</span> <span class='brk-val'>{data['BRK']}</span>", unsafe_allow_html=True)
        st.caption(f"⚡ Regen: {data['Regen']} (Max)")

    # --- PUNTO 3 ---
    with st.expander("🚩 P3: Zona de 'S'es (Ritmo)"):
        data = ahr_data["P3: Zona de 'S'es"]
        c1, c2 = st.columns(2)
        c1.markdown(f"<span class='data-label'>SPEED:</span> <span class='data-value'>{data['Speed']}</span>", unsafe_allow_html=True)
        c1.markdown(f"<span class='data-label'>TIME EST:</span> <span class='data-value'>{data['Time_Est']}</span>", unsafe_allow_html=True)
        c2.markdown(f"<span class='data-label'>THR:</span> <span class='thr-val'>{data['THR']}</span>", unsafe_allow_html=True)
        c2.markdown(f"<span class='data-label'>BRK:</span> <span class='brk-val'>{data['BRK']}</span>", unsafe_allow_html=True)
        st.caption(f"⚡ Regen: {data['Regen']}")

    # --- PUNTO 4 ---
    with st.expander("🚩 P4: Entrada Foro Sol (Lento)"):
        data = ahr_data["P4: Entrada Foro Sol"]
        c1, c2 = st.columns(2)
        c1.markdown(f"<span class='data-label'>SPEED:</span> <span class='data-value'>{data['Speed']}</span>", unsafe_allow_html=True)
        c1.markdown(f"<span class='data-label'>TIME EST:</span> <span class='data-value'>{data['Time_Est']}</span>", unsafe_allow_html=True)
        c2.markdown(f"<span class='data-label'>THR:</span> <span class='thr-val'>{data['THR']}</span>", unsafe_allow_html=True)
        c2.markdown(f"<span class='data-label'>BRK:</span> <span class='brk-val'>{data['BRK']}</span>", unsafe_allow_html=True)
        st.caption(f"⚡ Regen: {data['Regen']} (Max)")

st.divider()
st.caption("F.E. Telemetry Map | Diego Ríos | Lobos UPJR Racing | 2025")