import streamlit as st
from datetime import datetime

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Escapada a Roma 2026", page_icon="🇮🇹", layout="centered")

# --- ESTILOS CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #Fdfcf0; }
    
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

# --- 1. PANTALLA DE BIENVENIDA ---
if not st.session_state.viaje_iniciado:
    st.markdown(f"""
        <div style="text-align: center; padding: 50px 30px; background-color: white; border: 8px double #1E3A5F; border-radius: 15px; box-shadow: 0 20px 40px rgba(0,0,0,0.1); margin-top: 30px; max-width: 650px; margin-left: auto; margin-right: auto;">
            <h1 style="color: #1E3A5F; font-family: 'Georgia', serif; font-size: 50px; font-weight: 700; margin-bottom: 20px;">Escapada a Roma</h1>
            <p style="color: #ce1126; font-size: 28px; font-weight: 700; margin-bottom: 5px;">Febrero de 2026</p>
            <p style="color: #1E3A5F; font-size: 26px; font-weight: 600; margin-bottom: 35px;">Paco & Mari Trini</p>
            <div style="font-style: italic; font-size: 21px; color: #333; line-height: 1.7; border-top: 1px solid #eee; padding-top: 30px;">
                "Hay viajes que se escriben en el mapa, y otros que se graban en el corazón. 
                Esta aventura es el reflejo de <b>nuestro</b> camino juntos, un regalo lleno de 
                historia, luz y sabor, nacido del cariño más profundo de <b>nuestros</b> hijos."
                <br><br>
                <span style="font-weight: 800; color: #1E3A5F;">Un inolvidable regalo sorpresa de Cristina y Víctor.</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("") 
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🇮🇹 INICIAR VIAJE"):
            st.session_state.viaje_iniciado = True
            st.rerun()

# --- 2. CONTENIDO DEL VIAJE (AQUÍ ESTÁ TODO DENTRO DEL ELSE) ---
else:
    # --- DOMINGO ---
    st.markdown('<div class="highlight-day"><h1>📆 DOMINGO 1: Benvenuti</h1></div>', unsafe_allow_html=True)
    c1, c2 = st.columns([0.6, 0.4])
    with c1: st.write("🕑 **14:00** | 🛬 Traslado")
    with c2:
        if st.button("🚌 Transporte", key="t_dom"):
            abrir_ventana("Traslado", "Tren Leonardo Express (14€) o Taxi Oficial (50€).")
    
    c1, c2 = st.columns([0.6, 0.4])
    with c1: st.write("🕑 **17:30** | ⛪ Basílicas")
    with c2:
        if st.button("📖 Ver Guía", key="sm_dom"):
            abrir_ventana("Basílicas", "Santa Maria Maggiore y San Pietro in Vincoli.")

    # --- LUNES ---
    st.markdown('<div class="highlight-day"><h1>📆 LUNES 2: Vaticano</h1></div>', unsafe_allow_html=True)
    c1, c2 = st.columns([0.6, 0.4])
    with c1: st.write("🕑 **09:00** | 🏛️ Museos Vaticanos")
    with c2:
        if st.button("📖 Ver Guía", key="guia_lun"):
            abrir_ventana("Vaticano", "Reserva: 2L2NFFJ00000004GM. Capilla Sixtina.")

    # --- MARTES ---
    st.markdown('<div class="highlight-day"><h1>📆 MARTES 3: Roma Barroca</h1></div>', unsafe_allow_html=True)
    c1, c2 = st.columns([0.6, 0.4])
    with c1: st.write("🕑 **10:00** | ⛲ Trevi / España")
    with c2:
        if st.button("📖 Ver Guía", key="guia_mar"):
            abrir_ventana("Ruta Barroca", "Fontana di Trevi, Plaza España y Panteón.")

    # --- MIÉRCOLES ---
    st.markdown('<div class="highlight-day"><h1>📆 MIÉRCOLES 4: Borghese</h1></div>', unsafe_allow_html=True)
    c1, c2 = st.columns([0.6, 0.4])
    with c1: st.write("🕑 **12:00** | 🎨 Galería Borghese")
    with c2:
        if st.button("🎨 Ver Guía", key="guia_mie"):
            abrir_ventana("Borghese", "Estar 30 min antes. Bernini y Caravaggio.")

    # --- JUEVES ---
    st.markdown('<div class="highlight-day"><h1>📆 JUEVES 5: Regreso</h1></div>', unsafe_allow_html=True)
    c1, c2 = st.columns([0.6, 0.4])
    with c1: st.write("🕑 **03:00** | ⏰ Despertador")
    with c2:
        if st.button("🛫 Vuelo", key="fin"):
            abrir_ventana("Regreso", "Vuelo a las 06:40. Taxi reservado 03:45.")

    st.markdown("---")
    if st.button("🔙 VOLVER A PORTADA"):
        st.session_state.viaje_iniciado = False
        st.rerun()
