import pyupbit


access = "LsFYm0DmBXayU3UToP6etExeodeRwkElJxfBFOWI"          # 본인 값으로 변경
secret = "JH3Lvbb0gvZxz6ZUPx4i64TyI2Hi39jIXMURkYwI"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회
