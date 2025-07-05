import time
import random
from datetime import datetime

def generate_mock_logs(num_logs=200):
    logs = []
    threats = ["phishing_attempt", "ddos_flood", "suspicious_ip", "normal"]
    ips = [f"192.168.{random.randint(1, 254)}.{random.randint(1, 254)}" for _ in range(10)]

    for _ in range(num_logs):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ip = random.choice(ips)
        event = random.choices(threats, weights=[0.1, 0.05, 0.15, 0.7], k=1)[0]
        log = f"{timestamp} | {ip} | {event}"
        logs.append(log)
        time.sleep(0.01)
    return logs

def analyze_logs(logs):
    threats_detected = {"phishing_attempt": 0, "ddos_flood": 0, "suspicious_ip": 0}
    threat_logs = []

    for log in logs:
        for threat in threats_detected:
            if threat in log:
                threats_detected[threat] += 1
                threat_logs.append(log)
                break
    return threats_detected, threat_logs

def calculate_efficiency(logs, start_time):
    end_time = time.time()
    total_time = end_time - start_time
    baseline_time = len(logs) * 0.05
    reduction = ((baseline_time - total_time) / baseline_time) * 100
    return max(0, reduction)

def generate_report(threats_detected, threat_logs, efficiency):
    with open("threatsync_report.txt", "w") as f:
        f.write("ThreatSync – Log Analysis Report\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"Total Threats Detected: {sum(threats_detected.values())}\n")
        f.write(f" - Phishing Attempts: {threats_detected['phishing_attempt']}\n")
        f.write(f" - DDoS Floods: {threats_detected['ddos_flood']}\n")
        f.write(f" - Suspicious IPs: {threats_detected['suspicious_ip']}\n\n")
        f.write(f"Detection Efficiency: {efficiency:.2f}% faster than baseline\n\n")
        f.write("Threat Logs:\n")
        for log in threat_logs:
            f.write(f"{log}\n")

def run_threatsync():
    print("ThreatSync – Starting log analysis...")
    start_time = time.time()
    logs = generate_mock_logs(200)
    threats_detected, threat_logs = analyze_logs(logs)
    efficiency = calculate_efficiency(logs, start_time)
    generate_report(threats_detected, threat_logs, efficiency)
    print(f"✅ Done! Detected {sum(threats_detected.values())} threats. Report saved to 'threatsync_report.txt'.")

if __name__ == "__main__":
    run_threatsync()
