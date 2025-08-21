import requests
def convert(amount,from_currency,to_currency):
    try:
        url=f"https://v6.exchangerate-api.com/v6/ecd7b31b82069a325a686bc8/latest/{from_currency}"
        response=requests.get(url)
        if response.status_code==200:
            data=response.json()
            rates=data["conversion_rates"]
            if to_currency in rates:
                rate=rates[to_currency]
                converted=amount*rate
                return converted
            else:
                return f"currency{to_currency}not supported"
        else:
            return"not fetched"
    except Exception as e:
        print(e)
        
amount=float(input("enter the amount:"))
from_currency=input("enter the currency:").upper()
to_currency=input("enter the currency:").upper()
result=convert(amount,from_currency,to_currency)
print(f"{amount}{from_currency} - {result} {to_currency}")     
    

        