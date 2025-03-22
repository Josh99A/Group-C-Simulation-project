from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
import random
from datetime import datetime, timedelta

from .db import get_db


process_bp = Blueprint('process', __name__)

class Process:
    def __init__(self, id, name, arrival_time, burst_time, priority, status):
        self.id = id
        self.name = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.status = status

    def __repr__(self):
        return (f"Process(id={self.id}, name={self.name}, arrival_time={self.arrival_time}, "
                f"burst_time={self.burst_time}, priority={self.priority}, status={self.status})")

@process_bp.route('/')
def index():
    db = get_db()
    processes = db.execute(
        'SELECT id, name, arrival_time, burst_time, priority  FROM process'
    ).fetchall()
    
    scheduling_types = db.execute(
        'SELECT id, name FROM scheduling_type'
    ).fetchall()

    return render_template('index.html', processes=processes, scheduling_types=scheduling_types)


@process_bp.route('/add_process', methods=['POST'])
def add_process():
    name = request.form['name']
    arrival_time = request.form['arrival_time']
    burst_time = request.form['burst_time']
    priority = request.form['priority']
    

    db = get_db()
    db.execute(
        "INSERT INTO process (name, arrival_time, burst_time, priority) VALUES (?, ?, ?, ?)",
        (name, arrival_time, burst_time, priority),
    )
    db.commit()
    flash('Process added successfully')
    return redirect(url_for('process.index'))

@process_bp.route('/delete_process/<int:id>', methods=['POST'])
def delete_process(id):
    db = get_db()
    db.execute('DELETE FROM process WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('process.index'))



# class processes:
#     def __init__(self, id, at, bt, ct):
#         self.id = id
#         self.at = at
#         self.bt = bt
#         self.ct = ct
#         self.tat = self.ct-self.at
#         self.wt = self.tat-self.bt

#     def get(self):
#         print(f"{self.id}\t{self.at}\t{self.bt}\t{self.ct}\t{self.tat}\t{self.wt}")

#     def turnaround(self):
#         return self.tat

#     def waiting(self):
#         return self.wt


# num = int(input("Enter the Number of Processes:"))
# l = []
# ct = 0

# for i in range(num):

#     print(f'Process {i+1}')
#     at = int(input("Enter the Arrival Time:-"))
#     bt = int(input("Enter the Burst Time:-"))
#     if (len(l) == 0):
#         ct = bt
#         l.append(processes(i, at, bt, ct))
#     else:
#         ct += bt
#         l.append(processes(i, at, bt, ct))

#     print("\n")
# avg_tat = 0
# avg_wat = 0
# print("PID\tAT\tBT\tCT\tTAT\tWT")
# for process in l:
#     process.get()

# for process in l:
#     avg_tat += process.turnaround()
#     avg_wat += process.waiting()
# print(f"Avg_turnaround:{avg_tat/num}\nAvg_Waitingtime:{avg_wat/num}")

# # pid at bt
# # 0 0 5
# # 1 2 3
# # 2 6 2
# # 3 7 3


