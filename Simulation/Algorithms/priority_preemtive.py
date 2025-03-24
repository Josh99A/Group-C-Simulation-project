class Process:
    def __init__(self, id, name, arrival_time, burst_time, priority):
        self.id = id
        self.name = name
        self.burst_time = burst_time
        self.arrival_time = int(arrival_time)
        self.priority = priority
        self.remaining_time = burst_time
        self.waiting_time = 0
        self.turnaround_time = 0
        self.response_time = -1
        self.intime = -1
        self.outtime = 0
        self.start_time = 0
        self.end_time = 0

def insert(Heap, value, heapsize, currentTime):
    start = heapsize[0]
    Heap[start] = value
    if Heap[start].intime == -1:
        Heap[start].intime = currentTime
    heapsize[0] += 1

    # Ordering the Heap
    while start != 0 and Heap[(start - 1) // 2].priority > Heap[start].priority:
        Heap[(start - 1) // 2], Heap[start] = Heap[start], Heap[(start - 1) // 2]
        start = (start - 1) // 2

def order(Heap, heapsize, start):
    smallest = start
    left = 2 * start + 1
    right = 2 * start + 2
    if left < heapsize[0] and Heap[left].priority < Heap[smallest].priority:
        smallest = left
    if right < heapsize[0] and Heap[right].priority < Heap[smallest].priority:
        smallest = right

    # Ordering the Heap
    if smallest != start:
        Heap[start], Heap[smallest] = Heap[smallest], Heap[start]
        order(Heap, heapsize, smallest)

def extractminimum(Heap, heapsize, currentTime):
    min_process = Heap[0]
    if min_process.response_time == -1:
        min_process.response_time = currentTime - min_process.arrival_time
    heapsize[0] -= 1
    if heapsize[0] >= 1:
        Heap[0] = Heap[heapsize[0]]
        order(Heap, heapsize, 0)
    return min_process

def scheduling(Heap, array, n, heapsize, currentTime, execution_order):
    if heapsize[0] == 0:
        return

    min_process = extractminimum(Heap, heapsize, currentTime)
    min_process.outtime = currentTime + 1
    min_process.remaining_time -= 1
    execution_order.append((min_process.name, currentTime, currentTime + 1))
    print(f"process id = {min_process.id} current time = {currentTime}")

    # If the process is not yet finished, insert it back into the Heap
    if min_process.remaining_time > 0:
        insert(Heap, min_process, heapsize, currentTime)
        return

    for i in range(n):
        if array[i].id == min_process.id:
            array[i] = min_process
            break

def priority_scheduling(array, n):
    array.sort(key=lambda x: x.arrival_time)

    total_waiting_time = 0
    total_turnaround_time = 0
    inserted_process = 0
    heap_size = [0]
    current_time = array[0].arrival_time
    total_response_time = 0

    Heap = [None] * (4 * n)
    execution_order = []

    while True:
        if inserted_process != n:
            for i in range(n):
                if array[i].arrival_time == current_time:
                    inserted_process += 1
                    array[i].intime = -1
                    array[i].response_time = -1
                    insert(Heap, array[i], heap_size, current_time)
        scheduling(Heap, array, n, heap_size, current_time, execution_order)
        current_time += 1
        if heap_size[0] == 0 and inserted_process == n:
            break

    for i in range(n):
        total_response_time += array[i].response_time
        total_waiting_time += (array[i].outtime - array[i].intime - array[i].burst_time)
        total_turnaround_time += (array[i].outtime - array[i].intime)

   

    return (total_waiting_time / n, total_turnaround_time / n, execution_order)

def get_execution_order(execution_order):
    intervals = []
    if not execution_order:
        return intervals
    current_process = execution_order[0][0]
    start_time = execution_order[0][1]
    for i in range(1, len(execution_order)):
        if execution_order[i][0] != current_process:
            intervals.append((current_process, start_time, execution_order[i][1]))
            current_process = execution_order[i][0]
            start_time = execution_order[i][1]
    
    intervals.append((current_process, start_time, execution_order[-1][2]))
    return intervals

