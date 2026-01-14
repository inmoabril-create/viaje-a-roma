import streamlit as st
from datetime import datetime

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Roma 2026 - Paco & Trini", page_icon="🇮🇹", layout="centered")

# --- ESTILOS CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #Fdfcf0; }
    h1, h2, h3 { color: #CE1126; font-family: 'Helvetica', sans-serif; }
    .dia-header {
        background-color: #008C45;
        color: white;
        padding: 15px;
        border-radius: 10px;
        margin-top: 30px;
        margin-bottom: 20px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .evento {
        background: white;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        margin-bottom: 12px;
        border-left: 6px solid #CE1126;
    }
    .hora { font-weight: bold; color: #555; font-size: 1.1em; margin-right: 10px; }
    .descripcion {
        background-color: #fff;
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #ddd;
        margin-top: 10px;
        font-size: 0.95em;
        line-height: 1.5;
    }
    .destacado { font-weight: bold; color: #CE1126; }
    </style>
""", unsafe_allow_html=True)

# --- PORTADA ---
st.title("🇮🇹 Roma 2026")
st.subheader("Dossier de Viaje: Paco y Trini")

# Cálculo días
fecha_viaje = datetime(2026, 5, 22, 6, 40)
ahora = datetime.now()
dias_faltan = (fecha_viaje - ahora).days

if dias_faltan > 0:
    st.info(f"⏳ **CUENTA ATRÁS:** Faltan {dias_faltan} días para volar.")

# =========================================================
# DOMINGO 1: LLEGADA Y PRIMER CONTACTO
# =========================================================
st.markdown("<div class='dia-header'><h3>DOMINGO 1: Benvenuti a Roma</h3></div>", unsafe_allow_html=True)

st.markdown("""<div class="evento"><span class="hora">14:00</span>🛬 <b>Llegada y Traslado</b></div>""", unsafe_allow_html=True)
with st.expander("🚌 Opciones Transporte (Recomendación: Tren)"):
    st.write("**🚆 Leonardo Express:** La opción más fiable (32 min). Os deja en Termini, muy cerca del hotel.")
    st.write("**🚖 Taxi:** Tarifa fija 50€. Cómodo si estáis muy cansados.")

st.markdown("""<div class="evento"><span class="hora">15:30</span>🍕 <b>Almuerzo: La Gallina Bianca</b></div>""", unsafe_allow_html=True)

# --- VISITA 1: STA MARIA MAGGIORE ---
st.markdown("""<div class="evento"><span class="hora">17:30</span>⛪ <b>Basílica Sta. Maria Maggiore</b></div>""", unsafe_allow_html=True)
with st.expander("📸 GUÍA: El Oro de América y la Nieve"):
    st.image("https://images.unsplash.com/photo-1574088924962-d696116823c1?w=800&q=80")
    st.markdown("""
    <div class="descripcion">
    Esta es una de las 4 basílicas mayores de Roma y la única que conserva su estructura paleocristiana original.
    <br><br>
    ❄️ <b>La Leyenda:</b> Se dice que la Virgen señaló el lugar haciendo caer una nevada milagrosa en pleno agosto (el <i>Miracolo della Neve</i>).
    <br><br>
    ✨ <b>El Tesoro:</b> Mirad al techo. Esos casetones dorados no son pintura: están recubiertos con <b>el primer oro que Cristóbal Colón trajo de América</b>, un regalo de los Reyes Católicos al Papa español Alejandro VI (Borgia).
    </div>
    """, unsafe_allow_html=True)

# --- VISITA 2: MOISÉS ---
st.markdown("""<div class="evento"><span class="hora">18:30</span>⛪ <b>San Pietro in Vincoli</b></div>""", unsafe_allow_html=True)
with st.expander("📸 GUÍA: La Furia de Moisés"):
    st.image("https://images.unsplash.com/photo-1555626049-74e50774a387?w=800&q=80")
    st.markdown("""
    <div class="descripcion">
    Aquí venimos a ver dos cosas, pero una eclipsa a la otra:
    <br><br>
    🗿 <b>El Moisés de Miguel Ángel:</b> Es una de las esculturas más potentes de la historia. Moisés no está posando, está <b>enfadado</b>. Acaba de bajar del Monte Sinaí con las tablas y ve a su pueblo adorando a un becerro de oro. Fíjate en la tensión de los músculos del brazo y en la vena hinchada. Dicen que Miguel Ángel, al terminarla, le golpeó la rodilla con un martillo y le gritó: <i>"¡Habla!"</i>.
    <br><br>
    🔗 <b>Las Cadenas:</b> Bajo el altar están las cadenas con las que supuestamente ataron a San Pedro en Jerusalén.
    </div>
    """, unsafe_allow_html=True)

st.markdown("""<div class="evento"><span class="hora">21:00</span>🍷 <b>Cena: Barrio Monti</b></div>""", unsafe_allow_html=True)

# =========================================================
# LUNES 2: VATICANO
# =========================================================
st.markdown("<div class='dia-header'><h3>LUNES 2: La Grandeza del Vaticano</h3></div>", unsafe_allow_html=True)
st.warning("⏰ Despertador: 07:00 AM (Tickets reservados)")

# --- VISITA 3: MUSEOS VATICANOS ---
st.markdown("""<div class="evento"><span class="hora">09:00</span>🏛️ <b>Museos Vaticanos</b></div>""", unsafe_allow_html=True)
with st.expander("📸 GUÍA: La Capilla Sixtina y más"):
    st.success("🎫 TICKET: Código 2L2NFFJ00000004GM")
    st.image("https://images.unsplash.com/photo-1541544181961-b664d0089d53?w=800&q=80")
    st.markdown("""
    <div class="descripcion">
    No es solo un museo, son 7 km de galerías. Lo imprescindible:
    <br><br>
    🎨 <b>La Capilla Sixtina:</b> El lugar donde se eligen los Papas.
    <ul>
    <li><b>El Techo:</b> Miguel Ángel lo pintó de pie (no tumbado) y casi se queda ciego. Busca <i>La Creación de Adán</i> (los dedos tocándose).</li>
    <li><b>El Juicio Final (Pared):</b> Lo pintó años después, ya viejo y pesimista. Es un remolino de cuerpos. San Bartolomé sostiene su propia piel despellejada: ¡es un autorretrato macabro de Miguel Ángel!</li>
    </ul>
    🖌️ <b>Las Estancias de Rafael:</b> La competencia directa de Miguel Ángel. Fijaos en <i>La Escuela de Atenas</i>, donde salen Platón y Aristóteles.
    </div>
    """, unsafe_allow_html=True)

st.markdown("""<div class="evento"><span class="hora">14:30</span>🍝 <b>Almuerzo Rápido (Zona Vaticano)</b></div>""", unsafe_allow_html=True)

# --- VISITA 4: CASTEL SANT'ANGELO ---
st.markdown("""<div class="evento"><span class="hora">16:30</span>🏰 <b>Castel Sant'Angelo</b></div>""", unsafe_allow_html=True)
with st.expander("📸 GUÍA: De Tumba a Fortaleza"):
    st.image("https://images.unsplash.com/photo-1525874684015-58379d421a52?w=800&q=80")
    st.markdown("""
    <div class="descripcion">
    Este edificio lo ha sido todo. Nació como el <b>Mausoleo del Emperador Adriano</b> (año 135 d.C.), pero luego los Papas lo convirtieron en su fortaleza y cárcel de lujo.
    <br><br>
    🕵️ <b>El Pasadizo Secreto:</b> Existe un corredor elevado (<i>Il Passetto</i>) que conecta el castillo con el Vaticano. Por ahí huyó el Papa Clemente VII durante el Saqueo de Roma corriendo por su vida.
    <br><br>
    👼 <b>El Ángel:</b> La estatua de arriba recuerda la visión del Arcángel San Miguel envainando su espada, señal de que la peste había terminado. ¡Subid a la terraza para la mejor vista de la cúpula de San Pedro!
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# MARTES 3: BARROCO
# =========================================================
st.markdown("<div class='dia-header'><h3>MARTES 3: La Dolce Vita</h3></div>", unsafe_allow_html=True)

# --- VISITA 5: FONTANA DI TREVI ---
st.markdown("""<div class="evento"><span class="hora">10:00</span>⛲ <b>Fontana di Trevi y Pza. España</b>
