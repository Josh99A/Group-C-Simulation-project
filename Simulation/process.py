from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from .Algorithms import FCFS, SJF, SRTF, RR, priority_nonpreemptive, priority_preemtive
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

def get_processes():
    db = get_db()
    processes = db.execute(
        'SELECT id, name, arrival_time, burst_time, priority FROM process'
    ).fetchall()
    return processes

def get_schedules():
    db = get_db()
    scheduler = db.execute(
        'SELECT id, name FROM scheduling_type'
    ).fetchall()
    return scheduler


@process_bp.route('/')
def index():
    db = get_db()
    processes = get_processes()
    scheduling_types = get_schedules()

    return render_template('index.html', processes=processes, scheduling_types=scheduling_types)

@process_bp.route('/run_simulation', methods=['POST'])
def run_simulation():
    processes = get_processes()
    selected_scheduling_type = request.form['algorithm']
    scheduling_types = get_schedules()
   
   
    if selected_scheduling_type == '1':
        process_list = []
        for process in processes:
            process_list.append(FCFS.Process(int(process['id']), process['name'], int(process['arrival_time']), int(process['burst_time'])))
        
        avg_waiting_time, avg_turnaround_time = FCFS.fcfs_scheduling(process_list)
        execution_order = FCFS.get_execution_order(process_list)
        
 
        
        return render_template('index.html',
                               processes=processes,
                               process_result_list=process_list,
                               scheduling_types=scheduling_types,
                               selected_scheduling_type= str(selected_scheduling_type),
                               execution_order=execution_order,
                               avg_turnaround_time=avg_turnaround_time,
                               avg_waiting_time=avg_waiting_time)
        
            
    elif selected_scheduling_type == '3':
        print("SJF")
        process_list = []
        for process in processes:
            process_list.append(SJF.Process(process['id'], process['name'], process['arrival_time'], process['burst_time']))
            
        
        avg_waiting_time, avg_turnaround_time = SJF.sjf_scheduling(process_list)
        execution_order = SJF.get_execution_order(process_list)
        
 
        
        return render_template('index.html',
                               processes=processes,
                               process_result_list=process_list,
                               scheduling_types=scheduling_types,
                               selected_scheduling_type=selected_scheduling_type,
                               execution_order=execution_order,
                               avg_turnaround_time=avg_turnaround_time,
                               avg_waiting_time=avg_waiting_time)
        
        
    elif selected_scheduling_type == '2':
        print("SRTF")

        process_list = []
        for process in processes:
            process_list.append(SRTF.Process(process['id'], process['name'], int(process['arrival_time']), int(process['burst_time'])))
       
        SRTF.srtf_scheduling(process_list)
        avg_waiting_time, avg_turnaround_time = SRTF.find_avg_time(process_list)
        
        execution_order = SRTF.get_execution_order(process_list)
       
        
 
        
        return render_template('index.html',
                               processes=processes,
                               process_result_list=process_list,
                               scheduling_types=scheduling_types,
                               selected_scheduling_type=selected_scheduling_type,
                               execution_order=execution_order,
                               avg_turnaround_time=avg_turnaround_time,
                               avg_waiting_time=avg_waiting_time)
    elif selected_scheduling_type == '4':
        
        quantum = int(request.form["time_quantum"])
        print('Round Robin')
        process_list = []
        for process in processes:
            process_list.append(RR.Process(process['id'], process['name'], process['arrival_time'], process['burst_time']))
            
        
        avg_waiting_time, avg_turnaround_time = RR.findavgTime(process_list, quantum)
        execution_order = RR.getExecutionOrder(process_list)
        
 
        
        return render_template('index.html',
                               processes=processes,
                               process_result_list=process_list,
                               scheduling_types=scheduling_types,
                               selected_scheduling_type=selected_scheduling_type,
                               execution_order=execution_order,
                               avg_turnaround_time=avg_turnaround_time,
                               avg_waiting_time=avg_waiting_time)
    elif selected_scheduling_type == '6':
        print('Priority non-preemptive')
        
        process_list = []
        for process in processes:
            process_list.append(priority_nonpreemptive.Process(process['id'], process['name'], process['arrival_time'], process['burst_time'], process['priority']))
            
        
        avg_waiting_time, avg_turnaround_time = priority_nonpreemptive.priority_scheduling(process_list)
        execution_order = priority_nonpreemptive.get_execution_order(process_list)
        
 
        
        return render_template('index.html',
                               processes=processes,
                               process_result_list=process_list,
                               scheduling_types=scheduling_types,
                               selected_scheduling_type=selected_scheduling_type,
                               execution_order=execution_order,
                               avg_turnaround_time=avg_turnaround_time,
                               avg_waiting_time=avg_waiting_time)
    elif selected_scheduling_type == '5':
        print('Priority preemptive')
        process_list = []
        for process in processes:
            process_list.append(priority_preemtive.Process(process['id'], process['name'], int(process['arrival_time']), int(process['burst_time']), int(process['priority'])))
            
        number_of_processes = len(process_list)
            
        
        avg_waiting_time, avg_turnaround_time = priority_preemtive.priority_scheduling(process_list, number_of_processes)[0:2]
        execution_order = priority_preemtive.get_execution_order(priority_preemtive.priority_scheduling(process_list, number_of_processes)[2])
        
        
        
        return render_template('index.html',
                               processes=processes,
                               process_result_list=process_list,
                               scheduling_types=scheduling_types,
                               selected_scheduling_type=selected_scheduling_type,
                               execution_order=execution_order,
                               avg_turnaround_time=avg_turnaround_time,
                               avg_waiting_time=avg_waiting_time)
  
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

@process_bp.route('/clear_db', methods=['GET'])
def clear_db():
    db = get_db()
    db.execute('DELETE FROM process')
    db.commit()
    return redirect(url_for('process.index'))



