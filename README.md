# 🛰️ ASTRIA: Autonomous Collision Avoidance System
[![Status: V2 Research Phase](https://img.shields.io/badge/Status-V2_Research_Phase-blue.svg)]()

> **From Deterministic Distance to Probabilistic Risk:** A Hardware-in-the-Loop (HIL) testbed simulating satellite collision avoidance on Edge ARM processors.

## 📖 Project Evolution

ASTRIA is an independent aerospace systems engineering project. The architecture is evolving across two distinct phases to reflect true orbital dynamics:

### Phase 1: Edge AI Feasibility (Completed)
Demonstrated that consumer ARM hardware (Android via Termux) can propagate SGP4 orbital mechanics and execute XGBoost risk screening in real-time ($<2$ms latency). However, this phase relied on deterministic Euclidean distance (KD-Trees), which fundamentally conflates geometric proximity with actual collision risk.

### Phase 2: Probabilistic Rigor & B-Plane Projection (Current Focus)
Space is a highly dynamic environment governed by uncertainty. ASTRIA V2 transitions from 3D distance to **Probability of Collision ($P_c$)** integration. 
* **Covariance Modeling:** Replacing scalar distances with $3 \times 3$ RTN covariance matrices to model TLE (Two-Line Element) inaccuracies.
* **B-Plane Encounter:** Projecting the 3D error ellipsoid onto the 2D encounter plane (B-Plane) orthogonal to the relative velocity vector.
* **Mahalanobis Distance:** Re-training the XGBoost arbiter to evaluate risk using Mahalanobis distance instead of Euclidean distance, capturing the true "uncertainty lengths" between objects.

## 🛠️ System Architecture

* **The Satellite Node (Edge ARM):** Runs the orbital propagator (SGP4) and the mathematical risk engine natively on an ARM processor.
* **The Ground Station:** A localized simulation injecting real-world RF constraints (e.g., Gilbert-Elliott packet loss, Doppler shift delays) into the UDP telemetry link.

## 👨‍💻 Author
**Houssam Rharbi**  Casablanca, Morocco
