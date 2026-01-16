import streamlit as st
from datetime import datetime

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Roma 2026", page_icon="🇮🇹", layout="centered")

# --- ESTILOS CSS (PANTALLA TOTAL Y TEXTO VISIBLE) ---
st.markdown("""
    <style>
    /* Fondo color crema suave */
    .stApp { background-color: #Fdfcf0; }
    
    /* TEXTO NEGRO INTENSO SIEMPRE (Para arreglar lo del Xiaomi) */
    .stMarkdown p, .stMarkdown span, div, label, h1, h2, h3, li { 
        color: #000000 !important; 
    }
    
    /* ESTILO DE LOS DÍAS (Rojo) */
    .highlight-day {
        background-color: #CE1126;
        padding: 10px;
        border-radius: 8px;
        text-align: center;
        margin-top: 20px;
        margin-bottom: 10px;
    }
    .highlight-day h1 { 
        color: white !important; 
        font-size: 20px !important; 
        margin: 0; 
    }
    
    /* BOTONES VERDES */
    div.stButton > button {
        width: 100%;
        background-color: white !important;
        border: 2px solid #008C45 !important;
        color: #008C45 !important;
        font-weight: bold;
        padding: 10px;
        border-radius: 8px;
    }

    /* --- VENTANA A PANTALLA COMPLETA (FULL SCREEN) --- */
    div[data-testid="stDialog"] div[role="dialog"] {
        width: 100vw !important;
        height: 100vh !important;
        max-width: 100vw !important;
        max-height: 100vh !important;
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        margin: 0 !important;
        border-radius: 0 !important;
        background-color: white !important;
        z-index: 99999 !important;
    }

    /* Enlaces grandes y azules */
    a {
        color: #0066cc !important;
        text-decoration: underline !important;
        font-size: 18px !important;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# --- FUNCIÓN DE VENTANA ---
@st.dialog("🇮🇹 INFORMACIÓN DETALLADA")
def abrir_ventana(titulo, contenido):
    st.subheader(titulo)
    st.markdown(contenido, unsafe_allow_html=True)

# --- PORTADA ---
st.title("🇮🇹 Roma 2026")
st.markdown("### Paco & Mari Trini")

# Fecha: 1 de Febrero
fecha_viaje = datetime(2026, 2, 1)
dias = (fecha_viaje - datetime.now()).days

if dias > 0:
    st.info(f"⏳ ¡Faltan **{dias}** días para el viaje!")
elif dias == 0:
    st.success("🎉 ¡HOY ES EL DÍA! 🎉")
else:
    st.write("✈️ ¡A disfrutar!")

# Función para filas
def fila(hora, titulo_corto, id_btn, tit_modal, info_modal):
    st.write(f"**{hora}** | {titulo_corto}")
    if st.button("👁️ Ver detalles", key=id_btn):
        abrir_ventana(tit_modal, info_modal)
    st.markdown("---")

# ==========================================
# DOMINGO 1: LLEGADA (COMPLETO)
# ==========================================
st.markdown('<div class="highlight-day"><h1>📆 DOMINGO 1: Llegada</h1></div>', unsafe_allow_html=True)

fila("14:00", "🛫 Llegada y Traslado", "d1", "LOGÍSTICA LLEGADA", """
**TRASLADO AEROPUERTO -> HOTEL (Esquilino):**

1.  **TAXI (Opción Recomendada):**
    * **Precio:** Tarifa fija de **50 €** (Taxi oficial blanco).
    * **Tiempo:** Unos 35-40 minutos.
    * **Dirección:** Decidle al conductor vuestra calle en Esquilino.

2.  **TREN LEONARDO EXPRESS:**
    * **Precio:** 14 € por persona.
    * **Destino:** Estación Termini (luego andando al hotel).
""")

fila("15:30", "🍕 Almuerzo Tardío", "d2", "COMIDA CERCA DE TERMINI", """
**LA GALLINA BIANCA**
Perfecto para la primera toma de contacto. Cerca del hotel.
* **Qué pedir:** Pizzas romanas finas o pasta carbonara.
* 🌐 [Web Oficial](https://
