# --- PANTALLA DE BIENVENIDA (VERSION PERSONALIZADA) ---
if not st.session_state.viaje_iniciado:
    st.markdown(f"""
        <div style="
            text-align: center;
            padding: 50px 30px;
            background-color: white;
            border: 8px double #1E3A5F;
            border-radius: 15px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            margin-top: 30px;
            max-width: 650px;
            margin-left: auto;
            margin-right: auto;
        ">
            <h1 style="
                color: #1E3A5F;
                font-family: 'Georgia', serif; /* Tipo de letra más elegante y menos formal */
                font-size: 50px !important;
                font-weight: 700 !important;
                margin-bottom: 20px;
                letter-spacing: 1px;
            ">Escapada a Roma</h1>
            
            <p style="
                color: #ce1126;
                font-size: 28px !important;
                font-weight: 700;
                margin-bottom: 5px;
            ">Febrero de 2026</p>
            
            <p style="
                color: #1E3A5F;
                font-size: 26px !important;
                font-weight: 600;
                margin-bottom: 35px;
            ">Paco & Mari Trini</p>
            
            <div style="
                font-style: italic;
                font-size: 21px !important;
                color: #333;
                line-height: 1.7;
                margin-bottom: 20px;
                padding: 0 15px;
                border-top: 1px solid #eee;
                padding-top: 30px;
            ">
                "Hay viajes que se escriben en el mapa, y otros que se graban en el corazón. 
                Esta aventura es el reflejo de <b>nuestro</b> camino juntos, un regalo lleno de 
                historia, luz y sabor, nacido del cariño más profundo de <b>nuestros</b> hijos."
                <br><br>
                <span style="font-weight: 800; color: #1E3A5F;">
                Un inolvidable regalo sorpresa de Cristina y Víctor.
                </span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("") 
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🇮🇹 INICIAR VIAJE"):
            st.session_state.viaje_iniciado = True
            st.rerun()
