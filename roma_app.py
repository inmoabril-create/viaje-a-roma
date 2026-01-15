import streamlit as st
from datetime import datetime

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Roma 2026", page_icon="🇮🇹", layout="centered")

# --- ESTILOS CSS CORREGIDOS PARA MÓVIL ---
st.markdown("""
    <style>
    /* Color de fondo de la app */
    .stApp { background-color: #Fdfcf0; }
    
    /* Forzar color de texto para que no desaparezca en modo oscuro */
    p, span, div, label {
        color: #1a1a1a !important;
    }
    
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
        color: white !important; /* El título siempre blanco */
        font-size: 22px !important;
        margin: 0;
    }

    /* Estilo de los botones para que no se amontonen */
    div.stButton > button {
        width: 100%;
        border-radius: 8px;
        border: 2px solid #008C45;
        color: #008C45 !important;
        background-color: white !important;
        font-weight: bold;
        margin-top: 5px;
    }
    
    /* Ajuste para que las columnas no se vean vacías en móvil */
    [data-testid="column"] {
        width: 100% !important;
        flex: 1 1 calc(50% - 10px) !important;
        min-width: 0px !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- FUNCIÓN DE VENTANA MODAL ---
@st.dialog("🇮🇹 DETALLES", width="large")
def abrir_ventana(titulo, texto_markdown):
    st.markdown(f"### {titulo}")
    st.markdown(texto_markdown)

# --- PORTADA Y CONTADOR ---
st.title("🇮🇹 Roma 2026")
st.markdown("### Paco & Mari Trini")

fecha_viaje = datetime(2026, 2, 1)
dias_restantes = (fecha_viaje - datetime.now()).days

if dias_restantes > 0:
    st.info(f"⏳ ¡Solo faltan **{dias_restantes}** días para vuestro gran viaje!")
elif dias_restantes == 0:
    st.success("🎉 ¡EL VIAJE EMPIEZA HOY! 🎉")
else:
    st.write("✈️ ¡A disfrutar de Roma!")

# ==========================================
# LUNES 2 (Cerrado)
# ==========================================
st.markdown('<div class="highlight-day"><h1>📆 LUNES 2: Vaticano</h1></div>', unsafe_allow_html=True)

# Para cada fila, usamos una estructura que aguante bien el móvil
def fila_itinerario(hora, texto, id_boton, titulo_modal, contenido_modal):
    col1, col2 = st.columns([0.65, 0.35])
    with col1:
        st.write(f"**{hora}** | {texto}")
    with col2:
        if st.button("Ver", key=id_boton):
            abrir_ventana(titulo_modal, contenido_modal)

fila_itinerario("07:15", "🚌 Traslado Vaticano", "tr1", "Traslado", "Metro A desde Termini a Ottaviano.")
fila_itinerario("08:00", "☕ Desayuno Prati", "des1", "Desayuno", "Sciascia Caffè 1919 o Latteria Giuliani.")
fila_itinerario("09:00", "🏛️ Museos Vaticanos", "vat1", "Vaticano", "Reserva: 2L2NFFJ00000004GM.")
fila_itinerario("14:30", "🏰 Almuerzo y Castillo", "cas1", "Tarde", "Castel Sant'Angelo y vistas del Tíber.")
fila_itinerario("20:30", "🍷 Cena Trastevere", "cen1", "Cena", "Tonnarello o Da Enzo al 29.")

# ==========================================
# MARTES 3: La Roma Barroca
# ==========================================
st.markdown('<div class="highlight-day"><h1>📆 MARTES 3: Roma Barroca</h1></div>', unsafe_allow_html=True)

fila_itinerario("08:30", "☕ Desayuno Hotel", "des2", "Desayuno", "Regoli (Maritozzo) o Panella.")
fila_itinerario("10:00", "⛲ Trevi y España", "bar1", "Ruta Barroca", "Fontana di Trevi y Plaza de España.")
fila_itinerario("14:00", "🍝 Almuerzo Cantina", "com2", "Almuerzo", "Cantina e Cucina (Navona).")
fila_itinerario("16:30", "🏛️ Panteón y Navona", "bar2", "Panteón", "Cúpula de Agripa y Fuente de los 4 Ríos.")
fila_itinerario("20:30", "🍷 Cena Especial", "cen2", "Despedida", "Trattoria Monti (Gourmet) o Cul de Sac.")

# ==========================================
# MIÉRCOLES 4: Borghese e Imperial
# ==========================================
st.markdown('<div class="highlight-day"><h1>📆 MIÉRCOLES 4: Borghese</h1></div>', unsafe_allow_html=True)

fila_itinerario("09:00", "☕ Desayuno Esquilino", "des3", "Desayuno", "Dagnino o Gatsby Café.")
fila_itinerario("10:45", "🚌 Traslado Borghese", "tr3", "Transporte", "Taxi o Bus 910.")
fila_itinerario("12:00", "🎨 Galería Borghese", "bor1", "Museo", "Bernini y Caravaggio.")
fila_itinerario("16:00", "🏟️ Roma Iluminada", "noct1", "Nocturna", "Foros y Coliseo bajo las luces.")
fila_itinerario("20:30", "🍷 Cena Final", "cen3", "Cena", "Vecchia Roma (Amatriciana Flambé).")

# ==========================================
# JUEVES: El Regreso
# ==========================================
st.markdown('<div class="highlight-day"><h1>📆 JUEVES: Regreso</h1></div>', unsafe_allow_html=True)

fila_itinerario("03:00", "⏰ Despertador", "desp", "Aviso", "¡Hora de volver!")
fila_itinerario("03:45", "🚕 Taxi Aeropuerto", "aero", "Transporte", "Taxi tarifa fija 50€. Tarda 35 min.")

st.markdown("---")
st.caption("Dossier Roma 2026 - Paco & Trini")
