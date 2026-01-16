# --- PANTALLA DE BIENVENIDA (TEXTO DEFINITIVO PACO) ---
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
                font-family: 'Georgia', serif; 
                font-size: 50px; 
                font-weight: 700; 
                margin-bottom: 20px;
            ">Escapada a Roma</h1>
            
            <p style="
                color: #ce1126; 
                font-size: 28px; 
                font-weight: 700; 
                margin-bottom: 5px;
            ">Febrero de 2026</p>
            
            <p style="
                color: #1E3A5F; 
                font-size: 26px; 
                font-weight: 600; 
                margin-bottom: 35px;
            ">Paco & Mari Trini</p>
            
            <div style="
                font-style: italic; 
                font-size: 20px !important; 
                color: #333; 
                line-height: 1.8; 
                border-top: 1px solid #eee; 
                padding-top: 30px;
                text-align: justify;
                padding-left: 10px;
                padding-right: 10px;
            ">
                "Hay viajes que se escriben en el mapa, y otros que se graban en el corazón. 
                Esta aventura es un regalo que refleja el sinuoso y sorprendente camino 
                que hemos recorrido juntos, con el profundo deseo y la ilusión inquebrantable 
                de que el resto del camino que nos queda que andar supere abrumadoramente 
                las expectativas que podamos tener. Un regalo lleno de historia, luz y sabor, 
                nacido del cariño más profundo de nuestros hijos."
                <br><br>
                <p style="text-align: center; font-weight: 800; color: #1E3A5F; font-size: 22px;">
                Un inolvidable regalo sorpresa de Cristina y Víctor.
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("") 
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🇮🇹 INICIAR VIAJE"):
            st.session_state.viaje_iniciado = True
            st.rerun()
