import streamlit as st
from datetime import datetime

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Roma 2026", page_icon="🇮🇹", layout="centered")

# --- ESTILOS CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #Fdfcf0; }
    
    .highlight-day {
        background: linear-gradient(135deg, #1E3A5F 0%, #12263a 100%);
        color: white !important;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin-top: 30px;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    .highlight-day h1 { color: white !important; font-size: 24px !important; margin:0; }

    .stMarkdown p, .stMarkdown li, div {
        color: #1a1a1a !important;
        font-size: 18px !important;
        line-height: 1.6;
    }

    /* Enlaces */
    a { color: #0056b3 !important; font-weight: bold !important; }

    /* Botones de Actividades (Azul Marino borde) */
    div.stButton > button {
        width: 100%;
        background-color: white !important;
        border: 2px solid #1E3A5F !important;
        color: #1E3A5F !important;
        font-weight: bold;
        padding: 12px;
        border-radius: 12px;
        transition: all 0.3s;
    }
    div.stButton > button:hover {
        background-color: #1E3A5F !important;
        color: white !important;
    }

    /* Botón especial INICIAR VIAJE (Verde) */
    .btn-inicio button {
        background-color: #008C45 !important;
        color: white !important;
        border: none !important;
        height: 60px !important;
        font-size: 22px !important;
        border-radius: 50px !important;
        box-shadow: 0 5px 15px rgba(0,140,69,0.3);
    }
    .btn-inicio button:hover {
        background-color: #006b35 !important;
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)

# --- FUNCIÓN DE VENTANA (POP-UP) ---
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

# ==========================================
# 2. CONTENIDO COMPLETO DEL VIAJE
# ==========================================
else:
    # --- CABECERA INTERNA ---
    st.title("🇮🇹 Roma 2026")
    st.write("### Paco & Mari Trini")

    # ==========================================
    # DOMINGO 1: Benvenuti
    # ==========================================
    st.markdown('<div class="highlight-day"><h1>📆 DOMINGO 1: Benvenuti</h1></div>', unsafe_allow_html=True)

    # 1. TRASLADO
    c1, c2 = st.columns([0.6, 0.4])
    with c1: st.write("🕑 **14:00** | 🛬 Traslado Aeropuerto")
    with c2:
        if st.button("🚌 Transporte", key="t_dom"):
            info_t = """
            **OPCIONES DE LLEGADA:**
            * **🚆 Tren Leonardo Express**: Directo a Termini (32 min). 14€.
            * **🚌 Autobús (Terravision / TAM)**: Unos 6-7€. Tarda 1 hora.
            * **🚖 Taxi Oficial**: Tarifa fija de **50€**.
            
            💡 **Consejo**: El tren es lo más cómodo para evitar el tráfico de Roma.
            """
            abrir_ventana("Llegada a Roma", info_t)

    # 2. ALMUERZO
    c1, c2 = st.columns([0.6, 0.4])
    with c1: st.write("🕑 **15:30** | 🍕 Almuerzo")
    with c2:
        if st.button("🍴 Opciones", key="l_dom"):
            info_l = """
            **OPCIONES DE ALMUERZO:**
            1. **La Gallina Bianca**: Cocina tradicional romana muy cerca de Termini. 
            🌐 [Web Oficial](http://www.lagallinabiancaroma.it)
            
            2. **Mercato Centrale**: Puestos artesanos gourmet en la misma estación.
            🌐 [Web Oficial](https://www.mercatocentrale.it/roma/)
            """
            abrir_ventana("Almuerzo", info_l, img1="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Roma_Termini_Mercato_Centrale.jpg/800px-Roma_Termini_Mercato_Centrale.jpg", pie1="Mercato Centrale Termini")

    # 3. SANTA MARIA MAGGIORE
    c1, c2 = st.columns([0.6, 0.4])
    with c1: st.write("🕑 **17:30** | ⛪ Sta. Maria Maggiore")
    with c2:
        if st.button("📖 Ver Guía", key="sm_dom"):
            info_sm = """
            **LA BASÍLICA DE ORO:**
            Es la más grande de las iglesias dedicadas a la Virgen en Roma.
            
            * **El Techo**: Decorado con el primer oro traído de América.
            * **Reliquia**: El Pesebre de Belén se guarda bajo el altar.
            * 🌐 [Web Oficial (Vaticano)](https://www.vatican.va/various/basiliche/sm_maggiore/index_it.html)
            """
            abrir_ventana("Santa Maria Maggiore", info_sm, img1="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Basilica_di_Santa_Maria_Maggiore_-_Rome.jpg/800px-Basilica_di_Santa_Maria_Maggiore_-_Rome.jpg")

    # 4. SAN PIETRO IN VINCOLI
    c1, c2 = st.columns([0.6, 0.4])
    with c1: st.write("🕑 **18:30** | ⛪ S. Pietro in Vincoli")
    with c2:
        if st.button("📖 El Moisés", key="mo_dom"):
            info_mo = """
            **EL MOISÉS DE MIGUEL ÁNGEL:**
            Contemplad la potencia de su mirada y el detalle de las venas en el brazo.
            
            * **Curiosidad**: Los cuernos son un error histórico de traducción.
            * **Las Cadenas**: Se exponen las cadenas originales de San Pedro.
            * 🌐 [Información Turística](https://www.turismoroma.it/it/luoghi/basilica-di-san-pietro-vincoli)
            """
            abrir_ventana("San Pietro in Vincoli", info_mo, img1="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Mois%C3%A9s_de_Miguel_%C3%81ngel_en_San_Pietro_in_Vincoli.jpg/800px-Mois%C3%A9s_de_Miguel_%C3%81ngel_en_San_Pietro_in_Vincoli.jpg")

    # 5. CENA MONTI
    c1, c2 = st.columns([0.6, 0.4])
    with c1: st.write("🕑 **20:00** | 🍷 Cena (Barrio Monti)")
    with c2:
        if st.button("🍷 Comidas", key="ce_dom"):
            info_ce = """
            🍴 **Ai Tre Scalini**: Una de las vinerías más auténticas de Roma. 
            No aceptan reservas, así que es mejor llegar puntuales.
            
            🌐 [Web Oficial](http://www.aitrescalini.org)
            """
            abrir_ventana("Cena en Monti", info_ce, img1="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Via_Panisperna_-_Rione_Monti.jpg/800px-Via_Panisperna_-_Rione_Monti.jpg", pie1="Barrio Monti")


    # ==========================================
    # LUNES 2: El Corazón de Roma
    # ==========================================
    st.markdown('<div class="highlight-day"><h1>📆 LUNES 2: El Corazón de Roma</h1></div>', unsafe_allow_html=True)

    # 1. TRASLADO AL VATICANO
    c1, c2 = st.columns([0.6, 0.4])
    with c1: st.write("🕑 **07:15** | 🚌 Traslado al Vaticano")
    with c2:
        if st.button("🚇 Logística", key="tr_lun_1"):
            info_tr = """
            **CÓMO LLEGAR DESDE EL HOTEL:**
            * **Metro Línea A (Roja)**: Lo más directo. Bajad en la parada **Ottaviano**.
            * **Taxi**: Tardará unos 15-20 min y os costará unos 15€.
            * **Tap & Go**: Podéis pagar el metro apoyando vuestra tarjeta bancaria directamente en el torno.
            """
            abrir_ventana("Hacia el Vaticano", info_tr)

    # 2. MUSEOS VATICANOS
    c1, c2 = st.columns([0.6, 0.4])
    with c1: st.write("🕑 **09:00** | 🏛️ Museos Vaticanos")
    with c2:
        if st.button("📖 Ver Guía", key="guia_lun_1"):
            info_vat = """
            **EL TESORO DEL PAPA:**
            * **La Capilla Sixtina**: Obra cumbre de Miguel Ángel. El techo narra el Génesis y el testero el Juicio Final. **Importante**: No se permiten fotos y hay que guardar silencio.
            * **Estancias de Rafael**: No os perdáis 'La Escuela de Atenas'.
            * **Reserva**: Tened a mano el código `2L2NFFJ00000004GM`.
            * 🌐 [Web Oficial Museos](https://www.museivaticani.va)
            """
            abrir_ventana("Museos Vaticanos", info_vat, img1="https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Sistine_Chapel_Ceiling_01.jpg/800px-Sistine_Chapel_Ceiling_01.jpg")

    # 3. ALMUERZO EN PRATI
    c1, c2 = st.columns([0.6, 0.4])
    with c1: st.write("🕑 **14:30** | 🍝 Almuerzo (Zona Prati)")
    with c2:
        if st.button("🍕 Opciones", key="com_lun_1"):
            info_com = """
            **DÓNDE COMER CERCA:**
            1. **Pastasciutta**: Pasta fresca deliciosa a muy buen precio.
            🌐 [Web Oficial](https://www.pastasciuttaroma.it)
            
            2. **L'Isola della Pizza**: Excelente carne a la brasa y cocina romana.
            🌐 [Web Oficial](https://www.lisoladellapizza.com)
            """
            abrir_ventana("Almuerzo Vaticano", info_com)

    # 4. CASTEL SANT'ANGELO
    c1, c2 = st.columns([0.6, 0.4])
    with c1: st.write("🕑 **16:30** | 🏰 Castel Sant'Angelo")
    with c2:
        if st.button("🏰 Ver Guía", key="guia_lun_2"):
            info_cas = """
            **FORTALEZA Y REFUGIO:**
            * **El Ángel**: Arriba del todo veréis la estatua del Arcángel San Miguel.
            * **Vistas**: Subid a la terraza superior; para mí, es la mejor vista de la Cúpula de San Pedro.
            * 🌐 [Web Oficial](https://direzionemuseiroma.cultura.gov.it/museo-nazionale-di-castel-santangelo/)
            """
            abrir_ventana("Castel Sant'Angelo", info_cas, img1="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Castel_Sant%27Angelo_Rome.jpg/800px-Castel_Sant%27Angelo_Rome.jpg")

    # 5. PASEO RECOMENDADO
    c1, c2 = st.columns([0.6, 0.4])
    with c1: st.write("🕑 **18:00** | 🚶 Paseo Campo de' Fiori")
    with c2:
        if st.button("🗺️ Ver Ruta", key="ruta_lun"):
            info_ruta = """
            **EL PASEO PERFECTO AL ATARDECER:**
            1. **Puente Sant'Angelo**: Cruzad el río por el puente de los ángeles.
            2. **Via Giulia**: Caminad por esta calle histórica y señorial.
            3. **Campo de' Fiori**: Una plaza llena de vida.
            4. **Ponte Sisto**: Cruzad este puente peatonal hacia el Trastevere.
            """
            abrir_ventana("Paseo hacia Trastevere", info_ruta, img1="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/Campo_de%27_Fiori_after_the_market.jpg/800px-Campo_de%27_Fiori_after_the_market.jpg")

    # 6. CENA EN TRASTEVERE
    c1, c2 = st.columns([0.6, 0.4])
    with c1: st.write("🕑 **20:30** | 🍷 Cena en Trastevere")
    with c2:
        if st.button("🍷 Comidas", key="com_lun_2"):
            info_tras = """
            **NOCHE EN EL BARRIO MÁS VIVO:**
            1. **Tonnarello**: Muy famoso. Pasta en sartén. 
            🌐 [Web Oficial](https://tonnarello.it)
            
            2. **Da Enzo al 29**: Auténtica joya. Probad la 'Burrata' y la 'Carbonara'.
            🌐 [Web Oficial](https://www.daenzoal29.com/)
            """
            abrir_ventana("Cena Lunes", info_tras)

    # ==========================================
    # MARTES 3: La Roma Barroca
    # ==========================================
    st.markdown('<div class="highlight-day"><h1>📆 MARTES 3: La Roma Barroca</h1></div>', unsafe_allow_html=True)

    # 1. LOGÍSTICA Y DESAYUNO
    c1, c2 = st.columns([0.6, 0.4])
    with c1: st.write("🕑 **08:30** | ☕ Desayuno y Logística")
    with c2:
        if st.button("⚙️ Detalles", key="log_mar"):
            info_log_mar = """
            **DESAYUNO EN ESQUILINO:**
            * **Pasticceria Regoli**: Paco, el *Maritozzo* aquí es sagrado. 
            🌐 [Ver en TripAdvisor](https://www.tripadvisor.it/Restaurant_Review-g187791-d1840734-Reviews-Pasticceria_Regoli-Rome_Lazio.html)
            * **Panella**: Panadería artesana de lujo con terraza.
            🌐 [Web Oficial](https://www.panellaroma.com/)
            
            **TRASLADO AL CENTRO:**
            * **Bus 64 o 40**: Directo a 'Piazza Venezia'.
            """
            abrir_ventana("Logística Martes", info_log_mar)

    # 2. TREVI Y ESPAÑA
    c1, c2 = st.columns([0.6, 0.4])
    with c1: st.write("🕑 **10:00** | ⛲ Trevi / España")
    with c2:
        if st.button("📖 Ver Guía", key="guia_mar_1"):
            info_barroca = """
            **EL ESPLENDOR DE ROMA:**
            * **Fontana di Trevi**: Obra maestra de Nicola Salvi. Recordad tirar la moneda con la mano derecha sobre el hombro izquierdo.
            * **Piazza di España**: Sus 135 peldaños y la fuente de la Barcaccia de Bernini.
            """
            abrir_ventana("Trevi y España", info_barroca, img1="https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Fontana_di_Trevi_Front.jpg/800px-Fontana_di_Trevi_Front.jpg")

    # 3. ALMUERZO
    c1, c2 = st.columns([0.6, 0.4])
    with c1: st.write("🕑 **14:00** | 🍝 Almuerzo (Cantina)")
    with c2:
        if st.button("🍝 Ver Sitio", key="com_mar_1"):
            info_cantina = """
            **CANTINA E CUCINA:**
            Comida casera en un local con alma. 
            * **No os perdáis**: La focaccia y la Carbonara. El personal es famosamente amable.
            🌐 [Web Oficial](https://cantinaecucina.it)
            """
            abrir_ventana("Almuerzo Martes", info_cantina)

    # 4. PANTEÓN Y NAVONA
    c1, c2 = st.columns([0.6, 0.4])
    with c1: st.write("🕑 **16:30** | 🏛️ Panteón y Navona")
    with c2:
        if st.button("📖 Ver Guía", key="guia_mar_2"):
            info_pan = """
            **LUZ Y ARTE:**
            * **El Panteón**: Tumba de Rafael y de los reyes de Italia. 
            * 🎟️ **Entradas**: [Web Oficial Musei Italiani](https://portale.museiitaliani.it/b2c/#es/buyTicket/37823f66-f481-42a2-8947-f377a06a6c4c)
            * **Piazza Navona**: No olvidéis entrar en la iglesia de *Sant'Agnese in Agone*.
            """
            abrir_ventana("Panteón y Navona", info_pan, img1="https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Pantheon_Rome_2016.jpg/800px-Pantheon_Rome_2016.jpg")

    # 5. CENA ZONA NAVONA
    c1, c2 = st.columns([0.6, 0.4])
    with c1: st.write("🕑 **20:30** | 🍷 Cena Zona Navona")
    with c2:
        if st.button("🍷 Opciones", key="com_mar_2"):
            info_cena_mar = """
            **SABORES DE SIEMPRE:**
            1. **Cul de Sac**: Una experiencia para el paladar.
            🌐 [Web Oficial](https://www.enotecaculdesacroma.it/)
            2. **Mimi e Coco**: Pasta fresca y buena música ambiental.
            🌐 [Web Oficial](https://mimiecoco.com)
            """
            abrir_ventana("Cena Martes", info_cena_mar)

    # ==========================================
    # MIÉRCOLES 4: Borghese y Roma Imperial
    # ==========================================
    st.markdown('<div class="highlight-day"><h1>📆 MIÉRCOLES 4: Arte e Imperio</h1></div>', unsafe_allow_html=True)

    # 1. DESAYUNO
    c1, c2 = st.columns([0.6, 0.4])
    with c1: st.write("🕑 **09:00** | ☕ Desayuno (Esquilino)")
    with c2:
        if st.button("☕ Sitios", key="des_mie"):
            info_des_mie = """
            **DESAYUNO SICILIANO O MODERNO:**
            1. **Dagnino**: Sus *cannoli* son de otro planeta.
            🌐 [Web Oficial](https://www.dagnino.com/)
            2. **Santi Sebastiano e Valentino**: Para los amantes del buen pan.
            """
            abrir_ventana("Desayuno Miércoles", info_des_mie)

    # 2. GALERÍA BORGHESE
    c1, c2 = st.columns([0.6, 0.4])
    with c1: st.write("🕑 **12:00** | 🎨 Galería Borghese")
    with c2:
        if st.button("🎨 Ver Guía", key="guia_mie_1"):
            info_borg = """
            **LA COLECCIÓN PRIVADA MÁS BELLA:**
            * **Importante**: Hay que estar allí a las **11:30** (30 min antes).
            * **Bernini**: Buscad 'Apolo y Dafne'. Veréis cómo el mármol se convierte en piel.
            * **Caravaggio**: Sala dedicada a sus cuadros llenos de sombras y luces.
            * 🌐 [Web Oficial](https://galleriaborghese.beniculturali.it/)
            """
            abrir_ventana("Galería Borghese", info_borg, img1="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Apolo_y_Dafne_%28Bernini%29.jpg/800px-Apolo_y_Dafne_%28Bernini%29.jpg")

    # 3. TRASLADO AL CENTRO
    c1, c2 = st.columns([0.6, 0.4])
    with c1: st.write("🕑 **14:00** | 🚌 Traslado al Centro")
    with c2:
        if st.button("🚌 Logística", key="tr_mie_centro"):
            info_tr_centro = """
            **OPCIONES PARA BAJAR AL COLISEO:**
            * **Bus 160**: Desde parada S. Paolo Del Brasile hasta Piazza Venezia.
            * **Caminando**: 25 min bajando por Via Veneto.
            """
            abrir_ventana("Cómo bajar al centro", info_tr_centro)

    # 4. ALMUERZO COLISEO
    c1, c2 = st.columns([0.6, 0.4])
    with c1: st.write("🕑 **14:30** | 🍝 Almuerzo (Coliseo)")
    with c2:
        if st.button("🍝 Sitios", key="com_mie_1"):
            info_com_mie = """
            **CERCA DEL COLISEO:**
            1. **Hostaria al Gladiatore**: Vistas al anfiteatro.
            🌐 [Web Oficial](https://www.ristorantegladiatore.it/)
            2. **Trattoria Luzzi**: Muy auténtica y ruidosa. Lasaña buenísima.
            🌐 [Web Oficial](https://www.trattorialuzzi.it/)
            """
            abrir_ventana("Almuerzo Miércoles", info_com_mie)

    # 5. PASEO IMPERIAL
    c1, c2 = st.columns([0.6, 0.4])
    with c1: st.write("🕑 **18:00** | 🏟️ Roma Iluminada")
    with c2:
        if st.button("🏛️ Ver Guía", key="guia_mie_2"):
            info_iluminada = """
            **EL SUEÑO DE LOS CÉSARES:**
            * **El Mirador**: Subid a la Plaza del Campidoglio y asomaos por detrás al Foro Romano.
            * **Paseo**: Bajad por la *Via dei Fori Imperiali* hasta el Coliseo iluminado.
            """
            abrir_ventana("Roma Imperial", info_iluminada, img1="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Colosseum_at_night_2015.jpg/800px-Colosseum_at_night_2015.jpg")

    # 6. CENA FINAL
    c1, c2 = st.columns([0.6, 0.4])
    with c1: st.write("🕑 **21:00** | 🍝 Cena Final")
    with c2:
        if st.button("🍷 Detalles", key="com_mie_2"):
            info_cena_final = """
            **EL BROCHE DE ORO:**
            1. **Trattoria Vecchia Roma**: Pedid los *Amatriciana Flambé* (pasta en rueda de queso).
            🌐 [Web Oficial](https://www.trattoriavecchiaroma.it/)
            2. **Trattoria Monti**: Cocina regional de altísimo nivel.
            """
            abrir_ventana
