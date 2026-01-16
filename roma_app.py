import streamlit as st
from datetime import datetime

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Roma 2026", page_icon="🇮🇹", layout="centered")

# --- ESTILOS CSS (DISEÑO MEJORADO) ---
st.markdown("""
    <style>
    /* 1. Fondo general */
    .stApp { background-color: #Fdfcf0; }
    
    /* 2. Arreglo para las VENTANAS EMERGENTES (Para que no salgan negras) */
    div[role="dialog"], div[role="dialog"] > div {
        background-color: #ffffff !important;
        color: #000000 !important;
    }
    div[role="dialog"] h2 {
        color: #1E3A5F !important; /* Títulos de ventana en azul */
    }
    div[role="dialog"] p, div[role="dialog"] li {
        color: #333333 !important; /* Texto de ventana en gris oscuro */
        font-size: 18px !important;
    }

    /* 3. Títulos de los Días (Azul con sombra) */
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

    /* 4. TEXTO DE LA LISTA (Más grande y legible) */
    .stMarkdown p {
        font-size: 21px !important; /* AUMENTADO EL TAMAÑO */
        color: #333 !important;
        line-height: 1.6;
        vertical-align: middle;
    }
    /* Las horas y títulos en negrita (azul marino para destacar) */
    .stMarkdown strong {
        color: #1E3A5F !important;
        font-size: 22px !important;
    }

    /* 5. BOTONES */
    div.stButton > button {
        width: 100%;
        background-color: white !important;
        border: 2px solid #1E3A5F !important;
        color: #1E3A5F !important;
        font-weight: bold;
        padding: 10px;
        border-radius: 12px;
        font-size: 18px !important; /* Texto del botón más legible */
    }
    div.stButton > button:hover {
        background-color: #1E3A5F !important;
        color: white !important;
    }

    /* Botón INICIAR VIAJE (Verde y Grande) */
    .btn-inicio button {
        background-color: #008C45 !important;
        color: white !important;
        border: none !important;
        height: 65px !important;
        font-size: 24px !important;
        border-radius: 50px !important;
        box-shadow: 0 5px 15px rgba(0,140,69,0.4);
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
    st.markdown(f"""
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
    _, col_btn, _ = st.columns([0.5, 1, 0.5])
    with col_btn:
        st.markdown('<div class="btn-inicio">', unsafe_allow_html=True)
        if st.button("🇮🇹 INICIAR VIAJE", key="main_start"):
            st.session_state.viaje_iniciado = True
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# 2. CONTENIDO COMPLETO DEL VIAJE
# ==========================================
else:
    st.title("🇮🇹 Roma 2026")
    st.write("### Paco & Mari Trini")

    # --- DOMINGO ---
    st.markdown('<div class="highlight-day"><h1>📆 DOMINGO 1: Benvenuti</h1></div>', unsafe_allow_html=True)
    
    c1, c2 = st.columns([0.55, 0.45])
    with c1: st.write("🕑 **14:00** | 🛬 Traslado")
    with c2:
        if st.button("🚌 Transporte", key="t_dom"):
            info_t = """
            **OPCIONES DE LLEGADA:**
            * **🚆 Tren Leonardo Express**: Directo a Termini (32 min). 14€.
            * **🚌 Autobús (Terravision)**: Unos 6-7€. Tarda 1 hora.
            * **🚖 Taxi Oficial**: Tarifa fija de **50€**.
            """
            abrir_ventana("Llegada a Roma", info_t)

    c1, c2 = st.columns([0.55, 0.45])
    with c1: st.write("🕑 **15:30** | 🍕 Almuerzo")
    with c2:
        if st.button("🍴 Opciones", key="l_dom"):
            info_l = """
            **OPCIONES DE ALMUERZO:**
            1. **La Gallina Bianca**: Cocina tradicional romana cerca de Termini.
            2. **Mercato Centrale**: Puestos artesanos gourmet en la estación.
            """
            abrir_ventana("Almuerzo", info_l, img1="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Roma_Termini_Mercato_Centrale.jpg/800px-Roma_Termini_Mercato_Centrale.jpg")

    c1, c2 = st.columns([0.55, 0.45])
    with c1: st.write("🕑 **17:30** | ⛪ Sta. Maria")
    with c2:
        if st.button("📖 Ver Guía", key="sm_dom"):
            info_sm = "**LA BASÍLICA DE ORO:**\nEs la más grande dedicada a la Virgen. El techo tiene el primer oro traído de América."
            abrir_ventana("Santa Maria Maggiore", info_sm, img1="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Basilica_di_Santa_Maria_Maggiore_-_Rome.jpg/800px-Basilica_di_Santa_Maria_Maggiore_-_Rome.jpg")

    c1, c2 = st.columns([0.55, 0.45])
    with c1: st.write("🕑 **18:30** | ⛪ S. Pietro")
    with c2:
        if st.button("📖 El Moisés", key="mo_dom"):
            info_mo = "**EL MOISÉS DE MIGUEL ÁNGEL:**\nContemplad la potencia de su mirada. Los cuernos son un error de traducción histórica."
            abrir_ventana("San Pietro in Vincoli", info_mo, img1="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Mois%C3%A9s_de_Miguel_%C3%81ngel_en_San_Pietro_in_Vincoli.jpg/800px-Mois%C3%A9s_de_Miguel_%C3%81ngel_en_San_Pietro_in_Vincoli.jpg")

    c1, c2 = st.columns([0.55, 0.45])
    with c1: st.write("🕑 **20:00** | 🍷 Cena Monti")
    with c2:
        if st.button("🍷 Comidas", key="ce_dom"):
            abrir_ventana("Cena en Monti", "🍴 **Ai Tre Scalini**: Vinería mítica. No aceptan reservas.", img1="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Via_Panisperna_-_Rione_Monti.jpg/800px-Via_Panisperna_-_Rione_Monti.jpg")


    # --- LUNES ---
    st.markdown('<div class="highlight-day"><h1>📆 LUNES 2: Vaticano</h1></div>', unsafe_allow_html=True)

    c1, c2 = st.columns([0.55, 0.45])
    with c1: st.write("🕑 **07:15** | 🚌 Traslado")
    with c2:
        if st.button("🚇 Metro", key="tr_lun_1"):
            abrir_ventana("Logística", "**Metro Línea A (Roja)**: Bajad en Ottaviano. Usad Tap & Go.")

    c1, c2 = st.columns([0.55, 0.45])
    with c1: st.write("🕑 **09:00** | 🏛️ Museos")
    with c2:
        if st.button("📖 Guía", key="guia_lun_1"):
            info_vat = """
            **EL TESORO DEL PAPA:**
            * **Capilla Sixtina**: Silencio absoluto.
            * **Estancias de Rafael**: La Escuela de Atenas.
            * **Reserva**: `2L2NFFJ00000004GM`.
            """
            abrir_ventana("Museos Vaticanos", info_vat, img1="https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Sistine_Chapel_Ceiling_01.jpg/800px-Sistine_Chapel_Ceiling_01.jpg")

    c1, c2 = st.columns([0.55, 0.45])
    with c1: st.write("🕑 **14:30** | 🍝 Almuerzo")
    with c2:
        if st.button("🍕 Sitios", key="com_lun_1"):
            abrir_ventana("Zona Prati", "1. **Pastasciutta** (Pasta fresca rápida).\n2. **L'Isola della Pizza** (Carne y romana).")

    c1, c2 = st.columns([0.55, 0.45])
    with c1: st.write("🕑 **16:30** | 🏰 Castillo")
    with c2:
        if st.button("🏰 Guía", key="guia_lun_2"):
            abrir_ventana("Castel Sant'Angelo", "Mausoleo y fortaleza. Subid a la terraza para ver San Pedro.", img1="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Castel_Sant%27Angelo_Rome.jpg/800px-Castel_Sant%27Angelo_Rome.jpg")

    c1, c2 = st.columns([0.55, 0.45])
    with c1: st.write("🕑 **18:00** | 🚶 Paseo")
    with c2:
        if st.button("🗺️ Ruta", key="ruta_lun"):
            abrir_ventana("Ruta a pie", "Puente Sant'Angelo -> Via Giulia -> Campo de' Fiori -> Ponte Sisto -> Trastevere.")

    c1, c2 = st.columns([0.55, 0.45])
    with c1: st.write("🕑 **20:30** | 🍷 Cena")
    with c2:
        if st.button("🍷 Trastevere", key="com_lun_2"):
            abrir_ventana("Cena Lunes", "**Tonnarello** o **Da Enzo al 29**. El barrio con más ambiente.")


    # --- MARTES ---
    st.markdown('<div class="highlight-day"><h1>📆 MARTES 3: Barroco</h1></div>', unsafe_allow_html=True)

    c1, c2 = st.columns([0.55, 0.45])
    with c1: st.write("🕑 **08:30** | ☕ Desayuno")
    with c2:
        if st.button("⚙️ Detalles", key="log_mar"):
            abrir_ventana("Esquilino", "**Pasticceria Regoli**: Tenéis que probar el Maritozzo.")

    c1, c2 = st.columns([0.55, 0.45])
    with c1: st.write("🕑 **10:00** | ⛲ Trevi")
    with c2:
        if st.button("📖 Guía", key="guia_mar_1"):
            abrir_ventana("Trevi y España", "**Fontana di Trevi**: Moneda con la mano derecha sobre hombro izquierdo.", img1="https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Fontana_di_Trevi_Front.jpg/800px-Fontana_di_Trevi_Front.jpg")

    c1, c2 = st.columns([0.55, 0.45])
    with c1: st.write("🕑 **14:00** | 🍝 Almuerzo")
    with c2:
        if st.button("🍝 Cantina", key="com_mar_1"):
            abrir_ventana("Cantina e Cucina", "Local con alma. Pedid Carbonara y Focaccia.")

    c1, c2 = st.columns([0.55, 0.45])
    with c1: st.write("🕑 **16:30** | 🏛️ Panteón")
    with c2:
        if st.button("📖 Guía", key="guia_mar_2"):
            abrir_ventana("Panteón y Navona", "Tumba de Rafael. La cúpula de hormigón más grande del mundo.", img1="https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Pantheon_Rome_2016.jpg/800px-Pantheon_Rome_2016.jpg")

    c1, c2 = st.columns([0.55, 0.45])
    with c1: st.write("🕑 **20:30** | 🍷 Cena")
    with c2:
        if st.button("🍷 Navona", key="com_mar_2"):
            abrir_ventana("Cena Martes", "**Cul de Sac** (Vinos) o **Mimi e Coco**.")


    # --- MIÉRCOLES ---
    st.markdown('<div class="highlight-day"><h1>📆 MIÉRCOLES 4: Arte</h1></div>', unsafe_allow_html=True)

    c1, c2 = st.columns([0.55, 0.45])
    with c1: st.write("🕑 **09:00** | ☕ Desayuno")
    with c2:
        if st.button("☕ Sitios", key="des_mie"):
            abrir_ventana("Desayuno", "**Dagnino**: Cannoli sicilianos increíbles.")

    c1, c2 = st.columns([0.55, 0.45])
    with c1: st.write("🕑 **12:00** | 🎨 Borghese")
    with c2:
        if st.button("🎨 Guía", key="guia_mie_1"):
            abrir_ventana("Galería Borghese", "Estar a las 11:30. Bernini (Apolo y Dafne) y Caravaggio.", img1="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Apolo_y_Dafne_%28Bernini%29.jpg/800px-Apolo_y_Dafne_%28Bernini%29.jpg")

    c1, c2 = st.columns([0.55, 0.45])
    with c1: st.write("🕑 **14:00** | 🚌 Traslado")
    with c2:
        if st.button("🚌 Centro", key="tr_mie_centro"):
            abrir_ventana("Al Coliseo", "Bus 160 o paseo de 25 min bajando Via Veneto.")

    c1, c2 = st.columns([0.55, 0.45])
    with c1: st.write("🕑 **14:30** | 🍝 Almuerzo")
    with c2:
        if st.button("🍝 Coliseo", key="com_mie_1"):
            abrir_ventana("Zona Imperial", "**Hostaria al Gladiatore** o **Trattoria Luzzi**.")

    c1, c2 = st.columns([0.55, 0.45])
    with c1: st.write("🕑 **18:00** | 🏟️ Roma Luz")
    with c2:
        if st.button("🏛️ Guía", key="guia_mie_2"):
            abrir_ventana("Roma Imperial", "Mirador del Campidoglio y Via dei Fori Imperiali.", img1="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Colosseum_at_night_2015.jpg/800px-Colosseum_at_night_2015.jpg")

    c1, c2 = st.columns([0.55, 0.45])
    with c1: st.write("🕑 **21:00** | 🍝 Cena Final")
    with c2:
        if st.button("🍷 Despedida", key="com_mie_2"):
            abrir_ventana("Cena Final", "**Trattoria Vecchia Roma** (Amatriciana Flambé) o **Trattoria Monti**.")


    # --- JUEVES ---
    st.markdown('<div class="highlight-day"><h1>📆 JUEVES 5: Regreso</h1></div>', unsafe_allow_html=True)

    c1, c2 = st.columns([0.55, 0.45])
    with c1: st.write("🕑 **03:00** | ⏰ Alerta")
    with c2:
        if st.button("⏰ Plan", key="desp_jue"):
            abrir_ventana("Madrugada", "Ducha rápida y check-out. Estar listos a las 03:45.")

    c1, c2 = st.columns([0.55, 0.45])
    with c1: st.write("🕑 **03:45** | 🛫 Taxi")
    with c2:
        if st.button("🚕 Transporte", key="tr_jue_fin"):
            abrir_ventana("Al Aeropuerto", "**Taxi Oficial (Blanco)**: 50€. Pedidlo la tarde anterior en el hotel.")

    c1, c2 = st.columns([0.55, 0.45])
    with c1: st.write("🕑 **06:40** | ✈️ Vuelo")
    with c2:
        if st.button("📋 Pasos", key="vuelo_jue"):
            abrir_ventana("Regreso", "Llegada al aeropuerto sobre las 04:20. ¡Buen viaje!")

    # BOTÓN FINAL
    st.write("---")
    st.markdown("<div style='text-align: center; margin-bottom: 20px;'>", unsafe_allow_html=True)
    if st.button("🔙 VOLVER A PORTADA", key="btn_volver"):
        st.session_state.viaje_iniciado = False
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
