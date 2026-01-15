import streamlit as st
from datetime import datetime

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Roma 2026", page_icon="🇮🇹", layout="centered")

# --- ESTILOS CSS PARA QUE SE VEA PERFECTO EN MÓVIL ---
st.markdown("""
    <style>
    /* Fondo general color crema */
    .stApp { background-color: #Fdfcf0; }
    
    /* FORZAR COLOR DE TEXTO (Para que no desaparezca en móviles Xiaomi) */
    .stMarkdown p, .stMarkdown span, div, label {
        color: #1a1a1a !important;
    }
    
    /* Títulos de los días (Fondo Rojo, Letra Blanca) */
    .highlight-day {
        background-color: #CE1126;
        padding: 12px;
        border-radius: 10px;
        text-align: center;
        margin-top: 25px;
        margin-bottom: 20px;
    }
    .highlight-day h1 {
        color: white !important;
        font-size: 20px !important;
        margin: 0;
        font-weight: bold;
    }

    /* Botones Ver (Verdes y grandes para pulsar fácil) */
    div.stButton > button {
        width: 100%;
        border-radius: 8px;
        border: 2px solid #008C45;
        color: #008C45 !important;
        background-color: white !important;
        font-weight: bold;
        padding: 8px;
    }

    /* VENTANAS EMERGENTES (Siempre blancas con texto negro) */
    div[role="dialog"] {
        background-color: white !important;
    }
    div[role="dialog"] h2, div[role="dialog"] h3, div[role="dialog"] p, div[role="dialog"] li, div[role="dialog"] a {
        color: #1a1a1a !important;
        text-decoration: none;
    }
    </style>
""", unsafe_allow_html=True)

# --- FUNCIÓN DE VENTANA MODAL ---
@st.dialog("🇮🇹 INFORMACIÓN DETALLADA")
def abrir_ventana(titulo, contenido):
    st.markdown(f"### {titulo}")
    st.markdown(contenido)

# --- PORTADA Y CONTADOR ---
st.title("🇮🇹 Roma 2026")
st.markdown("### Paco & Mari Trini")

# Fecha de inicio: 1 de febrero
fecha_viaje = datetime(2026, 2, 1)
dias_restantes = (fecha_viaje - datetime.now()).days

if dias_restantes > 0:
    st.info(f"⏳ ¡Solo faltan **{dias_restantes}** días para vuestro gran viaje!")
elif dias_restantes == 0:
    st.success("🎉 ¡EL VIAJE EMPIEZA HOY! 🎉")
else:
    st.write("✈️ ¡Disfrutad de vuestra estancia en Roma!")

# Función para organizar las filas del itinerario
def fila(hora, texto, id_btn, tit_modal, info_modal):
    col_t, col_b = st.columns([0.7, 0.3])
    with col_t:
        st.write(f"**{hora}** | {texto}")
    with col_b:
        if st.button("Ver", key=id_btn):
            abrir_ventana(tit_modal, info_modal)

# ==========================================
# LUNES 2 (Vaticano)
# ==========================================
st.markdown('<div class="highlight-day"><h1>📆 LUNES 2: El Vaticano</h1></div>', unsafe_allow_html=True)

fila("07:15", "🚌 Traslado Vaticano", "l1", "Transporte al Vaticano", 
     "Tomar el **Metro A** en Termini dirección 'Battistini' y bajar en **Ottaviano**.\n\n"
     "* **Precio**: 1,50€ (usad Tap & Go).\n"
     "* **Tiempo**: 15 min aprox.")

fila("08:00", "☕ Desayuno en Prati", "l2", "Desayuno zona Vaticano", 
     "1. **Sciascia Caffè 1919**: Un clásico para el mejor café. [Web Oficial](https://www.sciasciacaffe1919.it)\n"
     "2. **Latteria Giuliani**: Famoso por sus dulces tradicionales.")

