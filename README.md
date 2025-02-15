# Flask URL Shortener 🚀

A simple **URL Shortener** built with Flask and SQLite. This application allows users to shorten long URLs and track the number of times they are accessed.

## Features ✅
- Shorten long URLs
- Redirect short URLs to the original link
- Track the number of times a short URL is accessed
- Simple and lightweight (Uses Flask and SQLite)

---

## Installation & Setup 🛠

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/ghazyp/flask-url-shortener.git
cd flask-url-shortener
```
### **2️⃣ Create a Virtual Environment (Recommended)**
```bash
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```
### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```
### **4️⃣ Initialize the Database**
```bash
python init_db.py
```
### **5️⃣ Run the Flask App**
```bash
python app.py
```
The app will run on ```http://127.0.0.1:5000/```

---

## **Usage 🚀**
### **Shorten a URL**
Make a ```POST``` request to ```/shorten``` with JSON data:
#### **Using cURL:**
```bash
curl -X POST http://127.0.0.1:5000/shorten \
     -H "Content-Type: application/json" \
     -d '{"url": "https://www.example.com"}'
```
#### **Response:**
```bash
{
  "short_url": "http://127.0.0.1:5000/abc123"
}
```

### **Redirect Using the Shortened URL**
Simply visit ```http://127.0.0.1:5000/abc123``` in your browser, and it will redirect to ```https://www.example.com```.
### **Check the Click Count (Manually in SQLite)**
To see how many times a short URL has been accessed:
```bash
sqlite3 instance/database.db "SELECT short, long, clicks FROM URL;"
```

---

## **Deployment (Optional) 🚀**
### **Deploy on Heroku**
```bash
heroku login
heroku create flask-url-shortener-ghazyp
git push heroku main
heroku open
```

---

## **GitHub Setup & Pushing Code 🛠**
### **1️⃣ Initialize Git & Add Remote Repository**
```bash
git init
git add .
git commit -m "Initial commit: Flask URL Shortener"
git remote add origin https://github.com/ghazyp/flask-url-shortener.git
git branch -M main
git push -u origin main
```

### **2️⃣ Using a Personal Access Token (If Authentication Fails)**
GitHub no longer supports password authentication for Git. Use a **Personal Access Token (PAT)**:
```bash
# Generate a token at https://github.com/settings/tokens
# Use the token instead of your password when pushing
```

### **3️⃣ Using SSH Authentication (Recommended)**
```bash
ssh-keygen -t rsa -b 4096 -C "your-email@example.com"
cat ~/.ssh/id_rsa.pub | pbcopy
# Add the copied key to GitHub: https://github.com/settings/keys
git remote set-url origin git@github.com:ghazyp/flask-url-shortener.git
git push -u origin main
```

---

## **Contributing 🤝**
Want to contribute? Feel free to fork this repository and submit a pull request!

---

## **License 📜**
This project is licensed under the MIT License.
