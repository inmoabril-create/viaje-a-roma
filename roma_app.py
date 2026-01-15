import streamlit as st
from datetime import datetime

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Roma 2026", page_icon="🇮🇹", layout="centered")

# --- ESTILOS CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #Fdfcf0; }
    .highlight-day {
        background-color: #CE1126;
        color: white;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        margin-top: 30px;
        margin-bottom: 25px;
    }
    div.stButton > button {
        width: 100%; padding: 12px; border-radius: 10px;
        border: 2px solid #008C45; color: #008C45;
        font-weight: bold; background-color: white;
    }
    div.stButton > button:hover { background-color: #008C45; color: white; }
    </style>
""", unsafe_allow_html=True)

# --- FUNCIÓN DE VENTANA MODAL ---


@st.dialog("🇮🇹 DETALLES DEL VIAJE", width="large")
def abrir_ventana(titulo, texto_markdown, img1=None, pie1=None):
    st.markdown(f"## {titulo}")
    if img1:
        st.image(img1, caption=pie1, use_container_width=True)
    st.markdown(texto_markdown)


# --- PORTADA Y CONTADOR (FEBRERO 2026) ---
st.title("🇮🇹 Roma 2026")
st.markdown("### Paco & Mari Trini")

# Fecha de inicio real: 1 de febrero de 2026
fecha_viaje = datetime(2026, 2, 1)
ahora = datetime.now()
dias_restantes = (fecha_viaje - ahora).days

if dias_restantes > 0:
    st.info(
        f"⏳ ¡Solo faltan **{dias_restantes}** días para vuestro gran viaje!")
elif dias_restantes == 0:
    st.success("🎉 ¡EL VIAJE EMPIEZA HOY! 🎉")
else:
    st.markdown("### ✈️ ¡A disfrutar de Roma! 🇮🇹")

# ==========================================
# DOMINGO 1: Benvenuti
# ==========================================
st.markdown('<div class="highlight-day"><h1>📆 DOMINGO 1: Benvenuti</h1></div>',
            unsafe_allow_html=True)

# 1. TRASLADO
c1, c2 = st.columns([0.6, 0.4])
with c1:
    st.write("🕑 **14:00** | 🛬 Traslado Aeropuerto ➔ Hotel")
with c2:
    if st.button("🚌 Info", key="t_dom"):
        info_t = """
        **OPCIONES PARA LLEGAR AL CENTRO:**
        * **🚆 Tren Leonardo Express**: 14€/pax. Directo a Termini (32 min). 
        * **🚌 Autobús (TAM/SIT)**: ~7€/pax. Tarda 50-60 min.
        * **🚖 Taxi**: Tarifa fija 50€.
        
        💡 **Anras recomienda**: Paco, el tren es el más rápido y fiable.
        """
        abrir_ventana("Transporte al Centro", info_t)

# 2. ALMUERZO
c1, c2 = st.columns([0.6, 0.4])
with c1:
    st.write("🕑 **15:30** | 🍕 Almuerzo")
with c2:
    if st.button("🍴 Opciones", key="l_dom"):
        info_l = """
        **OPCIONES DE ALMUERZO:**
        1. **La Gallina Bianca**: Cocina tradicional (Aprox. 50€).
           🌐 [Web traducida](https://translate.google.com/translate?sl=it&tl=es&u=http://www.lagallinabiancaroma.it)
        2. **Mercato Centrale**: Puestos artesanos en Termini.
           🌐 [Web traducida](https://translate.google.com/translate?sl=it&tl=es&u=https://www.mercatocentrale.it/roma/)
        """
        abrir_ventana("Almuerzo", info_l, img1="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Roma_Termini_Mercato_Centrale.jpg/800px-Roma_Termini_Mercato_Centrale.jpg", pie1="Mercato Centrale")

# 3. SANTA MARIA MAGGIORE
c1, c2 = st.columns([0.6, 0.4])
with c1:
    st.write("🕑 **17:30** | ⛪ Sta. Maria Maggiore")
with c2:
    if st.button("📖 Guía", key="sm_dom"):
        abrir_ventana("Santa Maria Maggiore",
                      "Mosaicos del siglo V y el famoso techo de oro. [Web Oficial](https://www.vatican.va/various/basiliche/sm_maggiore/index_it.html)")

# 4. SAN PIETRO IN VINCOLI
c1, c2 = st.columns([0.6, 0.4])
with c1:
    st.write("🕑 **18:30** | ⛪ San Pietro in Vincoli (Moisés)")
with c2:
    if st.button("📖 Guía", key="mo_dom"):
        abrir_ventana("El Moisés", "Obra maestra de Miguel Ángel. [Web Info](https://translate.google.com/translate?sl=it&tl=es&u=https://www.turismoroma.it/it/luoghi/basilica-di-san-pietro-vincoli)",
                      img1="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Mois%C3%A9s_de_Miguel_%C3%81ngel_en_San_Pietro_in_Vincoli.jpg/800px-Mois%C3%A9s_de_Miguel_%C3%81ngel_en_San_Pietro_in_Vincoli.jpg")

# 5. CENA MONTI
c1, c2 = st.columns([0.6, 0.4])
with c1:
    st.write("🕑 **21:00** | 🍷 Cena (Barrio Monti)")
with c2:
    if st.button("🍷 Comidas", key="ce_dom"):
        info_ce = "🍴 **Ai Tre Scalini** (Aprox. 50€). Barrio bohemio y vinería mítica.\n🌐 [Web traducida](https://translate.google.com/translate?sl=it&tl=es&u=http://www.aitrescalini.org)"
        abrir_ventana("Cena en Monti", info_ce,
                      img1="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Via_Panisperna_-_Rione_Monti.jpg/800px-Via_Panisperna_-_Rione_Monti.jpg", pie1="Barrio Monti")

# --- AJUSTE DE CSS PARA SEPARAR MÁS LAS FILAS Y BOTONES ---
st.markdown("""
    <style>
    div.stButton > button {
        padding: 5px 10px !important;
        font-size: 14px !important;
        height: auto !important;
    }
    /* Añade un poco de espacio extra entre las filas de Streamlit */
    [data-testid="column"] {
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# LUNES 2: El Corazón de Roma (Vaticano y Trastevere)
# ==========================================
st.markdown('<div class="highlight-day"><h1>📆 LUNES 2: El Corazón de Roma</h1></div>',
            unsafe_allow_html=True)

# 1. TRASLADO AL VATICANO
c1, c2 = st.columns([0.7, 0.3])
with c1:
    st.write("🕑 **07:15** | 🚌 **Traslado al Vaticano** (Desde Hotel)")
with c2:
    if st.button("🚇 Opciones", key="tr_lun_1"):
        info_tr = """
        **DESDE ZONA TERMINI/ESQUILINO:**
        1. **METRO A (Roja)**: Dirección 'Battistini' hasta **Ottaviano**. (15 min).
        2. **BUS 40 (Express)**: Hasta 'Traspontina'. (25 min).
        3. **TAXI/UBER**: Unos 15-18€. (15 min).
        
        **Billete**: 1,50€. Usad **Tap & Go** (tarjeta contactless directamente en el torno).
        """
        abrir_ventana("Traslado al Vaticano", info_tr)

# 2. DESAYUNO
c1, c2 = st.columns([0.7, 0.3])
with c1:
    st.write("🕑 **08:00** | ☕ **Desayuno en Prati** (Cerca Vaticano)")
with c2:
    if st.button("☕ Sitios", key="des_lun"):
        info_des = """
        **OPCIONES:**
        1. **Sciascia Caffè 1919**: Café histórico, pedid el cappuccino con chocolate. [Web](https://www.sciasciacaffe1919.it)
        2. **Bar Latteria Giuliani**: Auténtico y rápido para un cornetto de pie.
        """
        abrir_ventana("Desayuno Lunes", info_des)

st.write("---")  # Separador visual

# 3. MUSEOS VATICANOS
c1, c2 = st.columns([0.7, 0.3])
with c1:
    st.write("🕑 **09:00** | 🏛️ **MUSEOS VATICANOS**")
with c2:
    if st.button("📖 Guía", key="guia_lun_1"):
        info_vat = """
        **VISITA AL DETALLE:**
        Estáis en uno de los complejos museísticos más importantes de la historia.
        * **Imprescindibles**: Las **Estancias de Rafael** (La Escuela de Atenas) y la **Capilla Sixtina**. 
        * **Aviso**: Silencio y nada de fotos en la Sixtina.
        * **Reserva**: Código `2L2NFFJ00000004GM`.
        * 🌐 [Web Oficial Musei Vaticani](https://www.museivaticani.va)
        """
        abrir_ventana("Vaticano", info_vat,
                      img1="https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Sistine_Chapel_Ceiling_01.jpg/800px-Sistine_Chapel_Ceiling_01.jpg")

# 4. ALMUERZO
c1, c2 = st.columns([0.7, 0.3])
with c1:
    st.write("🕑 **14:30** | 🍝 **Almuerzo en Prati**")
with c2:
    if st.button("🍕 Sitios", key="com_lun_1"):
        info_com = """
        **OPCIONES:**
        1. **Pastasciutta**: Pasta fresca artesanal rápida. "La Carbonara más famosa de la zona". [Web](https://www.pastasciuttaroma.it)
        2. **L'Isola della Pizza**: Restaurante sentado. Cocina romana y carnes. [Web](https://www.lisoladellapizza.com)
        """
        abrir_ventana("Almuerzo Vaticano", info_com)

# 5. CASTEL SANT'ANGELO
c1, c2 = st.columns([0.7, 0.3])
with c1:
    st.write("🕑 **16:30** | 🏰 **Castel Sant'Angelo**")
with c2:
    if st.button("🏰 Guía", key="guia_lun_2"):
        info_cas = """
        **HISTORIA VIVA:**
        De mausoleo de Adriano a fortaleza papal. 
        * **No os perdáis**: El *Passetto di Borgo* (el pasadizo secreto del Papa) y la terraza superior. 
        * **Vistas**: Desde arriba veréis la cúpula de San Pedro como en ninguna otra parte.
        * 🌐 [Web Oficial](https://direzionemuseiroma.cultura.gov.it/museo-nazionale-di-castel-santangelo/)
        """
        abrir_ventana("Castel Sant'Angelo", info_cas)

st.write("---")

# 6. TRASLADO A TRASTEVERE
c1, c2 = st.columns([0.7, 0.3])
with c1:
    st.write("🕑 **19:30** | 🚌 **Traslado a Trastevere**")
with c2:
    if st.button("🚌 Opciones", key="tr_lun_2"):
        info_tr2 = """
        **DESDE EL CASTILLO:**
        1. **A PIE**: Paseo de 20 min por el Lungotevere (la orilla del río). Muy recomendado al atardecer.
        2. **BUS 23/280**: Parada 'Lgt Sanzio/Filipperi'. (1,50€ con Tap & Go).
        3. **TAXI**: Unos 10-12€.
        """
        abrir_ventana("Traslado a Trastevere", info_tr2)

# 7. CENA TRASTEVERE
c1, c2 = st.columns([0.7, 0.3])
with c1:
    st.write("🕑 **20:30** | 🍷 **Cena en Trastevere**")
with c2:
    if st.button("🍷 Sitios", key="com_lun_2"):
        abrir_ventana(
            "Cena", "1. **Tonnarello** (Muy animado, pasta en sartén) [Web](https://tonnarello.it) \n2. **Da Enzo al 29** (Auténtica trattoria) [Web](https://www.daenzoal29.com/)")


# ==========================================
# MARTES 3: La Roma Barroca
# ==========================================
st.markdown('<div class="highlight-day"><h1>📆 MARTES 3: La Roma Barroca</h1></div>',
            unsafe_allow_html=True)

# 1. LOGÍSTICA Y DESAYUNO
c1, c2 = st.columns([0.7, 0.3])
with c1:
    st.write("🕑 **08:30** | ☕ **Logística y Desayuno cerca Hotel**")
with c2:
    if st.button("⚙️ Detalles", key="log_mar"):
        info_des_mar = """
        **DESAYUNO EN ESQUILINO:**
        1. **Regoli Pasticceria**: Una leyenda desde 1916. Es de obligada visita para probar el auténtico *Maritozzo* romano (bollo tierno relleno de nata montada artesanal).
           🌐 [Ver en TripAdvisor](https://www.tripadvisor.es/Restaurant_Review-g187791-d1102555-Reviews-Pasticceria_Regoli-Rome_Lazio.html)
        2. **Panella**: Panadería artesana de gran calidad. Tienen una terraza magnífica donde disfrutar de un café de especialidad y bollería de alto nivel.
           🌐 [Web Oficial](https://www.panellaroma.com/)
        
        **TRASLADO AL CENTRO:**
        * **Bus 64 o 40** desde la zona de Termini hasta 'Piazza Venezia' o 'Largo Argentina'.
        * **Pago**: Sistema **Tap & Go** (1,50€ pasando la tarjeta contactless o el móvil directamente por el lector del bus).
        """
        abrir_ventana("Logística Martes", info_des_mar)

# 2. RUTA BARROCA I
c1, c2 = st.columns([0.7, 0.3])
with c1:
    st.write("🕑 **10:00** | ⛲ **Ruta Barroca (Trevi / España)**")
with c2:
    if st.button("📖 Guía", key="guia_mar_1"):
        info_barroca = """
        **EL ESPLENDOR DEL BARROCO ROMANO:**
        
        * **Fontana di Trevi**: Obra maestra de Nicola Salvi. Representa a Neptuno domando las aguas. 
          * *Tradición*: Debéis tirar una moneda de espaldas con la mano derecha sobre el hombro izquierdo. Dice la leyenda que una moneda asegura el regreso a Roma, dos un romance y tres un matrimonio.
          * *Dato curioso*: El gran bloque de piedra a la derecha, apodado el 'As de Copas', se puso estratégicamente para que un barbero que no paraba de criticar las obras no pudiera verlas desde su barbería.
        
        * **Piazza di España**: Famosa por su monumental escalinata de 135 peldaños. 
          * *La Barcaccia*: A los pies de la escalera se encuentra la fuente de Pietro Bernini. Tiene forma de barco naufragado porque, tras una gran inundación del Tíber en 1598, un bote llegó hasta aquí.
        
        * **Paseo**: Podéis recorrer la *Via Condotti*, la calle más lujosa de Roma, que nace justo frente a la plaza.
        """
        abrir_ventana("Ruta: Trevi y España", info_barroca,
                      img1="https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Fontana_di_Trevi_Front.jpg/800px-Fontana_di_Trevi_Front.jpg")

# 3. ALMUERZO
c1, c2 = st.columns([0.7, 0.3])
with c1:
    st.write("🕑 **14:00** | 🍝 **Almuerzo (CANTINA E CUCINA)**")
with c2:
    if st.button("🍝 Reserva", key="com_mar_1"):
        abrir_ventana(
            "Almuerzo", "**CANTINA E CUCINA**: Local con muchísima personalidad y un servicio muy alegre. \n* **Imprescindible**: Sus albóndigas caseras y su Tiramisú. Es uno de los restaurantes más queridos por su relación calidad-precio en el centro. \n🌐 [Web Oficial](https://cantinaecucina.it)")

# 4. RUTA BARROCA II
c1, c2 = st.columns([0.7, 0.3])
with c1:
    st.write("🕑 **16:30** | 🏛️ **Panteón y Plaza Navona**")
with c2:
    if st.button("📖 Guía", key="guia_mar_2"):
        info_panteon_navona = """
        **LA PERFECCIÓN DE LA ANTIGÜEDAD Y EL BARROCO:**
        
        * **Panteón de Agripa**: El edificio de la Antigua Roma mejor conservado del mundo. 
          * *La Cúpula*: Es un milagro de la ingeniería; 2.000 años después sigue siendo la cúpula de hormigón no armado más grande del planeta.
          * *El Óculo*: El agujero en el techo es la única fuente de luz. Simboliza el contacto con la divinidad. Si llueve, el suelo (ligeramente curvado) drena el agua por 22 orificios casi invisibles.
          * *Tumbas*: No olvidéis visitar la tumba del pintor Rafael Sanzio.
        
        * **Piazza Navona**: Sigue fielmente la forma del antiguo Estadio de Domiciano sobre el que se construyó.
          * *Fuente de los Cuatro Ríos*: Obra cumbre de Bernini. Las estatuas representan los cuatro grandes ríos de la época: Danubio, Ganges, Nilo (con la cara tapada porque no se conocía su origen) y el Río de la Plata.
          * *Rivalidad*: La fachada de la iglesia de *Sant'Agnese in Agone* es obra de Borromini. La leyenda dice que las estatuas de Bernini se tapan la cara para no ver "el horror" de la obra de su rival.
        """
        abrir_ventana("Panteón y Plaza Navona", info_panteon_navona,
                      img1="https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Pantheon_Rome_2016.jpg/800px-Pantheon_Rome_2016.jpg")

# 5. CENA
c1, c2 = st.columns([0.7, 0.3])
with c1:
    st.write("🕑 **20:30** | 🍷 **Cena (Zona Navona)**")
with c2:
    if st.button("🍷 Sitios", key="com_mar_2"):
        info_cena_navona = """
        **PARA CENAR CERCA DE NAVONA:**
        
        1. **Cul de Sac**: Una de las enotecas más antiguas y respetadas. Es un paraíso para los amantes del vino y los platos de caza o quesos italianos.
           🌐 [Web Oficial](https://www.enotecaculdesacroma.it/)
           
        2. **Mimi e Coco**: Ideal si buscáis algo un poco más dinámico. Excelente pasta y una selección de vinos por copas fantástica.
           🌐 [Web Oficial](https://mimiecoco.com)
        """
        abrir_ventana("Cena en Navona", info_cena_navona)


# ==========================================
# MIÉRCOLES 4: Galería Borghese e Imperial
# ==========================================
st.markdown('<div class="highlight-day"><h1>📆 MIÉRCOLES 4: Borghese e Imperial</h1></div>',
            unsafe_allow_html=True)

# 1. DESAYUNO
c1, c2 = st.columns([0.7, 0.3])
with c1:
    st.write("🕑 **09:00** | ☕ **Desayuno cerca Hotel** (Esquilino)")
with c2:
    if st.button("☕ Sitios", key="des_mie"):
        info_des_mie = """
        **OPCIONES DE DESAYUNO (Zona Esquilino):**
        1. **Dagnino**: Un rincón histórico de Sicilia en Roma. Sus *cannoli* y *cassatas* son legendarios.
           🌐 [Web Oficial](https://www.dagnino.com/)
        2. **Santi Sebastiano e Valentino**: Panadería artesana de autor con un ambiente moderno y excelente café.
           🌐 [Tripadvisor](https://https://www.tripadvisor.it/Restaurant_Review-g187791-d10147828-Reviews-Santi_Sebastiano_e_Valentino_Pane_e_Mangiare-Rome_Lazio.html)
        """
        abrir_ventana("Desayuno Miércoles", info_des_mie)

# 2. TRASLADO A BORGHESE
c1, c2 = st.columns([0.7, 0.3])
with c1:
    st.write("🕑 **10:45** | 🚌 **Traslado a Galería Borghese**")
with c2:
    if st.button("🚌 Opciones", key="tr_mie_1"):
        info_tr_mie = """
        **TRASLADO AL MUSEO (Desde Hotel):**
        * **A PIE**: Unos 25-30 min caminando hacia el norte por la zona de Via Veneto.
        * **AUTOBÚS**: **Línea 910 o 360** desde Termini hasta la parada 'Pinciana/Museo Borghese' (aprox. 15 min).
        * **TAXI**: Unos 10-12€ (muy recomendable para asegurar la llegada a las 11:30 para el control).
        * **Precio Bus**: 1,50€ (Usad Tap & Go).
        """
        abrir_ventana("Traslado a Borghese", info_tr_mie)

# 3. GALERÍA BORGHESE
c1, c2 = st.columns([0.7, 0.3])
with c1:
    st.write("🕑 **12:00** | 🎨 **GALERÍA BORGHESE (Visita Concertada)**")
with c2:
    if st.button("🎨 Guía", key="guia_mie_1"):
        info_borg = """
        **VISITA MAESTRA:**
        * **Importante**: Hay que estar 30 minutos antes para pasar el control de seguridad y dejar todo en el guardarropa obligatorio.
        * **Bernini**: No os perdáis 'Apolo y Dafne' y 'El Rapto de Proserpina'. La delicadeza del mármol es irreal.
        * **Caravaggio**: Poseen una de las mejores salas del mundo dedicadas al pintor.
        * 🌐 [Web Oficial Galería](https://galleriaborghese.beniculturali.it/)
        """
        abrir_ventana("Galería Borghese", info_borg)

st.write("---")

# 4. TRASLADO AL CENTRO (TRAS LA GALERÍA)
c1, c2 = st.columns([0.7, 0.3])
with c1:
    st.write("🕑 **14:00** | 🚶 **Traslado al Centro / Zona Monti**")
with c2:
    if st.button("🚌 Opciones", key="tr_mie_2"):
        info_tr_centro = """
        **DE LA GALERÍA AL CENTRO/MONTI:**
        * **A PIE**: Unos 25-30 min bajando por los jardines hacia la Plaza de España y luego hacia el centro.
        * **AUTOBÚS**: **Línea 160** desde 'San Paolo del Brasile' hasta 'Largo Chigi' (cerca de Trevi) o **Metro A** en Plaza de España hasta Termini/Cavour.
        * **Precio**: 1,50€ con Tap & Go.
        """
        abrir_ventana("Traslado al Centro", info_tr_centro)

# 5. ALMUERZO
c1, c2 = st.columns([0.7, 0.3])
with c1:
    st.write("🕑 **14:30** | 🍝 **Almuerzo (Dos Opciones)**")
with c2:
    if st.button("🍝 Sitios", key="com_mie_1"):
        info_com_mie = """
        **OPCIONES PARA COMER:**
        1. **Hostaria al Gladiatore**: Situado estratégicamente con vistas al Coliseo. Ideal para disfrutar de la estampa mientras coméis.
           🌐 [Web Oficial](https://www.ristorantegladiatore.it//)
        2. **Trattoria Luzzi**: Un clásico romano total. Ruidoso, auténtico y económico. Su pizza y su lasaña al horno son famosas entre los locales.
           🌐 [Web Oficial](https://www.trattorialuzzi.it/)
        """
        abrir_ventana("Almuerzo Miércoles", info_com_mie)

# 6. COLISEO ILUMINADO
c1, c2 = st.columns([0.7, 0.3])
with c1:
    st.write("🕑 **16:00** | 🏟️ **Coliseo y Foros (Iluminados)**")
with c2:
    if st.button("🏛️ Guía", key="guia_mie_2"):
        info_iluminada = """
        **LA MAGIA DE LA ROMA NOCTURNA:**
        
        Roma se transforma completamente cuando se encienden sus focos dorados. Este paseo es, posiblemente, el más fotogénico del viaje.
        
        * **Recorrido Sugerido**: Empezad en la **Piazza Venezia** (el Altare della Patria parece brillar). Subid por la escalinata de la Cordonata de Miguel Ángel hasta la Plaza del **Campidoglio**.
        * **La Vista Secreta**: Id a la parte trasera de la plaza (detrás del Palacio Senatorio). Desde allí tendréis la mejor vista del **Foro Romano iluminado** desde arriba. Es sobrecogedor.
        * **Via dei Fori Imperiali**: Bajad y caminad por esta avenida hacia el **Coliseo**. La iluminación resalta los arcos y la profundidad del anfiteatro de una forma que el sol no logra captar.
        * **Consejo**: Fijaos en el **Mercado de Trajano**; sus ladrillos rojos cobran un tono espectacular bajo los focos.
        """
        abrir_ventana("Roma Iluminada", info_iluminada)

st.write("---")

# 7. CENA DESPEDIDA
c1, c2 = st.columns([0.7, 0.3])
with c1:
    st.write("🕑 **21:00** | 🍝 **Cena Despedida (Vecchia Roma)**")
with c2:
    if st.button("🍷 Detalles", key="com_mie_2"):
        info_cena_final = """
        **EL BROCHE FINAL:**
        1. **Trattoria Vecchia Roma**: Tenéis que pedir los *Amatriciana Flambé* (pasta terminada en rueda de queso pecorino con fuego). Es la despedida perfecta. 
           🌐 [Web Oficial](https://www.trattoriavecchiaroma.it/)
        2. **Trattoria Monti**: Por si preferís una última noche más íntima con cocina regional de altísimo nivel. 
           🌐 [Ver en TripAdvisor](https://www.tripadvisor.es/Restaurant_Review-g187791-d793216-Reviews-Trattoria_Monti-Rome_Lazio.html)
        """
        abrir_ventana("Cena de Despedida", info_cena_final)


# ==========================================
# JUEVES: El Regreso
# ==========================================
st.markdown('<div class="highlight-day"><h1>📆 JUEVES: Fin del Viaje</h1></div>',
            unsafe_allow_html=True)

# 1. DESPERTADOR
c1, c2 = st.columns([0.7, 0.3])
with c1:
    st.write("🕑 **03:00** | ⏰ **DESPERTADOR (Vuelo 06:40)**")
with c2:
    if st.button("⚙️ Logística", key="log_jue"):
        abrir_ventana("Logística Salida",
                      "Ducha rápida, revisión de maletas y salida puntual. El aeropuerto de Fiumicino requiere estar al menos 2 horas antes.")

# 2. TRASLADO AEROPUERTO
c1, c2 = st.columns([0.7, 0.3])
with c1:
    st.write("🕑 **03:45** | 🛫 **Traslado al Aeropuerto**")
with c2:
    if st.button("🚕 Transporte", key="tr_jue"):
        info_aeropuerto = """
        **LOGÍSTICA AL AEROPUERTO (FCO):**
        * **TAXI / UBER**: A esta hora es la única opción viable y segura. 
        * **Precio Fijo**: El taxi oficial desde el centro (dentro de las murallas aurelianas) tiene un precio cerrado de **50€** hasta Fiumicino.
        * **Tiempo**: Unos 30-35 min sin tráfico.
        * **Consejo**: Podéis pedirlo por la App **'Free Now'** o reservar uno el día anterior en la recepción del hotel.
        """
        abrir_ventana("Traslado al Aeropuerto", info_aeropuerto)

st.markdown("---")
st.caption("Dossier Interactivo Roma 2026 - Paco & Trini")
