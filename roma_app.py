import streamlit as st
from datetime import datetime

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Roma 2026", page_icon="🇮🇹", layout="centered")

# --- ESTILOS CSS "PANTALLA TOTAL" ---
st.markdown("""
    <style>
    /* Fondo color crema suave */
    .stApp { background-color: #Fdfcf0; }
    
    /* TEXTO NEGRO INTENSO SIEMPRE */
    .stMarkdown p, .stMarkdown span, div, label, h1, h2, h3, li { 
        color: #000000 !important; 
    }
    
    /* ESTILO DE LOS DÍAS */
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

    /* --- CÓDIGO PARA VENTANA A PANTALLA COMPLETA REAL (100%) --- */
    div[data-testid="stDialog"] div[role="dialog"] {
        width
