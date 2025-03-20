DROP TABLE IF EXISTS process;


CREATE TABLE process (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    arrival_time TIMESTAMP NOT NULL,
    burst_time INTEGER NOT NULL,
    priority INTEGER NOT NULL,
    status TEXT NOT NULL
);

