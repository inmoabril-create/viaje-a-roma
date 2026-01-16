import streamlit as st
from datetime import datetime

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Roma 2026", page_icon="🇮🇹", layout="centered")

# --- ESTILOS CSS REFORZADOS ---
st.markdown("""
    <style>
    .stApp { background-color: #Fdfcf0; }
    
    .highlight-day {
        background-color: #1E3A5F;
        color: white !important;
        padding: 15px;
        border-radius: 12px;
        text-align: center;
        margin-top: 25px;
        margin-bottom: 20px;
    }
    .highlight-day h1 { color: white !important; font-size: 24px !important; margin:0; }

    .stMarkdown p, .stMarkdown li, div {
        color: #1a1a1a !important;
        font-size: 18px !important;
    }

    a {
        color: #0056b3 !important;
        text-decoration: underline !important;
        font-weight: bold !important;
    }

    div.stButton > button {
        width: 100%;
        background-color: white !important;
        border: 2px solid #1E3A5F !important;
        color: #1E3A5F !important;
        font-weight: bold;
        padding: 12px;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

@st.dialog("🇮🇹 DETALLES")
def abrir_ventana(titulo, texto_markdown, img1=None, pie1=None):
    st.markdown(f"# {titulo}")
    if img1:
        st.image(img1, caption=pie1, use_container_width=True)
    st.markdown(texto_markdown)

# --- PORTADA ---
st.title("🇮🇹 Roma 2026")
st.write("### Paco & Mari Trini")

# ==========================================
# DOMINGO 1: Benvenuti
# ==========================================
st.markdown('<div class="highlight-day"><h1>📆 DOMINGO 1: Benvenuti</h1></div>', unsafe_allow_html=True)

# 1. TRASLADO
c1, c2 = st.columns([0.6, 0.4])
with c1: st.write("🕑 **14:00** | 🛬 Traslado Aeropuerto")
with c2:
    if st.button("🚌 Transporte", key="t_dom"):
        info_t = """
        **OPCIONES DE LLEGADA:**
        * **🚆 Tren Leonardo Express**: Directo a Termini (32 min). 14€.
        * **🚌 Autobús (Terravision / TAM)**: Unos 6-7€. Tarda 1 hora.
        * **🚖 Taxi Oficial**: Tarifa fija de **50€**.
        
        💡 **Consejo**: El tren es lo más cómodo para evitar el tráfico de Roma.
        """
        abrir_ventana("Llegada a Roma", info_t)

# 2. ALMUERZO
c1, c2 = st.columns([0.6, 0.4])
with c1: st.write("🕑 **15:30** | 🍕 Almuerzo")
with c2:
    if st.button("🍴 Opciones", key="l_dom"):
        info_l = """
        **OPCIONES DE ALMUERZO:**
        1. **La Gallina Bianca**: Cocina tradicional romana muy cerca de Termini. 
        🌐 [Web Oficial](http://www.lagallinabiancaroma.it)
        
        2. **Mercato Centrale**: Puestos artesanos gourmet en la misma estación.
        🌐 [Web Oficial](https://www.mercatocentrale.it/roma/)
        """
        abrir_ventana("Almuerzo", info_l, img1="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Roma_Termini_Mercato_Centrale.jpg/800px-Roma_Termini_Mercato_Centrale.jpg", pie1="Mercato Centrale Termini")

# 3. SANTA MARIA MAGGIORE
c1, c2 = st.columns([0.6, 0.4])
with c1: st.write("🕑 **17:30** | ⛪ Sta. Maria Maggiore")
with c2:
    if st.button("📖 Ver Guía", key="sm_dom"):
        info_sm = """
        **LA BASÍLICA DE ORO:**
        Es la más grande de las iglesias dedicadas a la Virgen en Roma.
        
        * **El Techo**: Decorado con el primer oro traído de América.
        * **Reliquia**: El Pesebre de Belén se guarda bajo el altar.
        * 🌐 [Web Oficial (Vaticano)](https://www.vatican.va/various/basiliche/sm_maggiore/index_it.html)
        """
        abrir_ventana("Santa Maria Maggiore", info_sm, img1="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Basilica_di_Santa_Maria_Maggiore_-_Rome.jpg/800px-Basilica_di_Santa_Maria_Maggiore_-_Rome.jpg")

# 4. SAN PIETRO IN VINCOLI
c1, c2 = st.columns([0.6, 0.4])
with c1: st.write("🕑 **18:30** | ⛪ S. Pietro in Vincoli")
with c2:
    if st.button("📖 El Moisés", key="mo_dom"):
        info_mo = """
        **EL MOISÉS DE MIGUEL ÁNGEL:**
        Contemplad la potencia de su mirada y el detalle de las venas en el brazo.
        
        * **Curiosidad**: Los cuernos son un error histórico de traducción.
        * **Las Cadenas**: Se exponen las cadenas originales de San Pedro.
        * 🌐 [Información Turística](https://www.turismoroma.it/it/luoghi/basilica-di-san-pietro-vincoli)
        """
        abrir_ventana("San Pietro in Vincoli", info_mo, img1="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Mois%C3%A9s_de_Miguel_%C3%81ngel_en_San_Pietro_in_Vincoli.jpg/800px-Mois%C3%A9s_de_Miguel_%C3%81ngel_en_San_Pietro_in_Vincoli.jpg")

# 5. CENA MONTI
c1, c2 = st.columns([0.6, 0.4])
with c1: st.write("🕑 **20:00** | 🍷 Cena (Barrio Monti)")
with c2:
    if st.button("🍷 Comidas", key="ce_dom"):
        info_ce = """
        🍴 **Ai Tre Scalini**: Una de las vinerías más auténticas de Roma. 
        No aceptan reservas, así que es mejor llegar puntuales.
        
        🌐 [Web Oficial](http://www.aitrescalini.org)
        """
        abrir_ventana("Cena en Monti", info_ce, img1="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Via_Panisperna_-_Rione_Monti.jpg/800px-Via_Panisperna_-_Rione_Monti.jpg", pie1="Barrio Monti")

st.write("---")
st.caption("Guía Roma 2026 - Paco & Trini")
