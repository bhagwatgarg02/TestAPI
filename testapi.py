import yaml
import json
import requests
import pandas as pd

def load_openapi_spec_json(filename):
    with open(filename, 'r') as file:
        openapi_spec = json.load(file)
    return openapi_spec

def load_openapi_spec_yaml(filename):
    with open(filename, 'r') as file:
        openapi_spec = yaml.safe_load(file)
    return openapi_spec

def generate_test_cases(openapi_spec):
    test_cases = []
    for path, methods in openapi_spec['paths'].items():
        for method, details in methods.items():
            summary = details.get('summary', '')
            if method == 'get':
                test_cases.append((f"Test GET {path}: {summary}", path, method, None))
            elif method == 'post':
                #data = input(f"Enter test data for POST request to {path}: ")
                test_cases.append((f"Test POST {path}: {summary}", path, method, None))
            elif method == 'put':
                #data = input(f"Enter test data for PUT request to {path}: ")
                test_cases.append((f"Test PUT {path}: {summary}", path, method, None))
            elif method == 'delete':
                test_cases.append((f"Test DELETE {path}: {summary}", path, method, None))
    return test_cases

def run_test_case(base_url, path, method, data=None):
    url = f"{base_url}{path}"
    if method == 'get':
        response = requests.get(url)
    elif method == 'post':
        response = requests.post(url, json=data)
    elif method == 'put':
        response = requests.put(url, json=data)
    elif method == 'delete':
        response = requests.delete(url)
    return response

def run_test_suite(base_url, test_cases):
    for description, path, method, data in test_cases:
        print(description)
        response = run_test_case(base_url, path, method, data)
        print(f"Response status code: {response.status_code}")
        print(f"Response body: {response.json()}")
        print()

if __name__ == "__main__":
    # Load OpenAPI Specification
    json_file = "./openapi.json"
    yaml_file="./openapi.yaml"
    
    if json_file:
        openapi_spec = load_openapi_spec_json(json_file)

    # Generate test cases
    test_cases = generate_test_cases(openapi_spec)

    # Save test cases to an Excel file
    test_cases_df = pd.DataFrame(test_cases, columns=["Description", "Path", "Method", "Data"])
    test_cases_df.to_excel("test_cases.xlsx", index=False)

    # Run test suite against API endpoints
    base_url = "https://petstore.swagger.io/v2/swagger.json"  # Include scheme (http/https) here
    #run_test_suite(base_url, test_cases)