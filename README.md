# 🌤️ Weather Buddy

### Real-Time Weather Forecasting App

> A simple and interactive weather application built with **Python, Streamlit, and OpenWeatherMap API** to fetch and display real-time weather information for any city.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-App-red?logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/API-OpenWeatherMap-orange" />
  <img src="https://img.shields.io/badge/Status-In%20Progress-yellow" />
</p>

---

## ✨ Features

🌍 Search weather by city  
🌡️ Display current temperature  
💧 Display humidity  
💨 Display wind speed  
☁️ Display weather condition  
⚠️ Handle invalid city/API responses  
📊 Interactive Streamlit interface  

---

## 🛠️ Tech Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=python" />
</p>

**Libraries & Services**

- 🐍 Python
- 🎈 Streamlit
- 🔗 Requests
- ☁️ OpenWeatherMap API

---

## 🔄 How It Works

```text
👤 Enter City Name
        │
        ▼
🎈 Streamlit Interface
        │
        ▼
🔗 Send API Request
        │
        ▼
☁️ OpenWeatherMap API
        │
        ▼
📦 JSON Response
        │
        ▼
⚙️ Extract Weather Data
        │
        ▼
🌤️ Display Weather Information
```

---

## 📊 Weather Information

| Information | Description |
|---|---|
| 🌡️ Temperature | Current temperature in °C |
| 💧 Humidity | Current humidity percentage |
| 💨 Wind Speed | Current wind speed |
| ☁️ Condition | Current weather condition |
| 📍 City | Requested city |
| 🌍 Country | Country code |

---

## 📸 App Preview

> Add your application screenshot here.

```text
📁 assets/
   └── weather-buddy.png
```

After adding the screenshot:

```markdown
![Weather Buddy](./assets/weather-buddy.png)
```

---

## 📂 Project Structure

```text
Weather-Buddy/
│
├── .venv/
│
├── app.py
│
├── requirements.txt
│
├── .gitignore
│
├── assets/
│   └── weather-buddy.png
│
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone <your-repository-url>
cd Weather-Buddy
```

### 2️⃣ Create virtual environment

```bash
python -m venv .venv
```

### 3️⃣ Activate virtual environment

**Windows:**

```bash
.venv\Scripts\activate
```

### 4️⃣ Install dependencies

```bash
pip install streamlit requests
```

Or:

```bash
pip install -r requirements.txt
```

### 5️⃣ Run the application

```bash
streamlit run app.py
```

---

## 🔑 API Configuration

This project uses the **OpenWeatherMap API**.

⚠️ **Never upload your API key directly to GitHub.**

Use Streamlit Secrets for the final version:

```python
API_KEY = st.secrets["API_KEY"]
```

Store the key in:

```text
.streamlit/secrets.toml
```

and add it to `.gitignore`.

---

## 🧠 Concepts Practiced

This project helped me practice:

- Python programming
- Virtual environments
- Package installation
- Streamlit
- API integration
- HTTP requests
- HTTP status codes
- JSON response handling
- Data extraction
- Conditional statements
- Error handling
- Git & GitHub workflow

---

## 🚀 Development Progress

```text
[✅] Project Setup
     ↓
[✅] Virtual Environment
     ↓
[✅] Install Streamlit & Requests
     ↓
[✅] Connect Weather API
     ↓
[✅] Fetch Weather Data
     ↓
[✅] Extract JSON Data
     ↓
[✅] Display Weather Information
     ↓
[✅] Handle Invalid City
     ↓
[ ] Secure API Key
     ↓
[ ] Improve UI
     ↓
[ ] Add Weather Icons
     ↓
[ ] Add More Weather Details
     ↓
[ ] Final Deployment 🚀
```

---

## 📌 Git Commit Journey

This project is being developed **incrementally**, with separate commits for each training task.

```text
📌 Initialize Weather Buddy project
        ↓
📌 Setup Streamlit application
        ↓
📌 Install Requests library
        ↓
📌 Connect OpenWeatherMap API
        ↓
📌 Fetch weather data
        ↓
📌 Extract weather information
        ↓
📌 Display weather metrics
        ↓
📌 Add API response handling
        ↓
🚀 Future enhancements
```

---

## 🎯 Future Enhancements

- 🔐 Secure API key management
- 🌦️ Dynamic weather icons
- 📅 Weather forecast
- 🌡️ Feels-like temperature
- 🌅 Sunrise & sunset
- 📍 Current location weather
- 🔍 Better input validation
- 🎨 Improved UI/UX
- 📱 Responsive design
- ☁️ Deploy the application

---

## 👩‍💻 Developer

**Sakshi Zurale**

🎓 B.Tech — Electronics & Computer Engineering  
💻 Full Stack Development Training  
🤖 AI/ML & Software Development Enthusiast

---

<p align="center">

### 🌤️ Weather Buddy

**Search. Discover. Stay Weather-Ready. ☁️**

⭐ Built as part of my Full Stack Development Training.

</p>
