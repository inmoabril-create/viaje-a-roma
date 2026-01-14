import streamlit as st
from datetime import datetime

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Roma 2026", page_icon="🇮🇹", layout="centered")

# --- ESTILOS CSS (DISEÑO LIMPIO) ---
st.markdown("""
    <style>
    /* Fondo crema suave */
    .stApp { background-color: #Fdfcf0; }
    
    /* Botones grandes y bonitos para dedo */
    div.stButton > button {
        width: 100%;
        padding: 15px;
        border-radius: 12px;
        border: 2px solid #008C45;
        color: #008C45;
        font-weight: bold;
        font-size: 16px;
        background-color: white;
        transition: all 0.2s;
    }
    div.stButton > button:hover {
        background-color: #008C45;
        color: white;
    }
    
    /* Cajas de eventos */
    .evento-row {
        background-color: white;
        padding: 15px;
        border-radius: 10px;
        border-left: 6px solid #CE1126;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        margin-bottom: 15px;
    }
    
    /* Títulos */
    h3 { color: #CE1126; text-align: center; margin-top: 30px; }
    
    /* Texto normal sin scroll */
    .texto-normal { font-size: 16px; line-height: 1.6; color: #333; }
    </style>
""", unsafe_allow_html=True)

# --- FUNCIÓN DE VENTANA MODAL (OPTIMIZADA MÓVIL) ---
@st.dialog("🇮🇹 DETALLES", width="large")
def abrir_ventana(titulo, texto, imagen_1=None, pie_1=None, imagen_2=None, pie_2=None):
    # Título en Grande
    st.subheader(titulo)
    
    # Caso 1: Una sola imagen (Monumentos, Restaurantes normales)
    if imagen_1 and not imagen_2:
        st.image(imagen_1, caption=pie_1, use_column_width=True)
    
    # Caso 2: Dos imágenes (Comparativa Comida)
    if imagen_1 and imagen_2:
        colA, colB = st.columns(2)
        with colA:
            st.image(imagen_1, caption=pie_1, use_column_width=True)
        with colB:
            st.image(imagen_2, caption=pie_2, use_column_width=True)

    # Texto limpio (Markdown puro, sin HTML que de problemas)
    st.markdown(texto)

# --- PORTADA ---
st.title("🇮🇹 Roma 2026")
st.markdown("**Paco & Trini | Dossier de Viaje**")

# Cuenta atrás
fecha_viaje = datetime(2026, 5, 22, 6, 40)
dias_faltan = (fecha_viaje - datetime.now()).days
if dias_faltan > 0:
    st.info(f"⏳ Faltan **{dias_faltan} días** para el viaje.")

# =========================================================
# DOMINGO 1: LLEGADA
# =========================================================
st.markdown("### 📆 DOMINGO 1: La Llegada")

# --- 14:00 TRANSPORTE ---
col1, col2 = st.columns([0.6, 0.4])
with col1:
    st.write("🕑 **14:00**")
    st.write("🛬 **Llegada y Traslado**")
with col2:
    if st.button("🚌 Ver Opciones", key="btn_transporte"):
        texto_transporte = """
        **🚆 OPCIÓN A: Tren Leonardo Express (RECOMENDADO)**
        * **Precio:** 14€ (28€ total).
        * **Tiempo:** 32 min (Directo a Termini).
        * **Por qué:** Es el más rápido y cómodo.
        
        ---
        **🚌 OPCIÓN B: Autobús (Bus TAM / Terravision)**
        * **Precio:** 7€ pax (14€ total).
        * **Tiempo:** 60 min (Depende mucho del tráfico).
        * **Nota:** Más barato, pero más lento.
        
        ---
        **🚖 OPCIÓN C: Taxi Oficial**
        * **Precio:** 50€ (Tarifa fija).
        * **Tiempo:** 45 min.
        * **Nota:** Puerta a puerta.
        """
        abrir_ventana("🚌 Transporte al Hotel", texto_transporte)

# --- 15:30 ALMUERZO (COMPARATIVA) ---
col1, col2 = st.columns([0.6, 0.4])
with col1:
    st.write("🕑 **15:30**")
    st.write("🍕 **Almuerzo: Elige**")
