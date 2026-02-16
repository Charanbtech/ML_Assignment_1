from flask import Flask, render_template, request
from id3_algorithm import build_id3_model, predict_purchase

app = Flask(__name__)

# Build model on startup
csv_file = "buy_computer.csv"
decision_tree = build_id3_model(csv_file)

@app.route("/", methods=["GET", "POST"])
def sales_prediction():
    prediction = None
    
    # Defaults
    user_input = {
        "age": "",
        "income": "",
        "student": "",
        "credit": ""
    }

    if request.method == "POST":
        user_input["age"] = request.form.get("age")
        user_input["income"] = request.form.get("income")
        user_input["student"] = request.form.get("student")
        user_input["credit"] = request.form.get("credit")
        
        # Map form fields to internal names expected by the model
        query_sample = {
            "age": user_input["age"],
            "income": user_input["income"],
            "student": user_input["student"],
            "credit_rating": user_input["credit"]
        }
        
        prediction = predict_purchase(query_sample)

    return render_template(
        "index.html",
        result=prediction,
        **user_input
    )

if __name__ == "__main__":
    app.run(debug=True, port=5003)
