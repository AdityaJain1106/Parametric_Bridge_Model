````md
<div align="center">

# 🌉 Parametric Steel Girder Bridge Model  
### FOSSEE Osdag Internship Screening Task 2026

![Python](https://img.shields.io/badge/Python-3.9-blue?style=flat&logo=python)
![Library](https://img.shields.io/badge/Library-pythonOCC-orange)
![Status](https://img.shields.io/badge/Status-Completed-green)

A fully parametric **3D CAD model** of a steel girder bridge, developed effectively using **Constructive Solid Geometry (CSG)** logic and Python.
<br />

</div>

---

## 🚀 Key Features

* **⚡ Fully Parametric:** Geometry (Span, Width, Deck Thickness, Web Height) driven entirely by variables—resize instantly without rewriting code.  
* **🏗️ Component Assembly:**  
  - **I-Girders:** Constructed using CSG fusion of web and flange components.  
  - **Concrete Deck:** Automatically positioned with respect to girder height.  
* **🎨 Material Visualization:**  
  - **Steel → Blue**  
  - **Concrete → Gray/Translucent**  
  Enables easy visual differentiation between structural elements.

---

## 🛠️ Technical Specifications

All key parameters are defined within the main script:

| Parameter | Default Value | Unit | Description |
|----------|----------------|------|-------------|
| **SPAN** | `10000.0` | mm | Total length of the bridge |
| **WIDTH** | `4000.0` | mm | Overall deck width |
| **DECK_TH** | `250.0` | mm | Concrete deck thickness |
| **WEB_H** | `1000.0` | mm | Height of the steel girder web |

---

## 💻 Installation & Setup

This project uses **pythonOCC**, which is best installed in a Conda environment.

### 1️⃣ Prerequisites  
Install **Anaconda** or **Miniconda**:

- https://www.anaconda.com/  
- https://docs.conda.io/en/latest/miniconda.html  

### 2️⃣ Environment Setup  
Run the following commands:

```bash
# Create a new environment
conda create --name osdag_project python=3.9

# Activate the environment
conda activate osdag_project

# Install pythonOCC
conda install -c conda-forge pythonocc-core
````

---

## ▶️ Running the Model

Execute the main script:

```bash
python bridge_model.py
```

This launches a 3D viewer showing:

* I-girder assembly
* Concrete deck
* Color-coded materials

---

## 📂 Project Structure

```
📁 parametric_bridge
│── bridge_model.py          # Main file — geometry + assembly logic
│── utils/
│   └── primitives.py        # Web + flange shape creation utilities
│── README.md
```

---

## 📸 Output Visualization

The script renders:

* Parametric I-Girders
* Deck placement relative to girder height
* Fully assembled 3D CAD model

---

## 📜 License

Developed as part of **FOSSEE Osdag Internship Screening Task 2026**.

---

