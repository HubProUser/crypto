from web3 import Web3
from Projects.aavegotchi.get_gochi.abi import ABI
import time
import requests


def get_aave():

    def transaction():
        c_trans = cnt.functions.agreeGotchiLending(free_g[0][3], free_g[0][4], free_g[0][1], free_g[0][-2], free_g[0][-4]).buildTransaction({'from': acct.address, 'maxFeePerGas': int(w3.eth.gasPrice * 1.1), 'nonce': w3.eth.getTransactionCount(acct.address), 'gas': 500000})  # create transaction
        s_trans = w3.eth.account.signTransaction(c_trans, acct)  # using my private key sign my transaction
        a = w3.eth.sendRawTransaction(s_trans.rawTransaction)  # send transaction to server

        base_url = f'https://api.telegram.org/bot5373652188:AAF46DEh9k56Jaqt6teZCgXEC-S1_cPXLGI/sendMessage?chat_id=-710589490&text=Gochi borrowed for{free_g[0][-2] / 60 ** 2} hour(s)'
        requests.get(base_url)
        print('get_gochi')
        time.sleep(30)

    while True:
        w3 = Web3(Web3.HTTPProvider('https://polygon-rpc.com'))  # get poligon
        cnt = w3.eth.contract(address=w3.toChecksumAddress('*********'), abi=ABI)  # get contract info

        acct = w3.eth.account.privateKeyToAccount('**********')  # get my private key

        gchs = cnt.functions.getGotchiLendings(b'listed', 200).call()  # get list of 1000 last-listed gochies
        free_g = [a for a in gchs if ((a[1] <= 0.1) and (a[-4][1] >= 75) and (a[5] == 0))]  # search for gochi

        if len(free_g) > 0:
            transaction()
        else:
            time.sleep(2)


get_aave()
