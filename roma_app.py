import streamlit as st
from datetime import datetime

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Roma 2026", page_icon="🇮🇹", layout="centered")

# --- ESTILOS CSS (DISEÑO PREMIUM) ---
st.markdown("""
    <style>
    /* Fondo crema suave */
    .stApp { background-color: #Fdfcf0; }
    
    /* Botones grandes y elegantes para el dedo */
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
    
    /* Títulos */
    h3 { color: #CE1126; text-align: center; margin-top: 35px; font-family: sans-serif; }
    
    /* Textos explicativos */
    .texto-guia { font-size: 16px; line-height: 1.6; color: #2c3e50; margin-top: 15px; }
    .destacado { font-weight: bold; color: #CE1126; }
    
    /* Líneas separadoras sutiles */
    hr { margin-top: 20px; margin-bottom: 20px; border: 0; border-top: 1px solid #eee; }
    </style>
""", unsafe_allow_html=True)

# --- FUNCIÓN DE VENTANA (MODAL) ---
@st.dialog("🇮🇹 GUÍA DE VIAJE", width="large")
def abrir_ventana(titulo, texto, imagen_1=None, pie_1=None, imagen_2=None, pie_2=None):
    st.markdown(f"<h2 style='text-align: center; color: #CE1126; margin-bottom: 20px;'>{titulo}</h2>", unsafe_allow_html=True)
    
    # Caso A: Una sola imagen (Monumentos/Cenas)
    if imagen_1 and not imagen_2:
        st.image(imagen_1, caption=pie_1, use_column_width=True)
    
    # Caso B: Dos imágenes (Comparativa Comida)
    if imagen_1 and imagen_2:
        colA, colB = st.columns(2)
        with colA:
            st.image(imagen_1, caption=pie_1, use_column_width=True)
        with colB:
            st.image(imagen_2, caption=pie_2, use_column_width=True)

    # Texto limpio
    st.markdown(f"<div class='texto-guia'>{texto}</div>", unsafe_allow_html=True)

# --- PORTADA ---
st.title("🇮🇹 Roma 2026")
st.markdown("**Paco & Trini | Dossier de Viaje**")

# Cuenta atrás
fecha_viaje = datetime(2026, 5, 22, 6, 40)
dias_faltan = (fecha_viaje - datetime.now()).days
if dias_faltan > 0:
    st.success(f"⏳ **Faltan {dias_faltan} días** para el despegue.")

# =========================================================
# DOMINGO 1: LA LLEGADA
# =========================================================
st.markdown("### 📆 DOMINGO 1: Benvenuti a Roma")

# --- 14:00 TRANSPORTE ---
col1, col2 = st.columns([0.6, 0.4], gap="small")
with col1:
    st.write("🕑 **14:00 | Llegada**")
    st.caption("Aeropuerto Fiumicino")
with col2:
    if st.button("🚌 Transporte", key="btn_transporte"):
        texto = """
        <span class="destacado">🚆 OPCIÓN A: Leonardo Express (RECOMENDADO)</span><br>
        Es la opción más segura. Os ahorráis los atascos de entrada a Roma.<br>
        • <b>Precio:</b> 14€ (28€ total).<br>
        • <b>Tiempo:</b> 32 min (Directo a Termini).
        <hr>
        <span class="destacado">🚌 OPCIÓN B: Autobús (Bus TAM / Terravision)</span><br>
        Opción económica, pero arriesgada con el tráfico.<br>
        • <b>Precio:</b> 7€ pax (14€ total).<br>
        • <b>Tiempo:</b> 60 min aprox.
        <hr>
        <span class="destacado">🚖 OPCIÓN C: Taxi Oficial</span><br>
        Tarifa fija por ley. Cómodo si estáis agotados.<br>
        • <b>Precio:</b> 50€ (Total).<br>
        • <b>Tiempo:</b> 45 min.
        """
        abrir_ventana("🚌 Cómo llegar al Hotel", texto)

# --- 15:30 ALMUERZO ---
col1, col2 = st.columns([0.6, 0.4], gap="small")
with col1:
    st.write("🕑 **15:30 | Almuerzo**")
    st.caption("Dos opciones cerca")
