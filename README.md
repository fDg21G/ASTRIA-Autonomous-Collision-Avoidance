# ASTRIA-Autonomous-Collision-Avoidance
Student research prototype for LEO CubeSat collision risk assessment.  
⚠️ Student Research Prototype – This project is a learning-focused simulation and decision-support tool built using public TLE data.  
It does not represent an operational or certified autonomous system.

# ASTRIA – AI-assisted collision risk assessment research framework (simulation + prototype)

## What ASTRIA Is / Is Not

### What ASTRIA Is
- A student-built simulation for orbital propagation and conjunction analysis
- A decision-support prototype for exploring collision risk
- A learning project using open-source orbital data (TLE)

### What ASTRIA Is Not
- Not a real satellite control system
- Not an autonomous maneuver execution platform
- Not validated with classified or proprietary datasets

## Overview
ASTRIA is an independent aerospace research project exploring collision risk assessment for CubeSats in Low Earth Orbit (LEO).  
While the current prototype focuses on **simulation and conjunction analysis using public TLE data**, the project aims to **integrate AI-assisted decision-making in future iterations**.

## Example Simulation Script
This repository includes a simple Python script demonstrating orbital propagation and conjunction analysis using public TLE data.

📁 `scripts/astria_simulation.py`

⚠️ This script is a **student research prototype**. Results are approximate and intended for learning purposes only.

## Problem Statement
LEO is increasingly congested with active satellites and debris. CubeSats often lack continuous ground-based monitoring, increasing collision risk.

## Solution (Prototype)
ASTRIA integrates:
- TLE data ingestion (for simulation purposes)
- SGP4 orbital propagation
- Multi-stage conjunction screening (educational)
- Prototype risk classification logic  
> Conceptual plans include **AI-assisted decision-making for CubeSats in future iterations**.

## Technologies Used
- Python
- SGP4 (orbital propagation)
- NumPy
- Basic scripting for conjunction analysis

## Project Status
Prototype / Research Stage – No hardware or operational deployment yet

## Author
Houssam Rharbi  
Independent Research Project 2024–2025

## 📄 Technical Dissertation
The complete technical dissertation describing the ASTRIA system architecture, algorithms, simulations, and prototype logic is available here:  
[Download the full technical dissertation (PDF)](ASTRIA_Dissertation_HR.pdf)
