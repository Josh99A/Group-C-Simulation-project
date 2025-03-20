from flask import Flask, Blueprint, render_template, redirect, url_for
import random
from datetime import datetime, timedelta

app = Flask(__name__)
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
    processes = []
    return render_template('index.html', processes=processes)

@process_bp.route('/generate')
def generate_processes():
    processes = []
    for i in range(1, 6):  
        name = f'P{i}'
        arrival_time = random.randint(0,60)
        burst_time = random.randint(10, 50)
        priority = random.randint(1, 5)
        status = random.choice(['waiting', 'running', 'completed'])
        processes.append(Process(i, name, arrival_time, burst_time, priority, status))
    return render_template('index.html', processes=processes)

