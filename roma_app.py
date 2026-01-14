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
    
    /* Animación de aparición suave */
    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    .contenido-modal {
        animation: fadeIn 1.5s ease-out;
    }
    
    /* Cajas de texto dentro de las ventanas */
    .descripcion-box {
        background-color: #fff;
        padding: 15px;
        border-radius: 8px;
        border-left: 5px solid #008C45;
        margin-top: 10px;
        font-size: 1em;
        line-height: 1.6;
        color: #333;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }

    /* Títulos destacados en las descripciones */
    .titulo-opcion {
        color: #CE1126;
        font-weight: bold;
        font-size: 1.1em;
        margin-bottom: 5px;
        display: block;
    }
    
    /* Botones */
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
def abrir_modal(titulo, contenido_html, imagen_1=None, pie_1=None, imagen_2=None, pie_2=None):
    # Título principal
    st.markdown(f"<h2 style='color: #CE1126; text-align: center;'>{titulo}</h2>", unsafe_allow_html=True)
    
    # Si hay una imagen (Caso normal)
    if imagen_1 and not imagen_2:
        st.image(imagen_1, caption=pie_1, use_column_width=True)
    
    # Si hay DOS imágenes (Caso Comparativa Comida)
    if imagen_1 and imagen_2:
        col_a, col_b = st.columns(2)
        with col_a:
            st.image(imagen_1, caption=pie_1, use_column_width=True)
        with col_b:
            st.image(imagen_2, caption=pie_2, use_column_width=True)

    # Texto con formato HTML corregido
    st.markdown(f"""
        <div class="contenido-modal">
            <div class="descripcion-box">
                {contenido_html}
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- PORTADA ---
st.title("🇮🇹 Roma 2026")
st.caption("Dossier Interactivo: Paco y Trini")

fecha_viaje = datetime(2026, 5, 22, 6, 40)
ahora = datetime.now()
dias_faltan = (fecha_viaje - ahora).days
if dias_faltan > 0:
    st.success(f"⏳ **CUENTA ATRÁS:** Faltan {dias_faltan} días para volar.")

# =========================================================
# DOMINGO 1: BENVENUTI A ROMA
# =========================================================
st.markdown("<div class='dia-header'><h3>DOMINGO 1: La Llegada</h3></div>", unsafe_allow_html=True)

# --- TRANSPORTE ---
col1, col2 = st.columns([0.7, 0.3])
with col1:
    st.markdown("**14:00 | 🛬 Llegada y Traslado**")
with col2:
    if st.button("🚌 Ver Transporte", key="btn_transporte"):
        abrir_modal(
            "Transporte al Hotel",
            """
            <span class="titulo-opcion">🚆 OPCIÓN A: Leonardo Express (Recomendada)</span>
            <ul>
                <li><b>Precio:</b> 14€ (28€ total).</li>
                <li><b>Tiempo:</b> 32 min (Directo a Termini).</li>
                <li><b>Ventaja:</b> Rápido y sin atascos.</li>
            </ul>
            <hr>
            <span class="titulo-opcion">🚌 OPCIÓN B: Autobús (Bus TAM/Terravision)</span>
            <ul>
                <li><b>Precio:</b> 7€/pax (14€ total).</li>
                <li><b>Tiempo:</b> 60 min o más (Depende del tráfico).</li>
                <li><b>Ventaja:</b> El más barato.</li>
            </ul>
            <hr>
            <span class="titulo-opcion">🚖 OPCIÓN C: Taxi Oficial</span>
            <ul>
                <li><b>Precio:</b> 50€ (Tarifa fija).</li>
                <li><b>Tiempo:</b> 45 min aprox.</li>
                <li><b>Ventaja:</b> Puerta a puerta si estáis agotados.</li>
            </ul>
            """
        )

# --- ALMUERZO (DOBLE OPCIÓN) ---
col1, col2 = st.columns([0.7, 0.3])
with col1:
    st.markdown("**15:30 | 🍕 Almuerzo: Elige**")
with col2:
    if st.button("🍽️ Ver Opciones", key="btn_comida_dom"):
        abrir_modal(
            "¿Dónde comemos hoy?",
            """
            <span class="titulo-opcion">🏠 OPCIÓN 1: La Gallina Bianca</span>
            <p>Ambiente rústico, manteles de tela y tranquilidad. Ideal para relajarse nada más llegar. Cocina romana clásica.</p>
            <p><b>💰 Precio:</b> 50€ aprox.</p>
            <hr>
            <span class="titulo-opcion">🍕 OPCIÓN 2: Mercato Centrale</span>
            <p>Situado bajo la estación. Es un espacio moderno, vibrante y con mucho jaleo. Mesas compartidas y puestos de todo tipo.</p>
            <p><b>💰 Precio:</b> 30€ aprox.</p>
            """,
            imagen_1="https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=800&q=80",
            pie_1="La Gallina Bianca",
            imagen_2="https://images.unsplash.com/photo-1533900298318-6b8da08a523e?w=800&q=80",
            pie_2="Mercato Centrale"
        )

# --- VISITA 1: STA MARIA MAGGIORE ---
col1, col2 = st.columns([0.7, 0.3])
with col1:
    st.markdown("**17:30 | ⛪ Sta. Maria Maggiore**")
with col2:
    if st.button("📸 Ver Guía", key="btn_maggiore"):
        abrir_modal(
            "Basílica de Santa Maria Maggiore",
            """
            <b>✨ El Primer Oro de América:</b><br>
            Fíjate en el techo artesonado dorado. Se dice que fue decorado con el <b>primer oro que Cristóbal Colón trajo de América</b>, regalado por los Reyes Católicos al Papa.<br><br>
            <b>❄️ La Leyenda de la Nieve:</b><br>
            Se construyó aquí porque la Virgen señaló el lugar haciendo caer una nevada milagrosa en pleno mes de agosto (Siglo V).
            """,
            imagen_1="https://images.unsplash.com/photo-1574088924962-d696116823c1?w=800&q=80",
            pie_1="El techo con el oro de América"
        )

# --- VISITA 2: MOISÉS ---
col1, col2 = st.columns([0.7, 0.3])
with col1:
    st.markdown("**18:30 | ⛪ San Pietro in Vincoli**")
with col2:
    if st.button("📸 Ver Guía", key="btn_moises"):
        abrir_modal(
            "El Moisés y las Cadenas",
            """
            <b>🗿 El Moisés de Miguel Ángel:</b><br>
            Mira su expresión. No posa, está <b>enfadado</b> viendo a su pueblo adorar ídolos. Fíjate en la vena hinchada del brazo y la tensión muscular. Es tan real que Miguel Ángel le golpeó con un martillo gritando: <i>"¡Habla!"</i>.<br><br>
            <b>🔗 Las Cadenas:</b><br>
            Bajo el altar se guardan las cadenas con las que ataron a San Pedro en Jerusalén.
            """,
            imagen_1="https://images.unsplash.com/photo-1555626049-74e50774a387?w=800&q=80",
            pie_1="La furia del Moisés"
        )

# --- CENA ---
col1, col2 = st.columns([0.7, 0.3])
with col1:
    st.markdown("**21:00 | 🍷 Cena: Barrio Monti**")
with col2:
    if st.button("📍 Ver Sitio", key="btn_cena_dom"):
        abrir_modal(
            "Cena en Ai Tre Scalini",
            """
            Una taberna histórica en el barrio de moda (Monti). Ambiente muy romano, hiedra en la fachada y buenos vinos.<br>
            <b>💰 Presupuesto:</b> 50€ (Pareja).
            """,
            imagen_1="https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=800&q=80"
        )

# =========================================================
# LUNES 2: VATICANO
# =========================================================
st.markdown("<div class='dia-header'><h3>LUNES 2: Vaticano</h3></div>", unsafe_allow_html=True)
st.info("⏰ DESPERTADOR: 07:00 AM")

col1, col2 = st.columns([0.7, 0.3])
with col1:
    st.markdown("**09:00 | 🏛️ Museos Vaticanos**")
with col2:
    if st.button("🎟️ Ver Ticket", key="btn_vaticano"):
        abrir_modal(
            "Museos Vaticanos",
            """
            <b>🎫 CÓDIGO TICKET:</b> 2L2NFFJ00000004GM<br>
            (Francisco y Trinidad)<br><br>
            <b>Lo imprescindible:</b><br>
            1. <b>Capilla Sixtina:</b> El Juicio Final. Busca la piel despellejada de San Bartolomé (es un autorretrato de Miguel Ángel).<br>
            2. <b>Estancias de Rafael:</b> La Escuela de Atenas.
            """,
            imagen_1="https://images.unsplash.com/photo-1541544181961-b664d0089d53?w=800&q=80"
        )
