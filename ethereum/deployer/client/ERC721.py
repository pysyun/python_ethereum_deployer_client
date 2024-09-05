import requests
import json

class ERC721:
    
    def __init__(self, ethereum_deployer_uri):
        self.ethereum_deployer_uri = ethereum_deployer_uri

    @staticmethod
    def validate_data(data):
        required_keys = {"network", "name", "address", "to", "id"}
        
        if not isinstance(data, list):
            return False, "Data should be a list"

        for item in data:
            if not isinstance(item, dict):
                return False, "Each item in the list should be a dictionary"
            
            if not required_keys.issubset(item.keys()):
                return False, f"Each item must contain the keys: {required_keys}"
        
        return True, "Validation passed"

    def process(self, data):

        # Validate the data
        valid, message = self.validate_data(data)
        if not valid:
            raise ValueError(f"Invalid data: {message}")

        headers = {
            "Content-Type": "application/json"
        }

        # List data items
        for item in data:

            # Send POST request
            try:
                response = requests.post(self.ethereum_deployer_uri, headers=headers, json=item)
                response.raise_for_status()  # Will raise an HTTPError for bad responses

                if 200 == response.status_code:
                    return json.loads(response.text)

            except requests.exceptions.RequestException as e:
                print(f"An error occurred: {e}")

