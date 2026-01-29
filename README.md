# ASTRIA: Autonomous Collision Avoidance System
### 🛰️ Student Research Project | Mobile-Edge Simulation
## 📄 Technical Documentation
For a deep dive into the engineering methodology, mathematical models (SGP4), and hardware validation results, please refer to the full research paper:

> **[Download: ASTRIA Research Dissertation (2026) - PDF](./ASTRIA_Dissertation_2026_HIL_Verified.pdf)**
![Status](https://img.shields.io/badge/Status-Student%20Prototype-orange)
![Hardware](https://img.shields.io/badge/Hardware-Android%20Smartphone-blue)
![Goal](https://img.shields.io/badge/Goal-Learning%20%26%20Exploration-green)

> **Note:** This is an independent project by a pre-university student. It explores how consumer electronics can simulate complex aerospace logic when specialized hardware is unavailable.

---

## 📖 The Story: Why This Exists?
I am a student passionate about aerospace engineering, but I reside in a region where accessing specialized hardware (like flight computers or development boards) is difficult. 

Instead of letting this limitation stop my research, I asked a simple question:
**"Can I turn the phone in my pocket into a satellite Onboard Computer?"**

This repository documents my attempt to build a **Hardware-in-the-Loop (HIL)** testbed using only my laptop (Ground Station) and my Android phone (Satellite OBC) to simulate autonomous collision avoidance in space.

---

## 🛠️ How It Works (The "Hack")
Since I couldn't import a Raspberry Pi or Jetson Nano, I used **Termux** on Android to run Python flight software on the phone's ARM processor.

### System Architecture
1.  **The Satellite (My Phone):** Runs `sat_ai.py`. It uses the phone's CPU to calculate orbital mechanics (SGP4) and check for collisions.
2.  **The Ground Station (My Laptop):** Runs `ground_ai.py`. It sends time data to the phone via Wi-Fi (UDP Socket) and waits for a response.
3.  **The Scenario:** I programmed a simulation where "Space Debris" gets dangerously close to the satellite to see if the phone can detect it in time.

---

## 📊 Results (What I Learned)
Despite the simple setup, the results were surprising:
* **Speed:** My phone processed orbital calculations in **< 1 millisecond**.
* **Accuracy:** The system successfully triggered a "RED ALERT" when the debris came within 50km.
* **Conclusion:** You don't always need expensive labs to learn aerospace engineering; sometimes, you just need code and curiosity.

---

## 📂 Project Structure

```bash
ASTRIA/
├── hardware_hil_simulation/     # The code running on my Phone & Laptop
│   ├── sat_ai.py                # Runs on Android (Termux)
│   └── ground_ai.py             # Runs on Laptop (Windows/Linux)
├── data/                        # Sample TLE data used for learning
└── README.md                    # This file

