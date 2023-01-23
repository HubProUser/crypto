from web3 import Web3
from aavegotchi.get_gochi.abi import ABI
import time
import requests


#  pickle.dump({}, open('pic.txt', 'wb'))


def get_aave():

    def transaction():
        c_trans = cnt.functions.agreeGotchiLending(free_g[0][3], free_g[0][4], free_g[0][1], free_g[0][-2], free_g[0][-4]).buildTransaction({'from': acct.address, 'maxFeePerGas': int(w3.eth.gasPrice * 1.1), 'nonce': w3.eth.getTransactionCount(acct.address), 'gas': 500000})  # create transaction
        s_trans = acct.signTransaction(c_trans)  # using my private key sign my transaction
        a = w3.eth.sendRawTransaction(s_trans.rawTransaction)  # send transaction to server
        base_url = f'https://api.telegram.org/bot5373652188:AAF46DEh9k56Jaqt6teZCgXEC-S1_cPXLGI/sendMessage?chat_id=-710589490&text="Gochi borrowed for{free_g[0][-2] / 60 ** 2} hour(s), id: {free_g[0][4]}"'
        requests.get(base_url)
        print('get_gochi')
        time.sleep(30)

    while True:
        w3 = Web3(Web3.HTTPProvider('https://polygon-rpc.com'))  # get poligon
        cnt = w3.eth.contract(address=w3.toChecksumAddress('0x86935F11C86623deC8a25696E1C19a8659CbF95d'), abi=ABI)  # get contract info

        acct = w3.eth.account.privateKeyToAccount('569f4348c7450af4fa4a4763b1bb8de434348c3fca7b0b55ae8d446893b05c5e')  # get my private key

        gchs = cnt.functions.getGotchiLendings(b'listed', 1000).call()  # get list of 300 last-listed gochies
        free_g = [a for a in gchs if ((a[1] == 0) and (a[-4][1] >= 70) and (a[5] == 0))]  # search for gochi

        if len(free_g) > 0:
            transaction()
            break

        else:
            time.sleep(2)


get_aave()
