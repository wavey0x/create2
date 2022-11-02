# Brownie CREATE2 deployer

In `find_address.py` update the following fields at the top of the script.
- deployer account
- bytecode
- target_address

Run the script using `brownie run find_salt.py`

Try it in mainnet-fork for testing first.

*Note: Right now, this does not work on contracts that accept constructor args*