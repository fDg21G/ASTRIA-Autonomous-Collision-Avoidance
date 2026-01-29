import socket
import json
import time

# --- ASTRIA MISSION CONTROL ---
# Hardware-in-the-Loop Dashboard

IP = '127.0.0.1'
PORT = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.settimeout(3.0)

print("--- COLLISION MONITOR ACTIVE ---")

# Simulate 60 minutes timeline
for t in range(0, 65, 5):
    try:
        # 1. Uplink: Request Prediction
        client.sendto(str(t).encode('utf-8'), (IP, PORT))
        
        # 2. Downlink: Receive Telemetry
        data, _ = client.recvfrom(4096)
        telemetry = json.loads(data.decode('utf-8'))
        
        status = telemetry['status']
        dist = telemetry['dist']
        
        # 3. Display Logic (Red = Danger)
        if "CRITICAL" in status:
            print(f"[T+{t}m] \033[91m{status} !!! RANGE: {dist:.2f} km\033[0m")
        else:
            print(f"[T+{t}m] \033[92m{status}\033[0m | Range: {dist:.2f} km")
            
        time.sleep(0.5)
        
    except Exception as e:
        print(f"[ERROR] {e}")
        break

print("--- SIMULATION END ---")

