class Process:
    def __init__(self, pid, burst_time):
        self.pid = pid
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.waiting_time = 0
        self.turnaround_time = 0

def round_robin(processes, time_quantum):
    time = 0
    queue = processes.copy()
    while queue:
        for process in queue.copy():
            if process.remaining_time > time_quantum:
                time += time_quantum
                process.remaining_time -= time_quantum
            else:
                time += process.remaining_time
                process.remaining_time = 0
                process.turnaround_time = time
                process.waiting_time = time - process.burst_time
                queue.remove(process)
    return processes

def calculate_average_times(processes):
    total_waiting_time = sum(process.waiting_time for process in processes)
    total_turnaround_time = sum(process.turnaround_time for process in processes)
    n = len(processes)
    return total_waiting_time / n, total_turnaround_time / n

def print_processes_info(processes):
    print("PID\tBurst Time\tWaiting Time\tTurnaround Time")
    for process in processes:
        print(f"{process.pid}\t{process.burst_time}\t\t{process.waiting_time}\t\t{process.turnaround_time}")

# Example Usage
if __name__ == "__main__":
    processes = [
        Process(pid=1, burst_time=10),
        Process(pid=2, burst_time=5),
        Process(pid=3, burst_time=8),
    ]
    time_quantum = 2

    processes = round_robin(processes, time_quantum)
    print_processes_info(processes)

    avg_waiting_time, avg_turnaround_time = calculate_average_times(processes)
    print(f"\nAverage Waiting Time: {avg_waiting_time}")
    print(f"Average Turnaround Time: {avg_turnaround_time}")
