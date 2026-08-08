from flask import Flask, render_template, request, jsonify
from predictor import analyze_farm

app = Flask(__name__)


# ==========================================================
# HOME PAGE
# ==========================================================
@app.route("/")
def home():
    return render_template("home.html")


# ==========================================================
# DASHBOARD
# ==========================================================
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# ==========================================================
# ANALYZE FARM
# ==========================================================
@app.route("/analyze", methods=["POST"])
def analyze():

    try:

        data = request.form.to_dict()

        result = analyze_farm(data)

        return jsonify({

            "success": True,

            "result": result

        })

    except Exception as e:

        return jsonify({

            "success": False,

            "message": str(e)

        }), 500


# ==========================================================
# APPLICATION STATUS
# ==========================================================
@app.route("/status")
def status():

    return jsonify({

        "application": "Farm Performance & Forecasting",

        "status": "Running"

    })


# ==========================================================
# ERROR PAGES
# ==========================================================
@app.errorhandler(404)
def page_not_found(error):

    return render_template("home.html"), 404


@app.errorhandler(500)
def internal_error(error):

    return jsonify({

        "success": False,

        "message": "Internal Server Error"

    }), 500


# ==========================================================
# MAIN
# ==========================================================
if __name__ == "__main__":

    app.run(

        debug=True,

        host="127.0.0.1",

        port=5000

    )