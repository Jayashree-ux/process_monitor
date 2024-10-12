# process_monitor.py (after the fix)

import os
import psutil
import time
import argparse
import json
import csv

class ProcessMonitor:
    def __init__(self):
        self.processes = []

    def fetch_processes(self):
        """Fetch the current processes along with CPU and memory usage"""
        self.processes = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
            self.processes.append(proc.info)

    def display_processes(self):
        """Display the processes in a simple table format"""
        print(f"{'PID':<10}{'Process Name':<25}{'CPU (%)':<10}{'Memory (%)':<10}")
        print("=" * 55)
        for proc in self.processes:
            print(f"{proc['pid']:<10}{proc['name']:<25}{proc['cpu_percent']:<10}{proc['memory_percent']:<10}")

    def export_to_file(self, filename, filetype):
        """Export the process information to a CSV or JSON file"""
        if filetype == "csv":
            with open(filename, 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=self.processes[0].keys())
                writer.writeheader()
                writer.writerows(self.processes)
            print(f"Processes exported to {filename}")
        elif filetype == "json":
            with open(filename, 'w') as jsonfile:
                json.dump(self.processes, jsonfile, indent=4)
            print(f"Processes exported to {filename}")
        else:
            print("Unsupported file format!")

    def run(self, interval=2):
        """Main loop for continuous process monitoring with optimized sleep"""
        try:
            while True:
                os.system('clear')
                self.fetch_processes()
                self.display_processes()
                time.sleep(interval)  # Implementing sleep interval to reduce CPU usage
        except KeyboardInterrupt:
            print("Monitoring stopped.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Real-time Process Monitor Utility")
    parser.add_argument('-e', '--export', type=str, help="Export processes to a file (csv or json)")
    parser.add_argument('-f', '--file', type=str, help="File name for export")
    parser.add_argument('-i', '--interval', type=int, default=2, help="Interval (seconds) between process updates")

    args = parser.parse_args()

    monitor = ProcessMonitor()

    if args.export and args.file:
        monitor.fetch_processes()
        monitor.export_to_file(args.file, args.export)
    else:
        monitor.run(args.interval)
