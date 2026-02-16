from flask import Flask, render_template, request
from decision_tree import predict_loan_status

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def dashboard():
    loan_prediction = None
    income_val = ""
    credit_val = ""

    if request.method == "POST":
        income_val = request.form.get("income")
        credit_val = request.form.get("credit")
        
        loan_prediction = predict_loan_status(income_val, credit_val)

    return render_template(
        "index.html",
        result=loan_prediction,
        income=income_val,
        credit=credit_val
    )

if __name__ == "__main__":
    app.run(debug=True, port=5002)
