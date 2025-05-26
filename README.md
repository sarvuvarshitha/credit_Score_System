

---

# 💳 Credit Score System – Interactive Web-Based Credit Evaluation

## 🧾 Overview

**Credit Score System** is a web-based Python application that calculates a user’s credit score based on income, debt, and credit history. It features a responsive front-end UI and a secure backend using a Feistel cipher encryption mechanism to demonstrate basic data privacy. Built with Flask, this project is ideal for educational demos on encryption, scoring algorithms, and full-stack development.

---

## 🔧 Features

* 🌐 **Interactive Web UI**: Clean, responsive HTML/CSS interface to collect financial input.
* 🔒 **Feistel Encryption**: Encrypts income, debts, and credit history using a lightweight Feistel cipher before processing.
* 📊 **Score Calculation**:

  * Computes a score based on simple logic involving income, debt, and history weighting.
  * Credit score is bounded between 300–850.
* ⚙️ **REST API Backend**:

  * Built with Flask and Flask-CORS.
  * Accepts POST requests with encrypted data and returns the calculated score along with encrypted fields.
* 🎨 **Frontend-Backend Integration**: Simulates encryption/decryption and score calculation directly in the browser as well as via API.

---

## 🗂️ Files Breakdown

| File                | Purpose                                                      |
| ------------------- | ------------------------------------------------------------ |
| `app.py`            | Flask API backend with scoring and encryption logic          |
| `feistel_cipher.py` | Contains the XOR-based Feistel cipher implementation         |
| `index.html`        | Frontend UI for collecting user input and displaying results |
| `style.css`         | Styling for the frontend interface                           |
| `requirements.txt`  | Dependencies (Flask and Flask-CORS)                          |

---

## 💻 How to Run

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/credit-score-system.git
   cd credit-score-system
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the backend server**

   ```bash
   python app.py
   ```

4. **Open `index.html` in a browser**
   (No additional setup needed for the frontend)

---

## 📚 Requirements

* Python 3.x
* Flask
* Flask-CORS

(See `requirements.txt` for exact versions.)

---

## 🚀 Future Improvements

* Real encryption key management
* Persistent user data storage (DB integration)
* Enhanced credit scoring logic based on industry standards (e.g. FICO)
* Deployment using Docker or cloud platforms

---

## 🙌 Acknowledgements

* Credit score logic is educational and simplified.
* Feistel cipher inspired by classic block cipher designs.

---
