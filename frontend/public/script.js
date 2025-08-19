document.getElementById('simulation-form').addEventListener('submit', async function(event) {
    event.preventDefault(); // Evita que la página se recargue

    // Obtener los valores de los campos
    const presupuesto = document.getElementById('presupuesto').value;
    const audiencia = document.getElementById('audiencia').value;
    const plataforma = document.getElementById('plataforma').value;

    // Crear un objeto con los datos a enviar
    const data = {
        presupuesto: parseFloat(presupuesto),
        audiencia: parseInt(audiencia),
        plataforma: parseInt(plataforma)
    };

    // Enviar los datos al backend
    try {
        const response = await fetch('http://127.0.0.1:5000/simular', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        });

        const resultados = await response.json();

        if (response.ok) {
            // Mostrar los resultados en la pantalla
            document.getElementById('resultado-exito').textContent = resultados.exito_audiencia;
            document.getElementById('resultado-roi').textContent = `$${resultados.roi_predicho}`;
            document.getElementById('resultado-riesgo').textContent = `$${resultados.riesgo}`;
        } else {
            alert(`Error: ${resultados.error}`);
        }
    } catch (error) {
        alert('Hubo un error al conectar con el servidor.');
        console.error('Error:', error);
    }
});