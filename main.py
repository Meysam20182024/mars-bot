# main.py — основной бот MarsBot
# Приватные ключи, адреса кошельков и параметры вшиты прямо в код

from web3 import Web3
import time, random
from abi import token_abi, router_abi

RPC = "https://mainnet.base.org"
MTN = "0x9248f99e91f405ddd30821d9b7fa55b64f3fa993"
WETH = "0x4200000000000000000000000000000000000006"
ROUTER = "0xE592427A0AEce92De3Edee1F18E0157C05861564"  # Uniswap v2 Router
POOL = "0x60da00747a244277026f3e673933ca0254d0ae41"

wallets = [
    {"name": "Mars1", "address": "0x897a7c000e296F221c65d754A4Be9a0b691eBbAA", "key": "f080903b2682a987ead8b31c213ceac668681bf4073019046a42deae2efb8ef5", "amount": 0.01},
    {"name": "Mars2", "address": "0x6155BaF182D2997a26325Dc5078E88450a8Dc163", "key": "d87c02f021fb9036438d9dbd42de286a76df707de49dac59947ae53feb028111", "amount": 0.012},
    {"name": "Mars3", "address": "0xeFb5685465518f4Fcd16B6A664eea0776b64954d", "key": "27c77b7c6a50ff7cec2c0f95a2e0c055c036cb18017ec72e884b2d9ec515584c", "amount": 0.015},
    {"name": "Mars4", "address": "0x599D2F809b34cc8c462607B76Ead3b26a80381e1", "key": "5b892f476132213965273a7dcda11b3ab4d6fc4a46ef8ff41bba752f31852e3b", "amount": 0.018},
    {"name": "Mars5", "address": "0xC2F95D928a63e0d78C19Ee73Df0Cd24203Af4B52", "key": "50892f476132213965273a7dcda11b3ab4d6fc4a46ef8ff41bba752f31852e3b", "amount": 0.02},
]

# Заглушка: здесь будет вся логика покупки/продажи
print("MarsBot загружен и готов к запуску.")

# Логика 50 покупок и 1 продажи в цикле для каждого кошелька реализуется позже.
