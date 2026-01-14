import streamlit as st
from datetime import datetime

# Configuración de la página
st.set_page_config(page_title="Roma 2026 - Paco & Trini",
                   page_icon="🇮🇹", layout="centered")

# --- LÓGICA DE LA CUENTA ATRÁS ---
fecha_viaje = datetime(2026, 5, 22, 6, 40)
ahora = datetime.now()
diferencia = fecha_viaje - ahora
dias_faltan = diferencia.days

# --- ESTILO PERSONALIZADO ---
st.markdown(f"""
    <style>
    .stApp {{ background-color: #Fdfcf0; }}
    .card {{
        background: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        border-top: 5px solid #008C45;
        margin-bottom: 20px;
    }}
    .cuenta-atras {{
        background: #CE1126;
        color: white;
        padding: 10px;
        border-radius: 10px;
        text-align: center;
        font-weight: bold;
        font-size: 1.2rem;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- CABECERA ---
st.title("🇮🇹 Roma 2026")
st.subheader("La aventura de Paco y Trini")

if dias_faltan > 0:
    st.markdown(
        f'<div class="cuenta-atras">🚀 ¡Solo faltan {dias_faltan} días para el gran viaje!</div>', unsafe_allow_html=True)

st.image("https://images.unsplash.com/photo-1552832230-c0197dd311b5?w=800&q=80")

# --- PESTAÑAS ---
tab1, tab2, tab3 = st.tabs(["📅 ITINERARIO", "🍝 GASTRONOMÍA", "🚇 LOGÍSTICA"])

with tab1:
    st.markdown("### 📅 ¿Dónde comemos el primer día?")

    with st.expander("DOMINGO 1: Opciones de Almuerzo", expanded=True):
        opcion_domingo = st.radio(
            "Selecciona un lugar para ver el ambiente:",
            ["🏠 La Gallina Bianca (Clásico)", "🍕 Mercato Centrale (Moderno)"],
            index=0,
            key="comida_domingo"
        )

        if opcion_domingo == "🏠 La Gallina Bianca (Clásico)":
            # ESTA ES LA FOTO RÚSTICA REAL
            st.image("https://images.unsplash.com/photo-1551183053-bf91a1d81141?w=800&q=80",
                     caption="La Gallina Bianca - Interior rústico y tradicional")
            st.markdown("""<div class="card">
                <h4>La Gallina Bianca</h4>
                <p>Mesas de madera, ambiente cálido y cocina tradicional romana. A un paso del hotel.</p>
            </div>""", unsafe_allow_html=True)
        else:
            # ESTA ES LA FOTO DEL AMBIENTE DEL MERCADO
            st.image("https://images.unsplash.com/photo-1543007630-9710e4a00a20?w=800&q=80",
                     caption="Mercato Centrale Termini - El ambiente de las mesas comunes")
            st.markdown("""<div class="card" style="border-top-color: #f39c12;">
                <h4>Mercato Centrale</h4>
                <p>Bajo la estación. Un espacio vivo donde se comparte mesa y se disfruta de la mejor comida artesana.</p>
            </div>""", unsafe_allow_html=True)

    with st.expander("MARTES 3: Cantina e Cucina"):
        st.success("🍝 **LA CITA ESPECIAL**")
        if st.button("Ver el ambiente de Cantina e Cucina"):
            st.image("https://images.unsplash.com/photo-1559339352-11d035aa65de?w=800&q=80",
                     caption="El estilo alegre y rústico de Cantina e Cucina")

st.divider()
st.caption("Dossier interactivo finalizado por Paco.")
