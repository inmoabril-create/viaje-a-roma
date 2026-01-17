import streamlit as st
from datetime import datetime

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Roma 2026", page_icon="🇮🇹", layout="centered")

# --- ESTILOS CSS ---
st.markdown("""
    <style>
    /* Fondo color crema suave */
    .stApp { background-color: #Fdfcf0; }
    
    /* Ventanas emergentes en blanco */
    div[role="dialog"] {
        background-color: #ffffff !important;
        color: #000000 !important;
    }
    div[role="dialog"] h2 { color: #1E3A5F !important; }
    div[role="dialog"] p, div[role="dialog"] li {
        color: #333333 !important;
        font-size: 18px !important;
    }
    div[role="dialog"] a { color: #0056b3 !important; font-weight: bold; }

    /* Tarjetas de Días */
    .highlight-day {
        background: linear-gradient(135deg, #1E3A5F 0%, #12263a 100%);
        color: white !important;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin-top: 35px;
        margin-bottom: 25px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    .highlight-day h1 { color: white !important; font-size: 26px !important; margin:0; }

    /* Horas y Textos */
    .activity-time {
        font-weight: bold;
        color: #1E3A5F;
        font-size: 20px;
    }

    /* Botones Estándar Mejorados */
    div.stButton > button {
        width: 100%;
        background-color: white !important;
        border: 2px solid #1E3A5F !important;
        color: #1E3A5F !important;
        font-weight: bold;
        padding: 10px;
        border-radius: 12px;
        font-size: 17px !important;
        transition: all 0.3s;
    }
    div.stButton > button:hover {
        background-color: #1E3A5F !important;
        color: white !important;
    }
    
    /* Botón de Inicio Grande */
    div.row-widget.stButton > button[kind="primary"] {
        background-color: #008C45 !important;
        color: white !important;
        border: none !important;
        font-size: 24px !important;
        padding: 15px !important;
        height: auto !important;
        border-radius: 50px !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- FUNCIÓN DE VENTANA ---
@st.dialog("🇮🇹 DETALLES")
def abrir_ventana(titulo, texto_markdown, img1=None, pie1=None):
    st.markdown(f"## {titulo}")
    if img1:
        st.image(img1, caption=pie1, use_container_width=True)
    st.markdown(texto_markdown)

# --- LÓGICA DE NAVEGACIÓN ---
if 'viaje_iniciado' not in st.session_state:
    st.session_state.viaje_iniciado = False


# ==========================================
# 1. PANTALLA DE BIENVENIDA
# ==========================================
if not st.session_state.viaje_iniciado:
    
    # --- REPRODUCTOR VISIBLE ARRIBA (INTENTO DE AUTOPLAY) ---
    # Beethoven 9ª - Minuto 11:00 (660 seg)
    st.markdown("""
        <div style="margin-bottom: 20px; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
            <iframe width="100%" height="200" src="https://www.youtube.com/embed/Q0F5135z3wY?start=660&autoplay=1" title="Beethoven" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        </div>
        <p style="text-align: center; color: #666; font-size: 14px; margin-top: -15px;">🎵 Si no suena automático, pulsa Play</p>
    """, unsafe_allow_html=True)

    # --- TEXTO DE DEDICATORIA ---
    st.markdown("""
        <div style="text-align: center; padding: 40px 20px; background-color: white; border: 8px double #1E3A5F; border-radius: 15px; box-shadow: 0 20px 40px rgba(0,0,0,0.1); margin-top: 20px; max-width: 650px; margin-left: auto; margin-right: auto;">
            <h1 style="color: #1E3A5F; font-family: 'Georgia', serif; font-size: 42px; font-weight: 700; margin-bottom: 15px;">Escapada a Roma</h1>
            <p style="color: #ce1126; font-size: 26px; font-weight: 700; margin-bottom: 5px;">Febrero de 2026</p>
            <p style="color: #1E3A5F; font-size: 24px; font-weight: 600; margin-bottom: 30px;">Paco & Mari Trini</p>
            <div style="font-style: italic; font-size: 19px; color: #333; line-height: 1.7; border-top: 1px solid #eee; padding-top: 25px; text-align: justify;">
                "Hay viajes que se escriben en el mapa, y otros que se graban en el corazón. 
                Esta aventura es un regalo que refleja el sinuoso y sorprendente camino que hemos recorrido juntos, 
                con el profundo deseo y la ilusión inquebrantable de que el resto del camino que nos queda que andar 
                supere abrumadoramente las expectativas que podamos tener. Un regalo lleno de historia, luz y sabor, 
                nacido del cariño más profundo de nuestros hijos."
                <br><br>
                <p style="text-align: center; font-weight: 800; color: #1E3A5F; font-size: 20px; margin-bottom: 0;">
                Un inolvidable regalo sorpresa de Cristina y Víctor.
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    st.write("")
    
    # Botón de Inicio
    col1, col2, col3 = st.columns([0.1, 0.8, 0.1])
    with col2:
        if st.button("🇮🇹 INICIAR VIAJE", key="main_start", type="primary"):
            st.session_state.viaje_iniciado = True
            st.rerun()

# ==========================================
# 2. ITINERARIO COMPLETO
# ==========================================
else:
    st.title("🇮🇹 Roma 2026")
    st.write("### Paco & Mari Trini")

    # ------------------------------------------
    # DOMINGO 1
    # ------------------------------------------
    st.markdown('<div class="highlight-day"><h1>📆 DOMINGO 1: Benvenuti</h1></div>', unsafe_allow_html=True)
    
    # 1. Traslado
    c1, c2 = st.columns([0.55, 0.45])
    with c1: st.markdown('<div class="activity-time">14:00 | 🛬 Traslado</div>', unsafe_allow_html=True)
    with c2:
        if st.button("🚌 Logística Hotel", key="t_dom"):
            info_t = """
            **OPCIONES DESDE EL AEROPUERTO:**
            
            1. **🚆 Tren Leonardo Express**:
               - Precio: **14€**/pax.
               - Tiempo: 32 min directos a Termini.
               - *Recomendado para evitar tráfico.*
            
            2. **🚖 Taxi Oficial (Blanco)**:
               - Precio: **50€** (Tarifa fija cerrada).
               - Tiempo: 40-50 min.
            
            3. **🚌 Bus (Terravision/TAM)**:
               - Precio: ~7€. Más lento (1h).
            """
            abrir_ventana("Llegada al Hotel", info_t)

    # 2. Almuerzo
    c1, c2 = st.columns([0.55, 0.45])
    with c1: st.markdown('<div class="activity-time">15:30 | 🍕 Almuerzo</div>', unsafe_allow_html=True)
    with c2:
        if st.button("🍴 Ver Opciones", key="l_dom"):
            info_l = """
            **OPCIONES DE ALMUERZO:**
            
            1. **La Gallina Bianca**:
               - Cocina tradicional romana y pizzas.
               - 🌐 [Web Oficial](http://www.lagallinabiancaroma.
