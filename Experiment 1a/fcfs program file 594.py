class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.start_time = 0
        self.completion_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0

def fcfs_scheduling(processes):
    processes.sort(key=lambda x: x.arrival_time)
    
    current_time = 0
    for process in processes:
        if current_time < process.arrival_time:
            current_time = process.arrival_time
        process.start_time = current_time
        process.completion_time = process.start_time + process.burst_time
        process.turnaround_time = process.completion_time - process.arrival_time
        process.waiting_time = process.turnaround_time - process.burst_time
        current_time += process.burst_time
    
    return processes

def print_scheduling_result(processes):
    print(f"{'PID':<5}{'Burst':<10}{'Turnaround':<15}{'Waiting':<10}")
    for process in processes:
        print(f"{process.pid:<5}{process.burst_time:<10}{process.turnaround_time:<15}{process.waiting_time:<10}")
    avg_turnaround_time = sum(p.turnaround_time for p in processes) / len(processes)
    avg_waiting_time = sum(p.waiting_time for p in processes) / len(processes)
    print(f"\nAverage Turnaround Time: {avg_turnaround_time:.2f}")
    print(f"Average Waiting Time: {avg_waiting_time:.2f}")
    
# Example usage
if __name__ == "__main__":
    processes = [
        Process(1, 0, 6),
        Process(2, 1, 8),
        Process(3, 2, 7),
        Process(4, 3, 3)
    ]
    
    scheduled_processes = fcfs_scheduling(processes)
    print_scheduling_result(scheduled_processes)
