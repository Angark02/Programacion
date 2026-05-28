// Esta es la función que oculta el aviso de malware
function cerrarModal() {
    // Buscamos el elemento y le decimos que no se muestre
    document.getElementById('modal-malware').style.display = 'none';
}

window.addEventListener('DOMContentLoaded', () => {
    // Al cargar el contenido, hacemos la página visible
    document.body.classList.add('visible');

    // Buscamos todos los enlaces de la página
    const enlaces = document.querySelectorAll('a');

    enlaces.forEach(enlace => {
        enlace.addEventListener('click', (e) => {
            // Si el enlace abre una pestaña nueva (como tu GitHub), no hacemos animación
            if (enlace.target === "_blank") return;

            // Evitamos el salto inmediato
            e.preventDefault();
            const destino = enlace.href;

            // Iniciamos el desvanecimiento (Fade out)
            document.body.classList.remove('visible');

            // Esperamos 500ms (lo que dura la transición CSS) y cambiamos de página
            setTimeout(() => {
                window.location.href = destino;
            }, 500);
        });
    });
});