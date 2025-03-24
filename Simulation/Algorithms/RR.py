class Process:
    def __init__(self, id, name, arrival_time, burst_time):
        self.id = id
        self.name = name
        self.burst_time = burst_time
        self.arrival_time = arrival_time
        self.remaining_time = burst_time
        self.waiting_time = 0
        self.turnaround_time = 0
        self.start_times = []
        self.end_times = []

    def calculate_waiting_time(self):
        self.waiting_time = self.turnaround_time - self.burst_time

    def calculate_turnaround_time(self):
        
        self.turnaround_time = self.end_times[-1] - int(self.arrival_time)

def findWaitingTime(processes, quantum):
    t = 0  # Current time
    while True:
        done = True

        
        for p in processes:

            
            if p.remaining_time > 0:
                done = False  # There is a pending process

                if p.remaining_time > quantum:
                   
                    p.start_times.append(t)
                    t += quantum
                    # Record end time
                    p.end_times.append(t)
                    p.remaining_time -= quantum

                # If burst time is smaller than or equal to quantum. Last cycle for this process
                else:
                    # Record start time
                    p.start_times.append(t)

                    # Increase the value of t i.e. shows how much time a process has been processed
                    t += p.remaining_time

                    # Record end time
                    p.end_times.append(t)

                    # Waiting time is current time minus time used by this process
                    p.waiting_time = t - p.burst_time

                    # As the process gets fully executed make its remaining burst time = 0
                    p.remaining_time = 0

        # If all processes are done
        if done:
            break

def findTurnAroundTime(processes):
    # Calculating turnaround time
    for p in processes:
        p.calculate_turnaround_time()

def findavgTime(processes, quantum):
    # Function to find waiting time of all processes
    findWaitingTime(processes, quantum)

    # Function to find turn around time for all processes
    findTurnAroundTime(processes)
    
    n= len(processes)
   
    total_wt = 0
    total_tat = 0
    for p in processes:
        total_wt += p.waiting_time
        total_tat += p.turnaround_time
    return (total_wt / n , total_tat/ n)

   

def getExecutionOrder(processes):
    execution_order = []
    for p in processes:
        for start, end in zip(p.start_times, p.end_times):
            execution_order.append((p.name, start, end))
    # Sort the execution order by the start time
    execution_order.sort(key=lambda x: x[1])
    return execution_order
