import streamlit as st
from datetime import datetime

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Roma 2026", page_icon="🇮🇹", layout="centered")

# --- ESTILOS CSS (PANTALLA TOTAL Y TEXTO VISIBLE) ---
st.markdown("""
    <style>
    /* Fondo color crema suave */
    .stApp { background-color: #Fdfcf0; }
    
    /* TEXTO NEGRO INTENSO SIEMPRE (Para arreglar lo del Xiaomi) */
    .stMarkdown p, .stMarkdown span, div, label, h1, h2, h3, li { 
        color: #000000 !important; 
    }
    
    /* ESTILO DE LOS DÍAS (Rojo) */
    .highlight-day {
        background-color: #CE1126;
        padding: 10px;
        border-radius: 8px;
        text-align: center;
        margin-top: 20px;
        margin-bottom: 10px;
    }
    .highlight-day h1 { 
        color: white !important; 
        font-size: 20px !important; 
        margin: 0; 
    }
    
    /* BOTONES VERDES */
    div.stButton > button {
        width: 100%;
        background-color: white !important;
        border: 2px solid #008C45 !important;
        color: #008C45 !important;
        font-weight: bold;
        padding: 10px;
        border-radius: 8px;
    }

    /* --- VENTANA A PANTALLA COMPLETA (FULL SCREEN) --- */
    div[data-testid="stDialog"] div[role="dialog"] {
        width: 100vw !important;
        height: 100vh !important;
        max-width: 100vw !important;
        max-height: 100vh !important;
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        margin: 0 !important;
        border-radius: 0 !important;
        background-color: white !important;
        z-index: 99999 !important;
    }

    /* Enlaces grandes y azules */
    a {
        color: #0066cc !important;
        text-decoration: underline !important;
        font-size: 18px !important;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# --- FUNCIÓN DE VENTANA ---
@st.dialog("🇮🇹 INFORMACIÓN DETALLADA")
def abrir_ventana(titulo, contenido):
    st.subheader(titulo)
    st.markdown(contenido, unsafe_allow_html=True)

# --- PORTADA ---
st.title("🇮🇹 Roma 2026")
st.markdown("### Paco & Mari Trini")

# Fecha: 1 de Febrero
fecha_viaje = datetime(2026, 2, 1)
dias = (fecha_viaje - datetime.now()).days

if dias > 0:
    st.info(f"⏳ ¡Faltan **{dias}** días para el viaje!")
elif dias == 0:
    st.success("🎉 ¡HOY ES EL DÍA! 🎉")
else:
    st.write("✈️ ¡A disfrutar!")

# Función para filas
def fila(hora, titulo_corto, id_btn, tit_modal, info_modal):
    st.write(f"**{hora}** | {titulo_corto}")
    if st.button("👁️ Ver detalles", key=id_btn):
        abrir_ventana(tit_modal, info_modal)
    st.markdown("---")

# ==========================================
# DOMINGO 1: LLEGADA (COMPLETO)
# ==========================================
st.markdown('<div class="highlight-day"><h1>📆 DOMINGO 1: Llegada</h1></div>', unsafe_allow_html=True)

fila("14:00", "🛫 Llegada y Traslado", "d1", "LOGÍSTICA LLEGADA", """
**TRASLADO AEROPUERTO -> HOTEL (Esquilino):**

1.  **TAXI (Opción Recomendada):**
    * **Precio:** Tarifa fija de **50 €** (Taxi oficial blanco).
    * **Tiempo:** Unos 35-40 minutos.
    * **Dirección:** Decidle al conductor vuestra calle en Esquilino.

2.  **TREN LEONARDO EXPRESS:**
    * **Precio:** 14 € por persona.
    * **Destino:** Estación Termini (luego andando al hotel).
""")

fila("15:30", "🍕 Almuerzo Tardío", "d2", "COMIDA CERCA DE TERMINI", """
**LA GALLINA BIANCA**
Perfecto para la primera toma de contacto. Cerca del hotel.
* **Qué pedir:** Pizzas romanas finas o pasta carbonara.
* 🌐 [Web Oficial](https://www.lagallinabianca.com/)
""")

fila("17:30", "⛪ Ruta Basílicas (Gratis)", "d3", "PRIMER PASEO", """
**1. BASÍLICA DE SANTA MARÍA LA MAYOR**
Mosaicos del siglo V y el primer oro de América en el techo.

**2. SAN PIETRO IN VINCOLI** (Cierra 19:00)
Aquí está el **Moisés de Miguel Ángel**. Fijaos en la fuerza de su mirada.
""")

fila("21:00", "🍷 Cena Barrio Monti", "d4", "CENA ZONA MONTI", """
**OPCIÓN A: LA CARBONARA**
Un clásico histórico.
* 🌐 [Web Oficial](https://lacarbonara.it/)

**OPCIÓN B: AI TRE SCALINI**
Más informal, tipo enoteca con platos deliciosos.
* 🌐 [Web Oficial](https://www.aitrescalini.org/)
""")

# ==========================================
# LUNES 2: VATICANO
# ==========================================
st.markdown('<div class="highlight-day"><h1>📆 LUNES 2: Vaticano</h1></div>', unsafe_allow_html=True)

fila("08:00", "☕ Desayuno Prati", "l1", "DESAYUNO EN PRATI", """
**OPCIÓN A: SCIASCIA CAFFÈ 1919**
Dicen que es el mejor café de Roma.
* 🌐 [Web Oficial](https://www.sciasciacaffe1919.it)

**OPCIÓN B: LATTERIA GIULIANI**
Más tradicional, famosa por sus dulces.
""")

fila("09:00", "🏛️ Museos Vaticanos", "l2", "VISITA MUSEOS", """
**RESERVA:** Código 2L2NFFJ00000004GM (09:00h).

**IMPRESCINDIBLE:**
1. Galería de los Mapas (techo dorado).
2. Estancias de Rafael.
3. **Capilla Sixtina** (Silencio absoluto).
""")

fila("14:30", "🏰 Almuerzo y Castillo", "l3", "ALMUERZO Y TARDE", """
**OPCIÓN A: PASTASCIUTTA** (Rápido)
Pasta fresca para llevar o comer rápido.
* 🌐 [Web Oficial](https://www.pastasciuttaroma.it)

**OPCIÓN B: RISTORANTE ARLU** (Sentados)
Cocina refinada para descansar.
* 🌐 [Web Oficial](https://www.ristorantearlu.com/)

**DESPUÉS:** Paseo por el puente del Castillo de Sant'Angelo.
""")

fila("20:30", "🍷 Cena Trastevere", "l4", "CENA EN TRASTEVERE", """
**OPCIÓN A: TONNARELLO**
Muy famoso, servido en sartenes.
* 🌐 [Web Oficial](https://tonnarello.it)

**OPCIÓN B: DA ENZO AL 29**
La auténtica cocina romana.
* 🌐 [Web Oficial](https://www.daenzoal29.it/)
""")

# ==========================================
# MARTES 3: BARROCO Y DESPEDIDA
# ==========================================
st.markdown('<div class="highlight-day"><h1>📆 MARTES 3: Roma Barroca</h1></div>', unsafe_allow_html=True)

fila("08:30", "☕ Desayuno Hotel", "m1", "DESAYUNO ESQUILINO", """
**OPCIÓN A: REGOLI PASTICCERIA**
Obligatorio probar el **Maritozzo** (bollo con nata).
* 🌐 [Ver en TripAdvisor](https://www.tripadvisor.es/Restaurant_Review-g187791-d1102555-Reviews-Pasticceria_Regoli-Rome_Lazio.html)

**OPCIÓN B: PANELLA**
Panadería de lujo con terraza.
* 🌐 [Web Oficial](https://www.panellaroma.com/)
""")

fila("10:00", "⛲ Ruta Barroca", "m4", "GUÍA BARROCA", """
**1. FONTANA DI TREVI**
Tirad una moneda con la mano derecha sobre el hombro izquierdo.

**2. PLAZA DE ESPAÑA**
Subid la escalinata para ver las vistas desde arriba.
""")

fila("14:00", "🍝 Almuerzo Navona", "m2", "ALMUERZO CENTRO", """
**CANTINA E CUCINA**
Cerca de Plaza Navona. Ambiente rústico y alegre.
* **Plato:** Lasaña y albóndigas.
* 🌐 [Web Oficial](https://cantinaecucina.it)
""")

fila("16:30", "🏛️ Panteón y Navona", "m5", "GUÍA TARDE", """
**1. EL PANTEÓN**
El edificio mejor conservado de la antigüedad.

**2. PLAZA NAVONA**
Fuente de los Cuatro Ríos de Bernini en el centro.
""")

fila("20:30", "🍷 CENA DE GALA", "m3", "GRAN CENA (~100€)", """
**OPCIÓN PRINCIPAL: TRATTORIA MONTI**
Cocina elegante. Especialidad: Tortello gigante con huevo.
* 🌐 [Ver Opiniones](https://www.tripadvisor.es/Restaurant_Review-g187791-d1061245-Reviews-Trattoria_Monti-Rome_Lazio.html)

**OPCIÓN ALTERNATIVA: CUL DE SAC**
Enoteca histórica con miles de vinos.
* 🌐 [Web Oficial](https://www.enotecaculdesacroma.it/)
""")

# ==========================================
# MIÉRCOLES 4: BORGHESE
# ==========================================
st.markdown('<div class="highlight-day"><h1>📆 MIÉRCOLES 4: Arte</h1></div>', unsafe_allow_html=True)

fila("09:00", "☕ Desayuno", "mi1", "DESAYUNO", """
**OPCIÓN A: DAGNINO**
Pastelería siciliana (Cannoli).
* 🌐 [Web Oficial](https://www.pasticceriadagnino.com/)

**OPCIÓN B: GATSBY CAFÉ**
Estilo años 20 en Piazza Vittorio.
""")

fila("12:00", "🎨 Galería Borghese", "mi2", "VISITA BORGHESE", """
**IMPORTANTE:** Estar a las **11:30** para la consigna.

**OBRAS:** Apolo y Dafne, El Rapto de Proserpina (Bernini) y Caravaggio.
""")

fila("14:30", "🍝 Almuerzo Coliseo", "mi3", "COMIDA COLISEO", """
**OPCIÓN A: HOSTARIA AL GLADIATORE**
Vistas directas al Coliseo.
* 🌐 [Web Oficial](https://www.hostariaalgladiatore.it/)

**OPCIÓN B: TRATTORIA LUZZI**
Ruidoso, barato y 100% romano.
* 🌐 [TripAdvisor](https://www.tripadvisor.es/Restaurant_Review-g187791-d1088460-Reviews-Trattoria_Luzzi-Rome_Lazio.html)
""")

fila("16:00", "🏟️ Roma Iluminada", "mi5", "PASEO NOCTURNO", """
1. Subid al **Campidoglio**.
2. Ved el Foro Romano iluminado desde la terraza trasera.
3. Bajad hacia el Coliseo por la Vía de los Foros.
""")

fila("21:00", "🍷 Cena Final", "mi4", "ÚLTIMA CENA", """
**TRATTORIA VECCHIA ROMA**
Pedid la *Amatriciana Flambé* (le prenden fuego al queso).
* 🌐 [Web Oficial](https://www.trattoriavecchiaroma.it/)
""")

# ==========================================
# JUEVES: REGRESO
# ==========================================
st.markdown('<div class="highlight-day"><h1>📆 JUEVES: Regreso</h1></div>', unsafe_allow_html=True)
fila("03:45", "🚕 Taxi Aeropuerto", "j1", "LOGÍSTICA SALIDA", """
**TAXI A FIUMICINO (FCO)**
* **Hora:** 03:45 AM.
* **Precio:** 50 € (Tarifa fija).
* **Duración:** 35 min.
¡Buen viaje! ✈️
""")

st.markdown("---")
st.caption("Dossier Roma 2026 - Paco & Trini")
