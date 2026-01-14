import streamlit as st
from datetime import datetime

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Roma 2026", page_icon="🇮🇹", layout="centered")

# --- ESTILOS CSS (DISEÑO PREMIUM) ---
st.markdown("""
    <style>
    /* Fondo crema suave */
    .stApp { background-color: #Fdfcf0; }
    
    /* Botones grandes y elegantes */
    div.stButton > button {
        width: 100%;
        padding: 16px;
        border-radius: 12px;
        border: 2px solid #008C45;
        color: #008C45;
        font-weight: bold;
        font-size: 17px;
        background-color: white;
        transition: all 0.2s;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    div.stButton > button:hover {
        background-color: #008C45;
        color: white;
        transform: scale(1.01);
    }
    
    /* Títulos y textos */
    h1, h2, h3 { color: #CE1126; font-family: sans-serif; text-align: center; }
    p, li { font-size: 16px; line-height: 1.6; color: #333; }
    
    /* Separadores */
    hr { border-top: 1px solid #ddd; margin: 20px 0; }
    </style>
""", unsafe_allow_html=True)

# --- FUNCIÓN VENTANA (MODAL) ---
@st.dialog("🇮🇹 GUÍA DE VIAJE", width="large")
def abrir_ventana(titulo, contenido_markdown, imagen_1=None, pie_1=None, imagen_2=None, pie_2=None):
    st.subheader(titulo)
    
    # Caso A: Una sola imagen
    if imagen_1 and not imagen_2:
        st.image(imagen_1, caption=pie_1, use_column_width=True)
    
    # Caso B: Dos imágenes (Comparativa)
    if imagen_1 and imagen_2:
        colA, colB = st.columns(2)
        with colA:
            st.image(imagen_1, caption=pie_1, use_column_width=True)
        with colB:
            st.image(imagen_2, caption=pie_2, use_column_width=True)

    # Texto limpio
    st.markdown(contenido_markdown)

# --- PORTADA ---
st.title("🇮🇹 Roma 2026")
st.markdown("<h3 style='margin-top:0;'>Paco & Trini</h3>", unsafe_allow_html=True)

# Cuenta atrás
fecha_viaje = datetime(2026, 5, 22, 6, 40)
dias_faltan = (fecha_viaje - datetime.now()).days
if dias_faltan > 0:
    st.info(f"⏳ **Faltan {dias_faltan} días** para el viaje.")

# =========================================================
# DOMINGO 1: LLEGADA
# =========================================================
st.markdown("### 📆 DOMINGO 1: Benvenuti")

# --- 14:00 TRANSPORTE ---
col1, col2 = st.columns([0.6, 0.4])
with col1:
    st.write("🕑 **14:00 | Llegada**")
    st.caption("Fiumicino")
with col2:
    if st.button("🚌 Transporte", key="btn_transporte"):
        texto = """
        **🚆 OPCIÓN A: Leonardo Express (RECOMENDADO)**
        * **Precio:** 14€ (28€ total).
        * **Tiempo:** 32 min (Directo a Termini).
        
        ---
        **🚌 OPCIÓN B: Autobús**
        * **Precio:** 7€ pax (14€ total).
        * **Tiempo:** 60 min (Depende del tráfico).
        
        ---
        **🚖 OPCIÓN C: Taxi Oficial**
        * **Precio:** 50€ (Tarifa fija).
        """
        abrir_ventana("🚌 Cómo llegar al Hotel", texto)

# --- 15:30 ALMUERZO ---
col1, col2 = st.columns([0.6, 0.4])
with col1:
    st.write("🕑 **15:30 | Almuerzo**")
    st.caption("Dos opciones")
with col2:
    if st.button("🍽️ Ver Opciones", key="btn_comida"):
        texto = """
