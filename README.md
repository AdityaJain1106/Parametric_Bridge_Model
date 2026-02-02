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

* **⚡ Fully Parametric:** The entire geometry (Span, Width, Deck Depth) is driven by variable constants, allowing for instant resizing without code rewriting.
* **🏗️ Component Assembly:**
    * **I-Girders:** Custom-built using CSG fusion of web and flange primitives.
    * **Concrete Deck:** Automatically positioned relative to girder height.
* **🎨 Visual Materials:** Distinct color coding for **Steel (Blue)** and **Concrete (Gray/Translucent)** for clear structural differentiation.

## 🛠️ Technical Specifications

The model parameters can be adjusted within the main script variables:

| Parameter | Default Value | Unit | Description |
| :--- | :--- | :--- | :--- |
| **SPAN** | `10000.0` | mm | Total length of the bridge |
| **WIDTH** | `4000.0` | mm | Total width of the deck |
| **DECK_TH** | `250.0` | mm | Thickness of the concrete slab |
| **WEB_H** | `1000.0` | mm | Height of the steel girder web |

## 💻 Installation & Setup

This project utilizes **pythonOCC**, which requires a Conda environment for dependency management.

### 1. Prerequisites
Ensure you have [Anaconda](https://www.anaconda.com/) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html) installed.

### 2. Environment Configuration
Run the following commands in your Anaconda Prompt/Terminal:

```bash
# 1. Create a clean environment
conda create --name osdag_project python=3.9

# 2. Activate the environment
conda activate osdag_project

# 3. Install the core 3D library
conda install -c conda-forge pythonocc-core
