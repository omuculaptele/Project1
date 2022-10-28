from sys import exit
from bitcoin.core.script import *
from bitcoin.wallet import CBitcoinSecret

from lib.utils import *
from lib.config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)
from Q1 import send_from_P2PKH_transaction


cust1_private_key = CBitcoinSecret(
    'cN6zv2X8TLUPbTBjQcHLHqVexq1w3cgDybrNPk5CjFkJyUk7aCxG')
cust1_public_key = cust1_private_key.pub
cust2_private_key = CBitcoinSecret(
    'cPFeAEETtpjJD5cNRSPBp1ACUDxSo8eykY2CZ5GFUR5c3nNrtEvD')
cust2_public_key = cust2_private_key.pub
cust3_private_key = CBitcoinSecret(
    'cU332HqftWGsBKVzauhpGDwDNuELsQyQFNi6g7sagrqMj1mLwXS5')
cust3_public_key = cust3_private_key.pub


######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 3

# You can assume the role of the bank for the purposes of this problem
# and use my_public_key and my_private_key
# in lieu of bank_public_key and bank_private_key.

Q3a_txout_scriptPubKey = [OP_2, my_public_key, cust1_public_key, cust2_public_key, cust3_public_key, OP_4, OP_CHECKMULTISIG]
######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.001899342-0.00003 # amount of BTC in the output you're sending minus fee
    txid_to_spend = (
        '6c063aea1824bb760b1626e82768dc01c5aa423378e3a788fe86e6550bc0f213')
    utxo_index = 0 # index of the output you are spending, indices start at 0
    ######################################################################

    response = send_from_P2PKH_transaction(amount_to_send, txid_to_spend, 
        utxo_index, Q3a_txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)
