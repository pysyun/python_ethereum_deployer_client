# Python Ethereum Deployer Client

## Overview
`python_ethereum_deployer_client` is a Python SDK for Ethereum deployment. It provides a simplified interface for deploying ERC721 tokens to an Ethereum-like blockchain network. 

## Installation
You can install the dependencies required for this library by running:
```sh
pip install -r requirements.txt
```

## Project Structure
```
python_ethereum_deployer_client/
├── ethereum/
│   └── deployer/
│       └── client/
│           └── ERC721.py
├── git-config.sh
├── requirements.txt
├── setup.py
├── test.py
└── README.md
```

## Setup
1. Clone the repository:
    ```sh
    git clone git@github.com:pysyun/python_ethereum_deployer_client.git
    cd python_ethereum_deployer_client
    ```

2. Run the `setup.py`:
    ```sh
    python setup.py install
    ```

3. Configure the git settings:
    ```sh
    sh git-config.sh
    ```

4. Set up environment variables:
    - Create a `.env` file in the root directory and set the `ETHEREUM_DEPLOYER_URI` variable:
        ```
        ETHEREUM_DEPLOYER_URI=<your_ethereum_deployer_service_url>
        ```

## Usage
The `ERC721` class in the SDK allows you to process ERC721 token deployment. Below is an example of how to use this library.

### Example
#### 1. Importing and Initialization
Ensure you've set the environment variable `ETHEREUM_DEPLOYER_URI` as shown in the setup.

#### 2. Sample Script (`test.py`)
```python
import os
from dotenv import load_dotenv
from ethereum.deployer.client.ERC721 import ERC721

# Load environment variables from .env file
load_dotenv()

def main():
    ethereum_deployer_uri = os.getenv('ETHEREUM_DEPLOYER_URI')
    
    if ethereum_deployer_uri is None:
        raise EnvironmentError("ETHEREUM_DEPLOYER_URI is not set in the environment variables")

    # Initialize the ERC721 object with the loaded URI
    erc721 = ERC721(ethereum_deployer_uri)

    # Example data to be processed
    data = [{
        "network": "hamsterpunks_holesky",
        "name": "HamsterPunks",
        "address": "0xC2D3be7aAd17E853153ED10a0064e20112939bEB",
        "to": "0xee570fE3C36A3bBf6bdf4376e03959f949612105",
        "id": "QmWgQnjwJCjMX4gEwTfAwyUwnLxWeMMyWteJXJyp95vR1g" 
    }]

    # Pass the example data as an argument
    transaction = erc721.process(data)
    print(transaction)

if __name__ == "__main__":
    main()
```

### Explanation
1. **Import Libraries:** The script imports the necessary libraries including `os`, `dotenv`, and the custom `ERC721` class.
2. **Load Environment Variables:** It uses `dotenv` to load the environment variables from a `.env` file.
3. **Initialize ERC721 Object:** It initializes an `ERC721` object using the URI loaded from the environment variable.
4. **Prepare Data:** The data to be sent for deployment is prepared and must include `network`, `name`, `address`, `to`, and `id`.
5. **Process Data:** The `process` method of the `ERC721` object is called with the prepared data to deploy the token.

## Additional Information
### Validation
The `validate_data` method ensures that the provided data is a list of dictionaries and that each dictionary contains the required keys: `network`, `name`, `address`, `to`, and `id`.

### Error Handling
- The `validate_data` method raises a `ValueError` if the data is invalid.
- The `process` method handles exceptions related to network requests and prints appropriate error messages.

### Dependencies
The project relies on the following dependencies:
- `setuptools`
- `requests`
- `python-dotenv`

These can be installed via `pip` using the `requirements.txt` file.

Feel free to dive into the code in the `ethereum/deployer/client/` directory for more details and to extend the functionality as per your needs.