import streamlit as st
from datetime import datetime

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Roma 2026", page_icon="🇮🇹", layout="centered")

# --- ESTILOS CSS REFORZADOS ---
st.markdown("""
    <style>
    /* Fondo general de la página */
    .stApp { background-color: #Fdfcf0; }
    
    /* Títulos de los días (Rojo) */
    .highlight-day {
        background-color: #CE1126;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        margin-top: 20px;
        margin-bottom: 20px;
    }
    .highlight-day h1 {
        color: white !important;
        font-size: 22px !important;
        margin: 0;
    }

    /* Botones verdes estilo italiano */
    div.stButton > button {
        width: 100%;
        border-radius: 8px;
        border: 2px solid #008C45;
        color: #008C45 !important;
        background-color: white !important;
        font-weight: bold;
    }

    /* FORZAR VENTANAS BLANCAS CON TEXTO NEGRO */
    div[data-testid="stDialog"] div[role="dialog"] {
        background-color: white !important;
    }
    
    div[data-testid="stDialog"] p, 
    div[data-testid="stDialog"] h1, 
    div[data-testid="stDialog"] h2, 
    div[data-testid="stDialog"] h3,
    div[data-testid="stDialog"] li,
    div[data-testid="stDialog"] span {
        color: #1a1a1a !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- FUNCIÓN DE VENTANA MODAL ---
@st.dialog("🇮🇹 DETALLES")
def abrir_ventana(titulo, texto_markdown):
    # Forzamos que el contenido de la ventana sea legible
    st.markdown(f"## {titulo}")
    st.markdown(texto_markdown)

# --- PORTADA Y CONTADOR ---
st.title("🇮🇹 Roma 2026")
st.markdown("### Paco & Mari Trini")

# Fecha corregida: 1 de febrero
fecha_viaje = datetime(2026, 2, 1)
dias_restantes = (fecha_viaje - datetime.now()).days

if dias_restantes > 0:
    st.info(f"⏳ ¡Solo faltan **{dias_restantes}** días para vuestro gran viaje!")
elif dias_restantes == 0:
    st.success("🎉 ¡EL VIAJE EMPIEZA HOY! 🎉")
else:
    st.write("✈️ ¡A disfrutar de Roma!")

# Función para filas del itinerario que se vean bien en móvil
def fila(hora, texto, id_btn, titulo, contenido):
    col1, col2 = st.columns([0.7, 0.3])
    with col1:
        st.write(f"**{hora}** | {texto}")
    with col2:
        if st.button("Ver", key=id_btn):
            abrir_ventana(titulo, contenido)

# ==========================================
# LUNES 2
# ==========================================
st.markdown('<div class="highlight-day"><h1>📆 LUNES 2: Vaticano</h1></div>', unsafe_allow_html=True)
fila("07:15", "🚌 Traslado Vaticano", "l1", "Traslado", "Metro A desde Termini a Ottaviano.")
fila("08:00", "☕ Desayuno Prati", "l2", "Desayuno", "Sciascia Caffè o Latteria Giuliani.")
fila("09:00", "🏛️ Museos Vaticanos", "l3", "Vaticano", "Reserva: 2L2NFFJ00000004GM.")
fila("14:30", "🏰 Castillo Sant'Angelo", "l4", "Castillo", "Vistas espectaculares del Tíber.")
fila("20:30", "🍷 Cena Trastevere", "l5", "Cena", "Tonnarello o Da Enzo al 29.")

# ==========================================
# MARTES 3
# ==========================================
st.markdown('<div class="highlight-day"><h1>📆 MARTES 3: Roma Barroca</h1></div>', unsafe_allow_html=True)
fila("08:30", "☕ Desayuno Hotel", "m1", "Desayuno", "Regoli (Maritozzo) o Panella.")
fila("10:00", "⛲ Trevi y España", "m2", "Guía", "Fontana di Trevi y Plaza de España.")
fila("14:00", "🍝 Almuerzo Cantina", "m3", "Comida", "Cantina e Cucina.")
fila("16:30", "🏛️ Panteón y Navona", "m4", "Guía", "Cúpula del Panteón y Plaza Navona.")
fila("20:30", "🍷 Cena Despedida", "m5", "Cena", "Trattoria Monti o Cul de Sac.")

# ==========================================
# MIÉRCOLES 4
# ==========================================
st.markdown('<div class="highlight-day"><h1>📆 MIÉRCOLES 4: Borghese</h1></div>', unsafe_allow_html=True)
fila("09:00", "☕ Desayuno Esquilino", "mi1", "Desayuno", "Dagnino o Gatsby Café.")
fila("10:45", "🚌 Traslado Borghese", "mi2", "Traslado", "Taxi o Bus 910.")
fila("12:00", "🎨 Galería Borghese", "mi3", "Museo", "Bernini y Caravaggio.")
fila("16:00", "🏟️ Roma Iluminada", "mi4", "Guía", "Foros y Coliseo de noche.")
fila("21:00", "🍷 Cena Final", "mi5", "Cena", "Vecchia Roma.")

# ==========================================
# JUEVES
# ==========================================
st.markdown('<div class="highlight-day"><h1>📆 JUEVES: Regreso</h1></div>', unsafe_allow_html=True)
fila("03:00", "⏰ Despertador", "j1", "Aviso", "¡Ducha y maletas!")
fila("03:45", "🚕 Taxi Aeropuerto", "j2", "Transporte", "Taxi tarifa fija 50€ a Fiumicino.")

st.markdown("---")
st.caption("Dossier Roma 2026 - Paco & Trini")
