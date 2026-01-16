import streamlit as st
from datetime import datetime

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Roma 2026", page_icon="🇮🇹", layout="centered")

# --- ESTILOS CSS (DISEÑO PREMIUM Y LEGIBLE) ---
st.markdown("""
    <style>
    /* 1. Fondo general color crema suave */
    .stApp { background-color: #Fdfcf0; }
    
    /* 2. FORZAR VENTANAS EMERGENTES EN BLANCO (Arreglo Modo Oscuro) */
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

    /* 4. Textos y Títulos de Actividad */
    .activity-time {
        font-weight: bold;
        color: #1E3A5F;
        font-size: 20px;
    }
    .activity-title {
        font-size: 20px;
        color: #333;
    }

    /* 5. Botones Estilizados */
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

    /* Botón INICIAR VIAJE (Verde) */
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
# 1. PANTALLA DE BIENVENIDA (DEDICATORIA)
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
# 2. ITINERARIO COMPLETO (FINO Y DETALLADO)
# ==========================================
else:
    st.title("🇮🇹 Roma 2026")
    st.write("### Paco & Mari Trini")

    # ------------------------------------------
    # DOMINGO 1: LLEGADA Y PRIMER CONTACTO
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
            **OPCIÓN PRINCIPAL:**
            
            🐔 **La Gallina Bianca**
            * Cocina tradicional romana y pizzas al horno de leña.
            * 💶 Precio estimado: **50€** (pareja).
            * 📍 Muy cerca de Termini.
            * 🌐 [Sitio Web Oficial](http://www.lagallinabiancaroma.it)
            
            **ALTERNATIVA RÁPIDA:**
            🍕 **Mercato Centrale Roma**: Puestos gourmet dentro de la estación.
            """
            abrir_ventana("Almuerzo Domingo", info_l, img1="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Roma_Termini_Mercato_Centrale.jpg/800px-Roma_Termini_Mercato_Centrale.jpg")

    # 3. Sta Maria Maggiore
    c1, c2 = st.columns([0.55, 0.45])
    with c1: st.markdown('<div class="activity-time">17:30 | ⛪ S. M. Maggiore</div>', unsafe_allow_html=True)
    with c2:
        if st.button("📖 Guía Rápida", key="sm_dom"):
            info_sm = """
            **BASÍLICA DE SANTA MARIA MAGGIORE**
            
            * **Historia**: Siglo V. Es una de las cuatro basílicas mayores.
            * **El Techo**: Mirad arriba. Ese artesonado está decorado con el **primer oro traído de América** por los Reyes Católicos.
            * **Reliquia**: Bajo el altar mayor se guardan maderas del pesebre original de Belén.
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
            
            * **La Obra**: Fijaos en la tensión de los músculos y las venas del brazo. Parece que se va a levantar de la silla.
            * **Los Cuernos**: ¿Veis que tiene cuernos? Es un error de traducción de la Biblia (rayos de luz vs cuernos).
            * **Las Cadenas**: Al fondo del altar están las cadenas con las que ataron a San Pedro en Jerusalén.
            """
            abrir_ventana("San Pietro in Vincoli", info_mo, img1="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Mois%C3%A9s_de_Miguel_%C3%81ngel_en_San_Pietro_in_Vincoli.jpg/800px-Mois%C3%A9s_de_Miguel_%C3%81ngel_en_San_Pietro_in_Vincoli.jpg")

    # 5. Cena
    c1, c2 = st.columns([0.55, 0.45])
    with c1: st.markdown('<div class="activity-time">21:00 | 🍷 Cena Monti</div>', unsafe_allow_html=True)
    with c2:
        if st.button("🍴 Ai Tre Scalini", key="ce_dom"):
            info_ce = """
            **CENA EN BARRIO MONTI**
            
            🍷 **Ai Tre Scalini**
            * Vinería histórica y con mucho ambiente local.
            * 💶 Precio estimado: **50€**.
            * **Nota**: No suelen aceptar reservas, id con tiempo.
            * 🌐 [Web Oficial](http://www.aitrescalini.org)
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
            * **Pago**: Usad el móvil (NFC) directamente en el torno (Tap & Go).
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
            
            **QUÉ NO PERDERSE:**
            1. **Capilla Sixtina**: La obra cumbre. (Silencio absoluto).
            2. **Estancias de Rafael**: Buscad "La Escuela de Atenas".
            3. **Galería de los Mapas**.
            
            🌐 [Web Museos Vaticanos](https://www.museivaticani.va)
            """
            abrir_ventana("Vaticano", info_vat, img1="https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Sistine_Chapel_Ceiling_01.jpg/800px-Sistine_Chapel_Ceiling_01.jpg")

    # 3. Almuerzo
    c1, c2 = st.columns([0.55, 0.45])
    with c1: st.markdown('<div class="activity-time">14:30 | 🍝 Almuerzo</div>', unsafe_allow_html=True)
    with c2:
        if st.button("🍴 Zona Prati", key="com_lun"):
            info_com = """
            **OPCIONES ZONA VATICANO (PRATI):**
            
            1. **Pastasciutta** (Via delle Grazie, 5)
               - Pasta fresca casera, rápido y barato (~25€).
               - 🌐 [Web Oficial](https://www.pastasciuttaroma.it)
               
            2. **L'Isola della Pizza** (Via degli Scipioni, 45)
               - Carne a la brasa y ambiente romano clásico.
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
            
            * **Historia**: Fue la tumba del emperador Adriano y luego fortaleza de los Papas.
            * **El Pasadizo**: Existe un túnel (Il Passetto) que lo une con el Vaticano.
            * **La Foto**: Subid a la terraza superior. Tenéis la mejor vista frontal de la Basílica de San Pedro.
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
               - 💶 Precio: ~50€.
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

    # 1. Trevi y España
    c1, c2 = st.columns([0.55, 0.45])
    with c1: st.markdown('<div class="activity-time">10:00 | ⛲ Ruta Barroca</div>', unsafe_allow_html=True)
    with c2:
        if st.button("🗺️ Trevi y España", key="rut_mar"):
            info_rut = """
            **EL CORAZÓN DE ROMA:**
            
            💧 **Fontana di Trevi**:
            - Obra maestra del barroco. Neptuno domando las aguas.
            - **Tradición**: Tirar moneda con mano derecha sobre hombro izquierdo para volver a Roma.
            
            steps **Plaza de España**:
            - Sus 135 peldaños. Al pie está la fuente de la Barcaza de Bernini.
            """
            abrir_ventana("Ruta Barroca", info_rut, img1="https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Fontana_di_Trevi_Front.jpg/800px-Fontana_di_Trevi_Front.jpg")

    # 2. Almuerzo Cantina
    c1, c2 = st.columns([0.55, 0.45])
    with c1: st.markdown('<div class="activity-time">14:00 | 🍝 Almuerzo</div>', unsafe_allow_html=True)
    with c2:
        if st.button("🍷 Cantina e Cucina", key="can_mar"):
            info_can = """
            **CANTINA E CUCINA**
            (Via del Governo Vecchio, 87)
            
            * Sitio con muchísimo encanto y personal muy simpático.
            * **Recomendación**: Tabla de embutidos y Pasta Amatriciana.
            * 💶 Precio estimado: **60€**.
            * 🌐 [Web Oficial](https://cantinaecucina.it)
            """
            abrir_ventana("Almuerzo Martes", info_can)

    # 3. Panteón y Navona
    c1, c2 = st.columns([0.55, 0.45])
    with c1: st.markdown('<div class="activity-time">16:30 | 🏛️ Panteón</div>', unsafe_allow_html=True)
    with c2:
        if st.button("📖 Guía Rápida", key="pan_mar"):
            info_pan = """
            **PANTEÓN DE AGRIPA (125 d.C.)**
            
            * **Ingeniería**: Tiene la cúpula de hormigón no armado más grande del mundo.
            * **El Óculo**: El agujero del techo mide 9 metros de diámetro. Sí, cuando llueve, entra agua (pero el suelo tiene desagües).
            * **Tumbas**: Aquí descansa el pintor Rafael y los Reyes de Italia.
            
            **PIAZZA NAVONA**:
            * Antigua pista de estadio romano. Entrad a la iglesia de *Sant'Agnese*.
            """
            abrir_ventana("Panteón y Navona", info_pan, img1="https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Pantheon_Rome_2016.jpg/800px-Pantheon_Rome_2016.jpg")

    # 4. Cena Navona
    c1, c2 = st.columns([0.55, 0.45])
    with c1: st.markdown('<div class="activity-time">20:30 | 🍷 Cena Navona</div>', unsafe_allow_html=True)
    with c2:
        if st.button("🍴 Opciones", key="cen_mar"):
            info_cn = """
            **CENA ZONA NAVONA:**
            
            1. **Cul de Sac**: Enoteca histórica. Ideal para patés y vinos.
            🌐 [Web Oficial](https://www.enotecaculdesacroma.it/)
            
            2. **Mimi e Coco**: Muy buen ambiente, pasta y cócteles.
            🌐 [Web Oficial](https://mimiecoco.com)
            """
            abrir_ventana("Cena Martes", info_cn)


    # ------------------------------------------
    # MIÉRCOLES 4: ARTE E IMPERIO
    # ------------------------------------------
    st.markdown('<div class="highlight-day"><h1>📆 MIÉRCOLES 4: Arte e Imperio</h1></div>', unsafe_allow_html=True)

    # 1. Borghese
    c1, c2 = st.columns([0.55, 0.45])
    with c1: st.markdown('<div class="activity-time">12:00 | 🎨 Borghese</div>', unsafe_allow_html=True)
    with c2:
        if st.button("🎫 Guía y Entrada", key="bor_mie"):
            info_bor = """
            **GALERÍA BORGHESE**
            
            * **Horario**: Entrada a las 12:00. Estar a las **11:30** (control estricto).
            * **Guardarropa**: Es obligatorio dejar bolsos.
            
            **OBRAS MAESTRAS:**
            * **Bernini**: "Apolo y Dafne" (ved cómo los dedos se vuelven hojas) y "El Rapto de Proserpina" (la mano hundida en el muslo de mármol).
            * **Caravaggio**: Sala dedicada al maestro del claroscuro.
            
            🌐 [Web Oficial](https://galleriaborghese.beniculturali.it/)
            """
            abrir_ventana("Galería Borghese", info_bor, img1="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Apolo_y_Dafne_%28Bernini%29.jpg/800px-Apolo_y_Dafne_%28Bernini%29.jpg")

    # 2. Almuerzo Coliseo
    c1, c2 = st.columns([0.55, 0.45])
    with c1: st.markdown('<div class="activity-time">14:30 | 🍝 Almuerzo</div>', unsafe_allow_html=True)
    with c2:
        if st.button("🍴 Zona Imperial", key="alm_mie"):
            info_col = """
            **ALMUERZO CERCA DEL COLISEO:**
            
            1. **Hostaria al Gladiatore**:
               - Vistas directas al Coliseo. Turístico pero decente.
               - 🌐 [Web Oficial](https://www.ristorantegladiatore.it/)
               
            2. **Trattoria Luzzi** (Via di S. Giovanni in Laterano):
               - A 5 min andando. Muy ruidosa, muy barata y lasaña increíble.
            """
            abrir_ventana("Almuerzo Miércoles", info_col)

    # 3. Coliseo Iluminado
    c1, c2 = st.columns([0.55, 0.45])
    with c1: st.markdown('<div class="activity-time">16:00 | 🏟️ Roma Luz</div>', unsafe_allow_html=True)
    with c2:
        if st.button("🏛️ Paseo Imperial", key="imp_mie"):
            info_imp = """
            **ROMA IMPERIAL AL ATARDECER**
            
            * **Coliseo**: El anfiteatro más grande jamás construido. Imaginad a 50.000 espectadores gritando.
            * **Foros**: El centro político y social de la antigua Roma.
            * **Recomendación**: Subid a la Plaza del Campidoglio para ver el Foro Romano iluminado desde el mirador trasero.
            """
            abrir_ventana("Paseo Imperial", info_imp, img1="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Colosseum_at_night_2015.jpg/800px-Colosseum_at_night_2015.jpg")

    # 4. Cena Despedida
    c1, c2 = st.columns([0.55, 0.45])
    with c1: st.markdown('<div class="activity-time">21:00 | 🍝 Cena Final</div>', unsafe_allow_html=True)
    with c2:
        if st.button("🍷 Vecchia Roma", key="vec_mie"):
            info_vec = """
            **CENA DE DESPEDIDA**
            
            🍝 **Trattoria Vecchia Roma**
            * **Plato Estrella**: *Amatriciana Flambé*. Traen una rueda de queso pecorino enorme a la mesa, le prenden fuego con brandy y mezclan la pasta dentro. ¡Espectáculo puro!
            * **Reserva**: +39 06 446 7373.
            * 💶 Precio: ~60€.
            * 🌐 [Web Oficial](https://www.trattoriavecchiaroma.it/)
            """
            abrir_ventana("Cena de Despedida", info_vec)


    # ------------------------------------------
    # JUEVES 5: VUELTA A CASA
    # ------------------------------------------
    st.markdown('<div class="highlight-day"><h1>📆 JUEVES 5: Fin del Viaje</h1></div>', unsafe_allow_html=True)

    c1, c2 = st.columns([0.55, 0.45])
    with c1: st.markdown('<div class="activity-time">03:00 | ⏰ Arriba</div>', unsafe_allow_html=True)
    with c2:
        if st.button("🛫 Logística", key="jue_fin"):
            info_fin = """
            **OPERACIÓN RETORNO (VUELO 06:40)**
            
            * **03:00**: Despertador. Ducha rápida y cerrar maletas.
            * **03:45**: Estar en la calle esperando transporte.
            
            **OPCIONES AL AEROPUERTO:**
            1. **Taxi (Recomendado)**: 50€ tarifa fija. Pedidlo en recepción la tarde anterior. Salida 04:00.
            2. **Bus TAM**: Salida 03:45 desde Via Giolitti 34 (Termini). 7€.
            """
            abrir_ventana("Vuelta a Casa", info_fin)

    # BOTÓN FINAL
    st.write("---")
    st.markdown("<div style='text-align: center; margin-bottom: 20px;'>", unsafe_allow_html=True)
    if st.button("🔙 VOLVER A PORTADA", key="btn_volver"):
        st.session_state.viaje_iniciado = False
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
