<style>
    /* El contenedor del modal (oculto por defecto) */
    .modal {
        display: none; 
        position: fixed; 
        z-index: 1000; 
        left: 0; top: 0;
        width: 100%; height: 100%;
        background-color: rgba(0,0,0,0.8);
    }

    /* Contenido de la ventana */
    .modal-content {
        background-color: #fff;
        margin: 5% auto;
        padding: 20px;
        border-radius: 15px;
        width: 80%;
        max-width: 600px;
        max-height: 80vh;
        overflow-y: auto;
        text-align: center;
    }

    .close-btn {
        float: right;
        font-size: 28px;
        font-weight: bold;
        cursor: pointer;
    }

    .restaurante-card {
        margin-bottom: 30px;
        border-bottom: 1px solid #ddd;
        padding-bottom: 20px;
    }

    .foto-restaurante {
        width: 100%;
        height: auto;
        border-radius: 10px;
        margin-bottom: 15px;
    }
</style>

<section id="comida" style="text-align: center; padding: 20px;">
    <h2>🍴 Almuerzo y Cenas</h2>
    <p>Haz clic abajo para ver las recomendaciones de sitios en Roma.</p>
    <button onclick="abrirModal()" style="padding: 15px 30px; font-size: 18px; cursor: pointer; border-radius: 10px; background-color: #e67e22; color: white; border: none;">
        Ver sitios recomendados
    </button>
</section>

<div id="miModal" class="modal">
    <div class="modal-content">
        <span class="close-btn" onclick="cerrarModal()">&times;</span>
        <h1>Restaurantes Seleccionados</h1>

        <div class="restaurante-card">
            <img src="http://googleusercontent.com/image_collection/image_retrieval/5727478812607205064" alt="La Gallina Bianca" class="foto-restaurante">
            <h3>La Gallina Bianca</h3>
            <p><strong>Ubicación:</strong> Via Antonio Rosmini, 5-12 (Termini)</p>
            <p>Especialistas en pizza artesanal y cocina sin gluten certificada.</p>
        </div>

        <div class="restaurante-card">
            <div style="background: #eee; height: 200px; border-radius: 10px; display: flex; align-items: center; justify-content: center;">
                <p>📸 (Foto de Mercato próximamente)</p>
            </div>
            <h3>Mercato Centrale</h3>
            <p>Espacio gastronómico con múltiples puestos de comida artesanal.</p>
        </div>
    </div>
</div>

<script>
    function abrirModal() {
        document.getElementById("miModal").style.display = "block";
    }

    function cerrarModal() {
        document.getElementById("miModal").style.display = "none";
    }

    // Cerrar si se hace clic fuera de la ventana blanca
    window.onclick = function(event) {
        let modal = document.getElementById("miModal");
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
</script>
