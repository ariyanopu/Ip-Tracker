# IP Tracker (Termux Edition)
Simple IP tracker tool with a clean Termux-styled UI.  
Developer: **ARIYAN MIRZA**

---

## ✔ Features
- Runs on Termux without extra setup  
- Auto-installs Python modules (requests, rich, pyfiglet)  
- Clean banner + Termux color theme  
- Shows:
  - IP Address  
  - Country  
  - Region  
  - City  
  - ISP  
  - Timezone  
  - Latitude / Longitude

---

## 📥 Install & Run

```
pkg update -y && pkg upgrade -y
pkg install python git -y

git clone https://github.com/ariyanopu/Ip-Tracker
cd Ip-Tracker

python iptrack.py
```

---

## 🕵️ Usage

```
python iptrack.py
```

Then:
- Enter target IP  
- Or leave blank to fetch **your own IP**

---

## 🖼 Banner Preview

```
╔══╗───╔════╗──────╔╗
╚╣╠╝───║╔╗╔╗║──────║║
─║║╔══╗╚╝║║╠╩╦══╦══╣║╔╦══╦═╗
─║║║╔╗║──║║║╔╣╔╗║╔═╣╚╝╣║═╣╔╝
╔╣╠╣╚╝║──║║║║║╔╗║╚═╣╔╗╣║═╣║
╚══╣╔═╝──╚╝╚╝╚╝╚╩══╩╝╚╩══╩╝
───║║
───╚╝
```

---

## 👤 Developer
**ARIYAN MIRZA**

---

## 🔗 Notes
- Fully offline except API request  
- No API key or extra configuration  
- Fast, simple, clean tool
