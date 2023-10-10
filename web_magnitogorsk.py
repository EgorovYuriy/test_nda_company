from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Загрузка обученной модели и предварительной обработки
loaded_model = joblib.load('model_magnotogorsk_apartments.joblib')
preprocessor_trees = joblib.load('preprocessor_trees.joblib')

# Обработчик POST-запросов для предсказания цен
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Получаем данные в формате JSON из запроса
        data = request.json
        # Преобразуем данные в DataFrame
        input_data = pd.DataFrame([data])
        # Применяем предварительную обработку (preprocessor_trees)
        input_features = preprocessor_trees.transform(input_data)
        # Получаем предсказание от модели
        predicted_price = loaded_model.predict(input_features)
        # Отправляем ответ в формате JSON
        return jsonify({'predicted_price': int(predicted_price[0])})
    
    except Exception as e:
        # Отправляем сообщение об ошибке в ответ в формате JSON
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

