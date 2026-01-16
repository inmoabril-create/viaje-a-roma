import streamlit as st
from datetime import datetime

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Roma 2026", page_icon="🇮🇹", layout="centered")

# --- ESTILOS CSS (AQUÍ ESTÁ LA MAGIA) ---
st.markdown("""
    <style>
    /* Fondo color crema suave */
    .stApp { background-color: #Fdfcf0; }
    
    /* TEXTO SIEMPRE VISIBLE (Negro casi puro) */
    .stMarkdown p, .stMarkdown span, div, label, h1, h2, h3, li { 
        color: #0e1117 !important; 
    }
    
    /* ESTILO DE LOS DÍAS (Rojo Roma) */
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
    
    /* BOTONES VERDES (Grandes y fáciles de pulsar) */
    div.stButton > button {
        width: 100%;
        background-color: white !important;
        border: 2px solid #008C45 !important;
        color: #008C45 !important;
        font-weight: bold;
        padding: 10px;
        border-radius: 8px;
    }

    /* --- TRUCO PARA VENTANA GIGANTE (FULL SCREEN) --- */
    div[data-testid="stDialog"] div[role="dialog"] {
        width: 95vw !important; /* 95% del ancho de la pantalla */
        max-width: 1000px !important;
        height: 90vh !important; /* 90% del alto */
        max-height: 90vh !important;
        background-color: white !important;
        overflow-y: auto; /* Permite bajar si el texto es largo */
    }
    
    /* Enlaces en azul fuerte y subrayados para que se vean bien */
    a {
        color: #0066cc !important;
        text-decoration: underline !important;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# --- FUNCIÓN DE VENTANA GIGANTE ---
@st.dialog("🇮🇹 DETALLES COMPLETOS")
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

# Función para crear las filas del itinerario
def fila(hora, titulo_corto, id_btn, tit_modal, info_modal):
    # En móvil, ponemos primero el texto y debajo el botón ancho
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
    * **Precio:** Tarifa fija de **50 €** (aseguraos de que sea taxi oficial blanco).
    * **Tiempo:** Unos 35-40 minutos.
    * **Dirección:** Decidle al conductor vuestra calle en Esquilino.

2.  **TREN LEONARDO EXPRESS:**
    * **Precio:** 14 € por persona.
    * **Destino:** Estación Termini (luego andando al hotel).
""")

fila("15:30", "🍕 Almuerzo Tardío", "d2", "COMIDA CERCA DE TERMINI", """
**LA GALLINA BIANCA**
Es un sitio perfecto para la primera toma de contacto. Muy cerca de la estación y vuestro hotel.
* **Qué pedir:** Pizzas romanas finas o pasta carbonara.
* 🌐 [Ver Web Oficial](https://www.lagallinabianca.com/)
* 📍 [Ver en Google Maps](https://www.google.com/maps/search/La+Gallina+Bianca+Roma)
""")

fila("17:30", "⛪ Ruta Basílicas (Gratis)", "d3", "PRIMER PASEO", """
**1. BASÍLICA DE SANTA MARÍA LA MAYOR**
Es una de las 4 basílicas mayores de Roma.
* **El detalle:** Mirad los mosaicos del siglo V en la nave central y el techo artesonado con el primer oro traído de América.

**2. SAN PIETRO IN VINCOLI** (Cierra a las 19:00)
* **La Joya:** Aquí está el **Moisés de Miguel Ángel**. Fijaos en los "cuernos" de la estatua y la fuerza de su mirada.
""")

fila("21:00", "🍷 Cena Barrio Monti", "d4", "CENA ZONA MONTI", """
El barrio de Monti es bohemio y está lleno de vida. Dos opciones:

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
Antes de entrar al museo, coged fuerzas aquí:

**OPCIÓN A: SCIASCIA CAFFÈ 1919**
Dicen que es el mejor café de Roma.
* **Pedid:** Un cappuccino y un cornetto.
* 🌐 [Web Oficial](https://www.sciasciacaffe1919.it)

**OPCIÓN B: LATTERIA GIULIANI**
Más tradicional, famosa por sus dulces caseros y ambiente tranquilo.
""")

fila("09:00", "🏛️ Museos Vaticanos", "l2", "VISITA MUSEOS", """
**DATOS DE LA RESERVA:**
* **Código:** 2L2NFFJ00000004GM
* **Hora:** 09:00 (Llegad 15 min antes).

**RECORRIDO IMPRESCINDIBLE:**
1.  Patio de la Piña.
2.  Galería de los Mapas (techo dorado).
3.  Estancias de Rafael (La Escuela de Atenas).
4.  **Capilla Sixtina** (Silencio absoluto).
""")

fila("14:30", "🏰 Almuerzo y Castillo", "l3", "ALMUERZO Y TARDE", """
**PARA COMER (Zona Borgo):**

**OPCIÓN A: PASTASCIUTTA** (Rápido y barato)
Pasta fresca hecha al momento para llevar o comer rápido.
* 🌐 [Web Oficial](https://www.pastasciuttaroma.it)

**OPCIÓN B: RISTORANTE ARLU** (Sentados)
Cocina refinada si preferís descansar las piernas.
* 🌐 [Web Oficial](https://www.ristorantearlu.com/)

**DESPUÉS:**
Visita exterior y puente del **Castillo de Sant'Angelo**. Las vistas del río Tíber desde aquí son preciosas.
""")

