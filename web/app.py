from flask import Flask, render_template, request
import os
import sys
import shutil

# --- Add simulator folder ---
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "simulator")))
from sim_runner import run_simulation

# --- Add checker folder ---
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "checker")))
from checker import check_zip

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        file = request.files["file"]
        save_path = os.path.join(UPLOAD_FOLDER, "user.zip")
        file.save(save_path)

        report = check_zip(save_path)

        return render_template("report.html", report=report)

    return render_template("index.html")

@app.route("/simulate")
def simulate():
    # Run fake simulation
    result = run_simulation()

    # Copy frames to static folder
    static_dir = os.path.join(os.path.dirname(__file__), "static")
    os.makedirs(static_dir, exist_ok=True)

    for frame in result["frames"]:
        src = os.path.join("..", "simulator", "sim_results", frame)
        dst = os.path.join(static_dir, frame)
        shutil.copy(src, dst)

    return render_template("simulation.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
