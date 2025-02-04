# 📩 Spam Detection App

A machine learning-based **Spam Detection App** using **Naïve Bayes** and **CountVectorizer**. This project includes both a **Tkinter GUI version** and a **Streamlit web app version** for ease of use.

---

## 🚀 Features

✅ **Spam Detection:** Classifies messages as **Spam** or **Not Spam** using a trained Naïve Bayes model.  
✅ **Machine Learning Model:** Utilizes **CountVectorizer** for text transformation and **Multinomial Naïve Bayes** for classification.  
✅ **SQLite Database:** Saves predictions in an SQLite database.  
✅ **Dual UI:** Available as a **Tkinter desktop app** and a **Streamlit web app**.  
✅ **User-friendly:** Simple and intuitive UI for easy spam detection.  

---

## 🛠️ Installation

### Prerequisites
Make sure you have **Python 3.x** installed along with the required dependencies:
```bash
pip install -r requirements.txt
```

### Clone the Repository
```bash
git clone https://github.com/yourusername/spam-detection.git
cd spam-detection
```

---

## 💻 Usage

### 1️⃣ Running the **Streamlit Web App**
```bash
streamlit run streamlit_app.py
```
Then open the browser to `http://localhost:8501/`.

### 2️⃣ Running the **Tkinter GUI App**
```bash
python tkinter_app.py
```

---

## 📊 Dataset
This project uses an SMS Spam dataset. The dataset is loaded from `spam.csv`, cleaned, and stored in an SQLite database (`spam.db`).

---

## 🏗️ Project Structure
```bash
📂 spam-detection
├── 📄 spam.csv              # Dataset (if available)
├── 📄 spam_model.pkl        # Trained Model
├── 📄 vectorizer.pkl        # Trained Vectorizer
├── 📄 spam.db               # SQLite Database
├── 📄 requirements.txt      # Dependencies
├── 📄 tkinter_app.py        # Tkinter GUI App
├── 📄 streamlit_app.py      # Streamlit Web App
├── 📄 spam_detection.py     # Core Spam Detection Logic
└── 📄 README.md             # Project Documentation
```

---

## 🛠 Technologies Used
- **Python**
- **Scikit-learn**
- **Streamlit**
- **Tkinter**
- **SQLite**
- **Pandas**
- **Joblib**

---

## 📸 Screenshots
### 📌 Tkinter GUI
![Tkinter GUI](screenshots/tkinter_ui.png)

### 📌 Streamlit Web App
![Streamlit App](screenshots/streamlit_ui.png)

---

## 📜 License
This project is licensed under the **MIT License**.

---

## 📢 Contribution
Feel free to fork this project, make improvements, and submit a **pull request**! 🚀

---

## 📬 Contact
For any inquiries, contact **treshlol202@gmail.com** or visit the repository on [GitHub](https://github.com/mehdidinari/Email_Filter).

### 🔗 Connect with Me
[LinkedIn](https://www.linkedin.com/in/mehdi-dinari-b0487a2a9/)
