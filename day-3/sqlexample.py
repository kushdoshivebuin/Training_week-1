import connectdb
import logging

# Logging setup (make sure to configure logging properly in your main script or globally)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

'''Column Constraints :
    1. Not NULL
    2. Unique
    3. Primary Key
    4. Foreign Key
    5. Check
'''

def sqlexample():
    """
    A function that demonstrates SQL operations such as INSERT, UPDATE, DELETE, and SELECT
    with a MySQL database. It interacts with the user to perform CRUD operations on the 'employee' table.
    """

    # Establishing database connection and cursor
    crsr, connection = connectdb.connect()

    # Drop the existing 'employee' table if it exists
    crsr.execute('DROP TABLE IF EXISTS employee')

    try:
        # Reading the DDL (Data Definition Language) commands from the 'DDL.sql' file
        with open('DDL.sql', 'r') as create_file:
            create_command = create_file.read()
            crsr.execute(create_command)
            logging.info("Employee table created successfully.")

        ans = "Y"
        while ans == "Y" or ans == "y":
            # Displaying menu options for the user to choose from
            print("1. Insert")
            print("2. Update")
            print("3. Delete")
            print("4. Select")
            print("5. Exit")
            
            # Taking user input for the choice of operation
            choice = int(input("Enter your choice: "))
            
            # Insert Operation
            if choice == 1:
                insert_command = 'INSERT INTO employee (name, salary, dept_id) VALUES (%(name)s, %(salary)s, %(dept_id)s)'
                user_name = input("Enter the name: ")
                user_salary = int(input("Enter the salary: "))
                user_dept_id = input("Enter the dept id: ")
                values = {'name': user_name, 'salary': user_salary, 'dept_id': user_dept_id}
                
                crsr.execute(insert_command, values)
                logging.info(f"Inserted employee {user_name} with salary {user_salary} and dept_id {user_dept_id}.")
            
            # Update Operation (Salary increment by 50%)
            elif choice == 2:
                update_command = 'UPDATE employee SET salary = salary + (salary * 0.5)'
                crsr.execute(update_command)
                logging.info("Incremented salary by 50% for all employees.")

            # Delete Operation
            elif choice == 3:
                user_id = int(input("Enter the id of the employee you want to delete: "))
                delete_command = 'DELETE FROM employee WHERE id = %s'
                crsr.execute(delete_command, (user_id,))
                logging.info(f"Employee with id {user_id} has been successfully deleted.")

            # Select Operation (Fetch all employee records)
            elif choice == 4:
                select_command = 'SELECT * FROM employee'
                crsr.execute(select_command)
                rows = crsr.fetchall()
                print(rows)

            # Exit the loop
            elif choice == 5:
                break

            # Prompt to continue or exit
            ans = input("Do you want to continue? (Y/N): ")

    except Exception as error:
        # Log any errors that occur during execution
        logging.error(f"An error occurred: {error}")

    finally:
        # Ensure the cursor and connection are properly closed
        if crsr is not None:
            crsr.close()  # Close the cursor
            logging.warning("Cursor closed.")

        if connection is not None:
            connection.commit()  # Commit any changes to the database
            connection.close()  # Close the connection
            logging.warning("Database connection terminated.")

# Execute the SQL example function
sqlexample()
