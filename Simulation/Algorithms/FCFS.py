class Process:
    def __init__(self, id, name, arrival_time, burst_time):
        self.id = id
        self.name = name
        self.burst_time = burst_time
        self.arrival_time = arrival_time
        self.waiting_time = 0
        self.turnaround_time = 0
        self.start_time = 0
        self.end_time = 0

def find_waiting_time(processes):
    processes[0].waiting_time = 0

    # calculating waiting time
    for i in range(1, len(processes)):
        processes[i].waiting_time = processes[i - 1].burst_time + processes[i - 1].waiting_time

def find_turnaround_time(processes):
    # Calculating turnaround time by adding burst_time + waiting_time
    for p in processes:
        p.turnaround_time = p.burst_time + p.waiting_time

def find_avg_time(processes):
    find_waiting_time(processes)
    find_turnaround_time(processes)

    total_wt = 0
    total_tat = 0
    for p in processes:
        total_wt += p.waiting_time
        total_tat += p.turnaround_time

    return (total_wt / len(processes), total_tat / len(processes))

def fcfs_scheduling(processes):
    # Sort processes by arrival time
    processes.sort(key=lambda p: p.arrival_time)
    avg_results = find_avg_time(processes)
    return avg_results

def get_execution_order(processes):
    # Sort processes by arrival time
    processes.sort(key=lambda p: p.arrival_time)
    execution_order = []
    current_time = 0
    for p in processes:
        p.start_time = current_time
        current_time += p.burst_time
        p.end_time = current_time
        execution_order.append((p.name, p.start_time, p.end_time))
    return execution_order

