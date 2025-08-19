# Simulador de Campañas de Marketing con IA 🔮

## Descripción del Proyecto

Este proyecto es una plataforma web **full-stack** que simula el rendimiento de campañas publicitarias utilizando modelos de Inteligencia Artificial. La herramienta permite a los usuarios predecir el **Retorno de la Inversión (ROI)** y la respuesta de la audiencia al variar parámetros como el presupuesto, el tipo de audiencia y la plataforma publicitaria.

El simulador se compone de dos partes principales:

-   **Backend (Python con Flask):** El "cerebro" de la aplicación. Utiliza modelos de Machine Learning como **Árboles de Decisión** para predecir el éxito de la audiencia y **Simulación de Monte Carlo** para estimar el ROI y el riesgo de la inversión. La API está protegida con **CORS** y **Rate Limiting**.
-   **Frontend (HTML, CSS, JavaScript):** La interfaz de usuario. Permite a los usuarios interactuar con el simulador de forma intuitiva, con validaciones de formulario para asegurar la calidad de los datos.

## Características Clave

-   **Simulación de ROI:** Predice las ganancias potenciales de una campaña.
-   **Predicción de Audiencia:** Estima la probabilidad de que la audiencia reaccione positivamente.
-   **Modelos de IA:** Implementación de algoritmos de simulación y árboles de decisión.
-   **Arquitectura RESTful:** El frontend se comunica con el backend a través de una API.
-   **Validaciones y Seguridad:** Incluye validaciones básicas, protección contra CORS y limitación de peticiones (Rate Limiting).

## Tecnologías Utilizadas

### Backend

-   **Python**
-   **Flask:** Framework para el servidor web.
-   **Scikit-learn:** Librería para los modelos de Machine Learning.
-   **NumPy & Pandas:** Para el manejo y análisis de datos.
-   **Flask-CORS:** Para gestionar las políticas de CORS.
-   **Flask-Limiter:** Para limitar las peticiones a la API.

### Frontend

-   **HTML5:** Estructura de la interfaz.
-   **CSS3:** Estilos y diseño.
-   **JavaScript (ES6+):** Lógica del lado del cliente y comunicación con la API.

## Cómo Usar (Instrucciones de Instalación)

Sigue estos pasos para poner el simulador en funcionamiento en tu máquina local.

1.  **Clonar el repositorio:**
    ```bash
    git clone https://github.com/santiagourdaneta/Simulador-Campanas-Marketing-IA/
    cd Simulador-Campanas-Marketing-IA
    ```
2.  **Configurar el Backend:**
    -   Navega a la carpeta `backend`.
    -   Crea un entorno virtual (recomendado):
        ```bash
        python -m venv venv
        # En Windows: venv\Scripts\activate
        # En macOS/Linux: source venv/bin/activate
        ```
    -   Instala las dependencias de Python:
        ```bash
        pip install -r requirements.txt
        ```
    -   Inicia el servidor de Flask:
        ```bash
        python app.py
        ```
        El servidor se ejecutará en `http://127.0.0.1:5000`.

3.  **Acceder al Frontend:**
    -   Navega a la carpeta `frontend/public`.
    -   Abre el archivo `index.html` en tu navegador web.

¡Listo! Ya puedes empezar a simular campañas.

## Contribuciones

Si deseas contribuir a este proyecto, por favor, abre un "issue" o envía una "pull request". ¡Toda ayuda es bienvenida!

python flask machine-learning data-science monte-carlo-simulation decision-tree full-stack marketing web-app ux-ui

#Python #MachineLearning #DataScience #FullStack #Flask #WebDev #MarketingAnalytics #Simulacion #GitHub
