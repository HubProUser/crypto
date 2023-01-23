from web3 import Web3
from aavegotchi.get_gochi.abi import ABI
import time
import requests


def get_aave():
    while True:
        w3 = Web3(Web3.HTTPProvider('https://polygon-rpc.com'))  # get poligon
        cnt = w3.eth.contract(address=w3.toChecksumAddress('*********'), abi=ABI)
        acct = w3.eth.account.privateKeyToAccount('*********')
        gchs = cnt.functions.getGotchiLendings(b'listed', 200).call()
        aave = [a for a in gchs if ((a[0] == '*********') and (a[5] != 0) and (a[1] == 0))]

        if len(aave) > 0:
            c_trans = cnt.functions.agreeGotchiLending(aave[0][3], aave[0][4], aave[0][1], aave[0][-2], aave[0][-4]).buildTransaction({'from': acct.address, 'maxFeePerGas': int(w3.eth.gasPrice * 1.1),'nonce': w3.eth.getTransactionCount(acct.address), 'gas': 500000})  # create transaction
            s_trans = w3.eth.account.signTransaction(c_trans, acct)
            a = w3.eth.sendRawTransaction(s_trans.rawTransaction)
            base_url = f'https://api.telegram.org/bot5373652188:AAF46DEh9k56Jaqt6teZCgXEC-S1_cPXLGI/sendMessage?chat_id=-710589490&text=Gochi borrowed for{aave[0][-2] / 60 ** 2} hour(s)'
            requests.get(base_url)
            break


get_aave()
