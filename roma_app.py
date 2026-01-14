import streamlit as st
from datetime import datetime

# Configuración de la página
st.set_page_config(page_title="Roma 2026 - Paco & Trini", page_icon="🇮🇹", layout="centered")

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
    st.markdown(f'<div class="cuenta-atras">🚀 ¡Solo faltan {dias_faltan} días para el gran viaje!</div>', unsafe_allow_html=True)

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
            # FOTO BUENA: Interior elegante
            st.image("https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=800&q=80", 
                     caption="Ambiente clásico y acogedor (La Gallina Bianca)")
            st.markdown("""<div class="card">
                <h4>La Gallina Bianca</h4>
                <p>Estilo tradicional romano con manteles y ambiente tranquilo. Ideal para descansar y comer bien cerca del hotel.</p>
                <p><b>💰 Precio:</b> 45€ - 55€ (Pareja)</p>
            </div>""", unsafe_allow_html=True)
        else:
            # FOTO MERCADO: Gente y ambiente
            st.image("https://images.unsplash.com/photo-1533900298318-6b8da08a523e?w=800&q=80", 
                     caption="Mercato Centrale Termini - Ambiente vibrante")
            st.markdown("""<div class="card" style="border-top-color: #f39c12;">
                <h4>Mercato Centrale</h4>
                <p>Un espacio inmenso y moderno bajo la estación. Mucha vida, puestos variados y mesas compartidas.</p>
                <p><b>💰 Precio:</b> 25€ - 40€ (Pareja)</p>
            </div>""", unsafe_allow_html=True)

    with st.expander("MARTES 3: Cantina e Cucina"):
        st.success("🍝 **NUESTRO SITIO ESPECIAL**")
        if st.button("Ver el ambiente de Cantina e Cucina"):
            st.image("https://images.unsplash.com/photo-1559339352-11d035aa65de?w=800&q=80", 
                     caption="Decoración alegre y rústica típica de Cantina e Cucina")

st.divider()
st.caption("Hecho por Paco para Trini.")
