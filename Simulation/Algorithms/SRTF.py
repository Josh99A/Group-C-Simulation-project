class Process:
    def __init__(self, id, name, arrival_time, burst_time):
        self.id = id
        self.name = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.waiting_time = 0
        self.turnaround_time = 0
        self.completion_time = 0

def srtf_scheduling(processes):
    current_time, completed = 0, 0
    while completed < len(processes):
        idx = -1
        for i, p in enumerate(processes):
            if p.arrival_time <= current_time and p.remaining_time > 0 and (idx == -1 or p.remaining_time < processes[idx].remaining_time):
                idx = i
        if idx != -1:
            processes[idx].remaining_time -= 1
            current_time += 1
            if processes[idx].remaining_time == 0:
                processes[idx].completion_time = current_time
                processes[idx].turnaround_time = current_time - processes[idx].arrival_time
                processes[idx].waiting_time = processes[idx].turnaround_time - processes[idx].burst_time
                completed += 1
        else:
            current_time += 1

def find_avg_time(processes):
    total_wt, total_tat = 0, 0
    for p in processes:
        total_wt += p.waiting_time
        total_tat += p.turnaround_time
    return (total_wt / len(processes), total_tat / len(processes))

def get_execution_order(processes):
    execution_order = []
    for p in processes:
        execution_order.append((p, p.arrival_time, p.completion_time))
    return execution_order
