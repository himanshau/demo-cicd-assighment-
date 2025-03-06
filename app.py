from flask import Flask, render_template
import base64

app = Flask(__name__)

# Base64-encoded image string
image_base64 = "save_image.jpg"
@app.route("/")
def home():
    return render_template("index.html", image_data=image_base64)

if __name__ == "__main__":
    app.run(debug=True)
