import streamlit as st
from datetime import datetime

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Roma 2026 - Paco & Trini", page_icon="🇮🇹", layout="centered")

# --- ESTILOS CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #Fdfcf0; }
    h1, h2, h3 { color: #CE1126; font-family: 'Helvetica', sans-serif; }
    .dia-header {
        background-color: #008C45;
        color: white;
        padding: 15px;
        border-radius: 10px;
        margin-top: 30px;
        margin-bottom: 20px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .evento {
        background: white;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        margin-bottom: 12px;
        border-left: 6px solid #CE1126;
    }
    .hora { font-weight: bold; color: #555; font-size: 1.1em; margin-right: 10px; }
    
    /* Estilo para botones bonitos */
    .stButton button {
        width: 100%;
        background-color: white;
        border: 2px solid #008C45;
        color: #008C45;
        border-radius: 10px;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    .stButton button:hover {
        background-color: #008C45;
        color: white;
        transform: scale(1.02);
    }
    </style>
""", unsafe_allow_html=True)

# --- FUNCIÓN PARA VENTANA FLOTANTE (MODAL) ---
@st.dialog("🇮🇹 Detalles del Sitio")
def mostrar_detalle(titulo, imagen, descripcion, precio=None):
    st.subheader(titulo)
    st.image(imagen, use_column_width=True)
    st.write(descripcion)
    if precio:
        st.success(f"💰 Precio estimado: {precio}")

# --- PORTADA ---
st.title("🇮🇹 Roma 2026")
st.subheader("Dossier de Viaje: Paco y Trini")

fecha_viaje = datetime(2026, 5, 22, 6, 40)
ahora = datetime.now()
dias_faltan = (fecha_viaje - ahora).days

if dias_faltan > 0:
    st.info(f"⏳ **CUENTA ATRÁS:** Faltan {dias_faltan} días para volar.")

# =========================================================
# DOMINGO 1: LLEGADA
# =========================================================
st.markdown("<div class='dia-header'><h3>DOMINGO 1: Benvenuti a Roma</h3></div>", unsafe_allow_html=True)

st.markdown("""<div class="evento"><span class="hora">14:00</span>🛬 <b>Llegada y Traslado</b></div>""", unsafe_allow_html=True)
with st.expander("🚌 Opciones Transporte"):
    st.write("**🚆 Leonardo Express:** 32 min. Directo a Termini.")

# --- SECCIÓN ALMUERZO CON BOTONES Y VENTANA FLOTANTE ---
st.markdown("""<div class="evento"><span class="hora">15:30</span>🍕 <b>Almuerzo: Elige opción</b></div>""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    if st.button("🏠 La Gallina Bianca"):
        mostrar_detalle(
            "La Gallina Bianca",
            "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=800&q=80",
            "Ambiente clásico y tranquilo, ideal para descansar del viaje. Manteles de tela y buen servicio.",
            "50€ (Pareja)"
        )

with col2:
    if st.button("🍕 Mercato Centrale"):
        mostrar_detalle(
            "Mercato Centrale",
            "https://images.unsplash.com/photo-1533900298318-6b8da08a523e?w=800&q=80",
            "Ambiente vibrante y moderno bajo la estación. Puestos variados y mesas compartidas.",
            "30€ (Pareja)"
        )

# --- VISITAS (SIGUEN IGUAL POR AHORA) ---
st.markdown("""<div class="evento"><span class="hora">17:30</span>⛪ <b>Basílica Sta. Maria Maggiore</b></div>""", unsafe_allow_html=True)
with st.expander("📸 Ver Guía"):
    st.write("El oro de América en el techo.")

st.markdown("""<div class="evento"><span class="hora">21:00</span>🍷 <b>Cena: Barrio Monti</b></div>""", unsafe_allow_html=True)

# =========================================================
# LUNES 2: VATICANO
# =========================================================
st.markdown("<div class='dia-header'><h3>LUNES 2: La Grandeza del Vaticano</h3></div>", unsafe_allow_html=True)
st.warning("⏰ Despertador: 07:00 AM")

st.markdown("""<div class="evento"><span class="hora">09:00</span>🏛️ <b>Museos Vaticanos</b></div>""", unsafe_allow_html=True)
with st.expander("📸 Ver Guía + Tickets"):
    st.write("Ticket: 2L2NFFJ00000004GM")

# (Resto del código resumido para no hacerlo eterno, si te gusta el efecto lo ponemos en todo)
