import streamlit as st
from datetime import datetime

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Roma 2026", page_icon="🇮🇹", layout="centered")

# --- ESTILOS CSS (DISEÑO PREMIUM) ---
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
    </style>
""", unsafe_allow_html=True)

# --- FUNCIÓN DE VENTANA MODAL ---
@st.dialog("🇮🇹 DETALLES DEL VIAJE", width="large")
def abrir_ventana(titulo, texto_markdown, img1=None, pie1=None, img2=None, pie2=None):
    st.markdown(f"## {titulo}")
    
    # Mostrar imágenes con enlaces verificados
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
    if st.button("🚌 Ver Info", key="t_real"):
        info_t = """
        **TRASLADO AL HOTEL:**
        
        * **🚆 Leonardo Express:** 14€ por persona. Directo a Termini (32 min).
        * **🚌 Autobús:** 7€ por persona.
        * **🚖 Taxi:** Tarifa fija de 50€.
        """
        abrir_ventana("Transporte al Centro", info_t, 
                       img1="https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Trenitalia_Leonardo_Express.jpg/800px-Trenitalia_Leonardo_Express.jpg", 
                       pie1="El tren Leonardo Express en Fiumicino")

# 2. ALMUERZO
col1, col2 = st.columns([0.6, 0.4])
with col1:
    st.write("🕑 **15:30**")
    st.write("🍕 **Almuerzo: Dos opciones**")
with col2:
    if st.button("🍽️ Ver Sitios", key="l_real"):
        info_c = """
        **OPCIONES CERCA DEL HOTEL:**
        
        1. **La Gallina Bianca:** Cocina tradicional, ambiente relajado.
        2. **Mercato Centrale:** Puestos artesanos bajo la estación.
        """
        abrir_ventana("Opciones de Almuerzo", info_c, 
                       img1="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Restaurant_interior_in_Rome.jpg/800px-Restaurant_interior_in_Rome.jpg", pie1="Interior rústico (La Gallina Bianca)",
                       img2="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Roma_Termini_Mercato_Centrale.jpg/800px-Roma_Termini_Mercato_Centrale.jpg", pie2="Mercato Centrale Termini")

# 3. SANTA MARIA MAGGIORE
col1, col2 = st.columns([0.6, 0.4])
with col1:
    st.write("🕑 **17:30**")
    st.write("⛪ **Sta. Maria Maggiore**")
with col2:
    if st.button("📸 Guía Rápida", key="sm_real"):
        info_g1 = """
        **BASÍLICA DE SANTA MARIA MAGGIORE**
        
        * **El Techo:** Mira arriba, es el primer oro traído de América.
        * **La Leyenda:** Construida tras una nevada milagrosa en agosto.
        """
        abrir_ventana("Guía: Santa Maria Maggiore", info_g1, 
                       img1="https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/S_Maria_Maggiore_ceiling.jpg/800px-S_Maria_Maggiore_ceiling.jpg", 
                       pie1="El techo dorado original")

# 4. EL MOISÉS
col1, col2 = st.columns([0.6, 0.4])
with col1:
    st.write("🕑 **18:30**")
    st.write("⛪ **San Pietro / El Moisés**")
with col2:
    if st.button("📸 Guía Rápida", key="mo_real"):
        info_g2 = """
        **EL MOISÉS DE MIGUEL ÁNGEL**
        
        * **Furia en Piedra:** Fíjate en la mirada y la tensión de sus manos.
        * **Cadenas:** Debajo del altar están las cadenas de San Pedro.
        """
        abrir_ventana("Guía: El Moisés", info_g2, 
                       img1="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Mois%C3%A9s_de_Miguel_%C3%81ngel_en_San_Pietro_in_Vincoli.jpg/800px-Mois%C3%A9s_de_Miguel_%C3%81ngel_en_San_Pietro_in_Vincoli.jpg", 
                       pie1="Estatua real en San Pietro in Vincoli")

# 5. CENA MONTI
col1, col2 = st.columns([0.6, 0.4])
with col1:
    st.write("🕑 **21:00**")
    st.write("🍷 **Cena: Barrio Monti**")
with col2:
    if st.button("📍 Ver Sitio", key="ce_real"):
        info_c2 = """
        **BARRIO MONTI:**
        
        Es el barrio más bohemio. Calles de piedra, fachadas con hiedra y vinerías históricas como *Ai Tre Scalini*.
        """
        abrir_ventana("Cena en Monti", info_c2, 
                       img1="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Via_Panisperna_-_Rione_Monti.jpg/800px-Via_Panisperna_-_Rione_Monti.jpg", 
                       pie1="Fachadas típicas de Monti con hiedra")

st.markdown("---")
st.markdown("<h4 style='text-align: center; color: #555;'>Hecho con ilusión de Paco para Mari Trini</h4>", unsafe_allow_html=True)
st.caption("Dossier Interactivo Roma 2026")
