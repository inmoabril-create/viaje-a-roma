import streamlit as st
from datetime import datetime

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Roma 2026", page_icon="🇮🇹", layout="centered")

# --- ESTILOS CSS (SOLUCIÓN MODO OSCURO Y DISEÑO) ---
st.markdown("""
    <style>
    /* 1. Fondo general */
    .stApp { background-color: #Fdfcf0; }
    
    /* 2. FORZAR VENTANAS EN BLANCO (Crucial para leer bien) */
    div[role="dialog"] {
        background-color: #ffffff !important;
        color: #000000 !important;
    }
    div[role="dialog"] h2 {
        color: #1E3A5F !important;
    }
    div[role="dialog"] p, div[role="dialog"] li {
        color: #333333 !important;
        font-size: 18px !important;
    }
    div[role="dialog"] a {
        color: #0056b3 !important;
        font-weight: bold;
    }

    /* 3. Encabezados de Día */
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

    /* 4. Textos de la lista principal */
    .activity-time {
        font-weight: bold;
        color: #1E3A5F;
        font-size: 20px;
    }

    /* 5. Botones */
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
    .btn-inicio button:hover {
        background-color: #006b35 !important;
        transform: scale(1.05);
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
    # Usamos triple comilla normal para evitar errores de sintaxis
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
    _, col_btn, _ = st.columns([0.5, 1, 0.5])
    with col_btn:
        st.markdown('<div class="btn-inicio">', unsafe_allow_html=True)
        if st.button("🇮🇹 INICIAR VIAJE", key="main_start"):
            st.session_state.viaje_iniciado = True
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# 2. ITINERARIO COMPLETO
# ==========================================
else:
    st.title("🇮🇹 Roma 2026")
    st.write("### Paco & Mari Trini")

    # ------------------------------------------
    # DOMINGO 1: LLEGADA
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
               - Tiempo: 40-50 min (según tráfico).
            
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
               - 🌐 [Web Oficial](http://www.lagallinabiancaroma.it)
            
            2. **Mercato Centrale Roma**:
               - Puestos artesanos gourmet dentro de la estación Termini.
               - 🌐 [Web Oficial](https://www.mercatocentrale.it/roma/)
            """
            abrir_ventana("Almuerzo Domingo", info_l, img1="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Roma_Termini_Mercato_Centrale.jpg/800px-Roma_Termini_Mercato_Centrale.jpg")

    # 3. Sta Maria Maggiore
    c1, c2 = st.columns([0.55, 0.45])
    with c1: st.markdown('<div class="activity-time">17:30 | ⛪ S. M. Maggiore</div>', unsafe_allow_html=True)
    with c2:
        if st.button("📖 Guía Rápida", key="sm_dom"):
            info_sm = """
            **SANTA MARIA MAGGIORE**
            
            * **Historia**: Siglo V. Una de las 4 basílicas mayores.
            * **El Techo**: Decorado con el **primer oro traído de América** por los Reyes Católicos.
            * **Reliquia**: Bajo el altar mayor se guardan maderas del pesebre de Belén.
            * 🌐 [Web Vaticano](https://www.vatican.va/various/basiliche/sm_maggiore/index_it.html)
            """
            abrir_ventana("Santa Maria Maggiore", info_sm, img1="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Basilica_di_Santa_Maria_Maggiore_-_Rome.jpg/800px-Basilica_di_Santa_Maria_Maggiore_-_Rome.jpg")

    # 4. San Pietro in Vincoli
    c1, c2 = st.columns([0.55, 0.45])
    with c1: st.markdown('<div class="activity-time">18:30 | ⛪ S. Pietro Vincoli</div>', unsafe_allow_html=True)
    with c2:
        if st.button("🗿 El Moisés", key="mo_dom"):
            info_mo = """
            **EL MOISÉS DE MIGUEL ÁNGEL**
            
            * **La Obra**: Fijaos en la tensión de los músculos y las venas del brazo. Realismo asombroso.
            * **Los Cuernos**: Son un error histórico de traducción de la Biblia.
            * **Las Cadenas**: Al fondo del altar están las cadenas de San Pedro.
            * 🌐 [Web Turismo Roma](https://www.turismoroma.it/it/luoghi/basilica-di-san-pietro-vincoli)
            """
            abrir_ventana("San Pietro in Vincoli", info_mo, img1="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Mois%C3%A9s_de_Miguel_%C3%81ngel_en_San_Pietro_in_Vincoli.jpg/800px-Mois%C3%A9s_de_Miguel_%C3%81ngel_en_San_Pietro_in_Vincoli.jpg")

    # 5. Cena
    c1, c2 = st.columns([0.55, 0.45])
    with c1: st.markdown('<div class="activity-time">21:00 | 🍷 Cena Monti</div>', unsafe_allow_html=True)
    with c2:
        if st.button("🍴 Ver Opciones", key="ce_dom"):
            info_ce = """
            **CENA EN BARRIO MONTI:**
            
            1. **Ai Tre Scalini**
               - Vinería histórica y auténtica. No reservan.
               - 🌐 [Web Oficial](http://www.aitrescalini.org)
            
            2. **La Taverna dei Fori Imperiali**
               - Cocina familiar. Famosos por sus raviolis.
               - 🌐 [Web Oficial](https://latavernadeiforiimperiali.com/)
            """
            abrir_ventana("Cena Domingo", info_ce, img1="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Via_Panisperna_-_Rione_Monti.jpg/800px-Via_Panisperna_-_Rione_Monti.jpg")


    # ------------------------------------------
    # LUNES 2: EL VATICANO
    # ------------------------------------------
    st.markdown('<div class="highlight-day"><h1>📆 LUNES 2: El Vaticano</h1></div>', unsafe_allow_html=True)

    # 1. Despertador y Transporte
    c1, c2 = st.columns([0.55, 0.45])
    with c1: st.markdown('<div class="activity-time">07:00 | ⏰ Arriba</div>', unsafe_allow_html=True)
    with c2:
        if st.button("🚇 Logística", key="tr_lun"):
            info_tr = """
            **CÓMO LLEGAR AL VATICANO**
            
            * **Metro Línea A (Roja)**: Desde Termini dirección Battistini.
            * **Parada**: Bajad en **Ottaviano**.
            * **Pago**: Usad el móvil (NFC) en el torno (Tap & Go).
            """
            abrir_ventana("Logística Vaticano", info_tr)

    # 2. Museos Vaticanos
    c1, c2 = st.columns([0.55, 0.45])
    with c1: st.markdown('<div class="activity-time">09:00 | 🏛️ Museos</div>', unsafe_allow_html=True)
    with c2:
        if st.button("🎫 Tickets y Guía", key="vat_lun"):
            info_vat = """
            **MUSEOS VATICANOS Y CAPILLA SIXTINA**
            
            * **RESERVA CONFIRMADA**:
            * **Código**: `2L2NFFJ00000004GM`
            * **Titulares**: Francisco y Trinidad.
            
            **QUÉ VER:**
            1. **Capilla Sixtina**: La cumbre del arte. Silencio absoluto.
            2. **Estancias de Rafael**: Buscad "La Escuela de Atenas".
            
            🌐 [Web Museos Vaticanos](https://www.museivaticani.va)
            """
            abrir_ventana("Vaticano", info_vat, img1="https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Sistine_Chapel_Ceiling_01.jpg/800px-Sistine_Chapel_Ceiling_01.jpg")

    # 3. Almuerzo
    c1, c2 = st.columns([0.55, 0.45])
    with c1: st.markdown('<div class="activity-time">14:30 | 🍝 Almuerzo</div>', unsafe_allow_html=True)
    with c2:
        if st.button("🍴 Ver Opciones", key="com_lun"):
            info_com = """
            **OPCIONES ZONA VATICANO (PRATI):**
            
            1. **Pastasciutta** (Via delle Grazie, 5)
               - Pasta fresca casera, rápido y barato.
               - 🌐 [Web Oficial](https://www.pastasciuttaroma.it)
               
            2. **L'Isola della Pizza** (Via degli Scipioni, 45)
               - Carne a la brasa y ambiente clásico.
               - 🌐 [Web Oficial](https://www.lisoladellapizza.com)
            """
            abrir_ventana("Almuerzo Lunes", info_com)

    # 4. Castel Sant'Angelo
    c1, c2 = st.columns([0.55, 0.45])
    with c1: st.markdown('<div class="activity-time">16:30 | 🏰 Castillo</div>', unsafe_allow_html=True)
    with c2:
        if st.button("🏰 Guía y Vistas", key="cas_lun"):
            info_cas = """
            **CASTEL SANT'ANGELO**
            
            * **Historia**: Tumba de Adriano y fortaleza de los Papas.
            * **El Passetto**: El túnel secreto que lo une con el Vaticano.
            * **La Foto**: Subid a la terraza superior para ver San Pedro.
            * 🌐 [Web Oficial](https://direzionemuseiroma.cultura.gov.it/museo-nazionale-di-castel-santangelo/)
            """
            abrir_ventana("Castel Sant'Angelo", info_cas, img1="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Castel_Sant%27Angelo_Rome.jpg/800px-Castel_Sant%27Angelo_Rome.jpg")

    # 5. Cena Trastevere
    c1, c2 = st.columns([0.55, 0.45])
    with c1: st.markdown('<div class="activity-time">20:30 | 🍕 Trastevere</div>', unsafe_allow_html=True)
    with c2:
        if st.button("🍷 Ver Restaurantes", key="tras_lun"):
            info_tras = """
            **CENA EN TRASTEVERE:**
            
            1. **Tonnarello**:
               - Famoso por sus sartenes de pasta.
               - 🌐 [Web Oficial](https://tonnarello.it)
            
            2. **Da Enzo al 29**:
               - El romano más auténtico. La mejor carbonara.
               - 🌐 [Web Oficial](https://www.daenzoal29.com/)
            """
            abrir_ventana("Cena Lunes", info_tras)


    # ------------------------------------------
    # MARTES 3: ROMA BARROCA
    # ------------------------------------------
    st.markdown('<div class="highlight-day"><h1>📆 MARTES 3: Roma Barroca</h1></div>', unsafe_allow_html=True)

    # 1. Despertador y Desayuno
    c1, c2 = st.columns([0.55, 0.45])
    with c1: st.markdown('<div class="activity-time">08:30 | ⏰ Desayuno</div>', unsafe_allow_html=True)
    with c2:
        if st.button("☕ Opciones", key="des_mar"):
            info_des_mar = """
            **DESAYUNO EN ESQUILINO:**
            
            1. **Pasticceria Regoli**:
               - *Paco*: El **Maritozzo** aquí es sagrado.
               - 🌐 [Web Oficial](http://www.pasticceriaregoli.com/)
            
            2. **Panella**:
               - Panadería artesana de lujo con terraza.
               - 🌐 [Web Oficial](https://panellaroma.com/)
            """
            abrir_ventana("Buenos días Martes", info_des_mar)

    # 2. Trevi y España
    c1, c2 = st.columns([0.55, 0.45])
    with c1: st.markdown('<div class="activity-time">10:00 | ⛲ Ruta Barroca</div>', unsafe_allow_html=True)
    with c2:
        if
