from eth_utils import to_checksum_address
from web3 import Web3
import argparse
from brownie import Contract, convert, accounts, Create2Deployer, ExampleContract
import time

def main():
    deployer_account = 'wavey' # Just the string
    target_string = '0xc001' # Target address string must be valid hex. Suggest not doing anything more than 6 chars
    bytecode = ExampleContract.bytecode # Byetcode of contract you want to deploy
    



    ### DO NOT MODIFY BELOW THIS LINE ###




    factory = Contract('0x0e55AEF1B392b8491369091ad808E87feaa4AfAB')
    salt, result_address = find_salt(target_string, bytecode, factory.address)
    print(f'Deploying to {result_address} with salt={salt}... ')
    deploy(salt, bytecode, deployer_account, factory)

def deploy(salt, bytecode, deployer_account, factory):
    dev = accounts.load(deployer_account)
    
    bytecode = ExampleContract.bytecode
    tx = factory.deploy(bytecode, salt,{'from': dev})
    address = tx.events['Deployed']['addr']
    print(f'\n\nContract deployed at {address} !!')

def find_salt(target_address, bytecode, address):
    """Test the CREATE2 opcode Python.

    EIP-104
    https://github.com/ethereum/EIPs/blob/master/EIPS/eip-1014.md
    https://ethereum.stackexchange.com/questions/90895/how-to-implement-the-create2-in-python
    """
    address = '0x0e55AEF1B392b8491369091ad808E87feaa4AfAB' # Address of deploy factory. Can use the existing one, or deploy your own using Create2.sol
    pre = '0xff'
    b_pre = bytes.fromhex(pre[2:])
    b_address = bytes.fromhex(address[2:])
    b_init_code = bytes.fromhex(bytecode)
    keccak_b_init_code = Web3.keccak(b_init_code)
    target_address = target_address.lower()
    if target_address[0:2] == '0x':
        target_address = target_address[2:]
    length = len(target_address)
    
    found = False
    i = 0
    start = time.time()

    while not found:
        salt = convert.to_bytes(i, "bytes32")
        b_result = Web3.keccak(b_pre + b_address + salt + keccak_b_init_code)
        result_address = to_checksum_address(b_result[12:].hex())
        print(f'{result_address} {result_address[2:length+2].lower()} salt: {i}')
        if result_address[2:length+2].lower() == target_address:
            found = True
            salt = i
            print(f'Salt found! 🎉🍾🥳🍻 ---> {i}')
        i += 1
    end = time.time()
    print(f'Execution time: {end - start}s')
    return salt, result_address
    