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
st.markdown("""<div class="evento"><span class="hora">10:00</span>⛲ <b>Fontana di Trevi y Pza. España</b></div>""", unsafe_allow_html=True)
with st.expander("📸 GUÍA: El Agua de Roma"):
    st.image("https://images.unsplash.com/photo-1515542622106-78bda8ba30c3?w=800&q=80")
    st.markdown("""
    <div class="descripcion">
    La fuente barroca más famosa del mundo. No es solo decorativa: es el final del acueducto <i>Aqua Virgo</i>, que lleva trayendo agua a Roma desde el año 19 a.C.
    <br><br>
    🪙 <b>El Rito:</b> Moneda con la mano derecha sobre el hombro izquierdo.
    1 moneda = Volver a Roma.
    2 monedas = Encontrar el amor (¡vosotros ya vais servidos!).
    <br><br>
    Después, paseo hasta <b>Plaza de España</b> para ver la escalinata más cinematográfica de la ciudad.
    </div>
    """, unsafe_allow_html=True)

st.markdown("""<div class="evento"><span class="hora">14:00</span>🍝 <b>ALMUERZO: Cantina e Cucina</b></div>""", unsafe_allow_html=True)

# --- VISITA 6: PANTEÓN ---
st.markdown("""<div class="evento"><span class="hora">16:30</span>🏛️ <b>El Panteón de Agripa</b></div>""", unsafe_allow_html=True)
with st.expander("📸 GUÍA: La Perfección Geométrica"):
    st.image("https://images.unsplash.com/photo-1506547631742-0f135272a806?w=800&q=80")
    st.markdown("""
    <div class="descripcion">
    Es el edificio mejor conservado de la antigüedad (año 125 d.C.). Miguel Ángel dijo que era un "diseño de ángeles, no de humanos".
    <br><br>
    📐 <b>El Secreto:</b> Es una esfera perfecta. La altura es exactamente igual al diámetro (43,30m).
    <br><br>
    ☀️ <b>El Óculo:</b> El agujero del techo (9 metros de ancho) es la única fuente de luz. <b>Sí, cuando llueve, el agua entra</b>, pero el suelo tiene 22 agujeritos casi invisibles para drenarla. Aquí descansa Rafael Sanzio.
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# MIÉRCOLES 4: ARTE Y COLISEO
# =========================================================
st.markdown("<div class='dia-header'><h3>MIÉRCOLES 4: Roma Imperial</h3></div>", unsafe_allow_html=True)

# --- VISITA 7: BORGHESE ---
st.markdown("""<div class="evento"><span class="hora">12:00</span>🎨 <b>Galería Borghese</b></div>""", unsafe_allow_html=True)
with st.expander("📸 GUÍA: Mármol que parece Carne"):
    st.image("https://images.unsplash.com/photo-1555520978-0062f689f46b?w=800&q=80")
    st.markdown("""
    <div class="descripcion">
    La "Reina de las Colecciones Privadas". Aquí venimos a ver el genio de <b>Bernini</b>.
    <br><br>
    👀 <b>Fijaos bien:</b>
    1. <b>Apolo y Dafne:</b> El momento exacto en que ella se convierte en árbol. Mirad sus dedos transformándose en hojas y las raíces saliendo de los pies.
    2. <b>El Rapto de Proserpina:</b> Mirad cómo los dedos de Plutón se hunden en el muslo de ella. Parece carne blanda, pero es piedra dura. ¡Increíble!
    3. <b>Paulina Bonaparte:</b> La hermana de Napoleón posando como Venus vencedora (obra de Canova).
    </div>
    """, unsafe_allow_html=True)

# --- VISITA 8: COLISEO ---
st.markdown("""<div class="evento"><span class="hora">16:00</span>🏟️ <b>Coliseo y Foros Imperiales</b></div>""", unsafe_allow_html=True)
with st.expander("📸 GUÍA: Pan y Circo"):
    st.image("https://images.unsplash.com/photo-1552832230-c0197dd311b5?w=800&q=80")
    st.markdown("""
    <div class="descripcion">
    El símbolo eterno. Se inauguró en el año 80 d.C. con 100 días seguidos de juegos.
    <br><br>
    🦁 <b>La Ingeniería:</b> Bajo la arena (el suelo de madera) había un laberinto de túneles, ascensores y jaulas para subir fieras y gladiadores por sorpresa en mitad del espectáculo.
    <br><br>
    ☀️ <b>El Aire Acondicionado:</b> Tenía un sistema de toldos gigantes (<i>Velarium</i>) movido por marineros para dar sombra a los 50.000 espectadores.
    <br><br>
    A su lado, el <b>Foro Romano</b>: el centro del universo político y social de la época. Pisad las mismas piedras que Julio César.
    </div>
    """, unsafe_allow_html=True)

st.markdown("""<div class="evento"><span class="hora">21:00</span>🍝 <b>Cena Despedida: Vecchia Roma</b></div>""", unsafe_allow_html=True)

# =========================================================
# JUEVES: REGRESO
# =========================================================
st.markdown("<div class='dia-header'><h3>JUEVES: Arrivederci</h3></div>", unsafe_allow_html=True)
st.error("🛫 Vuelo a las 06:40 AM")
