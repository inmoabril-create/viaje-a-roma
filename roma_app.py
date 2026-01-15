import streamlit as st
from datetime import datetime

# CONFIGURACIÓN BÁSICA
st.set_page_config(page_title="Roma 2026", page_icon="🇮🇹")

# TÍTULO Y CONTADOR
st.title("🇮🇹 Roma 2026")
st.subheader("Paco & Mari Trini")

# Fecha: 1 de Febrero
fecha_viaje = datetime(2026, 2, 1)
dias = (fecha_viaje - datetime.now()).days

if dias > 0:
    st.warning(f"⏳ ¡Faltan {dias} días para el gran viaje!")
else:
    st.success("🎉 ¡YA ESTÁIS EN ROMA! 🎉")

# --- DOMINGO 1 ---
with st.expander("📆 DOMINGO 1: LLEGADA"):
    st.write("🕑 **14:00** | 🛫 Llegada y Traslado al Hotel")
    st.write("🕑 **16:00** | 🏨 Check-in y paseo por Esquilino")
    st.write("🕑 **20:00** | 🍷 Cena tranquila cerca del hotel")

# --- LUNES 2 ---
with st.expander("📆 LUNES 2: VATICANO"):
    st.write("🕑 **07:15** | 🚌 Traslado: Metro A (Termini -> Ottaviano)")
    st.write("🕑 **08:00** | ☕ Desayuno: Sciascia Caffè o Giuliani")
    st.write("🕑 **09:00** | 🏛️ Museos Vaticanos (Reserva: 2L2NFFJ00000004GM)")
    st.write("🕑 **14:30** | 🏰 Castillo Sant'Angelo y Almuerzo")
    st.write("🕑 **20:30** | 🍷 Cena en Trastevere (Tonnarello)")

# --- MARTES 3 ---
with st.expander("📆 MARTES 3: ROMA BARROCA"):
    st.write("🕑 **08:30** | ☕ Desayuno: Regoli (Maritozzo) o Panella")
    st.write("🕑 **10:00** | ⛲ Trevi y Plaza de España")
    st.write("🕑 **14:00** | 🍝 Almuerzo: Cantina e Cucina")
    st.write("🕑 **16:30** | 🏛️ Panteón y Plaza Navona")
    st.write("🕑 **20:30** | 🍷 CENA DE DESPEDIDA: Trattoria Monti")
    st.write("[TripAdvisor Monti](https://www.tripadvisor.es/Restaurant_Review-g187791-d1061245-Reviews-Trattoria_Monti-Rome_Lazio.html)")

# --- MIÉRCOLES 4 ---
with st.expander("📆 MIÉRCOLES 4: BORGHESE E IMPERIAL"):
    st.write("🕑 **09:00** | ☕ Desayuno: Dagnino o Gatsby Café")
    st.write("🕑 **12:00** | 🎨 Galería Borghese (Estar a las 11:30)")
    st.write("🕑 **14:30** | 🍝 Almuerzo: Hostaria al Gladiatore o Luzzi")
    st.write("🕑 **16:00** | 🏟️ Roma Iluminada (Campidoglio y Foros)")
    st.write("🕑 **21:00** | 🍷 Cena: Vecchia Roma (Pasta Flambé)")

# --- JUEVES 5 ---
with st.expander("📆 JUEVES 5: REGRESO"):
    st.write("🕑 **03:00** | ⏰ DESPERTADOR")
    st.write("🕑 **03:45** | 🚕 Taxi al Aeropuerto (Tarifa fija 50€)")

st.divider()
st.caption("Dossier interactivo - Paco & Trini")
