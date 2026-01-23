# Student research prototype
# Project: ASTRIA - Conjunction Analysis & Collision Risk Research Prototype
# Author: Houssam Rharbi
# Results are approximate and intended for learning purposes only.
# NOTE: This prototype uses public TLE data (e.g., Celestrak). It does NOT perform real satellite maneuvers
# and is not validated with classified/proprietary datasets.

import numpy as np
from sgp4.api import Satrec, jday
from datetime import datetime, timedelta

# --- 1. Load Satellite Data (TLE - Two-Line Elements) ---
# In a real scenario, this data is fetched from CelesTrak.
# Here we use hard-coded sample data for demonstration purposes only.
# Make sure to replace these with real TLEs or a TLE file for real tests.

# Satellite A: ISS (ZARYA) - example TLE (may be outdated)
tle_line1_satA = "1 25544U 98067A   23345.42436521  .00014798  00000-0  26845-3 0  9997"
tle_line2_satA = "2 25544  51.6415 168.6473 0001356 222.0004 225.2635 15.49553757429524"

# Satellite B: Hypothetical debris (example)
tle_line1_satB = "1 99999U 23999A   23345.42436521  .00015000  00000-0  30000-3 0  9991"
tle_line2_satB = "2 99999  51.6400 168.6500 0002000 220.0000 224.0000 15.49600000000001"

# Initialize SGP4 satellite objects
satellite_A = Satrec.twoline2rv(tle_line1_satA, tle_line2_satA)
satellite_B = Satrec.twoline2rv(tle_line1_satB, tle_line2_satB)

print("--- ASTRIA Simulation Started ---")
print("Note: This is a student research prototype using public TLE data.")
print("Propagating orbits for: ISS (Sat A) vs Debris Object (Sat B)")

# --- 2. Simulation Settings ---
start_time = datetime.utcnow()
simulation_duration_hours = 24  # Simulate for the next 24 hours
time_step_seconds = 60          # Check distance every 60 seconds

min_distance = float('inf')
time_of_closest_approach = start_time
checks = 0

# --- 3. Main Loop: Orbital Propagation & Conjunction Analysis ---
print("Running simulation...")

current_time = start_time
end_time = start_time + timedelta(hours=simulation_duration_hours)

while current_time < end_time:
    # Convert current time to Julian Date (required by SGP4)
    jd, fr = jday(current_time.year, current_time.month, current_time.day,
                  current_time.hour, current_time.minute, current_time.second + current_time.microsecond*1e-6)

    # Get Position (r) and Velocity (v) for both satellites
    e1, r1, v1 = satellite_A.sgp4(jd, fr)
    e2, r2, v2 = satellite_B.sgp4(jd, fr)

    # Check for SGP4 errors (e.g., if satellite decays or TLE invalid)
    if e1 != 0 or e2 != 0:
        # skip this time step but count it as a check
        current_time += timedelta(seconds=time_step_seconds)
        checks += 1
        continue

    # Convert positions to Numpy arrays for easy math
    pos_A = np.array(r1)  # Position in km (x, y, z)
    pos_B = np.array(r2)

    # Calculate Euclidean distance between the two satellites (km)
    distance_km = np.linalg.norm(pos_A - pos_B)

    # Track the minimum distance found
    if distance_km < min_distance:
        min_distance = distance_km
        time_of_closest_approach = current_time

    # Step forward in time
    current_time += timedelta(seconds=time_step_seconds)
    checks += 1

# --- 4. Risk Assessment (Decision-Support Logic) ---
# IMPORTANT: These thresholds are educational proxies only.
# Real operational systems use probability-of-collision and covariance data.
risk_level = "UNKNOWN"
action_recommendation = ""

# Example proxy thresholds (kilometers):
# HIGH: < 0.1 km (100 meters) — very close (educational)
# MEDIUM: 0.1 - 1.0 km
# LOW: >= 1.0 km
if min_distance == float('inf'):
    risk_level = "NO DATA"
    action_recommendation = "Simulation produced no valid positional results."
else:
    if min_distance < 0.1:
        risk_level = "HIGH (CRITICAL)"
        action_recommendation = "Educational alert: investigate further (no autonomous maneuver performed)."
    elif min_distance < 1.0:
        risk_level = "MEDIUM"
        action_recommendation = "Monitor closely and run higher-fidelity analysis."
    else:
        risk_level = "LOW"
        action_recommendation = "No immediate action needed for this prototype."

# --- 5. Output Results ---
print("\n" + "="*50)
print("             ASTRIA SIMULATION RESULTS             ")
print("="*50)
print(f"Simulation Window: {simulation_duration_hours} Hours")
print(f"Time (UTC) of Closest Approach: {time_of_closest_approach}")
if min_distance == float('inf'):
    print("Minimum Distance: No valid result (check TLEs / propagation errors)")
else:
    print(f"Minimum Distance: {min_distance:.6f} km")
print(f"Number of checks performed: {checks}")
print("-" * 50)
print(f"RISK LEVEL: {risk_level}")
print(f"Recommendation: {action_recommendation}")
print("="*50)
