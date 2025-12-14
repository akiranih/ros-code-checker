import os
import time
import json
from PIL import Image, ImageDraw

# Create a fake simulation result folder
RESULT_DIR = "sim_results"
os.makedirs(RESULT_DIR, exist_ok=True)

def generate_fake_image(path, text):
    """Creates a simple image with text."""
    img = Image.new("RGB", (400, 400), color=(200, 200, 200))
    draw = ImageDraw.Draw(img)
    draw.text((100, 180), text, fill="black")
    img.save(path)

def run_simulation():
    print("Running fake simulation...")

    # Create fake joint log
    joint_log_path = os.path.join(RESULT_DIR, "joint_log.csv")
    with open(joint_log_path, "w") as f:
        f.write("joint1,joint2,joint3\n")
        f.write("0.1,0.2,0.3\n")
        f.write("0.3,0.4,0.5\n")

    # Create 3 fake simulation images
    for i in range(3):
        img_path = os.path.join(RESULT_DIR, f"frame_{i}.png")
        generate_fake_image(img_path, f"Frame {i}")
        time.sleep(0.5)

    # Create fake simulation output
    outcome = {
        "status": "SUCCESS",
        "message": "Fake simulation completed.",
        "frames": [f"frame_{i}.png" for i in range(3)]
    }

    outcome_path = os.path.join(RESULT_DIR, "outcome.json")
    with open(outcome_path, "w") as f:
        json.dump(outcome, f, indent=4)

    return outcome

if __name__ == "__main__":
    print(run_simulation())
