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

    # Example process call with some data
    erc721.process("Example data")

if __name__ == "__main__":
    main()
