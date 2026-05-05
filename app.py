from flask import Flask, render_template, request, jsonify
import model

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
    app.run(debug=True)