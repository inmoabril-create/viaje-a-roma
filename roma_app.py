import streamlit as st
from datetime import datetime

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Roma 2026 - Paco & Trini", page_icon="🇮🇹", layout="centered")

# --- ESTILOS CSS (DISEÑO) ---
st.markdown("""
    <style>
    .stApp { background-color: #Fdfcf0; }
    h1, h2, h3 { color: #CE1126; }
    .dia-header {
        background-color: #008C45;
        color: white;
        padding: 10px;
        border-radius: 10px;
        margin-top: 30px;
        margin-bottom: 15px;
        text-align: center;
    }
    .evento {
        background: white;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        margin-bottom: 10px;
        border-left: 5px solid #CE1126;
    }
    .hora { font-weight: bold; color: #555; font-size: 1.1em; }
    .ticket-code {
        background-color: #e8f8f5;
        padding: 10px;
        border-radius: 5px;
        border: 1px dashed #008C45;
        font-family: monospace;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# --- PORTADA Y CUENTA ATRÁS ---
st.title("🇮🇹 Roma 2026: Paco y Trini")
fecha_viaje = datetime(2026, 5, 22, 6, 40)
ahora = datetime.now()
dias_faltan = (fecha_viaje - ahora).days

if dias_faltan > 0:
    st.info(f"⏳ **CUENTA ATRÁS:** Faltan {dias_faltan} días para el despegue.")
else:
    st.success("🚀 ¡ESTAMOS DE VIAJE!")

# =========================================================
# DOMINGO 1: LLEGADA Y PRIMER CONTACTO
# =========================================================
st.markdown("<div class='dia-header'><h3>DOMINGO 1: Benvenuti a Roma</h3></div>", unsafe_allow_html=True)

with st.container():
    st.markdown("""
    <div class="evento">
        <span class="hora">14:00</span> | 🛬 <b>Llegada y Traslado</b>
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("🚌 Ver opciones de Transporte (Aeropuerto -> Hotel)"):
        st.write("Según Módulo Transportes:")
        st.markdown("""
        * **🚆 Leonardo Express (Recomendado):** 14€/pax (28€ total). 32 min directo a Termini.
        * **🚖 Taxi:** 50€ tarifa fija. Cómodo si estamos cansados.
        * **🚌 Bus:** 7€/pax. Más lento por tráfico.
        """)

st.markdown("""
<div class="evento">
    <span class="hora">15:30</span> | 🍕 <b>Almuerzo: La Gallina Bianca</b>
</div>
""", unsafe_allow_html=True)
with st.expander("🍽️ Ver detalle restaurante"):
    st.image("https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=800&q=80")
    st.write("**La Gallina Bianca:** Cerca del hotel. Presupuesto aprox: 50€.")
    st.info("Alternativa: Mercato Centrale si queremos algo rápido.")

st.markdown("""
<div class="evento">
    <span class="hora">17:30</span> | ⛪ <b>Basílica Sta. Maria Maggiore</b>
</div>
""", unsafe_allow_html=True)
with st.expander("📖 Guía Rápida: Sta. Maria Maggiore"):
    st.write("**Siglo V.** Fíjate en el techo: dicen que está decorado con el **primer oro traído de América**.")

st.markdown("""
<div class="evento">
    <span class="hora">18:30</span> | ⛪ <b>San Pietro in Vincoli (El Moisés)</b>
</div>
""", unsafe_allow_html=True)
with st.expander("📖 Guía Rápida: El Moisés"):
    st.write("**Imperdible:** El Moisés de Miguel Ángel. Mira el realismo de las venas y los músculos. También están las cadenas de San Pedro.")

st.markdown("""
<div class="evento">
    <span class="hora">21:00</span> | 🍷 <b>Cena en Barrio Monti</b>
</div>
""", unsafe_allow_html=True)
with st.expander("🍽️ Opción recomendada: Ai Tre Scalini"):
    st.write("Ambiente de taberna romana. Presupuesto aprox: 50€.")

# =========================================================
# LUNES 2: EL VATICANO
# =========================================================
st.markdown("<div class='dia-header'><h3>LUNES 2: La Grandeza del Vaticano</h3></div>", unsafe_allow_html=True)

st.info("⏰ **DESPERTADOR:** 07:00 AM")

st.markdown("""
<div class="evento">
    <span class="hora">09:00</span> | 🏛️ <b>Museos Vaticanos</b>
</div>
""", unsafe_allow_html=True)
with st.expander("🎟️ TICKETS Y GUÍA (IMPORTANTE)"):
    st.markdown('<div class="ticket-code">CÓDIGO: 2L2NFFJ00000004GM</div>', unsafe_allow_html=True)
    st.write("*Francisco y Trinidad*")
    st.write("---")
    st.write("**Qué ver:** Capilla Sixtina y Estancias de Rafael. Es la cumbre del arte mundial.")

st.markdown("""
<div class="evento">
    <span class="hora">14:30</span> | 🍝 <b>Almuerzo Zona Vaticano</b>
</div>
""", unsafe_allow_html=True)
with st.expander("🍽️ Opciones"):
    st.write("**Pastasciutta:** Económico (25€) y rápido.")

st.markdown("""
<div class="evento">
    <span class="hora">16:30</span> | 🏰 <b>Castel Sant'Angelo</b>
</div>
""", unsafe_allow_html=True)
with st.expander("📖 Historia"):
    st.write("Antigua tumba del emperador Adriano y luego fortaleza de los Papas. Las vistas desde arriba son increíbles.")

st.markdown("""
<div class="evento">
    <span class="hora">20:30</span> | 🍕 <b>Cena en Trastevere</b>
</div>
""", unsafe_allow_html=True)
with st.expander("🍽️ Recomendación: Tonnarello"):
    st.write("Famoso por sus pastas en sartén. Suele haber cola pero va rápido. Presupuesto: 50€.")

# =========================================================
# MARTES 3: BARROCO Y NUESTRO SITIO
# =========================================================
st.markdown("<div class='dia-header'><h3>MARTES 3: La Dolce Vita</h3></div>", unsafe_allow_html=True)

st.info("⏰ **DESPERTADOR:** 08:30 AM")

st.markdown("""
<div class="evento">
    <span class="hora">10:00</span> | ⛲ <b>Ruta Barroca</b>
</div>
""", unsafe_allow_html=True)
with st.expander("📍 Recorrido"):
    st.write("Fontana di Trevi (Lanzar moneda) ➔ Plaza de España.")
    st.write("**Nota:** Neptuno domando las aguas en la Fontana.")

st.markdown("""
<div class="evento">
    <span class="hora">14:00</span> | 🍝 <b>ALMUERZO ESPECIAL: Cantina e Cucina</b>
</div>
""", unsafe_allow_html=True)
with st.expander("❤️ Nuestro Sitio (Ver foto)"):
    st.image("https://images.unsplash.com/photo-1559339352-11d035aa65de?w=800&q=80")
    st.write("Pedir Carbonara y Amatriciana. Presupuesto: 60€.")

st.markdown("""
<div class="evento">
    <span class="hora">16:30</span> | 🏛️ <b>Panteón y Plaza Navona</b>
</div>
""", unsafe_allow_html=True)
with st.expander("📖 Guía Rápida: Panteón"):
    st.write("Construido en 125 d.C. Tiene la cúpula de hormigón más grande del mundo. Dentro está la tumba de Rafael.")

st.markdown("""
<div class="evento">
    <span class="hora">20:30</span> | 🍷 <b>Cena Zona Navona</b>
</div>
""", unsafe_allow_html=True)

# =========================================================
# MIÉRCOLES 4: ARTE Y COLISEO
# =========================================================
st.markdown("<div class='dia-header'><h3>MIÉRCOLES 4: Roma Imperial</h3></div>", unsafe_allow_html=True)

st.info("⏰ **DESPERTADOR:** 09:00 AM")

st.markdown("""
<div class="evento">
    <span class="hora">12:00</span> | 🎨 <b>Galería Borghese</b>
</div>
""", unsafe_allow_html=True)
with st.expander("⚠️ LOGÍSTICA (Estar 11:30)"):
    st.warning("Hay que dejar bolsos en guardarropa obligatorio.")
    st.write("**Arte:** Esculturas de Bernini. El mármol parece piel real (Apolo y Dafne).")

st.markdown("""
<div class="evento">
    <span class="hora">16:00</span> | 🏟️ <b>Coliseo y Foros</b>
</div>
""", unsafe_allow_html=True)
with st.expander("📖 Historia"):
    st.write("El mayor anfiteatro del mundo. Imaginad a los gladiadores ahí.")

st.markdown("""
<div class="evento">
    <span class="hora">21:00</span> | 🍝 <b>Cena Despedida: Vecchia Roma</b>
</div>
""", unsafe_allow_html=True)
with st.expander("📞 Datos Reserva"):
    st.write("**Teléfono:** +39 06 446 7373")
    st.write("Presupuesto: 60€. Famosa por su pasta flambeada.")

# =========================================================
# JUEVES: VUELTA A CASA
# =========================================================
st.markdown("<div class='dia-header'><h3>JUEVES: Arrivederci Roma</h3></div>", unsafe_allow_html=True)

st.error("⏰ **DESPERTADOR:** 03:00 AM (Dolerá, pero necesario)")

st.markdown("""
<div class="evento">
    <span class="hora">03:45</span> | 🛫 <b>Traslado al Aeropuerto</b>
</div>
""", unsafe_allow_html=True)
with st.expander("🚌 Opciones Madrugada"):
    st.write("**Vuelo:** 06:40 AM")
    st.markdown("""
    * **Opción BUS TAM:** Salida 03:45 desde Via Giolitti 34. (7€/pax).
    * **Opción TAXI:** Pedir en recepción noche anterior para las 04:00. (50€).
    """)

st.divider()
st.caption("Dossier Interactivo creado para Paco y Trini.")
