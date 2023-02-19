# api-requests-2JSON-file

A Flask API for CRUD Operations on Employee Data

# Description:
This Python code implements a Flask-based API that allows the creation, retrieval, update, and deletion of employee data. The employee data is stored in a JSON file, and the API exposes four endpoints to handle HTTP requests.

# Dependencies:
This code requires the following dependencies:

Python 3
Flask
json

# Usage:
To run the code, execute the following command in the terminal:
python app.py

# Summary

This is a Python script that creates a web application for handling employee data. It uses the Flask library to create an API that can handle HTTP requests for adding, updating, retrieving, and deleting employee data.

The script reads employee data from a JSON file, and creates an endpoint '/employee' that handles requests for performing operations on the employee data. The endpoint can handle HTTP methods such as POST, PUT, GET, and DELETE.

When a request is made to the endpoint with a specific HTTP method, the corresponding block of code is executed. For example, if a POST request is made to the endpoint, the script will update an existing employee's data if the employee with the specified ID exists, or return an error message if the employee does not exist.

Similarly, if a GET request is made to the endpoint, the script retrieves all employee data or a specific employee's data based on the request arguments.

In summary, the Python script creates a web application that provides an API to manage employee data. The endpoint '/employee' can handle HTTP requests for performing operations such as adding, updating, retrieving, and deleting employee data from a JSON file.
