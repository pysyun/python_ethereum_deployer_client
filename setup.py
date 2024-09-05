from setuptools import setup

setup(
    name='python_ethereum_deployer_client',
    version='0.1',
    description='Syun\'s Python SDK for Ethereum deployment.',
    author='Py Syun',
    author_email='pysyun@vitche.com',
    py_modules=['ethereum.deployer.client.ERC721',],
    install_requires=['requests']
)