with col2:
    if st.button("🍽️ Ver Opciones", key="btn_comida"):
        texto = """
        <span class="destacado">🏠 OPCIÓN 1: La Gallina Bianca</span><br>
        Restaurante clásico con manteles de tela. Ideal para descansar y comer la primera pasta con tranquilidad.<br>
        • <b>Presupuesto:</b> 50€ aprox.
        <hr>
        <span class="destacado">🍕 OPCIÓN 2: Mercato Centrale</span><br>
        (Foto dcha). Situado bajo la estación. Es un mercado gastronómico moderno con mucho ambiente y jaleo.<br>
        • <b>Presupuesto:</b> 30€ aprox.
        """
        abrir_ventana(
            "¿Dónde comemos hoy?", 
            texto,
            imagen_1="https://images.unsplash.com/photo-1559339352-11d035aa65de?w=800&q=80",
            pie_1="La Gallina Bianca (Relax)",
            imagen_2="https://images.unsplash.com/photo-1533900298318-6b8da08a523e?w=800&q=80",
            pie_2="Mercato Centrale (Jaleo)"
        )

# --- 17:30 STA MARIA MAGGIORE ---
col1, col2 = st.columns([0.6, 0.4], gap="small")
with col1:
    st.write("🕑 **17:30 | Sta. M. Maggiore**")
    st.caption("Basílica Mayor")
with col2:
    if st.button("📸 Ver Guía", key="btn_maggiore"):
        texto = """
        <b>✨ EL ORO DE AMÉRICA</b><br>
        Fijaos en el impresionante techo dorado. Fue decorado con <b>el primer oro que Cristóbal Colón trajo de América</b>, un regalo de los Reyes Católicos al Papa Alejandro VI.<br><br>
        <b>❄️ EL MILAGRO DE LA NIEVE</b><br>
        Esta iglesia se construyó aquí porque, según la leyenda, la Virgen señaló el lugar haciendo caer una nevada milagrosa... ¡en pleno mes de agosto!
        """
        # FOTO NUEVA (Interior Dorado)
        abrir_ventana("Basílica de Sta. Maria Maggiore", texto, imagen_1="https://images.unsplash.com/photo-1589182373726-e4f658ab50f0?w=800&q=80", pie_1="El techo con el oro de América")

# --- 18:30 MOISÉS ---
col1, col2 = st.columns([0.6, 0.4], gap="small")
with col1:
    st.write("🕑 **18:30 | S. Pietro in Vincoli**")
    st.caption("El Moisés")
with col2:
    if st.button("📸 Ver Guía", key="btn_moises"):
        texto = """
        <b>🗿 EL MOISÉS DE MIGUEL ÁNGEL</b><br>
        Esta es una de las esculturas más potentes de la historia. Moisés no posa, está <b>enfadado</b>. Acaba de bajar del monte y ve a su pueblo adorando ídolos. Fíjate en la vena hinchada del brazo y la tensión muscular.<br><br>
        Dicen que es tan real que Miguel Ángel le tiró un martillo y le gritó: <i>"¡Habla!"</i>.<br><br>
        <b>🔗 LAS CADENAS</b><br>
        Bajo el altar se guardan las cadenas reales con las que ataron a San Pedro en Jerusalén.
        """
        # FOTO NUEVA (Estatua)
        abrir_ventana("El Moisés y las Cadenas", texto, imagen_1="https://images.unsplash.com/photo-1552432655-b40410d5135d?w=800&q=80", pie_1="Detalle de la escultura")

# --- 21:00 CENA MONTI ---
col1, col2 = st.columns([0.6, 0.4], gap="small")
with col1:
    st.write("🕑 **21:00 | Cena**")
    st.caption("Barrio Monti")
with col2:
    if st.button("📍 Ver Sitio", key="btn_cena"):
        texto = """
        <b>RECOMENDACIÓN: AI TRE SCALINI</b><br>
        Es una taberna histórica (desde 1895) con la fachada cubierta de hiedra. Es el sitio perfecto para sentir el ambiente romano de verdad, con buenos vinos y tablas de embutidos.<br><br>
        • <b>Presupuesto:</b> 50€ (Pareja).
        """
        # FOTO NUEVA (Calle romana con encanto)
        abrir_ventana("Cena en Ai Tre Scalini", texto, imagen_1="https://images.unsplash.com/photo-1555992336-03a231365110?w=800&q=80", pie_1="Ambiente nocturno en Monti")

# =========================================================
# (AQUÍ IRÁN LUNES, MARTES, MIÉRCOLES...)
# =========================================================
st.markdown("---")
st.caption("Hecho con ❤️ por Paco para Trini.")
