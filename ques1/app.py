from flask import Flask, render_template, request
from concept_learning import train_spam_filter, classify_email

app = Flask(__name__)

# Train the model once at startup
dataset_path = "emails.csv"
learned_hypothesis, feature_list = train_spam_filter(dataset_path)

@app.route("/", methods=["GET", "POST"])
def home():
    prediction_result = None
    
    # Default values for form persistence
    form_data = {
        "promo": "",
        "links": "",
        "sender": "",
        "caps": ""
    }

    if request.method == "POST":
        # Extract data from form
        form_data["promo"] = request.form.get("promo")
        form_data["links"] = request.form.get("links")
        form_data["sender"] = request.form.get("sender")
        form_data["caps"] = request.form.get("caps")

        # Prepare input vector
        email_features = [
            form_data["promo"],
            form_data["links"],
            form_data["sender"],
            form_data["caps"]
        ]

        # Make prediction
        prediction_result = classify_email(learned_hypothesis, feature_list, email_features)

    return render_template(
        "index.html",
        result=prediction_result,
        **form_data
    )


if __name__ == "__main__":
    app.run(debug=True, port=5001, host='0.0.0.0')

