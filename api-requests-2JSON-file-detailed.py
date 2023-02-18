#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 16:45:23 2023

@author: marco.herry
"""

import json #importing json library to use json functionalities
from flask import Flask, request, jsonify #importing flask, request, jsonify to create api, handle request and jsonify the response

# Initialize the Flask app
app = Flask(__name__)

# Load employee data from a JSON file, this line will open a json file named 'employees.json' and loads the data into the variable employees
with open('employees.json') as f:
    employees = json.load(f)

# Define the endpoint '/employee' that will handle HTTP requests, this line will create an endpoint '/employee' which will handle the requests
@app.route('/employee', methods=['POST', 'PUT', 'GET', 'DELETE'])
def employee():
    if request.method == 'POST':
        # Handle a POST request to update an existing employee in the JSON file
        # this line will get the request data in json format
        data = request.get_json()
        # this loop will iterate through all the employees in the json file
        for i, employee in enumerate(employees):
            # this if block will check if the id of the employee matches with the id of the employee in the request data
            if employee['employee_id'] == data['employee_id']:
                # this block of code will update the values of the employee with the values sent in the request
                employees[i]['name'] = data['name']
                employees[i]['department'] = data['department']
                employees[i]['email'] = data['email']
                employees[i]['number'] = data['number']
                # this block of code will open the json file and updates it with the new values
                with open('employees.json', 'w') as f:
                    json.dump(employees, f)
                # this line will return the success message after updating the employee
                return jsonify({'message': 'Employee updated successfully'})
        # this line will return if the employee with the given id is not found
        return jsonify({'message': 'Employee not found'}), 404
    elif request.method == 'PUT':
        # Handle a PUT request to add a new employee to the JSON file
        # this line will get the request data in json format
        data = request.get_json()
        # this line will append the new employee data to the existing json file
        employees.append(data)
        # this block of code will open the json file and updates it with the new values
        with open('employees.json', 'w') as f:
            json.dump(employees, f)
        # this line will return the success message after adding the employee
        return jsonify({'message': 'Employee added successfully'})
    elif request.method == 'GET':
        # Handle a GET request to retrieve employees from the JSON file
        if 'employee_id' in request.args:
            # Retrieve a specific employee by employee_id
            # this loop will iterate through all the employees in the json file
            for employee in employees:
                # this if block will check if the id of the employee matches with the ID
                if employee['employee_id'] == int(request.args['employee_id']):
                    return jsonify(employee)
            return jsonify({'message': 'Employee not found'}), 404
        else:
            # Retrieve all employees
            return jsonify(employees)
    elif request.method == 'DELETE':
        # Handle a DELETE request to delete an employee from the JSON file
        data = request.get_json()
        for i, employee in enumerate(employees):
            if employee['employee_id'] == data['employee_id']:
                del employees[i]
                with open('employees.json', 'w') as f:
                    json.dump(employees, f)
                return jsonify({'message': 'Employee deleted successfully'})
        return jsonify({'message': 'Employee not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)