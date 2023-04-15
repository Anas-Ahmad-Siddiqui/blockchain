# Import the Web3 library
from web3 import Web3

# Set the Infura URL and the test address
infra_url = "https://mainnet.infura.io/v3/76429c6507214cbeb6e1f2f8b9419bac"
test_address = "0xC8f9f30653B74087313d5bd5178B50bC5BFA29E5"

# Create a Web3 instance with the Infura URL
web3 = Web3(Web3.HTTPProvider(infra_url))

# Check if the Web3 instance is connected to the network
print("isConnected: ", web3.is_connected())

# Get the balance of the test address and convert it to Ether
balance = web3.eth.get_balance(test_address)
print("Balance: ", web3.from_wei(balance, "ether"))

# Get the latest block
latest_block = web3.eth.get_block("latest")
print("latest block: ", latest_block)

# Set the contract address and ABI
contract_address = '0xd665ce6Ef8AdA72B1CF946A6a71508bDD6D2EE04'

abi = '[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"_maxTxAmount","type":"uint256"}],"name":"MaxTxAmountUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"address","name":"notbot","type":"address"}],"name":"delBot","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"manualsend","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"manualswap","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"pure","type":"function"},{"inputs":[],"name":"openTrading","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"removeStrictTxLimit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address[]","name":"bots_","type":"address[]"}],"name":"setBots","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bool","name":"onoff","type":"bool"}],"name":"setCooldownEnabled","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"pure","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"stateMutability":"payable","type":"receive"}]'

# Create an instance of the contract by passing its address and ABI
contract_instance = web3.eth.contract(address=contract_address, abi=abi)

# Print the contract instance
print("contract instance: ", contract_instance)


# Call the totalSupply() function of the contract and store the result in the 'res' variable
res = contract_instance.functions.totalSupply().call()

# Print the value of 'res'
print("res: ", res)

# Call the symbol() function of the contract and store the result in the 'symbol' variable
symbol = contract_instance.functions.symbol().call()

# Print the value of 'symbol'
print("symbol: ", symbol)