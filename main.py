import os
import json
import time
import random
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

RPC = os.getenv("RPC_URL")
MTN = Web3.to_checksum_address(os.getenv("MTN_TOKEN"))
WETH = Web3.to_checksum_address(os.getenv("WETH_TOKEN"))
POOL = Web3.to_checksum_address(os.getenv("POOL_ADDRESS"))
PRIVATE_KEYS = json.loads(os.getenv("PRIVATE_KEYS"))

web3 = Web3(Web3.HTTPProvider(RPC))

BUY_AMOUNTS = [0.01, 0.012, 0.015, 0.018, 0.02]
SELL_AMOUNT = Web3.to_wei(0.1, "ether")

def simulate_wallet(pk, amount_eth):
    acct = web3.eth.account.from_key(pk)
    address = acct.address
    print(f"Buying MTN with {amount_eth} WETH from {address}")
    # Here should be the swap code using Uniswap Router v2
    time.sleep(random.randint(30, 120))

    print(f"Selling 0.1 MTN from {address}")
    # Here should be the MTN sell code
    time.sleep(random.randint(30, 90))

def main():
    for pk, eth in zip(PRIVATE_KEYS, BUY_AMOUNTS):
        simulate_wallet(pk, Web3.to_wei(eth, "ether"))

if __name__ == "__main__":
    main()
