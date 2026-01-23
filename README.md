# ASTRIA-Autonomous-Collision-Avoidance
AI-driven autonomous collision avoidance and risk assessment system for LEO CubeSats.
> ⚠️ Student Research Prototype  
> This project is a learning-focused simulation and decision-support tool built using public data.  
> It does not represent an operational or certified autonomous system.
# ASTRIA – AI-Driven Autonomous Collision Avoidance for LEO CubeSats
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
ASTRIA is an independent aerospace research project focused on developing an
autonomous, AI-assisted collision risk assessment and avoidance system for
CubeSats operating in Low Earth Orbit (LEO).
## Example Simulation Script

This repository includes a simple Python script demonstrating
orbital propagation and conjunction analysis using public TLE data.

📁 `scripts/astria_simulation.py`

⚠️ This script is a **student research prototype**.
Results are approximate and intended for learning purposes only.
## Problem Statement
LEO is increasingly congested with active satellites and debris.
CubeSats often lack continuous ground-based monitoring, increasing collision risk.

## Solution
ASTRIA integrates:
- Real-time TLE ingestion
- SGP4 orbital propagation
- Multi-stage conjunction screening
- Machine learning-based risk classification
- Fuel-efficient maneuver planning

## Technologies Used
- Python
- SGP4
- NumPy / SciPy
- XGBoost
- Poliastro
- Monte Carlo simulations

## Project Status
Prototype / Research Stage

## Author
Houssam Rharbi  
Independent Research Project  
2024–2025
## Future Directions
- Hardware-in-the-loop experimentation
- Edge-AI based onboard reasoning
## 📄 Technical Dissertation

The complete technical dissertation describing the ASTRIA system architecture,
algorithms, simulations, and AI models is available here:
[Download the full technical dissertation (PDF)](./ASTRIA_Dissertation_HR.pdf)
