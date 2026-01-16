import streamlit as st
from datetime import datetime

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Escapada a Roma 2026", page_icon="🇮🇹", layout="centered")

# --- ESTILOS CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #Fdfcf0; }
    
    /* Títulos de los días */
    .highlight-day {
        background: linear-gradient(135deg, #1E3A5F 0%, #12263a 100%);
        color: white !important;
        padding: 25px;
        border-radius: 20px;
        text-align: center;
        margin-top: 30px;
        margin-bottom: 25px;
    }
    .highlight-day h1 { color: white !important; font-size: 26px !important; margin:0; }

    /* Botones Modernos */
    div.stButton > button {
        width: 100%;
        background: #008C45 !important;
        color: white !important;
        border: none !important;
        padding: 15px !important;
        border-radius: 50px !important;
        font-weight: 700 !important;
        text-transform: uppercase;
    }
    
    /* Texto de las celdas */
    [data-testid="column"] {
        background: white;
        padding: 15px;
        border-radius: 15px;
        margin-bottom: 10px;
        border: 1px solid #eee;
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

# --- LÓGICA DE NAVEGACIÓN ---
if 'viaje_iniciado' not in st.session_state:
    st.session_state.viaje_iniciado = False

# --- PANTALLA DE BIENVENIDA ---
if not st.session_state.viaje_iniciado:
    st.markdown("""
        <div style="
            text-align: center;
            padding: 40px 20px;
            background-color: white;
            border: 6px double #1E3A5F;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            margin-top: 20px;
        ">
            <h1 style="color: #1E3A5F; font-size: 45px; font-weight: 900; margin-bottom: 10px;">ESCAPADA A ROMA</h1>
            <p style="color: #ce1126; font-size: 28px; font-weight: 700; margin-bottom: 5px;">Febrero de 2026</p>
            <p style="color: #1E3A5F; font-size: 26px; font-weight: 600; margin-bottom: 30px;">Paco & Mari Trini</p>
            <div style="font-style: italic; font-size: 19px; color: #444; line-height: 1.6; border-top: 1px solid #eee; padding-top: 20px;">
                "Hay viajes que se escriben en el mapa, y otros que se graban en el corazón. 
                Esta aventura es el reflejo de vuestro camino juntos, un regalo nacido del cariño más profundo de vuestros hijos."
                <br><br>
                <span style="font-weight: 800; color: #1E3A5F;">Un inolvidable regalo sorpresa de Cristina y Víctor.</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    if st.button("🇮🇹 INICIAR VIAJE"):
        st.session_state.viaje_iniciado = True
        st.rerun()

# --- CONTENIDO PRINCIPAL ---
else:
    # DOMINGO 1
    st.markdown('<div class="highlight-day"><h1>📆 DOMINGO 1: Benvenuti</h1></div>', unsafe_allow_html=True)

    c1, c2 = st.columns([0.6, 0.4])
    with c1: st.write("🕑 **14:00** | 🛬 Traslado Aeropuerto")
    with c2:
        if st.button("🚌 Transporte", key="t_dom"):
            abrir_ventana("Llegada", "Tren Leonardo Express (14€) o Taxi Oficial (50€).")

    c1, c2 = st.columns([0.6, 0.4])
    with c1: st.write("🕑 **15:30** | 🍕 Almuerzo")
    with c2:
        if st.button("🍴 Opciones", key="l_dom"):
            abrir_ventana("Almuerzo", "1. [La Gallina Bianca](http://www.lagallinabiancaroma.it)\n2. [Mercato Centrale](https://www.mercatocentrale.it/roma/)")

    c1, c2 = st.columns([0.6, 0.4])
    with c1: st.write("🕑 **17:30** | ⛪ Basílicas")
    with c2:
        if st.button("📖 Ver Guía", key="sm_dom"):
            abrir_ventana("Santa Maria Maggiore", "Mosaicos del siglo V y el famoso techo de oro.")
    
    # Aquí puedes seguir pegando el Lunes, Martes... respetando este mismo nivel de espacios.
