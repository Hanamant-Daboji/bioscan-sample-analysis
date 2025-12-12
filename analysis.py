import csv
from datetime import datetime

# Sample laboratory measurements (example data)
samples = [
    {"id": 1, "value": 12.5},
    {"id": 2, "value": 9.3},
    {"id": 3, "value": 15.7},
    {"id": 4, "value": 11.2},
]

def analyze(samples):
    total = len(samples)
    avg = sum(s["value"] for s in samples) / total

    timestamp = datetime.utcnow().isoformat() + "Z"
    return total, avg, timestamp

def main():
    total, avg, timestamp = analyze(samples)

    output_file = "analysis_output.csv"

    with open(output_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Generated At", "Total Samples", "Average Value"])
        writer.writerow([timestamp, total, round(avg, 2)])

    print(f"Analysis completed. Output saved to {output_file}")

if __name__ == "__main__":
    main()
