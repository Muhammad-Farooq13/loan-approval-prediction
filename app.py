from flask import Flask, request, jsonify
from src.predict import predict_loan

app = Flask(__name__)

@app.route("/")
def home():
    return "Loan Approval Prediction API Running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    result = predict_loan(data)
    return jsonify({"Loan Approved": bool(result)})

if __name__ == "__main__":
    app.run(debug=True)
