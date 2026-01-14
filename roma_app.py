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
        padding: 16px;
        border-radius: 12px;
        border: 2px solid #008C45;
        color: #008C45;
        font-weight: bold;
        font-size: 17px;
        background-color: white;
        transition: all 0.2s;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    div.stButton > button:hover {
        background-color: #008C45;
        color: white;
        transform: scale(1.01);
    }
    h1, h2, h3 { color: #CE1126; font-family: sans-serif; text-align: center; }
    .texto-guia { font-size: 16px; line-height: 1.6; color: #2c3e50; }
    </style>
""", unsafe_allow_html=True)

# --- FUNCIÓN DE VENTANA (MODAL) ---
@st.dialog("🇮🇹 GUÍA DE VIAJE", width="large")
def abrir_ventana(titulo, texto, imagen_1=None, pie_1=None, imagen_2=None, pie_2=None):
    st.markdown(f"<h2 style='text-align: center; color: #CE1126;'>{titulo}</h2>", unsafe_allow_html=True)
    
    if imagen_1 and not imagen_2:
        st.image(imagen_1, caption=pie_1, use_column_width=True)
    
    if imagen_1 and imagen_2:
        colA, colB = st.columns(2)
        with colA:
            st.image(imagen_1, caption=pie_1, use_column_width=True)
        with colB:
            st.image(imagen_2, caption=pie_2, use_column_width=True)

    st.markdown(f"<div class='texto-guia'>{texto}</div>", unsafe_allow_html=True)

# --- PORTADA ---
st.title("🇮🇹 Roma 2026")
st.markdown("<h3 style='margin-top:0;'>Paco & Trini</h3>", unsafe_allow_html=True)

fecha_viaje = datetime(2026, 5, 22, 6, 40)
dias_faltan = (fecha_viaje - datetime.now()).days
if dias_faltan > 0:
    st.success(f"⏳ **Faltan {dias_faltan} días** para el despegue.")

# =========================================================
# DOMINGO 1: BENAVENTI
# =========================================================
st.markdown("### 📆 DOMINGO 1: Benvenuti")

# --- 14:00 TRANSPORTE ---
col1, col2 = st.columns([0.6, 0.4])
with col1:
    st.write("🕑 **14:00 | Llegada**")
    st.caption("Fiumicino")
with col2:
    if st.button("🚌 Transporte", key="btn_transporte"):
        texto_t = """
        **🚆 OPCIÓN A: Leonardo Express (RECOMENDADO)**
        * **Precio:** 14€ (28€ total).
        * **Tiempo:** 32 min (Directo a Termini).
        
        ---
        **🚌 OPCIÓN B: Autobús**
        * **Precio:** 7€ pax (14€ total).
        * **Tiempo:** 60 min aprox.
        
        ---
        **🚖 OPCIÓN C: Taxi Oficial**
        * **Precio:** 50€ (Tarifa fija).
        """
        abrir_ventana("🚌 Cómo llegar al Hotel", texto_t)

# --- 15:30 ALMUERZO ---
col1, col2 = st.columns([0.6, 0.4])
with col1:
    st.write("🕑 **15:30 | Almuerzo**")
    st.caption("Dos opciones")
with col2:
    if st.button("🍽️ Ver Opciones", key="btn_comida"):
        texto_c = """
        **🏠 OPCIÓN 1: La Gallina Bianca**
        Ambiente clásico, tranquilo y con manteles.
        * **Precio:** 50€ aprox.
        
        ---
        **🍕 OPCIÓN 2: Mercato Centrale**
        Moderno, vibrante y con mucho jaleo.
        * **Precio:** 30€ aprox.
        """
        abrir_ventana(
            "¿Dónde comemos hoy?", 
            texto_c,
            imagen_1="https://images.unsplash.com/photo-1551183053-bf91a1d81141?w=800",
            pie_1="La Gallina Bianca",
            imagen_2="https://images.unsplash.com/photo-1533900298318-6b8da08a523e?w=800",
            pie_2="Mercato Centrale"
        )

# --- 17:30 STA MARIA MAGGIORE ---
col1, col2 = st.columns([0.6, 0.4])
with col1:
    st.write("🕑 **17:30 | Sta. M. Maggiore**")
    st.caption("Basílica Mayor")
with col2:
    if st.button("📸 Ver Guía", key="btn_maggiore"):
        texto_m = """
        **✨ EL ORO DE AMÉRICA**
        Mirad el techo dorado. Fue decorado con **el primer oro que Cristóbal Colón trajo de América**.
        
        **❄️ LA LEYENDA DE LA NIEVE**
        Se construyó aquí porque la Virgen señaló el lugar haciendo caer una nevada milagrosa en agosto.
        """
        abrir_ventana(
            "Basílica de Sta. Maria Maggiore", 
            texto_m, 
            imagen_1="https://images.unsplash.com/photo-1616422201931-18e478546f6e?w=800", 
            pie_1="Interior de la Basílica"
        )

# --- 18:30 MOISÉS ---
col1, col2 = st.columns([0.6, 0.4])
with col1:
    st.write("🕑 **18:30 | El Moisés**")
    st.caption("S. Pietro in Vincoli")
with col2:
    if st.button("📸 Ver Guía", key="btn_moises"):
        texto_mo = """
        **🗿 EL MOISÉS DE MIGUEL ÁNGEL**
        Moisés no posa, está **enfadado**. Fíjate en la vena hinchada del brazo y la tensión de los músculos.
        
        Dicen que es tan real que Miguel Ángel le tiró un martillo y le gritó: *"¡Habla!"*.
        """
        abrir_ventana(
            "El Moisés de Miguel Ángel", 
            texto_mo, 
            imagen_1="https://images.unsplash.com/photo-1605368307405-f938c538a7c5?w=800", 
            pie_1="Detalle de la escultura"
        )

# --- 21:00 CENA ---
col1, col2 = st.columns([0.6, 0.4])
with col1:
    st.write("🕑 **21:00 | Cena**")
    st.caption("Barrio Monti")
with col2:
    if st.button("📍 Ver Sitio", key="btn_cena"):
        texto_ce = """
        **RECOMENDACIÓN: AI TRE SCALINI**
        Es una taberna histórica con la fachada cubierta de hiedra. Sitio perfecto para sentir el ambiente romano.
        
        * **Qué pedir:** Tabla de embutidos y vino.
        * **Presupuesto:** 50€ (Pareja).
        """
        abrir_ventana(
            "Cena en Ai Tre Scalini", 
            texto_ce, 
            imagen_1="https://images.unsplash.com/photo-1541604193435-22287d32c2c2?w=800", 
            pie_1="Ambiente nocturno en Roma"
        )

st.markdown("---")
st.caption("Hecho con ❤️ por Paco para Trini.")
