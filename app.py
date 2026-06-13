from flask import Flask, render_template, request
from rag_engine import ask_rag

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    answer = ""
    question = ""

    if request.method == "POST":
        question = request.form.get("question")

        if question:
            answer = ask_rag(question)

    return render_template("index.html", question=question, answer=answer)


if __name__ == "__main__":
    app.run(debug=True)
    

