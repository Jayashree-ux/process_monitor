1. Clone or Download the Project
Download or clone the project from your repository:

bash
Copy code
git clone https://github.com/your_username/process-monitor-utility.git
Navigate to the project directory:

bash
Copy code
cd process-monitor-utility
2. Running the Real-Time Process Monitor
To start monitoring system processes in real-time, run:

bash
Copy code
python process_monitor.py
This will start a continuous monitoring session, displaying the process ID, process name, CPU percentage, and memory usage in a table format. The default refresh interval is 2 seconds.

3. Exporting Process Information
You can also export the current process information to a file:

Export to CSV:
bash
Copy code
python process_monitor.py --export csv --file processes.csv
Export to JSON:
bash
Copy code
python process_monitor.py --export json --file processes.json
4. Customizing the Monitoring Interval
By default, the monitor updates the process information every 2 seconds. You can customize this interval using the --interval flag:

bash
Copy code
python process_monitor.py --interval 5
This example will update the processes every 5 seconds.

5. Stopping the Monitor
To stop the real-time monitoring, press Ctrl + C in your terminal.
