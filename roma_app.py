import streamlit as st
from datetime import datetime

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Roma 2026", page_icon="🇮🇹", layout="centered")

# --- ESTILOS CSS REFORZADOS ---
st.markdown("""
    <style>
    .stApp { background-color: #Fdfcf0; }
    
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

    .stMarkdown p, .stMarkdown li, div {
        color: #1a1a1a !important;
        font-size: 18px !important;
    }

    a {
        color: #0056b3 !important;
        text-decoration: underline !important;
        font-weight: bold !important;
    }

    div.stButton > button {
        width: 100%;
        background-color: white !important;
        border: 2px solid #1E3A5F !important;
        color: #1E3A5F !important;
        font-weight: bold;
        padding: 12px;
        border-radius: 10px;
    }
    
    /* Estilo del Botón Iniciar Viaje (Verde) */
    .stButton>button[kind="primary"] {
        background-color: #008C45 !important;
        color: white !important;
        border: none !important;
        border-radius: 50px !important;
        padding: 15px !important;
        font-size: 20px !important;
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

# --- LÓGICA DE SESIÓN PARA LA PORTADA ---
if 'viaje_iniciado' not in st.session_state:
    st.session_state.viaje_iniciado = False

# --- PANTALLA DE BIENVENIDA ---
if not st.session_state.viaje_iniciado:
    st.markdown(f"""
        <div style="text-align: center; padding: 45px 30px; background-color: white; border: 8px double #1E3A5F; border-radius: 15px; box-shadow: 0 20px 40px rgba(0,0,0,0.1); margin-top: 30px; max-width: 650px; margin-left: auto; margin-right: auto;">
            <h1 style="color: #1E3A5F; font-family: 'Georgia', serif; font-size: 50px; font-weight: 700; margin-bottom: 20px;">Escapada a Roma</h1>
            <p style="color: #ce1126; font-size: 28px; font-weight: 700; margin-bottom: 5px;">Febrero de 2026</p>
            <p style="color: #1E3A5F; font-size: 26px; font-weight: 600; margin-bottom: 35px;">Paco & Mari Trini</p>
            <div style="font-style: italic; font-size: 19px; color: #333; line-height: 1.7; border-top: 1px solid #eee; padding-top: 30px; text-align: justify;">
                "Hay viajes que se escriben en el mapa, y otros que se graban en el corazón. 
                Esta aventura es un regalo que refleja el sinuoso y sorprendente camino que hemos recorrido juntos, 
                con el profundo deseo y la ilusión inquebrantable de que el resto del camino que nos queda que andar 
                supere abrumadoramente las expectativas que podamos tener. Un regalo lleno de historia, luz y sabor, 
                nacido del cariño más profundo de nuestros hijos."
                <br><br>
                <p style="text-align: center; font-weight: 800; color: #1E3A5F; font-size: 22px;">
                Un inolvidable regalo sorpresa de Cristina y Víctor.
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("") 
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🇮🇹 INICIAR VIAJE", type="primary"):
            st.session_state.viaje_iniciado = True
            st.rerun()

# --- CONTENIDO DEL VIAJE (TODA TU COPIA ESTÁ AQUÍ) ---
else:
    st.title("🇮🇹 Roma 2026")
    st.write("### Paco & Mari Trini")

    # DOMINGO
    st.markdown('<div class="highlight-day"><h1>📆 DOMINGO 1: Benvenuti</h1></div>', unsafe_allow_html=True)
    c1, c2 = st.columns([0.6, 0.4])
    with c1: st.write("🕑 **14:00** | 🛬 Traslado Aeropuerto")
    with c2:
        if st.button("🚌 Transporte", key="t_dom"):
            info_t = "**OPCIONES DE LLEGADA:**\n* **🚆 Tren Leonardo Express**: 14€.\n* **🚌 Autobús**: 6-7€.\n* **🚖 Taxi**: 50€."
            abrir_ventana("Llegada a Roma", info_t)

    c1, c2 = st.columns([0.6, 0.4])
    with c1: st.write("🕑 **20:00** | 🍷 Cena (Barrio Monti)")
    with c2:
        if st.button("🍷 Comidas", key="ce_dom"):
            info_ce = "🍴 **Ai Tre Scalini**. Vinería mítica de Monti.\n🌐 [Web Oficial](http://www.aitrescalini.org)"
            abrir_ventana("Cena en Monti", info_ce, img1="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Via_Panisperna_-_Rione_Monti.jpg/800px-Via_Panisperna_-_Rione_Monti.jpg")

    # LUNES
    st.markdown('<div class="highlight-day"><h1>📆 LUNES 2: El Corazón de Roma</h1></div>', unsafe_allow_html=True)
    c1, c2 = st.columns([0.6, 0.4])
    with c1: st.write("🕑 **09:00** | 🏛️ Museos Vaticanos")
    with c2:
        if st.button("📖 Ver Guía", key="guia_lun_1"):
            info_vat = "**MUSEOS VATICANOS:**\nReserva: `2L2NFFJ00000004GM`.\nNo os perdáis la Capilla Sixtina."
            abrir_ventana("Vaticano", info_vat, img1="https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Sistine_Chapel_Ceiling_01.jpg/800px-Sistine_Chapel_Ceiling_01.jpg")

    c1, c2 = st.columns([0.6, 0.4])
    with c1: st.write("🕑 **20:30** | 🍷 Cena en Trastevere")
    with c2:
        if st.button("🍷 Comidas", key="com_lun_2"):
            info_tras = "1. **Tonnarello**\n2. **Da Enzo al 29**"
            abrir_ventana("Cena Lunes", info_tras)

    # MARTES
    st.markdown('<div class="highlight-day"><h1>📆 MARTES 3: La Roma Barroca</h1></div>', unsafe_allow_html=True)
    c1, c2 = st.columns([0.6, 0.4])
    with c1: st.write("🕑 **10:00** | ⛲ Trevi / España")
    with c2:
        if st.button("📖 Ver Guía", key="guia_mar_1"):
            abrir_ventana("Trevi y España", "Fontana di Trevi y Plaza de España.", img1="https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Fontana_di_Trevi_Front.jpg/800px-Fontana_di_Trevi_Front.jpg")

    # MIÉRCOLES
    st.markdown('<div class="highlight-day"><h1>📆 MIÉRCOLES 4: Borghese</h1></div>', unsafe_allow_html=True)
    c1, c2 = st.columns([0.6, 0.4])
    with c1: st.write("🕑 **12:00** | 🎨 Galería Borghese")
    with c2:
        if st.button("🎨 Ver Guía", key="guia_mie_1"):
            abrir_ventana("Borghese", "Obras de Bernini y Caravaggio.", img1="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Apolo_y_Dafne_%28Bernini%29.jpg/800px-Apolo_y_Dafne_%28Bernini%29.jpg")

    # JUEVES
    st.markdown('<div class="highlight-day"><h1>📆 JUEVES 5: Regreso</h1></div>', unsafe_allow_html=True)
    c1, c2 = st.columns([0.6, 0.4])
    with c1: st.write("🕑 **03:45** | 🛫 Traslado Aeropuerto")
    with c2:
        if st.button("🚕 Transporte", key="tr_jue_fin"):
            abrir_ventana("Regreso", "Taxi oficial 50€. Salida vuelo 06:40.")

    # BOTÓN PARA VOLVER A LA PORTADA
    st.write("---")
    if st.button("🔙 VOLVER A PORTADA"):
        st.session_state.viaje_iniciado = False
        st.rerun()

    st.caption("Guía Roma 2026 - Paco & Trini")
