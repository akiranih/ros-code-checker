import zipfile
import os
import subprocess
import json

def extract_zip(zip_path):
    extract_dir = "upload_pkg"
    # Delete the folder if it exists
    if os.path.exists(extract_dir):
        subprocess.call("rmdir /s /q upload_pkg", shell=True)
    os.makedirs(extract_dir, exist_ok=True)

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)

    return extract_dir


def syntax_check(directory):
    python_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))

    errors = []

    for py in python_files:
        result = subprocess.run(["python", "-m", "flake8", py], capture_output=True, text=True)
        if result.stdout:
            errors.append(result.stdout)

    if errors:
        return {"status": "FAIL", "errors": errors}
    return {"status": "PASS", "errors": []}


def generate_report(data):
    with open("report.json", "w") as f:
        json.dump(data, f, indent=4)


def check_zip(zip_file):
    directory = extract_zip(zip_file)
    syntax = syntax_check(directory)

    report = {
        "syntax": syntax,
        "overall": "PASS" if syntax["status"] == "PASS" else "FAIL"
    }

    generate_report(report)
    return report


if __name__ == "__main__":
    print(check_zip("test.zip"))
