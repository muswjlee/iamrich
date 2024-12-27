import mojito
import pprint

f = open("./mocke.key")
lines = f.readlines()
key = lines[0].strip()
secret = lines[1].strip()
acc_no = lines[2].strip()
f.close()

broker = mojito.KoreaInvestment(
    api_key=key,
    api_secret=secret,
    acc_no=acc_no,
    mock=True
)


resp = broker.fetch_balance()
for comp in resp['output1']:
    print(comp['pdno'])
    print(comp['prdt_name'])
    print(comp['hldg_qty'])
    print(comp['pchs_amt'])
    print(comp['evlu_amt'])
    print("-" * 40)