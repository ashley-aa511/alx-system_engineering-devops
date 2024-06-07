#!/usr/bin/python3

import requests
import sys

def get_employee_todo_progress(employee_id):
    # Base URLs for the JSONPlaceholder API
    users_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todos_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    
    # Fetch the user information
    user_response = requests.get(users_url)
    if user_response.status_code != 200:
        print(f'Error: Unable to fetch user with ID {employee_id}')
        return

    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Fetch the TODOs for the user
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print(f'Error: Unable to fetch todos for user with ID {employee_id}')
        return

    todos = todos_response.json()

    # Calculate the number of completed tasks and total tasks
    completed_tasks = [todo for todo in todos if todo['completed']]
    total_tasks = len(todos)
    number_of_done_tasks = len(completed_tasks)

    # Print the progress information
    print(f'Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):')
    for task in completed_tasks:
        print(f'\t {task["title"]}')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)
    
    get_employee_todo_progress(employee_id)
