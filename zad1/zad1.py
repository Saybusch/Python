akcjeJanka1 = 2000.0
cenaAkcjeJanka1 = 40.0
prowizja = 0.03
cenaAkcjeJanka2 = 42.75
print(f"Janek zaplacil za akcje: {akcjeJanka1*cenaAkcjeJanka1:.2f} zl")
print(f"W momencie kupna akcji Janek zaplacil brokerowi: {akcjeJanka1*cenaAkcjeJanka1*prowizja:.2f} zl")
print(f"Janek sprzedal akcje za: {akcjeJanka1*cenaAkcjeJanka2:.2f} zl")
print(f"W momencie sprzedazy Janek zaplacil brokerowi: {akcjeJanka1*cenaAkcjeJanka2*prowizja:.2f} zl")
total = akcjeJanka1*cenaAkcjeJanka2 - akcjeJanka1*cenaAkcjeJanka2*prowizja - akcjeJanka1*cenaAkcjeJanka1 - akcjeJanka1*cenaAkcjeJanka1*prowizja
if total < 0.0:
    print(f"Janek stracil: {total:.2f} zl")
else:
    print(f"Janek zyskal: {total:.2f} zl")