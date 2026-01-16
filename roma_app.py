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
    .stMarkdown p, .stMarkdown li, div { color: #1a1a1a !important; font-size: 18px !important; }
    a { color: #0056b3 !important; text-decoration: underline !important; font-weight: bold !important; }
    div.stButton > button {
        width: 100%;
        background-color: white !important;
        border: 2px solid #1E3A5F !important;
        color: #1E3A5F !important;
        font-weight: bold;
        padding: 12px;
        border-radius: 10px;
    }
    .btn-inicio button {
        background-color: #008C45 !important;
        color: white !important;
        border: none !important;
        height: 60px !important;
        font-size: 22px !important;
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

# --- 1. PANTALLA DE BIENVENIDA ---
if not st.session_state.viaje_iniciado:
    st.markdown(f"""
        <div style="text-align: center; padding: 40px 25px; background-color: white; border: 8px double #1E3A5F; border-radius: 15px; box-shadow: 0 20px 40px rgba(0,0,0,0.1); margin-top: 20px; max-width: 650px; margin-left: auto; margin-right: auto;">
            <h1 style="color: #1E3A5F; font-family: 'Georgia', serif; font-size: 45px; font-weight: 700; margin-bottom: 15px;">Escapada a Roma</h1>
            <p style="color: #ce1126; font-size: 28px; font-weight: 700; margin-bottom: 5px;">Febrero de 2026</p>
            <p style="color: #1E3A5F; font-size: 26px; font-weight: 600; margin-bottom: 30px;">Paco & Mari Trini</p>
            <div style="font-style: italic; font-size: 19px; color: #333; line-height: 1.7; border-top: 1px solid #eee; padding-top: 25px; text-align: justify;">
                "Hay viajes que se escriben en el mapa, y otros que se graban en el corazón. 
                Esta aventura es un regalo que refleja el sinuoso y sorprendente camino que hemos recorrido juntos, 
                con el profundo deseo y la ilusión inquebrantable de que el resto del camino que nos queda que andar 
                supere abrumadoramente las expectativas que podamos tener. Un regalo lleno de historia, luz y sabor, 
                nacido del cariño más profundo de nuestros hijos."
                <br><br>
                <p style="text-align: center; font-weight: 800; color: #1E3A5F; font-size: 21px; margin-bottom: 0;">
                Un inolvidable regalo sorpresa de Cristina y Víctor.
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.write("") 
    _, col_btn, _ = st.columns([0.5, 1, 0.5])
    with col_btn:
        st.markdown('<div class="btn-inicio">', unsafe_allow_html=True)
        if st.button("🇮🇹 INICIAR VIAJE", key="main_start"):
            st.session_state.viaje_iniciado = True
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# --- 2. CONTENIDO DEL VIAJE ---
else:
    # --- DOMINGO ---
    st.markdown('<div class="highlight-day"><h1>📆 DOMINGO 1: Benvenuti</h1></div>', unsafe_allow_html=True)
    c1, c2 = st.columns([0.6, 0.4]); with c2:
        if st.button("🚌 Transporte", key="t_dom"):
            abrir_ventana("Llegada", "Tren Leonardo Express (14€) o Taxi Oficial (50€).")
    with c1: st.write("🕑 **14:00** | 🛬 Traslado Aeropuerto")
    
    c1, c2 = st.columns([0.6, 0.4]); with c2:
        if st.button("🍴 Almuerzo", key="l_dom"):
            abrir_ventana("Comida", "La Gallina Bianca o Mercato Centrale.", img1="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Roma_Termini_Mercato_Centrale.jpg/800px-Roma_Termini_Mercato_Centrale.jpg")
    with c1: st.write("🕑 **15:30** | 🍕 Almuerzo")

    # --- LUNES ---
    st.markdown('<div class="highlight-day"><h1>📆 LUNES 2: Vaticano</h1></div>', unsafe_allow_html=True)
    c1, c2 = st.columns([0.6, 0.4]); with c2:
        if st.button("🏛️ Ver Guía", key="vat_lun"):
            abrir_ventana("Vaticano", "Capilla Sixtina. Reserva: 2L2NFFJ00000004GM.", img1="https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Sistine_Chapel_Ceiling_01.jpg/800px-Sistine_Chapel_Ceiling_01.jpg")
    with c1: st.write("🕑 **09:00** | 🏛️ Museos Vaticanos")

    # --- MARTES ---
    st.markdown('<div class="highlight-day"><h1>📆 MARTES 3: Barroco</h1></div>', unsafe_allow_html=True)
    c1, c2 = st.columns([0.6, 0.4]); with c2:
        if st.button("⛲ Trevi", key="tre_mar"):
            abrir_ventana("Roma Barroca", "Fontana di Trevi y Panteón.", img1="https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Fontana_di_Trevi_Front.jpg/800px-Fontana_di_Trevi_Front.jpg")
    with c1: st.write("🕑 **10:00** | ⛲ Trevi / España")

    # --- MIÉRCOLES ---
    st.markdown('<div class="highlight-day"><h1>📆 MIÉRCOLES 4: Arte e Imperio</h1></div>', unsafe_allow_html=True)
    c1, c2 = st.columns([0.6, 0.4]); with c2:
        if st.button("🎨 Borghese", key="bor_mie"):
            abrir_ventana("Galería Borghese", "Obras de Bernini.", img1="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Apolo_y_Dafne_%28Bernini%29.jpg/800px-Apolo_y_Dafne_%28Bernini%29.jpg")
    with c1: st.write("🕑 **12:00** | 🎨 Galería Borghese")

    # --- JUEVES ---
    st.markdown('<div class="highlight-day"><h1>📆 JUEVES 5: Regreso</h1></div>', unsafe_allow_html=True)
    c1, c2 = st.columns([0.6, 0.4]); with c2:
        if st.button("🚕 Traslado", key="fin_jue"):
            abrir_ventana("Aeropuerto", "Taxi 03:45 (Tarifa fija 50€). Vuelo 06:40.")
    with c1: st.write("🕑 **03:45** | 🛫 Traslado")

    st.write("---")
    if st.button("🔙 VOLVER A PORTADA", key="rev"):
        st.session_state.viaje_iniciado = False
        st.rerun()
