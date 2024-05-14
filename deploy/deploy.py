from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__) # Initialize the flask App

@app.route('/') # Homepage
def home():
    return 'hello'

# @app.route('/predict', methods=['POST'])
# def predict():
#     # UI rendering the results
#     # Retrieve values from a form
#     init_features = [float(x) for x in request.form.values()]
#     final_features = [np.array(init_features)]
#     prediction = model.predict(final_features) # Make a prediction

#     return render_template('index.html', prediction_text='Predicted Species: {}'.format(prediction)) # Render the predicted result


if __name__ == "__main__":
    app.run(debug=True, port=(8888))