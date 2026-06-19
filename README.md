# CyberSecurity_Demo

## Overview

CyberSecurity_Demo is an educational cybersecurity awareness project designed for demonstrations in organizations, colleges, workshops, and awareness programs.

The objective is to demonstrate how attackers can collect sensitive device information simply by convincing a user to click an unknown link or scan an untrusted QR code.

The project simulates a realistic phishing-style prize website that appears harmless to the victim. Once visited, the application demonstrates:

* Device fingerprinting
* Browser and operating system identification
* IP address collection
* Network information gathering
* Screen resolution detection
* Battery status collection
* Language and timezone detection
* Clipboard access attempts
* Location permission requests
* Camera permission requests
* Live webcam streaming (only after user grants access)

A real-time SOC-style dashboard displays the collected information, helping participants understand the risks of interacting with unknown links.

> This project is intended strictly for cybersecurity awareness, education, training, and authorized demonstrations.

---

## Features

### Victim Simulation Page

A realistic promotional webpage that:

* Simulates a prize giveaway
* Collects publicly available browser/device information
* Requests optional permissions
* Demonstrates social engineering tactics
* Shows an educational awareness screen after interaction

### Live Dashboard

The dashboard provides:

* Real-time device intelligence feed
* Device profiling
* Event logging
* Camera stream monitoring
* Session statistics
* Awareness and mitigation recommendations

### Real-Time Communication

Uses Flask-SocketIO to:

* Push captured data instantly
* Stream webcam frames in real time
* Update dashboard metrics live

---

## Project Structure

```text
cybersecurity_demo/
│
├── app.py
│
├── templates/
│   ├── victim.html
│   └── dashboard.html
│
├── requirements.txt
│
└── README.md
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/cybersecurity_demo.git

cd cybersecurity_demo
```

### 2. Create Virtual Environment

Linux/macOS:

```bash
python3 -m venv venv

source venv/bin/activate
```

Windows:

```powershell
python -m venv venv

venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the server:

```bash
python app.py
```

You should see:

```text
Victim page -> http://<YOUR-IP>:5000/

Dashboard -> http://<YOUR-IP>:5000/dashboard
```

---

## Local Demonstration

### Victim Page

```text
http://localhost:5000/
```

### Dashboard

```text
http://localhost:5000/dashboard
```

Open the dashboard on the presenter machine and open the victim page on a participant device.

---

## Public Demonstration Using Ngrok

Ngrok allows you to expose the demo to external devices without configuring port forwarding.

### Step 1 – Install Ngrok

Download from:

https://ngrok.com/download

### Step 2 – Authenticate

```bash
ngrok config add-authtoken YOUR_NGROK_TOKEN
```

### Step 3 – Start the Flask Application

```bash
python app.py
```

### Step 4 – Expose Port 5000

Open a new terminal:

```bash
ngrok http 5000
```

Example output:

```text
Forwarding https://abcd-1234.ngrok-free.app -> http://localhost:5000
```

### Step 5 – Share the Link

Victim Page:

```text
https://abcd-1234.ngrok-free.app/
```

Dashboard:

```text
https://abcd-1234.ngrok-free.app/dashboard
```

You can also generate a QR code for the victim page during awareness workshops.

---

## Demonstration Flow

1. Start the dashboard.
2. Generate an Ngrok public URL.
3. Share the URL or QR code with participants.
4. Ask them to visit the page.
5. Observe how information appears on the dashboard.
6. Explain:

   * What data is automatically exposed.
   * What requires explicit permission.
   * How social engineering works.
7. Conclude with security best practices.

---

## Educational Takeaways

Participants learn that:

* Visiting an unknown website can reveal significant information.
* IP addresses and browser fingerprints are collected automatically.
* Permissions should never be granted blindly.
* QR codes should be treated like links.
* Camera and location prompts should always be verified.
* Public Wi-Fi and phishing campaigns can abuse these techniques.

---

## Security & Ethics

This project is intended only for:

* Cybersecurity awareness programs
* Security training sessions
* Educational workshops
* Authorized demonstrations

Do not use this project against systems, users, or organizations without explicit authorization.

The authors assume no responsibility for misuse.

---

## Author

Mayank Verma (Mayerust)
