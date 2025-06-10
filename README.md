# FINGERSTROKE_VIRTUAL_PAINT_WEBSITE

🎨 **Unleash Your Creativity through Gesture-Based Digital Painting**

[![Python](https://img.shields.io/badge/Python-3.9-blue.svg)](https://www.python.org/)
[![Conda](https://img.shields.io/badge/Package_Manager-conda-blue.svg)](https://docs.conda.io/)

> Built using Python, OpenCV, and MediaPipe

---

## 📑 Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Testing](#testing)

---

## 🧠 Overview

**Fingerstroke** transforms your webcam into a digital brush by harnessing the power of real-time hand gesture detection. Create, draw, and interact with digital canvases using only your fingers — no physical contact needed!

This project is a seamless blend of hand tracking and gesture interpretation, designed to deliver an intuitive and immersive creative experience.

### 🔍 Key Features

- 🖐️ **Hand Gesture-Based Drawing**  
  Track and interpret hand gestures to create fluid strokes in real time.

- ⚡ **Real-Time Feedback**  
  Instant visual feedback ensures a natural and dynamic drawing experience.

- 🔧 **MediaPipe + OpenCV Integration**  
  Combines Google’s MediaPipe for hand tracking with OpenCV for canvas rendering.

- 💻 **User-Friendly Interface**  
  Intuitive layout for ease of use, even for users without prior design experience.

- 🧪 **Automated Testing Framework**  
  Ensures robust performance and consistent quality across builds.

- 🌈 **Interactive Multimedia Elements**  
  Supports additional gesture-based triggers for toggling colors, brush sizes, and effects.

---

## 🚀 Getting Started

### Prerequisites

To run this project, ensure you have the following installed:

- **Python** ≥ 3.9  
- **Conda** (for environment and dependency management)

---

### 🔧 Installation

Follow these steps to clone and set up the project locally.

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/Fingerstroke.git
```

2. **Navigate to the project directory**
cd Fingerstroke

3. **Install the dependencies**
 
conda create -n fingerstroke_env python=3.9
conda activate fingerstroke_env
pip install -r requirements.txt

## ✅ **Testing**

Fingerstroke uses the pytest framework for testing key functionalities.

To run the test suite, use the following commands:

Using Conda
conda activate fingerstroke_env
pytest
