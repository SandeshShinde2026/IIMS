from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# Load trained AI model
with open("sales_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/predict-sales", methods=["POST"])
def predict_sales():
    data = request.json
    date = pd.to_datetime(data["date"]).toordinal()

    # Predict sales for the given date
    prediction = model.predict([[date]])[0]
    return jsonify({"predicted_sales": int(prediction)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
