import streamlit as st
from datetime import datetime

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Roma 2026", page_icon="🇮🇹", layout="centered")

# --- ESTILOS CSS REFORZADOS ---
st.markdown("""
    <style>
    .stApp { background-color: #Fdfcf0; }
    .stMarkdown p, .stMarkdown span, div, label { color: #1a1a1a !important; }
    .highlight-day {
        background-color: #CE1126;
        padding: 12px;
        border-radius: 10px;
        text-align: center;
        margin-top: 25px;
        margin-bottom: 20px;
    }
    .highlight-day h1 { color: white !important; font-size: 20px !important; margin: 0; font-weight: bold; }
    div.stButton > button {
        width: 100%;
        border-radius: 8px;
        border: 2px solid #008C45;
        color: #008C45 !important;
        background-color: white !important;
        font-weight: bold;
        padding: 8px;
    }
    div[role="dialog"] { background-color: white !important; }
    div[role="dialog"] h2, div[role="dialog"] h3, div[role="dialog"] p, div[role="dialog"] li, div[role="dialog"] a {
        color: #1a1a1a !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- FUNCIÓN DE VENTANA MODAL ---
@st.dialog("🇮🇹 INFORMACIÓN")
def abrir_ventana(titulo, contenido):
    st.markdown(f"### {titulo}")
    st.markdown(contenido)

# --- PORTADA Y CONTADOR ---
st.title("🇮🇹 Roma 2026")
st.markdown("### Paco & Mari Trini")

fecha_viaje = datetime(2026, 2, 1)
dias_restantes = (fecha_viaje - datetime.now()).days

if dias_restantes > 0:
    st.info(f"⏳ ¡Faltan **{dias_restantes}** días para el gran viaje!")
elif dias_restantes == 0:
    st.success("🎉 ¡EL VIAJE EMPIEZA HOY! 🎉")
else:
    st.write("✈️ ¡Disfrutad de Roma!")

# Función para organizar filas
def fila(hora, texto, id_btn, tit_modal, info_modal):
    col_t, col_b = st.columns([0.7, 0.3])
    with col_t:
        st.write(f"**{hora}** | {texto}")
    with col_b:
        if st.button("Ver", key=id_btn):
            abrir_ventana(tit_modal, info_modal)

# ==========================================
# DOMINGO 1: Llegada
# ==========================================
st.markdown('<div class="highlight-day"><h1>📆 DOMINGO 1: Llegada y Toma de Contacto</h1></div>', unsafe_allow_html=True)
fila("14:00", "🛫 Llegada y Traslado", "d1", "Traslado", "Llegada al Aeropuerto. Traslado al hotel en la zona de Esquilino/Termini.")
fila("16:00", "🏨 Check-in Hotel", "d2", "Alojamiento", "Dejar maletas y primer paseo por el barrio. Piazza Vittorio Emanuele II.")
fila("20:00", "🍷 Primera Cena", "d3", "Cena", "Cena tranquila cerca del hotel para descansar.")

# ==========================================
# LUNES 2: Vaticano
# ==========================================
st.markdown('<div class="highlight-day"><h1>📆 LUNES 2: El Vaticano</h1></div>', unsafe_allow_html=True)
fila("07:15", "🚌 Traslado Vaticano", "l1", "Transporte", "Metro A desde Termini a Ottaviano. Tap & Go (1,50€).")
fila("08:00", "☕ Desayuno Prati", "l2", "Desayuno", "1. Sciascia Caffè 1919. 2. Latteria Giuliani.")
fila("09:00", "🏛️ Museos Vaticanos", "l3", "Visita", "Reserva: 2L2NFFJ00000004GM. Capilla Sixtina.")
fila("14:30", "🏰 Castillo Sant'Angelo", "l4", "Tarde", "Almuerzo en Pastasciutta y paseo por el puente de los Ángeles.")
fila("20:30", "🍷 Cena Trastevere", "l5", "Cena", "Tonnarello o Da Enzo al 29.")

# ==========================================
# MARTES 3: Roma Barroca
# ==========================================
st.markdown('<div class="highlight-day"><h1>📆 MARTES 3: Roma Barroca</h1></div>', unsafe_allow_html=True)
fila("08:30", "☕ Desayuno Hotel", "m1", "Desayuno", "1. Regoli (Pasticceria histórica). 2. Panella.")
fila("10:00", "⛲ Trevi y España", "m2", "Guía", "Fontana di Trevi y Plaza de España. Tirad la moneda.")
fila("14:00", "🍝 Almuerzo Cantina", "m3", "Comida", "Cantina e Cucina (Navona). Muy recomendado.")
fila("16:30", "🏛️ Panteón y Navona", "m4", "Guía", "Panteón de Agripa y Fuente de los 4 Ríos de Bernini.")
fila("20:30", "🍷 Cena Despedida", "m5", "Cena de Gala", "1. Trattoria Monti (Gourmet). 2. Cul de Sac (Enoteca).")

# ==========================================
# MIÉRCOLES 4: Borghese e Imperial
# ==========================================
st.markdown('<div class="highlight-day"><h1>📆 MIÉRCOLES 4: Borghese</h1></div>', unsafe_allow_html=True)
fila("09:00", "☕ Desayuno Esquilino", "mi1", "Desayuno", "1. Dagnino (Siciliano). 2. Gatsby Café.")
fila("10:45", "🚌 Traslado Borghese", "mi2", "Transporte", "Taxi o Bus 910. Hay que estar allí a las 11:30 para la consigna.")
fila("12:00", "🎨 Galería Borghese", "mi3", "Museo", "Obras de Bernini y Caravaggio. Imprescindible.")
fila("16:00", "🏟️ Roma Iluminada", "mi5", "Nocturna", "Vista desde el Campidoglio y paseo por Foros Imperiales.")
fila("21:00", "🍷 Cena Final", "mi6", "Cena", "Trattoria Vecchia Roma (Pasta Flambé en queso).")

# ==========================================
# JUEVES 5: Regreso
# ==========================================
st.markdown('<div class="highlight-day"><h1>📆 JUEVES 5: El Regreso</h1></div>', unsafe_allow_html=True)
fila("03:00", "⏰ Despertador", "j1", "Aviso", "Ducha rápida y revisión de maletas.")
fila("03:45", "🚕 Taxi Aeropuerto", "j2", "Transporte", "Taxi tarifa fija 50€ a Fiumicino (FCO). 35 min.")

st.markdown("---")
st.caption("Dossier Interactivo Roma 2026 - Paco & Trini")
