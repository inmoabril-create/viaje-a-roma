import streamlit as st
from datetime import datetime

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Roma 2026 - Paco & Trini", page_icon="🇮🇹", layout="centered")

# --- ESTILOS CSS (DISEÑO Y ANIMACIONES) ---
st.markdown("""
    <style>
    /* Fondo color crema suave */
    .stApp { background-color: #Fdfcf0; }
    
    /* Títulos */
    h1, h2, h3 { color: #CE1126; font-family: 'Helvetica', sans-serif; }
    
    /* Encabezados de día */
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
    
    /* Animación de aparición suave (FADE IN) - 2 SEGUNDOS */
    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    
    .contenido-modal {
        animation: fadeIn 2s ease-out; /* Aquí controlamos la lentitud */
    }
    
    .descripcion {
        background-color: #fff;
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #ddd;
        margin-top: 10px;
        font-size: 1em;
        line-height: 1.6;
        color: #333;
    }
    
    /* Botones personalizados */
    div.stButton > button {
        width: 100%;
        border-radius: 20px;
        border: 1px solid #008C45;
        color: #008C45;
        font-weight: bold;
        background-color: white;
        transition: all 0.3s;
    }
    div.stButton > button:hover {
        background-color: #008C45;
        color: white;
        border-color: #008C45;
    }
    </style>
""", unsafe_allow_html=True)

