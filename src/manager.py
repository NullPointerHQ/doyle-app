# =============================================
#         To-Do List Database Manager
# =============================================

import sqlite3 

# - Makes the connection between the database and database manager
def open_cnx():
    # - Connects to DB and arranges the output to be a row
    cnx = sqlite3.connect("schema.db")
    cnx.row_factory = sqlite3.Row

    # -  Loads schema.sql as 'Read-Only'
    with open("src/schema.sql", "r", encoding="utf-8") as f: 
        schema_sql = f.read()

    cnx.executescript(schema_sql) 
    return cnx, schema_sql

# - Creates, outputs and deletes a entry in the table to test the connection 
def test_cnx(cursor, connection):

    # - Inserting dummy entry
    print("Inserting dummy entry. \n")
    query =  ("INSERT INTO task(name, description, state, target_time, target_date) VALUES(?, ?, ?, ?, ?)")
    parameters = ("Test Task", "Test Description", 0, "00:00:00", "2026-01-01")

    cursor.execute(query, parameters)
    connection.commit()

    # - Pulling all dummy entries
    print("Insertion of dummy entry successful, pulling dummy entry from database.\n")
    query = (" SELECT * FROM task WHERE name = ?")
    parameters = ("Test Task",)
    cursor.execute(query, parameters)
    print(cursor.fetchone())

    # - Deleting all dummy entries
    print("\nDummy entry inserted and pulled successfully, deleting entry from database.\n")
    query = (" DELETE FROM task WHERE name = ?")
    cursor.execute(query, parameters)
    connection.commit()

    # - Verifying all dummy entries are gone
    print("\nAll operations completed successfully, attempting to pull entry once more for manual verification.\n")
    query = (" SELECT * FROM task WHERE name = ?")
    parameters = ("Test Task",)
    cursor.execute(query, parameters)
    print(cursor.fetchone())
    print("\nAll operations completed successfully.\n")
    return

# - Ends the connection between the database and database manager
def close_cnx(cnx, schema_sql):
    # -  Closes schema.sql
    with open("src/schema.sql", "r", encoding="utf-8") as f: 
        schema_sql = f.close()
    cnx.close()
    return cnx, schema_sql

# - Creates an Entry in the DB
def create_entry(task_name, task_time, task_date, task_description=None): 
    if task_name != None and task_time != None and task_date != None:
        cnx, schema_sql = open_cnx()    # - Establishing the connection to the database 
        cur = cnx.cursor() 

        query =  ("INSERT INTO task(name, description, state, target_time, target_date) VALUES(?, ?, ?, ?, ?)")
        parameters = (task_name, task_description, 0, task_time,task_date) 

        cur.execute(query, parameters)
        cnx.commit()

        cnx, schema_sql = close_cnx(cnx, schema_sql)    # - Terminating the connection to the database
        return True 

    else: 
        raise ValueError
    
# - Retrieves an Entry in the DB
def retrieve_entry(task_id):
    if task_id != None: 
        cnx, schema_sql = open_cnx()    # - Establishing the connection to the database 
        cur = cnx.cursor() 

        query = (" SELECT * FROM task WHERE u_id = ?")
        parameters = (task_id,)
        cur.execute(query, parameters)

        result = cur.fetchone()

        cnx, schema_sql = close_cnx(cnx, schema_sql)    # - Terminating the connection to the database 
        return result
    else:
        raise ValueError

# - Updates an Entry in the DB
def update_entry(u_id=None, task_name=None, task_description=None, task_state=None, task_time=None, task_date=None):
    # - Checking if ID is missing
    if  u_id == None:
        raise ValueError

    # - Checking if any attribute was updated 
    elif task_name == None and task_description == None and task_state == None and task_time == None and task_date == None:
        raise ValueError 
    
    # - Paperwork is in order, make the connection
    else:
        cnx, schema_sql = open_cnx()    # - Establishing the connection to the database 
        cur = cnx.cursor() 

        # - Searching for changes
        if task_name != None: 
            query = (" UPDATE task SET name = ? WHERE u_id = ?")
            parameters = (task_name, u_id)
            cur.execute(query, parameters)

        if task_description != None:
            query = (" UPDATE task SET description = ? WHERE u_id = ?")
            parameters = (task_description, u_id)
            cur.execute(query, parameters)

        if task_state != None:
            query = (" UPDATE task SET state = ? WHERE u_id = ?")
            parameters = (task_state, u_id)
            cur.execute(query, parameters)

        if task_time != None:
            query = (" UPDATE task SET target_time = ? WHERE u_id = ?")
            parameters = (task_time, u_id)
            cur.execute(query, parameters)

        if task_date != None:
            query = (" UPDATE task SET target_date = ? WHERE u_id = ?")
            parameters = (task_date, u_id)
            cur.execute(query, parameters)

        # - Save all changes to the database, terminate connection and return to main
        cnx.commit() 
        cnx, schema_sql = close_cnx(cnx, schema_sql)    # - Terminating the connection to the database 
        return True

# - Deletes an Entry in the DB
def delete_entry (task_id):
    if task_id != None:
        cnx, schema_sql = open_cnx()    # - Establishing the connection to the database 
        cur = cnx.cursor() 

        query = (" DELETE FROM task WHERE u_id = ?")
        parameters = (task_id,) 

        cur.execute(query, parameters)
        cnx.commit()    
        cnx, schema_sql = close_cnx(cnx, schema_sql)    # - Terminating the connection to the database 

        return True
    else:
        raise ValueError
    

# - Main
def main():
    #test_cnx(cur, cnx)
    print("Hello!")

  

# - Executes the 'main()' function.
if __name__ == "__main__":
    main()