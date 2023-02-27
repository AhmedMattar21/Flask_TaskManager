CREATE TABLE IF NOT EXISTS tasks(
        id integer primary key,
        task text,
        add_date datetime,
        is_completed integer default 0
);
