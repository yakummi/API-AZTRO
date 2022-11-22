from pyaztro import Aztro

horosope = Aztro('Gemini', day='tomorrow')
horosope1 = Aztro('Leo', day='tomorrow')

print(horosope1.sign)
print(horosope1.mood)
print(horosope1.color)
print(horosope1.lucky_number)
print(horosope1.description)