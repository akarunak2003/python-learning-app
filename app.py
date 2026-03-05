from flask import Flask, render_template, request, jsonify
import sys
import io

app = Flask(__name__)

lessons = {
    1:{
        "title":"Python Variables",
        "content":"Variables store values in Python.",
        "example":"x = 5\ny = 10\nprint(x + y)"
    },
    2:{
        "title":"Python Loops",
        "content":"Loops repeat a block of code.",
        "example":"for i in range(5):\n    print(i)"
    },
    3:{
        "title":"Python Functions",
        "content":"Functions reuse code.",
        "example":"def greet():\n    print('Hello Python')\n\ngreet()"
    }
}

@app.route("/")
def home():
    return render_template("index.html", lessons=lessons)

@app.route("/lesson/<int:id>")
def lesson(id):
    lesson = lessons[id]
    return render_template("lesson.html", lesson=lesson)


@app.route("/run", methods=["POST"])
def run_code():

    code = request.json["code"]

    old_stdout = sys.stdout
    sys.stdout = buffer = io.StringIO()

    try:
        exec(code)
        output = buffer.getvalue()
    except Exception as e:
        output = str(e)

    sys.stdout = old_stdout

    return jsonify({"output": output})


if __name__ == "__main__":
    app.run(debug=True)