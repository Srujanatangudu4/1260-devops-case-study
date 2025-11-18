from flask import Flask, render_template, request

app = Flask(__name__)

COLOR_MEANINGS = {
    "red": "Red symbolizes energy, passion, and excitement.",
    "blue": "Blue represents calmness, trust, and peace.",
    "green": "Green stands for growth, balance, and harmony.",
    "yellow": "Yellow is linked with happiness, optimism, and creativity.",
    "purple": "Purple symbolizes luxury, wisdom, and imagination."
}

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    selected_color = request.form.get("color")
    meaning = COLOR_MEANINGS.get(selected_color, "")
    return render_template("result.html", color=selected_color, meaning=meaning)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
