import streamlit as st
from datetime import datetime

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="Roma 2026 - Paco & Trini", page_icon="🇮🇹", layout="centered")

# --- FECHAS ---
fecha_viaje = datetime(2026, 5, 22, 6, 40) 
ahora = datetime.now()
dias_faltan = (fecha_viaje - ahora).days

# --- ESTILOS (CSS) ---
st.markdown("""
    <style>
    .stApp { background-color: #Fdfcf0; }
    h1, h2, h3 { color: #CE1126; }
    .dia-header {
        background-color: #008C45;
        color: white;
        padding: 10px;
        border-radius: 10px;
        margin-top: 20px;
        margin-bottom: 10px;
    }
    .hora { font-weight: bold; color: #555; }
    .recomendacion {
        background-color: #e8f8f5;
        border-left: 5px solid #008C45;
        padding: 10px;
        margin-top: 10px;
    }
    .card {
        background: white; padding: 15px; border-radius: 10px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05); margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# --- PORTADA ---
st.title("🇮🇹 Itinerario Maestro: Roma 2026")
if dias_faltan > 0:
    st.info(f"🚀 **Cuenta atrás:** Faltan {dias_faltan} días para el despegue.")

# ==========================================
# DÍA 1: DOMINGO 22 (LLEGADA)
# ==========================================
st.markdown("<div class='dia-header'><h3>📆 DOMINGO 22: Benvenuti a Roma</h3></div>", unsafe_allow_html=True)

st.markdown("#### 🛬 09:30 - Aterrizaje en Fiumicino")
st.write("Recogida de maletas y traslado al centro.")

# --- BLOQUE LOGÍSTICA TRANSPORTE ---
with st.expander("🚌 Opciones de Transporte al Hotel (Ver comparativa)"):
    st.markdown("""
    | Opción | Duración | Coste (2 pax) | Comodidad |
    | :--- | :---: | :---: | :---: |
    | **🚆 Leonardo Express** | 32 min | 28€ | ⭐⭐⭐⭐⭐ (Directo a Termini) |
    | **🚌 Bus (Terravision)** | 60 min+ | 12€ | ⭐⭐⭐ (Depende del tráfico) |
    | **🚖 Taxi Oficial** | 45 min | 50€ (Fijo) | ⭐⭐⭐⭐ (Puerta a puerta) |
    """)
    
    st.markdown("""
    <div class="recomendacion">
    <b>💡 Recomendación de Anras:</b><br>
    Sin duda, coged el <b>Leonardo Express</b>. Aunque es un poco más caro que el bus, os ahorráis el tráfico de entrada a Roma (que es horrible) y os deja en Termini, muy cerca de vuestro hotel. Merece la pena pagar esos 16€ extra por empezar el viaje sin estrés.
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.markdown("#### 🏨 11:30 - Check-in Hotel")
st.write("*Dejar maletas en recepción si la habitación no está lista.*")

st.markdown("---")

st.markdown("#### 🍝 14:00 - Primera Comida Romana")
st.write("Opciones cerca del hotel para no cansarnos:")

# --- BLOQUE COMIDA DOMINGO (EL QUE ARREGLAMOS) ---
opcion_domingo = st.radio("Elige ambiente:", ["La Gallina Bianca (Relax)", "Mercato Centrale (Jaleo)"], horizontal=True)

if "Gallina" in opcion_domingo:
    st.image("https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=800&q=80")
    st.caption("Ambiente clásico y tranquilo.")
else:
    st.image("https://images.unsplash.com/photo-1533900298318-6b8da08a523e?w=800&q=80")
    st.caption("Ambiente vibrante y variado.")

# ==========================================
# DÍA 2: LUNES 23
# ==========================================
st.markdown("<div class='dia-header'><h3>📆 LUNES 23: Roma Imperial (Por definir)</h3></div>", unsafe_allow_html=True)
st.info("🚧 Paco, aquí tenemos que poner qué hacemos este día. ¿Coliseo y Foros? ¿Panteón?")

# ==========================================
# DÍA 3: MARTES 24
# ==========================================
st.markdown("<div class='dia-header'><h3>📆 MARTES 24: Vaticano y Trastevere</h3></div>", unsafe_allow_html=True)
st.write("Mañana reservada para San Pedro y Museos.")

st.markdown("#### 🌙 21:00 - Cena Especial")
with st.expander("Ver nuestra reserva en Cantina e Cucina"):
    st.image("https://images.unsplash.com/photo-1559339352-11d035aa65de?w=800&q=80")
    st.write("**Cantina e Cucina:** Nuestro sitio favorito. Pedid la Carbonara y la Amatriciana para compartir.")

# ==========================================
# DÍA 4: MIÉRCOLES 25
# ==========================================
st.markdown("<div class='dia-header'><h3>📆 MIÉRCOLES 25: (Día Libre / Compras)</h3></div>", unsafe_allow_html=True)
st.info("🚧 Pendiente de definir.")

# ==========================================
# DÍA 5: JUEVES 26 (REGRESO)
# ==========================================
st.markdown("<div class='dia-header'><h3>📆 JUEVES 26: Arrivederci Roma</h3></div>", unsafe_allow_html=True)
st.markdown("#### 🛫 18:00 - Vuelo de vuelta")
st.write("Salida del hotel a las 14:30 aprox.")
