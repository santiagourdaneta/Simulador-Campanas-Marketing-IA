from flask import Flask, request, jsonify
from flask_cors import CORS
from sklearn.tree import DecisionTreeClassifier
import numpy as np
import pandas as pd

app = Flask(__name__)
CORS(app)

# --- Modelos de simulación ---

# 1. Árbol de Decisión para predecir la respuesta de la audiencia (Ejemplo)
data = {
    'presupuesto_gastado': [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],
    'audiencia_segmentada': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    'plataforma': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    'compro': [0, 0, 1, 1, 0, 1, 1, 1, 0, 1]
}
df = pd.DataFrame(data)

X = df[['presupuesto_gastado', 'audiencia_segmentada', 'plataforma']]
y = df['compro']

modelo_decision_tree = DecisionTreeClassifier()
modelo_decision_tree.fit(X, y)

# 2. Modelo de Monte Carlo para simular ROI (Retorno de la Inversión)
def simular_roi(presupuesto, ventas_promedio, costo_por_venta):
    num_simulaciones = 10000
    ganancias_simuladas = []

    for _ in range(num_simulaciones):
        ventas_obtenidas = np.random.normal(loc=ventas_promedio, scale=0.1*ventas_promedio)
        ganancias = (ventas_obtenidas * costo_por_venta) - presupuesto
        ganancias_simuladas.append(ganancias)

    roi_promedio = np.mean(ganancias_simuladas)
    riesgo = np.std(ganancias_simuladas)

    return roi_promedio, riesgo

# --- Rutas de la API ---

@app.route('/simular', methods=['POST'])
def simular_campana():
    try:
        data = request.json
        presupuesto = data['presupuesto']
        audiencia = data['audiencia']
        plataforma = data['plataforma']

        # **Líneas de código corregidas**
        datos_entrada = pd.DataFrame([[presupuesto, audiencia, plataforma]], 
                                     columns=['presupuesto_gastado', 'audiencia_segmentada', 'plataforma'])

        prediccion_compra = modelo_decision_tree.predict(datos_entrada)
        
        respuesta_audiencia = "Muy probable" if prediccion_compra[0] == 1 else "Poco probable"

        ventas_promedio_estimado = 50 + (presupuesto / 100)
        costo_por_venta_estimado = 15

        roi_predicho, riesgo = simular_roi(presupuesto, ventas_promedio_estimado, costo_por_venta_estimado)
        
        return jsonify({
            'exito_audiencia': respuesta_audiencia,
            'roi_predicho': round(roi_predicho, 2),
            'riesgo': round(riesgo, 2)
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)