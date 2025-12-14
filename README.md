# ros-code-checker

# ROS Code Checker & Simulation Preview Tool

This project implements a simplified ROS code validation and simulation preview workflow.  
Features
### 1. Code Checker (Backend)
- Accepts uploaded ZIP files
- Extracts contents automatically
- Performs syntax checking using flake8
- Validates minimal ROS package structure
- Generates JSON + text reports

### 2. Simulation Runner
- Generates artificial simulation frames
- Produces joint log CSV
- Outputs success/failure JSON
- Returns preview images for the web interface

### 3. Web Interface (Flask)
- Upload ROS packages
- Display validation results
- Trigger simulation
- Preview generated frames and logs

## 📁 Project Structure
ros-code-checker/
├── checker/
│ ├── checker.py
│ ├── test_pkg/
│ └── upload_pkg/
├── simulator/
│ ├── sim_runner.py
│ └── sim_results/
├── web/
│ ├── app.py
│ ├── templates/
│ └── static/
├── correct_pkg.zip
├── faulty_pkg.zip
└── README.md
##  Running the Application

### 1. Install dependencies
pip install flask flake8 pillow

### 2. Start the web interface
cd web
python app.py

### 3. Open in browser
http://localhost:5000

Two reference test packages are included:

- **correct_pkg.zip** — valid ROS structure
- **faulty_pkg.zip** — missing files or syntax errors

This tool demonstrates:
- Code analysis
- Simple simulation workflow
- Web UI integration
- Logging + report generation