fila("20:30", "🍷 Cena Trastevere", "l4", "CENA EN TRASTEVERE", """
El barrio con más encanto de noche.

**OPCIÓN A: TONNARELLO**
Muy famoso. Hacen la pasta en sartenes pequeñas. Suele haber cola, pero va rápido.
* 🌐 [Web Oficial](https://tonnarello.it)

**OPCIÓN B: DA ENZO AL 29**
La auténtica cocina romana. Es pequeño y muy solicitado.
* 🌐 [Web Oficial](https://www.daenzoal29.it/)
""")

# ==========================================
# MARTES 3: BARROCO Y DESPEDIDA
# ==========================================
st.markdown('<div class="highlight-day"><h1>📆 MARTES 3: Roma Barroca</h1></div>', unsafe_allow_html=True)

fila("08:30", "☕ Desayuno Hotel", "m1", "DESAYUNO ESQUILINO", """
**OPCIÓN A: REGOLI PASTICCERIA**
Es obligatorio probar aquí el **Maritozzo** (bollo relleno de nata). Es una institución en Roma desde 1916.
* 🌐 [Ver en TripAdvisor](https://www.tripadvisor.es/Restaurant_Review-g187791-d1102555-Reviews-Pasticceria_Regoli-Rome_Lazio.html)

**OPCIÓN B: PANELLA**
Panadería de lujo con una terraza muy agradable.
* 🌐 [Web Oficial](https://www.panellaroma.com/)
""")

fila("14:00", "🍝 Almuerzo Navona", "m2", "ALMUERZO CENTRO", """
**CANTINA E CUCINA**
Situado cerca de Plaza Navona.
* **Ambiente:** Rústico, divertido y muy alegre.
* **Plato estrella:** Lasaña y albóndigas.
* 🌐 [Web Oficial](https://cantinaecucina.it)
""")

fila("20:30", "🍷 CENA DE GALA", "m3", "GRAN CENA DESPEDIDA (~100€)", """
Esta es la noche para darse un homenaje.

**OPCIÓN PRINCIPAL: TRATTORIA MONTI**
Cocina elegante y gestión familiar.
* **Especialidad:** El Tortello gigante con huevo dentro.
* **Consejo:** Reservad ya.
* 🌐 [Ver Opiniones](https://www.tripadvisor.es/Restaurant_Review-g187791-d1061245-Reviews-Trattoria_Monti-Rome_Lazio.html)

**OPCIÓN ALTERNATIVA: CUL DE SAC**
Enoteca histórica con miles de vinos y tablas de embutidos/patés increíbles.
* 🌐 [Web Oficial](https://www.enotecaculdesacroma.it/)
""")

# ==========================================
# MIÉRCOLES 4: BORGHESE
# ==========================================
st.markdown('<div class="highlight-day"><h1>📆 MIÉRCOLES 4: Arte</h1></div>', unsafe_allow_html=True)

fila("09:00", "☕ Desayuno", "mi1", "DESAYUNO", """
**OPCIÓN A: DAGNINO**
Pastelería siciliana. Probad los *Cannoli*.
* 🌐 [Web Oficial](https://www.pasticceriadagnino.com/)

**OPCIÓN B: GATSBY CAFÉ**
Local precioso en Piazza Vittorio, estilo años 20.
""")

fila("12:00", "🎨 Galería Borghese", "mi2", "VISITA BORGHESE", """
**IMPORTANTE:** Hay que estar a las **11:30** para dejar bolsos en consigna.

**OBRAS MAESTRAS:**
1.  *Apolo y Dafne* (Bernini): Mirad las hojas saliendo de los dedos.
2.  *El Rapto de Proserpina* (Bernini): Los dedos hundiéndose en la piel.
3.  Sala de Caravaggio.
""")

fila("14:30", "🍝 Almuerzo Coliseo", "mi3", "COMIDA ZONA COLISEO", """
**OPCIÓN A: HOSTARIA AL GLADIATORE**
Vistas directas al Coliseo. Turístico pero con calidad decente y vistas inmejorables.
* 🌐 [Web Oficial](https://www.hostariaalgladiatore.it/)

**OPCIÓN B: TRATTORIA LUZZI**
A unas calles del Coliseo. Ruidoso, barato y 100% romano.
* 🌐 [TripAdvisor](https://www.tripadvisor.es/Restaurant_Review-g187791-d1088460-Reviews-Trattoria_Luzzi-Rome_Lazio.html)
""")

fila("21:00", "🍷 Cena Final", "mi4", "ÚLTIMA CENA", """
**TRATTORIA VECCHIA ROMA**
El broche final perfecto.
* **El Show:** Pedid la *Amatriciana Flambé*. Traen la rueda de queso gigante a la mesa y le prenden fuego con la pasta dentro.
* 🌐 [Web Oficial](https://www.trattoriavecchiaroma.it/)
""")

# ==========================================
# JUEVES: REGRESO
# ==========================================
st.markdown('<div class="highlight-day"><h1>📆 JUEVES: Regreso</h1></div>', unsafe_allow_html=True)
fila("03:45", "🚕 Taxi Aeropuerto", "j1", "LOGÍSTICA SALIDA", """
**RUMBO A FIUMICINO (FCO)**
* **Hora:** 03:45 AM.
* **Transporte:** Taxi.
* **Precio:** 50 € (Tarifa fija).
* **Duración:** 35 minutos sin tráfico.
¡Buen viaje de vuelta! ✈️
""")

st.markdown("---")
st.caption("Hecho con ❤️ para Paco y Trini")
