import streamlit as st
import datetime

# Configuración de la página
st.set_page_config(page_title="Roma 2026 - Dossier de Viaje", layout="wide")

# --- LÓGICA DEL CONTADOR (Sidebar) ---
st.sidebar.title("⏳ Cuenta Atrás")
fecha_viaje = datetime.datetime(2026, 5, 20, 10, 0) # Ajusta la fecha real aquí
ahora = datetime.datetime.now()
diferencia = fecha_viaje - ahora

if diferencia.days > 0:
    st.sidebar.success(f"Faltan {diferencia.days} días para el gran viaje, Paco.")
else:
    st.sidebar.info("¡El viaje ha comenzado o ya ha pasado!")

# --- TÍTULO PRINCIPAL ---
st.title("🇮🇹 Itinerario Roma 2026")
st.markdown("---")

# --- SECCIÓN: DÍA 1 (Llegada) ---
st.header("📍 Día 1: Primer contacto con la ciudad")

col1, col2 = st.columns([1, 3])

with col1:
    st.subheader("14:00")
with col2:
    st.write("🏠 **Llegada y Check-in:** Dejar las maletas en el alojamiento y un pequeño descanso.")

st.markdown("---")

# --- SECCIÓN: 15:30 ALMUERZO (CON EL MODAL DE LAS FOTOS) ---
col1, col2 = st.columns([1, 3])
with col1:
    st.subheader("15:30")
with col2:
    st.write("🍴 **Almuerzo: Dos opciones cerca de Termini.**")
    
    # HTML/CSS/JS para el Modal de Restaurantes
    modal_html = """
    <style>
        .modal {
            display: none; position: fixed; z-index: 1000; 
            left: 0; top: 0; width: 100%; height: 100%;
            background-color: rgba(0,0,0,0.8);
        }
        .modal-content {
            background-color: #fff; margin: 5% auto; padding: 20px;
            border-radius: 15px; width: 85%; max-width: 500px;
            color: #333; text-align: center; font-family: sans-serif;
        }
        .close-btn { float: right; font-size: 28px; cursor: pointer; color: #aaa; }
        .restaurante-card { margin-bottom: 25px; padding-bottom: 15px; border-bottom: 1px solid #eee; }
        .foto-restaurante { width: 100%; border-radius: 10px; margin-bottom: 10px; }
        .btn-ver { padding: 10px 20px; background-color: #e67e22; color: white; border: none; border-radius: 5px; cursor: pointer; font-size: 16px; }
    </style>

    <button class="btn-ver" onclick="document.getElementById('modalComida').style.display='block'">
        🔎 Ver Sitios (La Gallina Bianca)
    </button>

    <div id="modalComida" class="modal">
        <div class="modal-content">
            <span class="close-btn" onclick="document.getElementById('modalComida').style.display='none'">&times;</span>
            <h2 style="color: #2c3e50;">Recomendaciones para Hoy</h2>
            
            <div class="restaurante-card">
                <img src="http://googleusercontent.com/image_collection/image_retrieval/5727478812607205064" class="foto-restaurante">
                <h3>La Gallina Bianca</h3>
                <p>Ubicada en Via Antonio Rosmini. Famosa por su horno de leña y opciones sin gluten.</p>
                <small>📍 A 5 min de la estación</small>
            </div>
            
            <div class="restaurante-card">
                <h3>Mercato Centrale</h3>
                <p>Ubicado dentro de la misma estación Termini. Muchas opciones gourmet rápidas.</p>
                <p>📸 <em>(Pendiente de añadir foto de Mercato)</em></p>
            </div>
        </div>
    </div>

    <script>
        window.onclick = function(event) {
            var modal = document.getElementById('modalComida');
            if (event.target == modal) { modal.style.display = "none"; }
        }
    </script>
    """
    st.markdown(modal_html, unsafe_allow_html=True)

st.markdown("---")

# --- SECCIÓN: 17:30 SANTA MARIA MAGGIORE ---
col1, col2 = st.columns([1, 3])
with col1:
    st.subheader("17:30")
with col2:
    st.write("⛪ **Basílica de Santa María la Mayor:** Una de las cuatro basílicas mayores de Roma.")
    
    if st.button("📖 Guía Rápida: Santa Maria"):
        st.info("""
        **No te pierdas:**
        * Los mosaicos del siglo V en la nave central.
        * El relicario de la Sagrada Cuna bajo el altar mayor.
        * El techo artesonado, que dicen fue dorado con el primer oro traído de América.
        """)

st.markdown("---")

# --- SECCIÓN: 18:30 SAN PIETRO IN VINCOLI ---
col1, col2 = st.columns([1, 3])
with col1:
    st.subheader("18:30")
with col2:
    st.write("🗿 **San Pietro in Vincoli:** Famosa por albergar el **Moisés de Miguel Ángel** y las cadenas de San Pedro.")

st.markdown("---")

st.caption("Dossier gestionado por Anras para Paco - Roma 2026")
