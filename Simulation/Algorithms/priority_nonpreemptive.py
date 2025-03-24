class Process:
    def __init__(self, id, name, arrival_time, burst_time, priority):
        self.id = id
        self.name = name
        self.burst_time = burst_time
        self.arrival_time = arrival_time
        self.priority = priority
        self.waiting_time = 0
        self.turnaround_time = 0
        self.start_time = 0
        self.end_time = 0

    def calculate_waiting_time(self, previous_process):
        if previous_process:
            self.waiting_time = previous_process.burst_time + previous_process.waiting_time

    def calculate_turnaround_time(self):
        self.turnaround_time = self.burst_time + self.waiting_time

def find_avg_time(processes):
    for i in range(1, len(processes)):
        processes[i].calculate_waiting_time(processes[i - 1])
    for p in processes:
        p.calculate_turnaround_time()

    total_wt = 0
    total_tat = 0
    for p in processes:
        total_wt += p.waiting_time
        total_tat += p.turnaround_time
    return (total_wt / len(processes), total_tat / len(processes))
        

   
def priority_scheduling(processes):
    # Sort processes by priority
    processes.sort(key=lambda p: p.priority, reverse=True)

    avg_results = find_avg_time(processes)
    return avg_results

def get_execution_order(processes):
    execution_order = []
    current_time = 0
    for p in processes:
        p.start_time = current_time
        current_time += p.burst_time
        p.end_time = current_time
        execution_order.append((p , p.start_time, p.end_time))
    return execution_order

