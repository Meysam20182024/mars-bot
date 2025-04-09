UNISWAP_ROUTER_ABI = [{'inputs': [{'internalType': 'uint256', 'name': 'amountOutMin', 'type': 'uint256'}, {'internalType': 'address[]', 'name': 'path', 'type': 'address[]'}, {'internalType': 'address', 'name': 'to', 'type': 'address'}, {'internalType': 'uint256', 'name': 'deadline', 'type': 'uint256'}], 'name': 'swapExactETHForTokensSupportingFeeOnTransferTokens', 'outputs': [], 'stateMutability': 'payable', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': 'amountIn', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'amountOutMin', 'type': 'uint256'}, {'internalType': 'address[]', 'name': 'path', 'type': 'address[]'}, {'internalType': 'address', 'name': 'to', 'type': 'address'}, {'internalType': 'uint256', 'name': 'deadline', 'type': 'uint256'}], 'name': 'swapExactTokensForETHSupportingFeeOnTransferTokens', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}]

ERC20_ABI = [{'constant': True, 'inputs': [{'name': 'owner', 'type': 'address'}], 'name': 'balanceOf', 'outputs': [{'name': '', 'type': 'uint256'}], 'type': 'function'}, {'constant': False, 'inputs': [{'name': 'spender', 'type': 'address'}, {'name': 'value', 'type': 'uint256'}], 'name': 'approve', 'outputs': [{'name': '', 'type': 'bool'}], 'type': 'function'}]