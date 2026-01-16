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

    /* Estilo para el botón INICIAR VIAJE */
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

# --- 2. CONTENIDO DEL VIAJE (RECUPERANDO TU COPIA BUENA) ---
else:
    # --- DOMINGO ---
    st.markdown('<div class="highlight-day"><h1>📆 DOMINGO 1: Benvenuti</h1></div>', unsafe_allow_html=True)
    
    # 1. TRASLADO
    c1, c2 = st.columns([0.6, 0.4])
    with c1: st.write("🕑 **14:00** | 🛬 Traslado Aeropuerto")
    with c2:
        if st.button("🚌 Transporte", key="t_dom"):
            info_t = """**OPCIONES DE LLEGADA:**\n* **🚆 Tren Leonardo Express**: Directo a Termini (32 min). 14€.\n* **🚌 Autobús (Terravision / TAM)**: Unos 6-7€. Tarda 1 hora.\n* **🚖 Taxi Oficial**: Tarifa fija de **50€**.\n\n💡 **Consejo**: El tren es lo más cómodo para evitar el tráfico."""
            abrir_ventana("Llegada a Roma", info_t)

    # 2. ALMUERZO
    c1, c2 = st.columns([0.6, 0.4])
    with c1: st.write("🕑 **15:30** | 🍕 Almuerzo")
    with c2:
        if st.button("🍴 Opciones", key="l_dom"):
            info_l = """**OPCIONES DE ALMUERZO:**\n1. **La Gallina Bianca**: Cocina tradicional romana.\n🌐 [Web Oficial](http://www.lagallinabiancaroma.it)\n2. **Mercato Centrale**: Puestos artesanos gourmet.\n🌐 [Web Oficial](https://www.mercatocentrale.it/roma/)"""
            abrir_ventana("Almuerzo", info_l, img1="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Roma_Termini_Mercato_Centrale.jpg/800px-Roma_Termini_Mercato_Centrale.jpg", pie1="Mercato Centrale Termini")

    # 3. SANTA MARIA MAGGIORE
    c1, c2 = st.columns([0.6, 0.4])
    with c1: st.write("🕑 **17:30** | ⛪ Sta. Maria Maggiore")
    with c2:
        if st.button("📖 Ver Guía", key="sm_dom"):
            info_sm = """**LA BASÍLICA DE ORO:**\nEs la más grande de las iglesias dedicadas a la Virgen en Roma.\n* **El Techo**: Decorado con el primer oro traído de América.\n* **Reliquia**: El Pesebre de Belén se guarda bajo el altar.\n* 🌐 [Web Oficial](https://www.vatican.va/various/basiliche/sm_maggiore/index_it.html)"""
            abrir_ventana("Santa Maria Maggiore", info_sm, img1="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Basilica_di_Santa_Maria_Maggiore_-_Rome.jpg/800px-Basilica_di_Santa_Maria_Maggiore_-_Rome.jpg")

    # 4. SAN PIETRO IN VINCOLI
    c1, c2 = st.columns([0.6, 0.4])
    with c1: st.write("🕑 **18:30** | ⛪ S. Pietro in Vincoli")
    with c2:
        if st.button("📖 El Moisés", key="mo_dom"):
            info_mo = """**EL MOISÉS DE MIGUEL ÁNGEL:**\nContemplad la potencia de su mirada y el detalle de las venas en el brazo.\n* **Curiosidad**: Los cuernos son un error histórico de traducción.\n* **Las Cadenas**: Se exponen las cadenas originales de San Pedro.\n* 🌐 [Información Turística](https://www.turismoroma.it/it/luoghi/basilica-di-san-pietro-vincoli)"""
            abrir_ventana("San Pietro in Vincoli", info_mo, img1="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Mois%C3%A9s_de_Miguel_%C3%81ngel_en_San_Pietro_in_Vincoli.jpg/800px-Mois%C3%A9s_de_Miguel_%C3%81ngel_en_San_Pietro_in_Vincoli.jpg")

    # 5. CENA MONTI
    c1, c2 = st.columns([0.6, 0.4])
    with c1: st.write("🕑 **20:00** | 🍷 Cena (Barrio Monti)")
    with c2:
        if st.button("🍷 Comidas", key="ce_dom"):
            info_ce = """🍴 **Ai Tre Scalini**: Una de las vinerías más auténticas de Roma.\n🌐 [Web Oficial
