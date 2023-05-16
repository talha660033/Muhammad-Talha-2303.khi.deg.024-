import json
import logging
import os
import sys

from flask import Flask, render_template, request


#switch from test to production

app = Flask(__name__)
app.debug = bool(os.environ.get("DEBUG", False))

# Set up logging
app.logger.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s", datefmt="%H:%M:%S")
stream_handler.setFormatter(formatter)
app.logger.addHandler(stream_handler)

TODO_FILE_NAME = "/app/todo_data/todo.json"  # You can change the path anytime when you want to 
# Load todo items from file or initialize an empty list
if os.path.exists(TODO_FILE_NAME):
    with open(TODO_FILE_NAME) as f:
        TODO_ITEMS = json.load(f)
else:
    TODO_ITEMS = []

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        content = request.form["content"]
        TODO_ITEMS.append(content)
        save_todo_items()
        app.logger.info("Added new item: %s", content)

    return render_template("index.html", todo_items=TODO_ITEMS)

def save_todo_items():
    with open(TODO_FILE_NAME, "w") as f:
        json.dump(TODO_ITEMS, f)

if __name__ == "__main__":
    app.run(host="0.0.0.0")

