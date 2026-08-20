# 📱 Mobile Price Predictor

A machine learning-based desktop application built with **Python, Tkinter, and Scikit-learn** that predicts the estimated price of a mobile phone based on its specifications.

The project uses a **Linear Regression** machine learning model to learn the relationship between mobile specifications and their prices. Users can enter the specifications through a simple Tkinter GUI and instantly receive an estimated price.

---

## 🚀 Features

* 📱 Mobile price prediction
* 🤖 Machine Learning model using Linear Regression
* 🧠 Built with Scikit-learn
* 🖥️ User-friendly Tkinter GUI
* ⚡ Instant price prediction
* 📊 Prediction based on mobile specifications
* 🔢 Numerical feature processing
* 🧪 Trained model for real-time predictions

---

## 🧠 Machine Learning

The project uses **Linear Regression** from Scikit-learn.

The model learns from a dataset containing mobile phone specifications and their corresponding prices.

### Basic Workflow

```text
Mobile Dataset
      ↓
Data Preprocessing
      ↓
Feature Selection
      ↓
Train/Test Split
      ↓
Linear Regression
      ↓
Model Training
      ↓
User Input
      ↓
Price Prediction
```

---

## 📊 Input Features

The predictor can use mobile specifications such as:

* RAM
* Internal Storage
* Battery Capacity
* Camera Specifications
* Screen Size
* Processor-related specifications
* Other numerical specifications included in the dataset

> Update this section according to the exact features used in your model.

---

## 🖥️ Application Interface

The application provides a simple graphical interface using **Tkinter**.

Users enter the required mobile specifications and click the prediction button.

```text
┌───────────────────────────────────┐
│       📱 MOBILE PRICE PREDICTOR   │
├───────────────────────────────────┤
│                                   │
│  RAM:              [________]     │
│  Storage:          [________]     │
│  Battery:          [________]     │
│  Camera:           [________]     │
│  Screen Size:      [________]     │
│                                   │
│       [  PREDICT PRICE  ]         │
│                                   │
│  Estimated Price:  $XXX           │
│                                   │
└───────────────────────────────────┘
```

---

## 🛠️ Technologies Used

### Programming Language

* 🐍 Python

### GUI

* Tkinter

### Machine Learning

* Scikit-learn
* Linear Regression

### Data Processing

* Pandas
* NumPy

---

## 📂 Project Structure

```text
mobile-price-predictor/
│
├── dataset/
│   └── mobile_prices.csv
│
├── model/
│   └── model.pkl
│
├── main.py
├── train_model.py
├── requirements.txt
├── README.md
└── .gitignore
```

> The structure may vary depending on the actual project implementation.

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/mobile-price-predictor.git
```

### 2. Navigate to the Project

```bash
cd mobile-price-predictor
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
python main.py
```

The Tkinter application will open and you can enter the mobile specifications to generate a price prediction.

---

## 🧪 Model Training

If the model needs to be trained again, run:

```bash
python train_model.py
```

The training process generally includes:

1. Loading the dataset
2. Cleaning the data
3. Selecting relevant features
4. Splitting data into training and testing sets
5. Training the Linear Regression model
6. Evaluating the model
7. Saving the trained model

---

## 📈 Prediction Process

When the user enters mobile specifications:

```text
User Input
    ↓
Feature Preparation
    ↓
Trained Linear Regression Model
    ↓
Prediction
    ↓
Estimated Mobile Price
```

---

## 💡 Example

For example, a user can provide specifications such as:

```text
RAM: 8 GB
Storage: 128 GB
Battery: 5000 mAh
Camera: 50 MP
```

The trained model processes these features and returns an estimated mobile price.

---

## 🎯 Project Objective

The main objective of this project is to demonstrate how **Machine Learning can be integrated into a desktop application**.

Instead of only training a model inside a Python script or notebook, this project connects the trained ML model with a **Tkinter graphical interface**, allowing users to interact with the prediction system easily.

---

## 🔮 Future Improvements

Possible future improvements include:

* 📊 Add more training data
* 🎯 Improve prediction accuracy
* 🌳 Test other ML algorithms
* 📈 Add model performance metrics
* 💾 Save prediction history
* 📱 Add more mobile specifications
* 🎨 Improve the GUI design
* 🌐 Convert the model into a web API
* 📱 Build a mobile version
* ☁️ Deploy the prediction model online

---

## 📌 Project Highlights

```text
🐍 Python
🖥️ Tkinter GUI
🤖 Machine Learning
📊 Scikit-learn
📈 Linear Regression
📱 Mobile Price Prediction
⚡ Real-Time Prediction
```

---

## 📄 License

This project is created for **learning, experimentation, and educational purposes**.

You can add an MIT License or another license depending on how you want to distribute the project.

---

## 👨‍💻 Developer

Developed with ❤️ using **Python, Tkinter, and Machine Learning**.

### ⭐ If you find this project useful

Give the repository a ⭐ on GitHub and feel free to explore, modify, and improve the project.

**Built with Python + Machine Learning to predict mobile prices. 📱🤖**