fila("09:00", "🏛️ Museos Vaticanos", "l3", "Visita Museos", 
     "**Reserva**: 2L2NFFJ00000004GM.\n\n"
     "Imprescindible: Estancias de Rafael, Galería de los Mapas y la **Capilla Sixtina**.")

fila("14:30", "🏰 Castillo Sant'Angelo", "l4", "Tarde", 
     "1. **Almuerzo**: [Pastasciutta](https://www.pastasciuttaroma.it) (Pasta fresca rápida).\n"
     "2. **Visita**: Paseo por el puente de los ángeles y vistas desde el Castillo.")

fila("20:30", "🍷 Cena en Trastevere", "l5", "Cena Trastevere", 
     "1. **Tonnarello**: Famoso por sus huevos con pasta. [Web](https://tonnarello.it)\n"
     "2. **Da Enzo al 29**: Auténtica cocina romana. [Web](https://www.daenzoal29.it/)")

# ==========================================
# MARTES 3 (Barroco)
# ==========================================
st.markdown('<div class="highlight-day"><h1>📆 MARTES 3: La Roma Barroca</h1></div>', unsafe_allow_html=True)

fila("08:30", "☕ Desayuno Hotel", "m1", "Desayuno Esquilino", 
     "1. **Regoli Pasticceria**: Tenéis que probar el **Maritozzo** (bollo con nata). [TripAdvisor](https://www.tripadvisor.es/Restaurant_Review-g187791-d1102555-Reviews-Pasticceria_Regoli-Rome_Lazio.html)\n\n"
     "2. **Panella**: Panadería artesana increíble. [Web Oficial](https://www.panellaroma.com/)")

fila("10:00", "⛲ Trevi y España", "m2", "Guía Barroca", 
     "**Fontana di Trevi**: Tirad la moneda de espaldas. Neptuno domando las aguas.\n\n"
     "**Plaza de España**: La fuente de la Barcaccia y la gran escalinata. Recorred la Via Condotti.")

fila("14:00", "🍝 Almuerzo Cantina", "m3", "Almuerzo Centro", 
     "**Cantina e Cucina**: Muy recomendado por su ambiente y lasaña. [Web](https://cantinaecucina.it)")

fila("16:30", "🏛️ Panteón y Navona", "m4", "Guía Detallada", 
     "**El Panteón**: El edificio mejor conservado de la antigua Roma. Mirad hacia el óculo de la cúpula.\n\n"
     "**Plaza Navona**: Disfrutad de la Fuente de los Cuatro Ríos de Bernini.")

fila("20:30", "🍷 Cena Despedida", "m5", "Cena de Gala (~100€)", 
     "Esta es vuestra gran cena de despedida:\n\n"
     "1. **Trattoria Monti**: Gourmet, íntima y cerca del hotel. [TripAdvisor](https://www.tripadvisor.es/Restaurant_Review-g187791-d1061245-Reviews-Trattoria_Monti-Rome_Lazio.html)\n\n"
     "2. **Cul de Sac**: Enoteca histórica con vinos espectaculares. [Web](https://www.enotecaculdesacroma.it/)")

# ==========================================
# MIÉRCOLES 4 (Borghese / Imperial)
# ==========================================
st.markdown('<div class="highlight-day"><h1>📆 MIÉRCOLES 4: Borghese e Imperial</h1></div>', unsafe_allow_html=True)

fila("09:00", "☕ Desayuno Esquilino", "mi1", "Desayuno", 
     "1. **Dagnino**: El mejor rincón siciliano de Roma. [Web](https://www.pasticceriadagnino.com/)\n"
     "2. **Gatsby Café**: Un local con mucha clase en vuestro barrio. [TripAdvisor](https://www.tripadvisor.es/Restaurant_Review-g187791-d11913959-Reviews-Gatsby_Cafe-Rome_Lazio.html)")

fila("10:45", "🚌 Traslado Borghese", "mi2", "Transport
