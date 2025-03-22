DROP TABLE IF EXISTS process;
DROP TABLE IF EXISTS scheduling_type;

CREATE TABLE process (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    arrival_time  NOT NULL,
    burst_time INTEGER NOT NULL,
    completed_time INTEGER,
    waiting_time INTEGER,
    turnaround_time INTEGER,
    priority INTEGER,
    time_quantum INTEGER,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE scheduling_type (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

-- Insert default scheduling types
INSERT INTO scheduling_type (name) VALUES ('First Come First Served');
INSERT INTO scheduling_type (name) VALUES ('SJF Preemptive');
INSERT INTO scheduling_type (name) VALUES ('SJF Non-preemptive');
INSERT INTO scheduling_type (name) VALUES ('Round Robin');
INSERT INTO scheduling_type (name) VALUES ('Priority Scheduling Preemptive');
INSERT INTO scheduling_type (name) VALUES ('Priority Scheduling Non-preemptive');