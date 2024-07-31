class Process:
    def __init__(self, pid, burst_time, priority):
        self.pid = pid
        self.burst_time = burst_time
        self.priority = priority
        self.waiting_time = 0
        self.turnaround_time = 0

def priority_scheduling(processes):
    # Sort processes based on priority (lower number indicates higher priority)
    processes.sort(key=lambda x: x.priority)
    
    time = 0
    for process in processes:
        process.waiting_time = time
        time += process.burst_time
        process.turnaround_time = time
    
    return processes

def calculate_average_times(processes):
    total_waiting_time = sum(process.waiting_time for process in processes)
    total_turnaround_time = sum(process.turnaround_time for process in processes)
    n = len(processes)
    return total_waiting_time / n, total_turnaround_time / n

def print_processes_info(processes):
    print("PID\tBurst Time\tPriority\tWaiting Time\tTurnaround Time")
    for process in processes:
        print(f"{process.pid}\t{process.burst_time}\t\t{process.priority}\t\t{process.waiting_time}\t\t{process.turnaround_time}")

# Example Usage
if __name__ == "__main__":
    processes = [
        Process(pid=1, burst_time=1, priority=1),
        Process(pid=4, burst_time=5, priority=2),
        Process(pid=0, burst_time=10, priority=3),
        Process(pid=2, burst_time=2, priority=4),
        Process(pid=3, burst_time=6, priority=5),
        Process(pid=5, burst_time=1, priority=6),
        Process(pid=7, burst_time=8, priority=7),
        
    ]

    processes = priority_scheduling(processes)
    print_processes_info(processes)

    avg_waiting_time, avg_turnaround_time = calculate_average_times(processes)
    print(f"\nAverage Waiting Time: {avg_waiting_time}")
    print(f"Average Turnaround Time: {avg_turnaround_time}")
