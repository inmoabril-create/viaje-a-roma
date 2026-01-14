import streamlit as st
from datetime import datetime

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Roma 2026", page_icon="🇮🇹", layout="centered")

# --- ESTILOS CSS (DISEÑO LIMPIO Y MÓVIL) ---
st.markdown("""
    <style>
    /* Fondo crema suave */
    .stApp { background-color: #Fdfcf0; }
    
    /* Botones grandes y cómodos para el dedo */
    div.stButton > button {
        width: 100%;
        padding: 18px;
        border-radius: 15px;
        border: 2px solid #008C45;
        color: #008C45;
        font-weight: bold;
        font-size: 18px;
        background-color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    div.stButton > button:hover {
        background-color: #008C45;
        color: white;
    }
    
    /* Títulos */
    h1, h2, h3 { color: #CE1126; text-align: center; font-family: sans-serif; }
    </style>
""", unsafe_allow_html=True)

# --- FUNCIÓN DE VENTANA MODAL ---
@st.dialog("🇮🇹 DETALLES DEL VIAJE", width="large")
def abrir_ventana(titulo, texto_markdown, img1=None, pie1=None, img2=None, pie2=None):
    st.subheader(titulo)
    
    # Mostrar imágenes
    if img1 and not img2:
        st.image(img1, caption=pie1, use_column_width=True)
    if img1 and img2:
        c1, c2 = st.columns(2)
        with c1: st.image(img1, caption=pie1, use_column_width=True)
        with c2: st.image(img2, caption=pie2, use_column_width=True)
    
    # Texto limpio sin signos de programación
    st.markdown(texto_markdown)

# --- PORTADA ---
st.title("🇮🇹 Roma 2026")
st.markdown("### Paco & Trini")

# Cuenta atrás
fecha_viaje = datetime(2026, 5, 22, 6, 40)
dias = (fecha_viaje - datetime.now()).days
if dias > 0:
    st.success(f"⏳ **Faltan {dias} días** para nuestro gran viaje.")

# =========================================================
# DOMINGO 1
# =========================================================
st.markdown("---")
st.markdown("### 📆 DOMINGO 1: La Llegada")

# 1. TRANSPORTE
col1, col2 = st.columns([0.6, 0.4])
with col1:
    st.write("🕑 **14:00**")
    st.write("🛬 **Llegada y Traslado**")
with col2:
    if st.button("🚌 Ver Info", key="t1"):
        info_t = """
        **TRANSPORTE AL HOTEL:**
        
        * **🚆 Leonardo Express:** 14€ por persona. Es directo a Termini (32 min). La mejor opción para evitar atascos.
        * **🚌 Autobús:** 7€ por persona. Más barato, pero tarda 1 hora o más.
        * **🚖 Taxi:** Tarifa fija de 50€. Cómodo si llevamos mucho peso.
        """
        abrir_ventana("Transporte", info_t)

# 2. ALMUERZO
col1, col2 = st.columns([0.6, 0.4])
with col1:
    st.write("🕑 **15:30**")
    st.write("🍕 **Almuerzo: Dos opciones**")
with col2:
    if st.button("🍽️ Ver Sitios", key="c1"):
        info_c = """
        **¿DÓNDE COMEMOS?**
        
        1. **La Gallina Bianca:** Estilo clásico romano, muy tranquilo. Perfecto para el primer contacto. (Precio: 50€ aprox).
        2. **Mercato Centrale:** Bajo la estación. Moderno, con muchos puestos y mucha vida. (Precio: 30€ aprox).
        """
        abrir_ventana("Opciones de Almuerzo", info_c, 
                       img1="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Santa_Maria_Maggiore_Interior_Rome.jpg/800px-Santa_Maria_Maggiore_Interior_Rome.jpg", pie1="Cerca de Sta. Maria",
                       img2="https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Mercato_Centrale_Termini.jpg/800px-Mercato_Centrale_Termini.jpg", pie2="Mercato Centrale")

# 3. SANTA MARIA MAGGIORE
col1, col2 = st.columns([0.6, 0.4])
with col1:
    st.write("🕑 **17:30**")
    st.write("⛪ **Sta. Maria Maggiore**")
with col2:
    if st.button("📸 Ver Guía", key="g1"):
        info_g1 = """
        **BASÍLICA DE SANTA MARIA MAGGIORE**
        
        * **El Oro:** El techo está decorado con el primer oro traído de América por Colón.
        * **La Nieve:** Se dice que la Virgen indicó dónde construirla haciendo nevar un 5 de agosto.
        """
        # Foto del interior dorado real (Wikimedia)
        abrir_ventana("Guía: Santa Maria Maggiore", info_g1, 
                       img1="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Santa_Maria_Maggiore_Interior_Rome.jpg/1024px-Santa_Maria_Maggiore_Interior_Rome.jpg", 
                       pie1="Interior de la Basílica")

# 4. EL MOISÉS
col1, col2 = st.columns([0.6, 0.4])
with col1:
    st.write("🕑 **18:30**")
    st.write("⛪ **San Pietro / El Moisés**")
with col2:
    if st.button("📸 Ver Guía", key="g2"):
        info_g2 = """
        **EL MOISÉS DE MIGUEL ÁNGEL**
        
        * **Furia Real:** Fíjate en la vena del brazo. Miguel Ángel quería que la piedra "hablara".
        * **Las Cadenas:** En esta iglesia están las cadenas reales que ataron a San Pedro.
        """
        # Foto del Moisés real (Wikimedia)
        abrir_ventana("Guía: El Moisés", info_g2, 
                       img1="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/Michelangelo%27s_Moses_at_San_Pietro_in_Vincoli_01.jpg/800px-Michelangelo%27s_Moses_at_San_Pietro_in_Vincoli_01.jpg", 
                       pie1="El Moisés en San Pietro in Vincoli")

# 5. CENA MONTI
col1, col2 = st.columns([0.6, 0.4])
with col1:
    st.write("🕑 **21:00**")
    st.write("🍷 **Cena: Barrio Monti**")
with col2:
    if st.button("📍 Ver Sitio", key="c2"):
        info_c2 = """
        **CENA EN BARRIO MONTI**
        
        * **Lugar:** Ai Tre Scalini.
        * **Ambiente:** Es una vinería histórica con la fachada llena de hiedra. 
        * **Plan:** Tablas de quesos, embutidos y buen vino italiano. (Precio: 50€ aprox).
        """
        # Foto estética de calle en Monti (No cóctel)
        abrir_ventana("Cena en Monti", info_c2, 
                       img1="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Via_Panisperna_-_Rione_Monti.jpg/800px-Via_Panisperna_-_Rione_Monti.jpg", 
                       pie1="Las encantadoras calles de Monti")

st.markdown("---")
st.caption("Hecho con ilusión para Paco y Trini.")
