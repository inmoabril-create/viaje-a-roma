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
    </style>
""", unsafe_allow_html=True)

@st.dialog("🇮🇹 DETALLES")
def abrir_ventana(titulo, texto_markdown, img1=None, pie1=None):
    st.markdown(f"# {titulo}")
    if img1:
        st.image(img1, caption=pie1, use_container_width=True)
    st.markdown(texto_markdown)

# --- PORTADA ---
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

st.write("---")
st.caption("Guía Roma 2026 - Paco & Trini")

# ==========================================
# LUNES 2: El Corazón de Roma (Vaticano y Trastevere)
# ==========================================
st.markdown('<div class="highlight-day"><h1>📆 LUNES 2: El Corazón de Roma</h1></div>', unsafe_allow_html=True)

# 1. TRASLADO AL VATICANO
c1, c2 = st.columns([0.6, 0.4])
with c1: 
    st.write("🕑 **07:15** | 🚌 Traslado al Vaticano")
with c2:
    if st.button("🚇 Logística", key="tr_lun_1"):
        info_tr = """
        **CÓMO LLEGAR DESDE EL HOTEL:**
        * **Metro Línea A (Roja)**: Lo más directo. Bajad en la parada **Ottaviano**.
        * **Taxi**: Tardará unos 15-20 min y os costará unos 15€.
        * **Tap & Go**: Podéis pagar el metro apoyando vuestra tarjeta bancaria directamente en el torno.
        """
        abrir_ventana("Hacia el Vaticano", info_tr)




# 2. MUSEOS VATICANOS Y CAPILLA SIXTINA
c1, c2 = st.columns([0.6, 0.4])
with c1: 
    st.write("🕑 **09:00** | 🏛️ Museos Vaticanos")
with c2:
    if st.button("📖 Ver Guía", key="guia_lun_1"):
        info_vat = """
        **EL TESORO DEL PAPA:**
        Estáis ante una de las colecciones de arte más grandes del mundo. 
        
        * **La Capilla Sixtina**: Obra cumbre de Miguel Ángel. El techo narra el Génesis y el testero el Juicio Final. **Importante**: No se permiten fotos y hay que guardar silencio.
        * **Estancias de Rafael**: No os perdáis 'La Escuela de Atenas', donde aparecen los grandes filósofos con caras de artistas de la época (Leonardo, Miguel Ángel...).
        * **Galería de los Mapas**: Un pasillo de 120 metros con mapas pintados al fresco que es sencillamente espectacular.
        * **Reserva**: Tened a mano el código `2L2NFFJ00000004GM`.
        
        🌐 [Web Oficial Museos](https://www.museivaticani.va)
        """
        abrir_ventana("Museos Vaticanos", info_vat, img1="https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Sistine_Chapel_Ceiling_01.jpg/800px-Sistine_Chapel_Ceiling_01.jpg")

# 3. ALMUERZO EN PRATI
c1, c2 = st.columns([0.6, 0.4])
with c1: 
    st.write("🕑 **14:30** | 🍝 Almuerzo (Zona Prati)")
with c2:
    if st.button("🍕 Opciones", key="com_lun_1"):
        info_com = """
        **DÓNDE COMER CERCA:**
        1. **Pastasciutta**: Ideal si queréis algo rápido pero artesano. Pasta fresca deliciosa a muy buen precio.
        🌐 [Web Oficial](https://www.pastasciuttaroma.it)
        
        2. **L'Isola della Pizza**: Un sitio de toda la vida. Excelente carne a la brasa y cocina romana sentados tranquilos.
        🌐 [Web Oficial](https://www.lisoladellapizza.com)
        """
        abrir_ventana("Almuerzo Vaticano", info_com)

# 4. CASTEL SANT'ANGELO
c1, c2 = st.columns([0.6, 0.4])
with c1: 
    st.write("🕑 **16:30** | 🏰 Castel Sant'Angelo")
with c2:
    if st.button("🏰 Ver Guía", key="guia_lun_2"):
        info_cas = """
        **FORTALEZA Y REFUGIO:**
        Este castillo ha sido mausoleo, cárcel y palacio de los Papas.
        
        * **El Ángel**: Arriba del todo veréis la estatua del Arcángel San Miguel envainando la espada, que simboliza el fin de una antigua peste.
        * **El Passetto**: Existe un pasadizo amurallado que conecta el Vaticano con el castillo para que el Papa pudiera escapar en caso de ataque.
        * **Vistas**: Subid a la terraza superior; para mí, es la mejor vista de la Cúpula de San Pedro de toda Roma.
        
        🌐 [Web Oficial](https://direzionemuseiroma.cultura.gov.it/museo-nazionale-di-castel-santangelo/)
        """
        abrir_ventana("Castel Sant'Angelo", info_cas, img1="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Castel_Sant%27Angelo_Rome.jpg/800px-Castel_Sant%27Angelo_Rome.jpg")

# 5. PASEO RECOMENDADO (Entre Castillo y Cena)
c1, c2 = st.columns([0.6, 0.4])
with c1: 
    st.write("🕑 **18:00** | 🚶 Paseo Campo de' Fiori")
with c2:
    if st.button("🗺️ Ver Ruta", key="ruta_lun"):
        info_ruta = """
        **EL PASEO PERFECTO AL ATARDECER:**
        Como tenéis tiempo antes de cenar, os recomiendo este camino a pie (15-20 min):
        
        1. **Puente Sant'Angelo**: Cruzad el río por el puente de los ángeles.
        2. **Via Giulia**: Caminad por esta calle histórica y señorial.
        3. **Campo de' Fiori**: Una plaza llena de vida. Es el sitio ideal para sentarse en una terraza a ver la gente pasar y tomar un aperitivo.
        4. **Ponte Sisto**: Cruzad este puente peatonal; al otro lado ya estaréis en las calles mágicas del Trastevere.
        
        💡 **Consejo de Anrras**: No tengáis prisa, disfrutad de las luces de las farolas reflejadas en el Tíber.
        """
        abrir_ventana("Paseo hacia Trastevere", info_ruta, img1="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/Campo_de%27_Fiori_after_the_market.jpg/800px-Campo_de%27_Fiori_after_the_market.jpg")

# 6. CENA EN TRASTEVERE (Ajustada a las 20:30 para ir sin prisas)
c1, c2 = st.columns([0.6, 0.4])
with c1: 
    st.write("🕑 **20:30** | 🍷 Cena en Trastevere")
with c2:
    if st.button("🍷 Comidas", key="com_lun_2"):
        info_tras = """
        **NOCHE EN EL BARRIO MÁS VIVO:**
        1. **Tonnarello**: Muy famoso. Pasta en sartén de aluminio. 
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
with c1: 
    st.write("🕑 **08:30** | ☕ Desayuno y Logística")
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
        * **Pago**: Sistema Tap & Go (1,50€).
        """
        abrir_ventana("Logística Martes", info_log_mar)

# 2. RUTA BARROCA I (TREVI Y ESPAÑA)
c1, c2 = st.columns([0.6, 0.4])
with c1: 
    st.write("🕑 **10:00** | ⛲ Trevi / España")
with c2:
    if st.button("📖 Ver Guía", key="guia_mar_1"):
        info_barroca = """
        **EL ESPLENDOR DE ROMA:**
        * **Fontana di Trevi**: Obra maestra de Nicola Salvi. Recordad tirar la moneda con la mano derecha sobre el hombro izquierdo.
        * **Piazza di España**: Sus 135 peldaños y la fuente de la Barcaccia de Bernini.
        * **Curiosidad**: En la Plaza de España está el McDonald's más elegante del mundo (por si queréis cotillear el interior).
        """
        abrir_ventana("Trevi y España", info_barroca, img1="https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Fontana_di_Trevi_Front.jpg/800px-Fontana_di_Trevi_Front.jpg")

# 3. ALMUERZO (CANTINA E CUCINA)
c1, c2 = st.columns([0.6, 0.4])
with c1: 
    st.write("🕑 **14:00** | 🍝 Almuerzo (Cantina e Cucina)")
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
with c1: 
    st.write("🕑 **16:30** | 🏛️ Panteón y Navona")
with c2:
    if st.button("📖 Ver Guía", key="guia_mar_2"):
        info_pan = """
        **LUZ Y ARTE:**
        * **El Panteón**: Tumba de Rafael y de los reyes de Italia. 
        * 🎟️ **Entradas**: [Web Oficial Musei Italiani](https://portale.museiitaliani.it/b2c/#es/buyTicket/37823f66-f481-42a2-8947-f377a06a6c4c)
        * **Piazza Navona**: No olvidéis entrar en la iglesia de *Sant'Agnese in Agone* (es gratis y preciosa).
        """
        abrir_ventana("Panteón y Navona", info_pan, img1="https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Pantheon_Rome_2016.jpg/800px-Pantheon_Rome_2016.jpg")

# 5. CENA ZONA NAVONA
c1, c2 = st.columns([0.6, 0.4])
with c1: 
    st.write("🕑 **20:30** | 🍷 Cena Zona Navona")
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

# 1. DESAYUNO CERCA DEL HOTEL
c1, c2 = st.columns([0.6, 0.4])
with c1: 
    st.write("🕑 **09:00** | ☕ Desayuno (Esquilino)")
with c2:
    if st.button("☕ Sitios", key="des_mie"):
        info_des_mie = """
        **DESAYUNO SICILIANO O MODERNO:**
        1. **Dagnino**: Un pedazo de Sicilia en Roma. Sus *cannoli* son de otro planeta.
        🌐 [Web Oficial](https://www.dagnino.com/)
        2. **Santi Sebastiano e Valentino**: Para los amantes del buen pan y el café.
        🌐 [Ver en TripAdvisor](https://www.tripadvisor.es/Restaurant_Review-g187791-d10147828-Reviews-Santi_Sebastiano_e_Valentino-Rome_Lazio.html)
        """
        abrir_ventana("Desayuno Miércoles", info_des_mie)

# 2. TRASLADO Y GALERÍA BORGHESE
c1, c2 = st.columns([0.6, 0.4])
with c1: 
    st.write("🕑 **12:00** | 🎨 Galería Borghese")
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

# 3. ALMUERZO ZONA COLISEO
c1, c2 = st.columns([0.6, 0.4])
with c1: 
    st.write("🕑 **14:30** | 🍝 Almuerzo (Zona Imperial)")
with c2:
    if st.button("🍝 Sitios", key="com_mie_1"):
        info_com_mie = """
        **CERCA DEL COLISEO:**
        1. **Hostaria al Gladiatore**: Comer con vistas al gran anfiteatro.
        🌐 [Web Oficial](https://www.ristorantegladiatore.it/)
        2. **Trattoria Luzzi**: Muy auténtica y ruidosa. Lasaña buenísima.
        🌐 [Web Oficial](https://www.trattorialuzzi.it/)
        """
        abrir_ventana("Almuerzo Miércoles", info_com_mie)

# 4. PASEO IMPERIAL ILUMINADO
c1, c2 = st.columns([0.6, 0.4])
with c1: 
    st.write("🕑 **18:00** | 🏟️ Roma Iluminada")
with c2:
    if st.button("🏛️ Ver Guía", key="guia_mie_2"):
        info_iluminada = """
        **EL SUEÑO DE LOS CÉSARES:**
        No hay nada como ver los Foros y el Coliseo iluminados.
        * **El Mirador**: Subid a la Plaza del Campidoglio y asomaos por detrás al Foro Romano.
        * **Paseo**: Bajad por la *Via dei Fori Imperiali* hasta el Coliseo.
        """
        abrir_ventana("Roma Imperial", info_iluminada, img1="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Colosseum_at_night_2015.jpg/800px-Colosseum_at_night_2015.jpg")

# 5. CENA DE DESPEDIDA
c1, c2 = st.columns([0.6, 0.4])
with c1: 
    st.write("🕑 **21:00** | 🍝 Cena Final")
with c2:
    if st.button("🍷 Detalles", key="com_mie_2"):
        info_cena_final = """
        **EL BROCHE DE ORO:**
        1. **Trattoria Vecchia Roma**: Pedid los *Amatriciana Flambé* (pasta en rueda de queso).
        🌐 [Web Oficial](https://www.trattoriavecchiaroma.it/)
        2. **Trattoria Monti**: Cocina regional de altísimo nivel, más íntimo.
        🌐 [Ver en TripAdvisor](https://www.tripadvisor.es/Restaurant_Review-g187791-d793216-Reviews-Trattoria_Monti-Rome_Lazio.html)
        """
        abrir_ventana("Cena de Despedida", info_cena_final)
