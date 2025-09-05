# 📌 Load Blaster

**Load Blaster** is a powerful DDOS tool for teting created by **Muhammad Anas (Technical Corp)**.  
It allows you to simulate high traffic on your own servers or applications to test their performance under heavy load.

⚠️ **Disclaimer:** This tool is for **educational and testing purposes only**. Use it only on servers and systems that you own or have explicit permission to test. Unauthorized use against external systems is illegal.

---

## 🚀 Features
- Real-time dashboard with live stats (Requests Sent, Failed, RPS).
- Option to stop attack early (`s` + Enter).
- Colorful and user-friendly interface.
- Works on **Kali Linux** and **Termux**.
- ASCII art banner for a professional look.

---

## 🔧 Installation

### 📍 On Kali Linux
1. Update system:
   ```bash
   sudo apt update && sudo apt upgrade -y
   ```
2. Install dependencies:
   ```bash
   sudo apt install python3 python3-venv python3-pip -y
   ```
3. Clone the repository:
   ```bash
   git clone https://github.com/techcorp/load-blaster.git
   cd load-blaster
   ```
4. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
5. Install Python requirements:
   ```bash
   pip install -r requirements.txt
   ```
6. Run the tool:
   ```bash
   python3 load-blaster.py
   ```

---

### 📍 On Termux (Android)
1. Update Termux:
   ```bash
   pkg update && pkg upgrade -y
   ```
2. Install Python:
   ```bash
   pkg install python -y
   ```
3. Clone the repository:
   ```bash
   git clone https://github.com/techcorp/load-blaster.git
   cd load-blaster
   ```
4. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the tool:
   ```bash
   python load-blaster.py
   ```

---

## 📦 Requirements
- Python 3.8+
- Modules:
  - `requests`
  - `colorama`
  - `pyfiglet`

Install with:
```bash
pip install -r requirements.txt
```

---

## ✍️ Author
Created by **Muhammad Anas (Technical Corp)**  
Cybersecurity Expert & Ethical Hacker  

**Subscribe Youtube Channel** Technical Corp[https://youtube.com/@technicalcorp]
