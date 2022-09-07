CREATE TABLE users(
    id SERIAL NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    name TEXT NOT NULL
);
ALTER TABLE
    users ADD PRIMARY KEY(id);

CREATE TABLE shifts(
    id SERIAL NOT NULL,
    user_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT NOT NULL
);
ALTER TABLE
    shifts ADD PRIMARY KEY(id);

CREATE TABLE shift_entry(
    id SERIAL NOT NULL,
    shift_id INTEGER NOT NULL,
    time_clock_in TIMESTAMP NOT NULL,
    time_clock_out TIMESTAMP,
    description TEXT NOT NULL
);
ALTER TABLE
    shift_entry ADD PRIMARY KEY(id);

ALTER TABLE shifts
    ADD CONSTRAINT shifts_users_id_foreign FOREIGN KEY(user_id) REFERENCES users(id);
ALTER TABLE shift_entry
    ADD CONSTRAINT shift_entry_shifts_id_foreign FOREIGN KEY(shift_id) REFERENCES shifts(id);