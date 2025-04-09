import os
import json
import time
import random
import logging
from web3 import Web3
from dotenv import load_dotenv

# Загрузка переменных из .env
load_dotenv()

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("mars_bot.log"),
        logging.StreamHandler()
    ]
)

# Инициализация Web3
w3 = Web3(Web3.HTTPProvider(os.getenv("RPC_URL")))
if not w3.is_connected():
    raise Exception("Не удалось подключиться к RPC")

# Переменные из .env
PRIVATE_KEYS = json.loads(os.getenv("PRIVATE_KEYS"))
MTN = Web3.to_checksum_address(os.getenv("MTN_TOKEN"))
WETH = Web3.to_checksum_address(os.getenv("WETH_TOKEN"))
ROUTER = Web3.to_checksum_address(os.getenv("UNISWAP_ROUTER"))

# Покупки по разным суммам
BUY_AMOUNTS = [0.01, 0.012, 0.015, 0.018, 0.02]
SELL_AMOUNT = w3.to_wei(0.1, "ether")

# ABI
UNISWAP_ROUTER_ABI = [
    {
        "name": "swapExactETHForTokens",
        "type": "function",
        "stateMutability": "payable",
        "inputs": [
            {"name": "amountOutMin", "type": "uint256"},
            {"name": "path", "type": "address[]"},
            {"name": "to", "type": "address"},
            {"name": "deadline", "type": "uint256"},
        ],
        "outputs": [
            {"name": "amounts", "type": "uint256[]"}
        ]
    },
    {
        "name": "swapExactTokensForETH",
        "type": "function",
        "stateMutability": "nonpayable",
        "inputs": [
            {"name": "amountIn", "type": "uint256"},
            {"name": "amountOutMin", "type": "uint256"},
            {"name": "path", "type": "address[]"},
            {"name": "to", "type": "address"},
            {"name": "deadline", "type": "uint256"},
        ],
        "outputs": [
            {"name": "amounts", "type": "uint256[]"}
        ]
    }
]

ERC20_ABI = [
    {
        "constant": False,
        "inputs": [
            {"name": "_spender", "type": "address"},
            {"name": "_value", "type": "uint256"}
        ],
        "name": "approve",
        "outputs": [{"name": "", "type": "bool"}],
        "type": "function"
    }
]

# Функция approve
def approve_token(acct, token, spender, amount):
    contract = w3.eth.contract(address=token, abi=ERC20_ABI)
    nonce = w3.eth.get_transaction_count(acct.address)
    tx = contract.functions.approve(spender, amount).build_transaction({
        "from": acct.address,
        "nonce": nonce,
        "gas": 100000,
        "gasPrice": w3.eth.gas_price
    })
    signed_tx = acct.sign_transaction(tx)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    w3.eth.wait_for_transaction_receipt(tx_hash)
    logging.info(f"[APPROVED] {acct.address} → {spender}")
    return tx_hash.hex()

# Покупка MTN за ETH
def buy_token(acct, eth_amount):
    router = w3.eth.contract(address=ROUTER, abi=UNISWAP_ROUTER_ABI)
    deadline = int(time.time()) + 600
    path = [WETH, MTN]
    tx = router.functions.swapExactETHForTokens(
        0, path, acct.address, deadline
    ).build_transaction({
        "from": acct.address,
        "value": w3.to_wei(eth_amount, "ether"),
        "gas": 300000,
        "gasPrice": w3.eth.gas_price,
        "nonce": w3.eth.get_transaction_count(acct.address)
    })
    signed_tx = acct.sign_transaction(tx)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    logging.info(f"[BUY] {acct.address} купил MTN на {eth_amount} ETH — TX: {tx_hash.hex()}")
    return receipt

# Продажа MTN за ETH
def sell_token(acct, mtn_amount):
    approve_token(acct, MTN, ROUTER, mtn_amount)
    router = w3.eth.contract(address=ROUTER, abi=UNISWAP_ROUTER_ABI)
    deadline = int(time.time()) + 600
    path = [MTN, WETH]
    tx = router.functions.swapExactTokensForETH(
        mtn_amount, 0, path, acct.address, deadline
    ).build_transaction({
        "from": acct.address,
        "gas": 300000,
        "gasPrice": w3.eth.gas_price,
        "nonce": w3.eth.get_transaction_count(acct.address)
    })
    signed_tx = acct.sign_transaction(tx)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    logging.info(f"[SELL] {acct.address} продал {w3.from_wei(mtn_amount, 'ether')} MTN — TX: {tx_hash.hex()}")
    return receipt

# Основной цикл
def run():
    for i, pk in enumerate(PRIVATE_KEYS):
        acct = w3.eth.account.from_key(pk)
        amount = BUY_AMOUNTS[i]
        logging.info(f"--- Mars{i+1} {acct.address} ---")
        buy_token(acct, amount)
        delay = random.randint(10, 30)
        logging.info(f"[WAIT] {delay} сек...")
        time.sleep(delay)

    # Продажа 0.1 MTN с последнего кошелька
    acct = w3.eth.account.from_key(PRIVATE_KEYS[-1])
    sell_token(acct, SELL_AMOUNT)

if __name__ == "__main__":
    run()
