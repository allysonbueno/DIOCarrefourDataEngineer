import phonenumbers
from phonenumbers import geocoder

phone = input('Digite o telefone (formato +554433445566: ' )

phone_number = phonenumbers.parse(phone)

print(geocoder.description_for_number(phone_number, 'pt'))