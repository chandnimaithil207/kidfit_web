from flask import Flask, render_template, request
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('kids_clothing_svm_model.pkl')

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    if request.method == 'POST':
        try:
            height = float(request.form['height'])
            weight = float(request.form['weight'])
            age = int(request.form['age'])
            gender = request.form['gender'].lower()

            # Prepare input DataFrame
            user_input = pd.DataFrame({
                'height': [height],
                'weight': [weight],
                'age': [age],
                'gender': [gender]
            })

            # Predict clothing size
            prediction = model.predict(user_input)[0]
        except Exception as e:
            prediction = f"Error: {str(e)}"

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
