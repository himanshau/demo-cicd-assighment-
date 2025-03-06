from flask import Flask, render_template
import base64

app = Flask(__name__)

# Base64-encoded image string
image_base64 = "https://img.freepik.com/free-vector/done-concept-illustration_114360-3060.jpg?t=st=1741275352~exp=1741278952~hmac=4b3f66c9c69bdab4ff9c46fcd2091e15ce99d93d674e84d526eaff193c829ea9&w=900"
@app.route("/")
def home():
    return render_template("index.html", image_data=image_base64)

if __name__ == "__main__":
    app.run(debug=True)
