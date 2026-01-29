import socket
import json
import math
from sgp4.api import Satrec, jday

# --- ASTRIA FLIGHT SOFTWARE (ARM-OBC) ---
# Scenario: Collision Course Simulation

HOST = '127.0.0.1'
PORT = 9999

# 1. Initialize Orbitals (ISS vs Debris)
line1_me = '1 25544U 98067A   19343.69339541  .00001764  00000-0  38792-4 0  9991'
line2_me = '2 25544  51.6439 211.2001 0007417  85.6165 274.5802 15.50103472202482'
sat_me = Satrec.twoline2rv(line1_me, line2_me)

line1_deb = '1 99999U 21000A   19343.69339541  .00001764  00000-0  38792-4 0  9991'
line2_deb = '2 99999  51.6400 211.2100 0007417  85.6165 274.5802 15.50103472202482'
sat_debris = Satrec.twoline2rv(line1_deb, line2_deb)

# 2. Setup UDP Server
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))

print("[SYSTEM] OBC ONLINE. AWAITING UPLINK...")

while True:
    try:
        msg, addr = server.recvfrom(1024)
        offset_mins = float(msg.decode('utf-8'))
        
        # A. Propagate Orbits (SGP4)
        jd, fr = jday(2025, 12, 9, 12, 0, 0 + offset_mins)
        e1, r1, v1 = sat_me.sgp4(jd, fr)
        e2, r2, v2 = sat_debris.sgp4(jd, fr)
        
        # B. Calculate Real Distance
        dx, dy, dz = r1[0]-r2[0], r1[1]-r2[1], r1[2]-r2[2]
        real_dist = math.sqrt(dx**2 + dy**2 + dz**2)
        
        # C. Inject Collision Scenario (Test only)
        # Artificially close gap by 4.9 km/min to force trigger
        sim_dist = max(0.0, real_dist - (offset_mins * 4.9))
        
        # D. Autonomous Decision Logic
        status = "NOMINAL"
        if sim_dist < 50.0:
            status = "CRITICAL WARNING"
            
        # E. Send Telemetry
        resp = {
            "status": status,
            "dist": sim_dist,
            "pos": r1
        }
        server.sendto(json.dumps(resp).encode('utf-8'), addr)
            
    except Exception as e:
        print(f"[ERROR] {e}")
      
