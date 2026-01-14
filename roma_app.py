import streamlit as st
from datetime import datetime

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Roma 2026", page_icon="🇮🇹", layout="centered")

# --- ESTILOS CSS (DISEÑO PREMIUM MÓVIL) ---
st.markdown("""
    <style>
    .stApp { background-color: #Fdfcf0; }
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
    h1, h2, h3 { color: #CE1126; text-align: center; font-family: sans-serif; }
    .texto-guia { font-size: 16px; line-height: 1.6; color: #2c3e50; }
    </style>
""", unsafe_allow_html=True)

# --- FUNCIÓN DE VENTANA MODAL ---
@st.dialog("🇮🇹 DETALLES DEL VIAJE", width="large")
def abrir_ventana(titulo, texto_markdown, img1=None, pie1=None, img2=None, pie2=None):
    st.markdown(f"## {titulo}")
    
    # Mostrar imágenes con la función de ancho de contenedor actualizada
    if img1 and not img2:
        st.image(img1, caption=pie1, use_container_width=True)
    if img1 and img2:
        c1, c2 = st.columns(2)
        with c1: st.image(img1, caption=pie1, use_container_width=True)
        with c2: st.image(img2, caption=pie2, use_container_width=True)
    
    st.markdown(texto_markdown)

# --- PORTADA ---
st.title("🇮🇹 Roma 2026")
st.markdown("### Paco & Mari Trini")

fecha_viaje = datetime(2026, 5, 22, 6, 40)
dias = (fecha_viaje - datetime.now()).days
if dias > 0:
    st.success(f"⏳ **Faltan {dias} días** para nuestro gran viaje.")

# =========================================================
# DOMINGO 1: LA LLEGADA
# =========================================================
st.markdown("---")
st.markdown("### 📆 DOMINGO 1: Benvenuti")

# 1. TRANSPORTE
col1, col2 = st.columns([0.6, 0.4])
with col1:
    st.write("🕑 **14:00**")
    st.write("🛬 **Llegada y Traslado**")
with col2:
    if st.button("🚌 Ver Info", key="t_dom"):
        info_t = """
        **TRASLADO AL HOTEL:**
        
        * **🚆 Leonardo Express:** 14€ por persona. Directo a Termini (32 min).
        * **🚌 Autobús:** 7€ por persona. Tarda 1 hora o más.
        * **🚖 Taxi:** Tarifa fija de 50€.
        """
        abrir_ventana("Transporte al Centro", info_t)

# 2. ALMUERZO
col1, col2 = st.columns([0.6, 0.4])
with col1:
    st.write("🕑 **15:30**")
    st.write("🍕 **Almuerzo: Dos opciones**")
with col2:
    if st.button("🍽️ Ver Sitios", key="l_dom"):
        info_c = """
        **OPCIONES CERCA DEL HOTEL:**
        
        1. **La Gallina Bianca:** Clásico y acogedor. (50€ aprox).
        2. **Mercato Centrale:** Moderno y variado. (30€ aprox).
        """
        # Imágenes de alta disponibilidad
        abrir_ventana("Opciones de Almuerzo", info_c, 
                       img1="https://images.pexels.com/photos/262978/pexels-photo-262978.jpeg", pie1="La Gallina Bianca",
                       img2="https://images.pexels.com/photos/1035665/pexels-photo-1035665.jpeg", pie2="Mercato Centrale")

# 3. SANTA MARIA MAGGIORE
col1, col2 = st.columns([0.6, 0.4])
with col1:
    st.write("🕑 **17:30**")
    st.write("⛪ **Sta. Maria Maggiore**")
with col2:
    if st.button("📸 Guía Rápida", key="sm_dom"):
        info_g1 = """
        **BASÍLICA DE SANTA MARIA MAGGIORE**
        
        * **Oro de América:** El techo dorado se hizo con el primer oro traído por Colón.
        * **Nieve en Agosto:** Según la leyenda, la Virgen señaló el lugar con una nevada.
        """
        abrir_ventana("Guía: Santa Maria Maggiore", info_g1, 
                       img1="https://images.pexels.com/photos/2349165/pexels-photo-2349165.jpeg", 
                       pie1="Interior de la Basílica")

# 4. EL MOISÉS
col1, col2 = st.columns([0.6, 0.4])
with col1:
    st.write("🕑 **18:30**")
    st.write("⛪ **San Pietro / El Moisés**")
with col2:
    if st.button("📸 Guía Rápida", key="mo_dom"):
        info_g2 = """
        **EL MOISÉS DE MIGUEL ÁNGEL**
        
        * **Detalle:** Fíjate en la vena del brazo y la barba.
        * **Dato:** Los cuernos son por un error de traducción antiguo.
        * **Cadenas:** Aquí se guardan las que ataron a San Pedro.
        """
        abrir_ventana("Guía: El Moisés", info_g2, 
                       img1="https://images.pexels.com/photos/15942475/pexels-photo-15942475.jpeg", 
                       pie1="Obra de Miguel Ángel")

# 5. CENA MONTI
col1, col2 = st.columns([0.6, 0.4])
with col1:
    st.write("🕑 **21:00**")
    st.write("🍷 **Cena: Barrio Monti**")
with col2:
    if st.button("📍 Ver Sitio", key="ce_dom"):
        info_c2 = """
        **CENA EN BARRIO MONTI**
        
        * **Lugar:** Ai Tre Scalini o similar.
        * **Ambiente:** Calles bohemias con hiedra.
        * **Menú:** Tablas y vino. (50€ aprox).
        """
        abrir_ventana("Cena en Monti", info_c2, 
                       img1="https://images.pexels.com/photos/1797161/pexels-photo-1797161.jpeg", 
                       pie1="El encanto de Monti")

st.markdown("---")
st.markdown("<h4 style='text-align: center; color: #555;'>Hecho con ilusión de Paco para Mari Trini</h4>", unsafe_allow_html=True)
st.caption("Dossier Interactivo Roma 2026")
