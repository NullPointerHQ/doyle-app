-- =============================================
--          To-Do List App Database
-- =============================================

DROP TABLE IF EXISTS task; -- TO DO: Come up with name for app, replace 'app' with name

-- Task Entity
CREATE TABLE IF NOT EXISTS task(
    -- Attributes
    u_id            INTEGER PRIMARY KEY AUTOINCREMENT,
    name            TEXT NOT NULL,
    description     TEXT,
    state           INTEGER NOT NULL, -- 0 for Incomplete, 1 for Complete, 2 for Archival, 3 for Deletion
    target_time     TEXT,
    target_date     TEXT,

    -- Constraints
    CONSTRAINT name_len         CHECK (length(name) <= 50),
    CONSTRAINT time_len         CHECK (length(target_time) <= 15),
    CONSTRAINT date_len         CHECK (length(target_date) <= 15),

    CONSTRAINT valid_task_state CHECK (state IN (0, 1, 2, 3)) -- Makes sure the state of a task is a valid option, shouldn't be an issue but just to be safe
);