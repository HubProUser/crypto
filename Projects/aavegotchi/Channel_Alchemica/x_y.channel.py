from web3.exceptions import TransactionNotFound
from web3 import Web3
from aavegotchi.Channel_Alchemica.channel_abi import ABI
import requests
import time
from aavegotchi.Channel_Alchemica.distr import DISTRICTS
u = DISTRICTS


def x_y_channel():
    API = 'https://api.polygonscan.com/api?module=account&action=txlist&address=0x1D0360BaC7299C86Ec8E99d0c1C9A95FEfaF2a11&startblock=0&endblock=99999999&page=1&offset=10&sort=desc&apikey=CR9DD3XN6QEJY8MMUQSP7EZBUGRA6Q63MP'

    w3 = Web3(Web3.HTTPProvider('https://polygon-rpc.com'))
    contract = w3.eth.contract(address=w3.toChecksumAddress('0x1D0360BaC7299C86Ec8E99d0c1C9A95FEfaF2a11'), abi=ABI)

    def send(c, m):
        base_url = f'https://api.telegram.org/bot5373652188:AAF46DEh9k56Jaqt6teZCgXEC-S1_cPXLGI/sendMessage?chat_id=-710589490&text=District {a[6]}  {c}\n\n{int(FUD / 10**18)}   FUD\n{int(FOMO / 10**18)}   FOMO\n{int(ALPHA / 10**18)}     ALPHA\n{int(KEK / 10**18)}     KEK\n\n{m}'
        requests.get(base_url)
        time.sleep(30)

    def send1(c, q, m):
        base_url = f'https://api.telegram.org/bot5373652188:AAF46DEh9k56Jaqt6teZCgXEC-S1_cPXLGI/sendMessage?chat_id=-710589490&text=District {a[6]}{q}  {c}\n\n{int(FUD / 10 ** 18)}   FUD\n{int(FOMO / 10 ** 18)}   FOMO\n{int(ALPHA / 10 ** 18)}     ALPHA\n{int(KEK / 10 ** 18)}     KEK\n\n{m}'
        requests.get(base_url)
        time.sleep(30)

    def send_error(a):
        base_url = f'https://api.telegram.org/bot5373652188:AAF46DEh9k56Jaqt6teZCgXEC-S1_cPXLGI/sendMessage?chat_id=-710589490&text={a} occurred.'
        requests.get(base_url)
        time.sleep(10)

    def districts(a, b, c, d, e, f, z):
        if a < x < c and b < y < d:
            if x < e and y < f:
                send(c='↖', m=z)
            elif x > e and y < f:
                send(c='↗', m=z)
            elif x > e and y > f:
                send(c='↘', m=z)
            elif x < e and y > f:
                send(c='↙', m=z)

    def district1(a, b, c, d, e, f, t, z):
        if a < x < c and b < y < d:
            if x < e and y < f:
                send1(c='↖', q=t, m=z)
            elif x > e and y < f:
                send1(c='↗', q=t, m=z)
            elif x > e and y > f:
                send1(c='↘', q=t, m=z)
            elif x < e and y > f:
                send1(c='↙', q=t, m=z)

    while True:
        try:
            url = requests.get(API)
            results = url.json()['result']
            for a in results:
                address = a['input']
                hash = a['hash']
            r = contract.decode_function_input(address)
            transaction = w3.eth.get_transaction_receipt(hash)
            try:
                if r[0].fn_name == 'channelAlchemica':
                    realmId = (r[1]['_realmId'])
                    a = contract.functions.getParcelInfo(realmId).call()

                    x, y = a[3], a[4]

                    logs = transaction['logs']
                    fud_hash = logs[0]['data']
                    FUD = w3.toInt(hexstr=fud_hash)
                    fomo_hash = logs[2]['data']
                    FOMO = w3.toInt(hexstr=fomo_hash)
                    alpha_hash = logs[4]['data']
                    ALPHA = w3.toInt(hexstr=alpha_hash)
                    kek_hash = logs[6]['data']
                    KEK = w3.toInt(hexstr=kek_hash)

                    if FUD / 10**18 >= 30:  # a = start_x    b = start_y   c = end_x   d = end_y   e = mid_x   f = mid_y    z = closest_spawn

                        if (a[6] == 1) and (u['d1a_x_s'] < x < u['d1a_x_e']) and (u['d1a_y_s'] < y < u['d1a_y_e']):
                            district1(a=u['d1a_x_s'], b=u['d1a_y_s'], c=u['d1a_x_e'], d=u['d1a_y_e'], e=u['d1a_x_m'], f=u['d1a_y_m'], t='a', z='↖')
                        elif (a[6] == 1) and (u['d1b_x_s'] < x < u['d1b_x_e']) and (u['d1b_y_s'] < y < u['d1b_y_e']):
                            district1(a=u['d1b_x_s'], b=u['d1b_y_s'], c=u['d1b_x_e'], d=u['d1b_y_e'], e=u['d1b_x_m'], f=u['d1b_y_m'], t='b', z='⬆')
                        elif (a[6] == 1) and (u['d1c_x_s'] < x < u['d1c_x_e']) and (u['d1c_y_s'] < y < u['d1c_y_e']):
                            district1(a=u['d1c_x_s'], b=u['d1c_y_s'], c=u['d1c_x_e'], d=u['d1c_y_e'], e=u['d1c_x_m'], f=u['d1c_y_m'], t='c', z='↗')
                        elif (a[6] == 1) and (u['d1d_x_s'] < x < u['d1d_x_e']) and (u['d1d_y_s'] < y < u['d1d_y_e']):
                            district1(a=u['d1d_x_s'], b=u['d1d_y_s'], c=u['d1d_x_e'], d=u['d1d_y_e'], e=u['d1d_x_m'], f=u['d1d_y_m'], t='d', z='↘')
                        elif (a[6] == 1) and (u['d1e_x_s'] < x < u['d1e_x_e']) and (u['d1e_y_s'] < y < u['d1e_y_e']):
                            district1(a=u['d1e_x_s'], b=u['d1e_y_s'], c=u['d1e_x_e'], d=u['d1e_y_e'], e=u['d1e_x_m'], f=u['d1e_y_m'], t='e', z='⬇')
                        elif (a[6] == 1) and (u['d1f_x_s'] < x < u['d1f_x_e']) and (u['d1f_y_s'] < y < u['d1f_y_e']):
                            district1(a=u['d1f_x_s'], b=u['d1f_y_s'], c=u['d1f_x_e'], d=u['d1f_y_e'], e=u['d1f_x_m'], f=u['d1f_y_m'], t='f', z='↙')

                        elif a[6] == 2:
                            districts(a=u['d2_x_s'], b=u['d2_y_s'], c=u['d2_x_e'], d=u['d2_y_e'], e=u['d2_x_m'], f=u['d2_y_m'], z='↙')
                        elif a[6] == 3:
                            districts(a=u['d3_x_s'], b=u['d3_y_s'], c=u['d3_x_e'], d=u['d3_y_e'], e=u['d3_x_m'], f=u['d3_y_m'], z='↖')
                        elif a[6] == 4:
                            districts(a=u['d4_x_s'], b=u['d4_y_s'], c=u['d4_x_e'], d=u['d4_y_e'], e=u['d4_x_m'], f=u['d4_y_m'], z='↖')
                        elif a[6] == 5:
                            districts(a=u['d5_x_s'], b=u['d5_y_s'], c=u['d5_x_e'], d=u['d5_y_e'], e=u['d5_x_m'], f=u['d5_y_m'], z='↖')
                        elif a[6] == 6:
                            districts(a=u['d6_x_s'], b=u['d6_y_s'], c=u['d6_x_e'], d=u['d6_y_e'], e=u['d6_x_m'], f=u['d6_y_m'], z='⬆')
                        elif a[6] == 7:
                            districts(a=u['d7_x_s'], b=u['d7_y_s'], c=u['d7_x_e'], d=u['d7_y_e'], e=u['d7_x_m'], f=u['d7_y_m'], z='↗')
                        elif a[6] == 8:
                            districts(a=u['d8_x_s'], b=u['d8_y_s'], c=u['d8_x_e'], d=u['d8_y_e'], e=u['d8_x_m'], f=u['d8_y_m'], z='↗')
                        elif a[6] == 9:
                            districts(a=u['d9_x_s'], b=u['d9_y_s'], c=u['d9_x_e'], d=u['d9_y_e'], e=u['d9_x_m'], f=u['d9_y_m'], z='↗')
                        elif a[6] == 10:
                            districts(a=u['d10_x_s'], b=u['d10_y_s'], c=u['d10_x_e'], d=u['d10_y_e'], e=u['d10_x_m'], f=u['d10_y_m'], z='↘')
                        elif a[6] == 11:
                            districts(a=u['d11_x_s'], b=u['d11_y_s'], c=u['d11_x_e'], d=u['d11_y_e'], e=u['d11_x_m'], f=u['d11_y_m'], z='↘')
                        elif a[6] == 12:
                            districts(a=u['d12_x_s'], b=u['d12_y_s'], c=u['d12_x_e'], d=u['d12_y_e'], e=u['d12_x_m'], f=u['d12_y_m'], z='↘')
                        elif a[6] == 13:
                            districts(a=u['d13_x_s'], b=u['d13_y_s'], c=u['d13_x_e'], d=u['d13_y_e'], e=u['d13_x_m'], f=u['d13_y_m'], z='⬇')
                        elif a[6] == 14:
                            districts(a=u['d14_x_s'], b=u['d14_y_s'], c=u['d14_x_e'], d=u['d14_y_e'], e=u['d14_x_m'], f=u['d14_y_m'], z='↙')
                        elif a[6] == 15:
                            districts(a=u['d15_x_s'], b=u['d15_y_s'], c=u['d15_x_e'], d=u['d15_y_e'], e=u['d15_x_m'], f=u['d15_y_m'], z='↙')
                        elif a[6] == 41:
                            base_url = f'https://api.telegram.org/bot5373652188:AAF46DEh9k56Jaqt6teZCgXEC-S1_cPXLGI/sendMessage?chat_id=-710589490&text=Alchemica channeled in district 41'
                            requests.get(base_url)
                            time.sleep(10)

            except IndexError:
                send_error(a='IndexError')
        except requests.exceptions.JSONDecodeError:
            send_error(a='requests.exceptions.JSONDecodeError')
        except TransactionNotFound:
            send_error(a='web3.exceptions.TransactionNotFound')


x_y_channel()
