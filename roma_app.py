import streamlit as st
from datetime import datetime

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Roma 2026", page_icon="🇮🇹", layout="centered")

# --- ESTILOS CSS REFORZADOS PARA XIAOMI ---
st.markdown("""
    <style>
    .stApp { background-color: #Fdfcf0; }
    /* Forzar texto visible */
    .stMarkdown p, .stMarkdown span, div, label { color: #1a1a1a !important; }
    
    /* Títulos de los días */
    .highlight-day {
        background-color: #CE1126;
        padding: 12px;
        border-radius: 10px;
        text-align: center;
        margin-top: 25px;
        margin-bottom: 20px;
    }
    .highlight-day h1 { color: white !important; font-size: 20px !important; margin: 0; font-weight: bold; }
    
    /* Botones Ver (Ajustados para que no desaparezcan) */
    div.stButton > button {
        width: 100%;
        border-radius: 8px;
        border: 2px solid #008C45;
        color: #008C45 !important;
        background-color: white !important;
        font-weight: bold;
        margin-bottom: 10px;
    }
    
    /* Ventanas blancas */
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

# Función robusta para filas (Evita que el botón desaparezca en móvil)
def fila(hora, texto, id_btn, tit_modal, info_modal):
    st.write(f"**{hora}** | {texto}")
    if st.button("Ver detalles", key=id_btn):
        abrir_ventana(tit_modal, info_modal)
    st.write("---")

# ==========================================
# DOMINGO 1: Llegada (RECUPERADO COMPLETO)
# ==========================================
st.markdown('<div class="highlight-day"><h1>📆 DOMINGO 1: Llegada</h1></div>', unsafe_allow_html=True)

fila("14:00", "🛫 Traslado Aeropuerto -> Hotel", "d1", "Transporte", 
     "Traslado al hotel en la zona de Esquilino/Termini. \n* **Taxi**: Tarifa fija 50€.\n* **Tren**: Leonardo Express (14€) hasta Termini.")

fila("15:30", "🍕 Almuerzo (La Gallina Bianca)", "d2", "Comida", 
     "**La Gallina Bianca**: Excelente cocina romana cerca de Termini. [Web](https://www.lagallinabianca.com/)")

fila("17:30", "⛪ Sta. Maria Maggiore", "d3", "Guía", 
     "Una de las 4 basílicas papales. Impresionantes mosaicos del siglo V. Entrada gratuita.")

fila("18:30", "⛪ San Pietro in Vincoli", "d4", "Guía", 
     "Hogar del majestuoso **Moisés de Miguel Ángel**. Entrada gratuita.")

fila("21:00", "🍷 Cena (Barrio Monti)", "d5", "Cena", 
     "Zona bohemia con mucho encanto. Recomendado: *La Carbonara* o *Ai Tre Scalini*.")

# ==========================================
# LUNES 2: Vaticano
# ==========================================
st.markdown('<div class="highlight-day"><h1>📆 LUNES 2: El Vaticano</h1></div>', unsafe_allow_html=True)
fila("09:00", "🏛️ Museos Vaticanos", "l1", "Visita", "Reserva: 2L2NFFJ00000004GM. Capilla Sixtina y Estancias de Rafael.")
fila("20:30", "🍷 Cena Trastevere", "l2", "Cena", "Tonnarello o Da Enzo al 29.")

# ==========================================
# MARTES 3: Roma Barroca
# ==========================================
st.markdown('<div class="highlight-day"><h1>📆 MARTES 3: Roma Barroca</h1></div>', unsafe_allow_html=True)
fila("10:00", "⛲ Trevi y España", "m1", "Guía", "Fontana di Trevi y Plaza de España.")
fila("20:30", "🍷 Gran Cena Despedida", "m2", "Cena Gala", "Trattoria Monti (Gourmet) o Cul de Sac.")

# ==========================================
# MIÉRCOLES 4: Borghese
# ==========================================
st.markdown('<div class="highlight-day"><h1>📆 MIÉRCOLES 4: Borghese</h1></div>', unsafe_allow_html=True)
fila("12:00", "🎨 Galería Borghese", "mi1", "Museo", "Bernini y Caravaggio. (Estar a las 11:30).")
fila("16:00", "🏟️ Roma Iluminada", "mi2", "Nocturna", "Paseo por el Campidoglio y los Foros de noche.")

# ==========================================
# JUEVES: Regreso
# ==========================================
st.markdown('<div class="highlight-day"><h1>📆 JUEVES: El Regreso</h1></div>', unsafe_allow_html=True)
fila("03:45", "🚕 Taxi Aeropuerto", "j1", "Transporte", "Taxi tarifa fija 50€. 35 min de trayecto.")

st.markdown("---")
st.caption("Dossier Interactivo Roma 2026 - Paco & Trini")
