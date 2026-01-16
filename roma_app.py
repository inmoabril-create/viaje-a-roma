import streamlit as st
from datetime import datetime

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Roma 2026", page_icon="🇮🇹", layout="centered")

# --- ESTILOS CSS REFORZADOS ---
st.markdown("""
    <style>
    .stApp { background-color: #Fdfcf0; }
    
    /* Títulos de los días: Azul Suave / Marino */
    .highlight-day {
        background-color: #1E3A5F;
        color: white !important;
        padding: 15px;
        border-radius: 12px;
        text-align: center;
        margin-top: 25px;
        margin-bottom: 20px;
    }
    .highlight-day h1 { color: white !important; font-size: 24px !important; margin:0; }

    /* Texto general más oscuro y legible */
    .stMarkdown p, .stMarkdown li, div {
        color: #1a1a1a !important;
        font-size: 18px !important;
    }

    /* Botones Estilo Premium */
    div.stButton > button {
        width: 100%;
        background-color: white !important;
        border: 2px solid #1E3A5F !important;
        color: #1E3A5F !important;
        font-weight: bold;
        padding: 12px;
        border-radius: 10px;
    }
    
    /* Ventanas emergentes amplias */
    div[data-testid="stDialog"] div[role="dialog"] {
        background-color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- FUNCIÓN DE VENTANA ---
@st.dialog("🇮🇹 DETALLES")
def abrir_ventana(titulo, texto_markdown, img1=None, pie1=None):
    st.markdown(f"# {titulo}")
    if img1:
        st.image(img1, caption=pie1, use_container_width=True)
    st.markdown(texto_markdown)

# --- PORTADA ---
st.title("🇮🇹 Roma 2026")
st.write("### Paco & Mari Trini")

# ==========================================
# DOMINGO 1: Benvenuti
# ==========================================
st.markdown('<div class="highlight-day"><h1>📆 DOMINGO 1: Benvenuti</h1></div>', unsafe_allow_html=True)

# 1. TRASLADO
c1, c2 = st.columns([0.6, 0.4])
with c1: st.write("🕑 **14:00** | 🛬 Traslado Aeropuerto")
with c2:
    if st.button("🚌 Transporte", key="t_dom"):
        info_t = """
        **OPCIONES DE LLEGADA:**
        * **🚆 Tren Leonardo Express**: La opción más rápida. Sale cada 15 min y llega directo a Termini en 32 minutos. (14€).
        * **🚌 Autobús (Terravision / TAM)**: Más económico (aprox. 6-7€). Tarda unos 50-60 min dependiendo del tráfico.
        * **🚖 Taxi Oficial**: Tarifa fija de **50€** (todo incluido) hasta el hotel.
        
        💡 **Recomendación de Anrras**: Paco, para no complicaros el primer día, el **Tren Leonardo Express** es imbatible por puntualidad y comodidad.
        """
        abrir_ventana("Llegada a Roma", info_t)

# 2. ALMUERZO
c1, c2 = st.columns([0.6, 0.4])
with c1: st.write("🕑 **15:30** | 🍕 Almuerzo")
with c2:
    if st.button("🍴 Opciones", key="l_dom"):
        abrir_ventana("Dónde comer", "1. **La Gallina Bianca**: Muy cerca de Termini, excelente pasta y trato familiar.\n2. **Mercato Centrale**: Ideal para probar distintos bocados artesanales italianos en un ambiente moderno.")

# 3. SANTA MARIA MAGGIORE
c1, c2 = st.columns([0.6, 0.4])
with c1: st.write("🕑 **17:30** | ⛪ Sta. Maria Maggiore")
with c2:
    if st.button("📖 Ver Guía", key="sm_dom"):
        info_sm = """
        **UNA JOYA IMPRESCINDIBLE:**
        Esta es una de las cuatro basílicas mayores de Roma y la más importante dedicada a la Virgen.
        
        * **El Techo**: Se dice que fue dorado con el primer oro que llegó de América.
        * **Los Mosaicos**: Son del siglo V, de un valor incalculable.
        * **Reliquia**: Bajo el altar mayor se encuentra el "Sagrado Cuna", restos de madera que se dice pertenecen al pesebre de Jesús.
        * **Suelo Cosmatesco**: Fijaos en los dibujos del suelo, son de mármoles de colores del medievo.
        """
        abrir_ventana("Santa Maria Maggiore", info_sm, img1="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Basilica_di_Santa_Maria_Maggiore_-_Rome.jpg/800px-Basilica_di_Santa_Maria_Maggiore_-_Rome.jpg")

# 4. SAN PIETRO IN VINCOLI
c1, c2 = st.columns([0.6, 0.4])
with c1: st.write("🕑 **18:30** | ⛪ S. Pietro in Vincoli")
with c2:
    if st.button("📖 El Moisés", key="mo_dom"):
        info_mo = """
        **EL MOISÉS DE MIGUEL ÁNGEL:**
        En esta iglesia, aparentemente sencilla por fuera, se esconde una de las esculturas más famosas del mundo.
        
        * **La Mirada**: Miguel Ángel dotó al Moisés de una mirada tan real (la "terribilità") que parece que va a levantarse y hablar en cualquier momento.
        * **Los Cuernos**: Tiene dos pequeños cuernos en la cabeza por una mala traducción bíblica de la época (confundieron "rayos de luz" con "cuernos").
        * **Las Cadenas**: La iglesia también guarda las cadenas con las que San Pedro fue encarcelado en Jerusalén y Roma.
        """
        abrir_ventana("San Pietro in Vincoli", info_mo, img1="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Mois%C3%A9s_de_Miguel_%C3%81ngel_en_San_Pietro_in_Vincoli.jpg/800px-Mois%C3%A9s_de_Miguel_%C3%81ngel_en_San_Pietro_in_Vincoli.jpg")

# 5. CENA MONTI
c1, c2 = st.columns([0.6, 0.4])
with c1: st.write("🕑 **20:00** | 🍷 Cena (Barrio Monti)")
with c2:
    if st.button("🍷 Comidas", key="ce_dom"):
        info_ce = """
        🍴 **Ai Tre Scalini** (Aprox. 50€). 
        Es una vinería mítica del barrio de Monti. El ambiente es bohemio, con hiedra en la fachada y una luz muy acogedora.
        
        * **Especialidad**: Probad sus embutidos, sus quesos y, por supuesto, la lasaña o la berenjena a la parmesana.
        * **Ubicación**: Está en Via Panisperna, una de las calles más bonitas de Roma.
        
        🌐 [Ver sitio web](http://www.aitrescalini.org)
        """
        abrir_ventana("Cena en Monti", info_ce, img1="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Via_Panisperna_-_Rione_Monti.jpg/800px-Via_Panisperna_-_Rione_Monti.jpg", pie1="Calle Via Panisperna")

st.write("---")
st.caption("Guía Roma 2026 - Paco & Trini")