# --- FUNCIÓN MAESTRA DE VENTANA FLOTANTE ---
@st.dialog("🇮🇹 Guía de Viaje")
def abrir_modal(titulo, imagen, texto_html, extra_info=None):
    # Envolvemos todo en un div con la clase 'contenido-modal' para que aparezca suave
    st.markdown(f"""
        <div class="contenido-modal">
            <h2 style='color: #CE1126; margin-top: 0;'>{titulo}</h2>
        </div>
    """, unsafe_allow_html=True)
    
    if imagen:
        st.image(imagen, use_column_width=True)
    
    st.markdown(f"""
        <div class="contenido-modal">
            <div class="descripcion">
                {texto_html}
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    if extra_info:
        st.info(extra_info)

# --- PORTADA ---
st.title("🇮🇹 Roma 2026")
st.caption("Dossier Interactivo: Paco y Trini")

fecha_viaje = datetime(2026, 5, 22, 6, 40)
ahora = datetime.now()
dias_faltan = (fecha_viaje - ahora).days
if dias_faltan > 0:
    st.success(f"⏳ **CUENTA ATRÁS:** Faltan {dias_faltan} días para volar.")

# =========================================================
# DOMINGO 1
# =========================================================
st.markdown("<div class='dia-header'><h3>DOMINGO 1: La Llegada</h3></div>", unsafe_allow_html=True)

# EVENTO 1
col1, col2 = st.columns([0.7, 0.3])
with col1:
    st.markdown("**14:00 | 🛬 Llegada y Traslado**")
with col2:
    if st.button("🚌 Ver Info", key="btn_transporte"):
        abrir_modal(
            "Transporte al Hotel",
            None,
            """
            <b>Opción A (Recomendada): 🚆 Leonardo Express</b><br>
            • Precio: 14€ (28€ total).<br>
            • Tiempo: 32 min directo a Termini.<br>
            • Por qué: Evitáis el tráfico de Roma que es caótico.<br><br>
            <b>Opción B: 🚖 Taxi</b><br>
            • Precio: 50€ (Tarifa fija).<br>
            • Por qué: Si estáis muy cansados y queréis puerta a puerta.
            """
        )

# EVENTO 2
col1, col2 = st.columns([0.7, 0.3])
with col1:
    st.markdown("**15:30 | 🍕 Almuerzo: Elige**")
with col2:
    if st.button("🍽️ Ver Opciones", key="btn_comida_dom"):
        abrir_modal(
            "¿Dónde comemos hoy?",
            "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=800&q=80",
            """
            <b>🏠 La Gallina Bianca (Clásico)</b><br>
            Sitio elegante con manteles. Ideal para relajarse tras el viaje.<br>
            <i>Presupuesto: 50€</i><br><br>
            <b>🍕 Mercato Centrale (Moderno)</b><br>
            Jaleo, puestos variados y ambiente joven.<br>
            <i>Presupuesto: 30€</i>
            """
        )

# EVENTO 3
col1, col2 = st.columns([0.7, 0.3])
with col1:
    st.markdown("**17:30 | ⛪ Sta. Maria Maggiore**")
with col2:
    if st.button("📸 Ver Guía", key="btn_maggiore"):
        abrir_modal(
            "Basílica de Santa Maria Maggiore",
            "https://images.unsplash.com/photo-1574088924962-d696116823c1?w=800&q=80",
            """
            <b>✨ El Primer Oro de América</b><br>
            Mirad al techo dorado. Ese oro fue el primero que trajo Colón desde el Nuevo Mundo. Los Reyes Católicos se lo regalaron al Papa.<br><br>
            <b>❄️ El Milagro de la Nieve</b><br>
            Se construyó aquí porque, según la leyenda, la Virgen hizo nevar en este punto exacto en pleno mes de agosto.
            """
        )

# EVENTO 4
col1, col2 = st.columns([0.7, 0.3])
with col1:
    st.markdown("**18:30 | ⛪ San Pietro in Vincoli**")
with col2:
    if st.button("📸 Ver Guía", key="btn_moises"):
        abrir_modal(
            "El Moisés de Miguel Ángel",
            "https://images.unsplash.com/photo-1555626049-74e50774a387?w=800&q=80",
            """
            <b>🗿 Una escultura con vida</b><br>
            Moisés no está posando, está <b>enfadado</b>. Acaba de ver a su pueblo adorando ídolos falsos. Fíjate en la vena hinchada de su brazo y la tensión de los músculos.<br><br>
            Dicen que es tan realista que Miguel Ángel le golpeó la rodilla con un martillo gritando: <i>"¡Por qué no hablas!"</i>.
            """
        )

# =========================================================
# LUNES 2
# =========================================================
st.markdown("<div class='dia-header'><h3>LUNES 2: Vaticano</h3></div>", unsafe_allow_html=True)

# EVENTO 5
col1, col2 = st.columns([0.7, 0.3])
with col1:
    st.markdown("**09:00 | 🏛️ Museos Vaticanos**")
with col2:
    if st.button("🎟️ Ver Ticket", key="btn_vaticano"):
        abrir_modal(
            "Museos Vaticanos y Capilla Sixtina",
            "https://images.unsplash.com/photo-1541544181961-b664d0089d53?w=800&q=80",
            """
            <b>🎨 La Capilla Sixtina</b><br>
            Obra cumbre de la humanidad. Miguel Ángel pintó el techo de pie, casi quedándose ciego. Buscad <i>La Creación de Adán</i> (los dedos tocándose).<br><br>
            <b>💀 El Juicio Final</b><br>
            En la pared del fondo. San Bartolomé sostiene una piel despellejada... ¡es un autorretrato macabro del propio Miguel Ángel!
            """,
            extra_info="CÓDIGO TICKET: 2L2NFFJ00000004GM"
        )

# EVENTO 6
col1, col2 = st.columns([0.7, 0.3])
with col1:
    st.markdown("**16:30 | 🏰 Castel Sant'Angelo**")
with col2:
    if st.button("📸 Ver Guía", key="btn_castillo"):
        abrir_modal(
            "Castillo de Sant'Angelo",
            "https://images.unsplash.com/photo-1525874684015-58379d421a52?w=800&q=80",
            """
            De tumba de emperador a fortaleza de los Papas. <br><br>
            <b>🕵️ El Pasadizo Secreto</b><br>
            Existe un corredor elevado (<i>Il Passetto</i>) que conecta el castillo con el Vaticano. Por ahí huyeron varios Papas para salvar la vida durante los asedios a Roma.
            """
        )

# =========================================================
# MARTES 3
# =========================================================
st.markdown("<div class='dia-header'><h3>MARTES 3: Barroco</h3></div>", unsafe_allow_html=True)

# EVENTO 7
col1, col2 = st.columns([0.7, 0.3])
with col1:
    st.markdown("**10:00 | ⛲ Fontana di Trevi**")
with col2:
    if st.button("📸 Ver Guía", key="btn_trevi"):
        abrir_modal(
            "Fontana di Trevi",
            "https://images.unsplash.com/photo-1515542622106-78bda8ba30c3?w=800&q=80",
            """
            <b>🪙 La Tradición</b><br>
            Lanzar moneda con mano derecha sobre hombro izquierdo = Volver a Roma.<br><br>
            Es el final de un acueducto romano que lleva funcionando más de 2000 años. El agua que veis viene de manantiales puros a las afueras de la ciudad.
            """
        )

# EVENTO 8
col1, col2 = st.columns([0.7, 0.3])
with col1:
    st.markdown("**14:00 | 🍝 Almuerzo Especial**")
with col2:
    if st.button("❤️ Ver Sitio", key="btn_cantina"):
        abrir_modal(
            "Cantina e Cucina",
            "https://images.unsplash.com/photo-1559339352-11d035aa65de?w=800&q=80",
            """
            <b>Nuestro sitio favorito</b><br>
            Ambiente rústico y alegre. Tenéis que pedir:<br>
            1. Pasta Carbonara (sin nata, solo huevo y queso).<br>
            2. Pasta Amatriciana.<br><br>
            Presupuesto aprox: 60€
            """
        )

# EVENTO 9
col1, col2 = st.columns([0.7, 0.3])
with col1:
    st.markdown("**16:30 | 🏛️ El Panteón**")
with col2:
    if st.button("📸 Ver Guía", key="btn_panteon"):
        abrir_modal(
            "El Panteón de Agripa",
            "https://images.unsplash.com/photo-1506547631742-0f135272a806?w=800&q=80",
            """
            El edificio mejor conservado de la antigüedad (año 125 d.C).<br><br>
            <b>☀️ El Óculo</b><br>
            El agujero del techo es la única luz. Cuando llueve, el agua entra, pero el suelo tiene agujeritos invisibles para drenarla. Aquí está la tumba del pintor Rafael.
            """
        )

# =========================================================
# MIÉRCOLES 4
# =========================================================
st.markdown("<div class='dia-header'><h3>MIÉRCOLES 4: Arte y Coliseo</h3></div>", unsafe_allow_html=True)

col1, col2 = st.columns([0.7, 0.3])
with col1:
    st.markdown("**12:00 | 🎨 Galería Borghese**")
with col2:
    if st.button("📸 Ver Guía", key="btn_borghese"):
        abrir_modal(
            "Galería Borghese",
            "https://images.unsplash.com/photo-1555520978-0062f689f46b?w=800&q=80",
            """
            <b>Bernini: Mármol o Carne</b><br>
            Fijaos en <i>El Rapto de Proserpina</i>. Los dedos de Plutón se hunden en el muslo de ella como si fuera carne real. Es impresionante.<br>
            En <i>Apolo y Dafne</i>, veréis cómo los dedos de ella se transforman en ramas y hojas ante vuestros ojos.
            """
        )

col1, col2 = st.columns([0.7, 0.3])
with col1:
    st.markdown("**16:00 | 🏟️ Coliseo**")
with col2:
    if st.button("📸 Ver Guía", key="btn_coliseo"):
        abrir_modal(
            "El Coliseo Romano",
            "https://images.unsplash.com/photo-1552832230-c0197dd311b5?w=800&q=80",
            """
            Tenía capacidad para 50.000 personas. Tenía un techo de lona retráctil (Velarium) para dar sombra.<br><br>
            Bajo la arena, hay túneles y montacargas para subir leones y gladiadores por sorpresa.
            """
        )

# =========================================================
# JUEVES
# =========================================================
st.markdown("<div class='dia-header'><h3>JUEVES: Regreso</h3></div>", unsafe_allow_html=True)
st.error("🛫 Vuelo de vuelta: 06:40 AM")

col1, col2 = st.columns([0.7, 0.3])
with col1:
    st.markdown("**03:45 | 🚌 Bus al Aeropuerto**")
with col2:
    if st.button("📍 Ver Parada", key="btn_bus_vuelta"):
        abrir_modal(
            "Bus de Vuelta (TAM)",
            None,
            """
            <b>Salida:</b> Via Giolitti 34 (Lado de Termini).<br>
            <b>Hora:</b> 03:45 AM (Sed puntuales).<br>
            <b>Precio:</b> 7€ por persona.<br><br>
            <i>Alternativa: Pedir taxi en el hotel (50€).</i>
            """
        )
