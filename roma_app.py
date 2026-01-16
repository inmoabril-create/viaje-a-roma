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

# --- FUNCIÓN DE VENTANA (MODAL) ---
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
    st.markdown("""
        <div style="text-align: center; padding: 40px 25px; background-color: white; border: 8px double #1E3A5F; border-radius: 15px; box-shadow: 0 20px 40px rgba(0,0,0,0.1); margin-top: 20px; max-width: 650px; margin-left: auto; margin-right: auto;">
            <h1 style="color: #1E3A5F; font-family: 'Georgia', serif; font-size: 48px; font-weight: 700; margin-bottom: 15px;">Escapada a Roma</h1>
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
    col_a, col_b, col_c = st.columns([1, 2, 1])
    with col_b:
        if st.button("🇮🇹 INICIAR VIAJE", key="btn_inicio"):
            st.session_state.viaje_iniciado = True
            st.rerun()

# --- 2. CONTENIDO DEL VIAJE ---
else:
    # --- DOMINGO ---
    st.markdown('<div class="highlight-day"><h1>📆 DOMINGO 1: Benvenuti</h1></div>', unsafe_allow_html=True)
    
    c1, c2 = st.columns([0.6, 0.4])
    with c1: st.write("🕑 **14:00** | 🛬 Traslado Aeropuerto")
    with c2:
        if st.button("🚌 Logística", key="dom_trans"):
            abrir_ventana("Llegada a Roma", "Tren Leonardo Express (14€) o Taxi Oficial (Tarifa fija 50€).")

    c1, c2 = st.columns([0.6, 0.4])
    with c1: st.write("🕑 **20:00** | 🍷 Cena Barrio Monti")
    with c2:
        if st.button("🍴 Opciones", key="dom_cena"):
            abrir_ventana("Cena de Bienvenida", "Ai Tre Scalini. Vinería mítica con excelente embutido y pasta.")

    # --- LUNES ---
    st.markdown('<div class="highlight-day"><h1>📆 LUNES 2: El Corazón de Roma</h1></div>', unsafe_allow_html=True)

    c1, c2 = st.columns([0.6, 0.4])
    with c1: st.write("🕑 **09:00** | 🏛️ Museos Vaticanos")
    with c2:
        if st.button("🏛️ Ver Guía", key="lun_vat"):
            info_vat = "Reserva: 2L2NFFJ00000004GM. No os perdáis la Capilla Sixtina y las Estancias de Rafael."
            abrir_ventana("Vaticano", info_vat, img1="https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Sistine_Chapel_Ceiling_01.jpg/800px-Sistine_Chapel_Ceiling_01.jpg")

    c1, c2 = st.columns([0.6, 0.4])
    with c1: st.write("🕑 **18:00** | 🚶 Paseo y Trastevere")
    with c2:
        if st.button("🗺️ Ruta", key="lun_ruta"):
            abrir_ventana("Paseo al Atardecer", "Cruzad el Puente Sant'Angelo, pasad por Campo de' Fiori y terminad en Trastevere.")

    # --- BOTÓN PARA VOLVER ---
    st.write("---")
    if st.button("🔙 VOLVER A LA PORTADA", key="btn_volver"):
        st.session_state.viaje_iniciado = False
        st.rerun()