with col2:
    if st.button("🍽️ Dónde comer", key="btn_comida"):
        texto_comida = """
        **🏠 OPCIÓN 1: La Gallina Bianca**
        Ambiente clásico, tranquilo y con manteles. Ideal si queréis relajaros nada más llegar.
        * 💰 **Precio:** 50€ aprox.
        
        ---
        **🍕 OPCIÓN 2: Mercato Centrale**
        (Ver foto derecha) Situado bajo la estación. Mucho jaleo, moderno y divertido.
        * 💰 **Precio:** 30€ aprox.
        """
        abrir_ventana(
            "¿Dónde comemos hoy?", 
            texto_comida,
            imagen_1="https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=800&q=80",
            pie_1="Opción Relax: La Gallina Bianca",
            imagen_2="https://images.unsplash.com/photo-1533900298318-6b8da08a523e?w=800&q=80",
            pie_2="Opción Jaleo: Mercato Centrale"
        )

# --- 17:30 STA MARIA MAGGIORE ---
col1, col2 = st.columns([0.6, 0.4])
with col1:
    st.write("🕑 **17:30**")
    st.write("⛪ **Sta. Maria Maggiore**")
with col2:
    if st.button("📸 Guía Rápida", key="btn_maggiore"):
        texto_maggiore = """
        **✨ El Primer Oro de América**
        Mirad hacia arriba. El techo dorado que veis se hizo con el **primer oro que trajo Cristóbal Colón** de América, regalado por los Reyes Católicos al Papa.
        
        **❄️ La Leyenda de la Nieve**
        Se construyó aquí porque la Virgen señaló el lugar haciendo caer una nevada milagrosa... ¡en pleno mes de agosto!
        """
        abrir_ventana(
            "Basílica de Santa Maria Maggiore", 
            texto_maggiore, 
            imagen_1="https://images.unsplash.com/photo-1574088924962-d696116823c1?w=800&q=80",
            pie_1="El techo con el oro de América"
        )

# --- 18:30 SAN PIETRO IN VINCOLI ---
col1, col2 = st.columns([0.6, 0.4])
with col1:
    st.write("🕑 **18:30**")
    st.write("⛪ **San Pietro in Vincoli**")
with col2:
    if st.button("📸 Guía Rápida", key="btn_moises"):
        texto_moises = """
        **🗿 El Moisés de Miguel Ángel**
        Moisés no posa, está **enfadado**. Acaba de bajar del monte y ve a su pueblo adorando ídolos falsos.
        * Fíjate en la vena hinchada del brazo.
        * Fíjate en la tensión de los músculos.
        
        Dicen que es tan real que Miguel Ángel le tiró un martillo y le gritó: *"¡Habla!"*.
        
        **🔗 Las Cadenas**
        Bajo el altar están las cadenas reales con las que ataron a San Pedro en Jerusalén.
        """
        abrir_ventana(
            "El Moisés y las Cadenas", 
            texto_moises, 
            imagen_1="https://images.unsplash.com/photo-1555626049-74e50774a387?w=800&q=80",
            pie_1="La furia del Moisés"
        )

# --- 21:00 CENA MONTI ---
col1, col2 = st.columns([0.6, 0.4])
with col1:
    st.write("🕑 **21:00**")
    st.write("🍷 **Cena: Barrio Monti**")
with col2:
    if st.button("📍 Ver Sitio", key="btn_cena_monti"):
        texto_cena = """
        **Recomendación: Ai Tre Scalini**
        
        Es una taberna histórica (desde 1895) cubierta de hiedra en la fachada. Es el sitio perfecto para sentir el ambiente romano de verdad.
        
        * **Qué pedir:** Tabla de quesos y un buen vino de la casa.
        * **Presupuesto:** 50€ (Pareja).
        """
        abrir_ventana(
            "Cena en Ai Tre Scalini", 
            texto_cena, 
            imagen_1="https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=800&q=80",
            pie_1="Ambiente de taberna romana (Barrio Monti)"
        )

# =========================================================
# (AQUÍ IRÁN EL RESTO DE DÍAS - MANTENGO LA ESTRUCTURA)
# =========================================================
st.markdown("---")
st.caption("Dossier interactivo creado para Paco y Trini.")
