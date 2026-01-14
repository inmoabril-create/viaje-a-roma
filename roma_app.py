import streamlit as st

# Usamos st.markdown con unsafe_allow_html=True para que Streamlit acepte el CSS y el JS
st.markdown("""
    <style>
        /* Estilos para el modal */
        .modal {
            display: none; 
            position: fixed; 
            z-index: 1000; 
            left: 0; top: 0;
            width: 100%; height: 100%;
            background-color: rgba(0,0,0,0.8);
        }

        .modal-content {
            background-color: #fff;
            margin: 5% auto;
            padding: 20px;
            border-radius: 15px;
            width: 85%;
            max-width: 500px;
            color: #333;
            text-align: center;
        }

        .close-btn {
            float: right;
            font-size: 28px;
            font-weight: bold;
            cursor: pointer;
            color: #aaa;
        }

        .restaurante-card {
            margin-bottom: 25px;
            padding-bottom: 15px;
            border-bottom: 1px solid #eee;
        }

        .foto-restaurante {
            width: 100%;
            border-radius: 10px;
        }
    </style>

    <div style="text-align: center;">
        <button onclick="document.getElementById('miModal').style.display='block'" 
                style="padding: 10px 20px; background-color: #4CAF50; color: white; border: none; border-radius: 5px; cursor: pointer;">
            🍴 Ver Sitios (La Gallina Bianca)
        </button>
    </div>

    <div id="miModal" class="modal">
        <div class="modal-content">
            <span class="close-btn" onclick="document.getElementById('miModal').style.display='none'">&times;</span>
            <h2 style="color: #2c3e50;">Recomendaciones</h2>
            
            <div class="restaurante-card">
                <img src="http://googleusercontent.com/image_collection/image_retrieval/5727478812607205064" class="foto-restaurante">
                <h3>La Gallina Bianca</h3>
                <p>Pizza artesanal y carnes a la brasa. ¡Tienen opciones sin gluten!</p>
                <small>📍 Via Antonio Rosmini, 5-12</small>
            </div>
            
            <div class="restaurante-card">
                <p>📸 <em>Próximamente: Mercato Centrale</em></p>
            </div>
        </div>
    </div>

    <script>
        // Cerrar si se pulsa fuera del recuadro blanco
        window.onclick = function(event) {
            var modal = document.getElementById('miModal');
            if (event.target == modal) {
                modal.style.display = "none";
            }
        }
    </script>
    """, unsafe_allow_html=True)
