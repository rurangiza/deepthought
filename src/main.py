from flask import Flask, render_template, request
import helpers as h

app = Flask(__name__)

@app.get("/")
def home() -> str:
    return render_template("index.html")

@app.get("/about/")
def about() -> str:
    return render_template("about.html")

@app.post("/process/")
def process() -> str:
    raw_text = request.form['trace']
    html = h.text_to_HTML(raw_text)
    return render_template("result.html", html_content=html)

if __name__ == "__main__":
    app.run(debug=True)