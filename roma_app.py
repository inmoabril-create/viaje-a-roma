import streamlit as st
from datetime import datetime

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Roma 2026", page_icon="🇮🇹", layout="centered")

# --- ESTILOS CSS REFORZADOS ---
st.markdown("""
    <style>
    /* Fondo crema */
    .stApp { background-color: #Fdfcf0; }
    
    /* Títulos de los días: Verde Italiano con letra Blanca */
    .highlight-day {
        background-color: #008C45;
        color: white !important;
        padding: 12px;
        border-radius: 10px;
        text-align: center;
        margin-top: 25px;
        margin-bottom: 20px;
        border-bottom: 4px solid #ce1126; /* Detalle en rojo abajo */
    }
    .highlight-day h1 { color: white !important; font-size: 22px !important; margin:0; }

    /* Forzar texto negro en toda la app para lectura clara */
    .stMarkdown p, .stMarkdown li, div, label {
        color: #1a1a1a !important;
        font-size: 17px !important;
    }

    /* Botones más grandes y verdes */
    div.stButton > button {
        width: 100%;
        background-color: white !important;
        border: 2px solid #008C45 !important;
        color: #008C45 !important;
        font-weight: bold;
        padding: 10px;
        border-radius: 8px;
    }

    /* VENTANA MODAL A PANTALLA COMPLETA */
    div[data-testid="stDialog"] div[role="dialog"] {
        width: 100vw !important;
        height: 100dvh !important;
        max-width: 100vw !important;
        max-height: 100dvh !important;
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        margin: 0 !important;
        border-radius: 0 !important;
        background-color: white !important;
    }
    
    /* Enlaces Azules y Grandes */
    a {
        color: #0056b3 !important;
        text-decoration: underline !important;
        font-weight: bold !important;
        font-size: 18px !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- FUNCIÓN DE VENTANA ---
@st.dialog("🇮🇹 INFORMACIÓN")
def abrir_ventana(titulo, texto_markdown, img1=None, pie1=None):
    st.markdown(f"# {titulo}")
    if img1:
        st.image(img1, caption=pie1, use_container_width=True)
    st.markdown(texto_markdown, unsafe_allow_html=True)

# --- PORTADA ---
st.title("🇮🇹 Roma 2026")
st.markdown("### Paco & Mari Trini")

fecha_viaje = datetime(2026, 2, 1)
dias = (fecha_viaje - datetime.now()).days

if dias > 0:
    st.info(f"⏳ ¡Faltan **{dias}** días!")
else:
    st.success("🎉 ¡A disfrutar!")

# ==========================================
# DOMINGO 1
# ==========================================
st.markdown('<div class="highlight-day"><h1>📆 DOMINGO 1: Llegada</h1></div>', unsafe_allow_html=True)

c1, c2 = st.columns([0.6, 0.4])
with c1: st.write("🕑 **14:00** | 🛬 Traslado")
with c2:
    if st.button("🚌 Info", key="t_dom"):
        abrir_ventana("Transporte", "Taxi oficial (blanco): **50€ tarifa fija**. Tren Leonardo Express: **14€/pax**.")

c1, c2 = st.columns([0.6, 0.4])
with c1: st.write("🕑 **15:30** | 🍕 Almuerzo")
with c2:
    if st.button("🍴 Opciones", key="l_dom"):
        abrir_ventana("Comida", """
        1. **La Gallina Bianca**: Tradicional. 
        🌐 [Web Oficial](http://www.lagallinabiancaroma.it)
        2. **Mercato Centrale**: Muchos puestos en Termini. 
        🌐 [Web Oficial](https://www.mercatocentrale.it/roma/)
        """)

c1, c2 = st.columns([0.6, 0.4])
with c1: st.write("🕑 **17:30** | ⛪ Basílicas")
with c2:
    if st.button("📖 Ver", key="sm_dom"):
        abrir_ventana("Basílicas", "Santa Maria Maggiore (Mosaicos) y San Pietro in Vincoli (Moisés de Miguel Ángel).")

# ==========================================
# LUNES 2
# ==========================================
st.markdown('<div class="highlight-day"><h1>📆 LUNES 2: Vaticano</h1></div>', unsafe_allow_html=True)

c1, c2 = st.columns([0.6, 0.4])
with c1: st.write("🕑 **09:00** | 🏛️ Museos Vaticanos")
with c2:
    if st.button("🎟️ Reserva", key="guia_lun_1"):
        abrir_ventana("Vaticano", """
        **Entrada a las 09:00**. Código: `2L2NFFJ00000004GM`.
        No olvidar: Capilla Sixtina y Estancias de Rafael.
        🌐 [Web Museos](https://www.museivaticani.va)
        """)

c1, c2 = st.columns([0.6, 0.4])
with c1: st.write("🕑 **14:30** | 🍝 Almuerzo Prati")
with c2:
    if st.button("🍕 Sitios", key="com_lun_1"):
        abrir_ventana("Comida", "1. **Pastasciutta** (Rápido) [Web](https://www.pastasciuttaroma.it) \n2. **Isola della Pizza** [Web](https://www.lisoladellapizza.com)")

c1, c2 = st.columns([0.6, 0.4])
with c1: st.write("🕑 **20:30** | 🍷 Cena Trastevere")
with c2:
    if st.button("🍷 Ver", key="com_lun_2"):
        abrir_ventana("Cena", "1. **Tonnarello** [Web](https://tonnarello.it) \n2. **Da Enzo al 29** [Web](https://www.daenzoal29.com/)")

# ==========================================
# MARTES 3
# ==========================================
st.markdown('<div class="highlight-day"><h1>📆 MARTES 3: Barroco</h1></div>', unsafe_allow_html=True)

c1, c2 = st.columns([0.6, 0.4])
with c1: st.write("🕑 **10:00** | ⛲ Trevi / España")
with c2:
    if st.button("📖 Ruta", key="guia_mar_1"):
        abrir_ventana("Ruta Barroca", "Fontana di Trevi y Plaza de España. ¡No olvides tirar la moneda!")

c1, c2 = st.columns([0.6, 0.4])
with c1: st.write("🕑 **14:00** | 🍝 Almuerzo")
with c2:
    if st.button("🍝 Reserva", key="com_mar_1"):
        abrir_ventana("Cantina e Cucina", "Imprescindible sus albóndigas. \n🌐 [Web Oficial](https://cantinaecucina.it)")

c1, c2 = st.columns([0.6, 0.4])
with c1: st.write("🕑 **20:30** | 🍷 Cena Gala")
with c2:
    if st.button("🍷 Sitios", key="com_mar_2"):
        abrir_ventana("Cena", "1. **Cul de Sac** (Enoteca) [Web](https://www.enotecaculdesacroma.it/) \n2. **Mimi e Coco** [Web](https://mimiecoco.com)")

# ==========================================
# MIÉRCOLES 4
# ==========================================
st.markdown('<div class="highlight-day"><h1>📆 MIÉRCOLES 4: Borghese</h1></div>', unsafe_allow_html=True)

c1, c2 = st.columns([0.6, 0.4])
with c1: st.write("🕑 **12:00** | 🎨 Galería Borghese")
with c2:
    if st.button("🎨 Info", key="guia_mie_1"):
        abrir_ventana("Borghese", "Estar a las 11:30. 'Apolo y Dafne' es lo mejor. \n🌐 [Web Oficial](https://galleriaborghese.beniculturali.it/)")

c1, c2 = st.columns([0.6, 0.4])
with c1: st.write("🕑 **16:00** | 🏟️ Coliseo Noche")
with c2:
    if st.button("🏛️ Guía", key="guia_mie_2"):
        abrir_ventana("Roma Iluminada", "Vistas desde el Campidoglio al Foro Romano iluminado.")

c1, c2 = st.columns([0.6, 0.4])
with c1: st.write("🕑 **21:00** | 🍝 Cena Final")
with c2:
    if st.button("🍷 Ver", key="com_mie_2"):
        abrir_ventana("Última Cena", "1. **Vecchia Roma** (Amatriciana Flambé) [Web](https://www.trattoriavecchiaroma.it/) \n2. **Trattoria Monti** [Web](https://www.tripadvisor.es/Restaurant_Review-g187791-d793216-Reviews-Trattoria_Monti-Rome_Lazio.html)")

# ==========================================
# JUEVES
# ==========================================
st.markdown('<div class="highlight-day"><h1>📆 JUEVES: Regreso</h1></div>', unsafe_allow_html=True)
c1, c2 = st.columns([0.6, 0.4])
with c1: st.write("🕑 **03:45** | 🛫 Taxi Aeropuerto")
with c2:
    if st.button("🚕 Taxi", key="tr_jue"):
        abrir_ventana("Regreso", "Taxi oficial: 50€. Pedir en recepción el día anterior o por Free Now.")

st.markdown("---")
st.caption("Dossier Roma 2026 - Paco & Trini")
