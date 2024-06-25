import yaml
import json
import requests

def generate_openapi_yaml(api_url, output_file):
    response = requests.get(f"{api_url}/swagger.json")  # Adjust endpoint to fetch OpenAPI spec
    api_data = response.json()

    with open(output_file, 'w') as file:
        yaml.dump(api_data, file)

def generate_openapi_json(api_url, output_file):
    response = requests.get(f"{api_url}/swagger.json")  # Adjust endpoint to fetch OpenAPI spec
    api_data = response.json()

    with open(output_file, 'w') as file:
        json.dump(api_data, file, indent=4)

if __name__ == "__main__":
    api_url = "http://petstore.swagger.io/v2"  # Replace with your API base URL
    yaml_output_file = "openapi.yaml"
    json_output_file = "openapi.json"

    generate_openapi_yaml(api_url, yaml_output_file)
    generate_openapi_json(api_url, json_output_file)
