from flask import Flask, render_template, request
from src.pipeline.predict_pipeline import PredictPipeline, CustomData

application = Flask(__name__)
app = application


# Home Page
@app.route("/")
def index():
    return render_template("index.html")


# Prediction Page
@app.route("/predictdata", methods=["GET", "POST"])
def predict_datapoint():

    if request.method == "GET":
        return render_template("home.html")

    try:

        data = CustomData(

            gender=request.form.get("gender"),

            SeniorCitizen=int(request.form.get("SeniorCitizen")),

            Partner=request.form.get("Partner"),

            Dependents=request.form.get("Dependents"),

            tenure=int(request.form.get("tenure")),

            PhoneService=request.form.get("PhoneService"),

            MultipleLines=request.form.get("MultipleLines"),

            InternetService=request.form.get("InternetService"),

            OnlineSecurity=request.form.get("OnlineSecurity"),

            OnlineBackup=request.form.get("OnlineBackup"),

            DeviceProtection=request.form.get("DeviceProtection"),

            TechSupport=request.form.get("TechSupport"),

            StreamingTV=request.form.get("StreamingTV"),

            StreamingMovies=request.form.get("StreamingMovies"),

            Contract=request.form.get("Contract"),

            PaperlessBilling=request.form.get("PaperlessBilling"),

            PaymentMethod=request.form.get("PaymentMethod"),

            MonthlyCharges=float(request.form.get("MonthlyCharges")),

            TotalCharges=float(request.form.get("TotalCharges"))

        )

        pred_df = data.get_data_as_dataframe()

        predict_pipeline = PredictPipeline()

        prediction, probability = predict_pipeline.predict(pred_df)

        confidence = round(max(probability[0]) * 100, 2)

        if prediction[0] == 1:
            result = "Customer is likely to Churn"
            color = "danger"
        else:
            result = "Customer is likely to Stay"
            color = "success"

        return render_template(
            "home.html",
            prediction=result,
            confidence=confidence,
            color=color
        )

    except Exception as e:

        return render_template(
            "home.html",
            prediction=f"Error : {str(e)}",
            confidence=0,
            color="warning"
        )


if __name__ == "__main__":
    app.run(debug=True)