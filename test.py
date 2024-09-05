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
