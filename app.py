from flask import Flask, render_template, request, jsonify
import model
import os # Add this at the top of your file

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    skills = data.get('skills', '')

    # Функция сама проверит, нужно ли обучение
    prediction = model.get_prediction(skills)

    return jsonify({'role': prediction})


if __name__ == '__main__':
    # Railway provides the port via an environment variable
    port = int(os.environ.get("PORT", 5000))
    # '0.0.0.0' tells Flask to listen on all available network interfaces
    app.run(host='0.0.0.0', port=port)