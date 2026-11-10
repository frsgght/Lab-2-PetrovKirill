import xml.etree.ElementTree as ET

tree = ET.parse("currency.xml")
root = tree.getroot()

currencies = {}

for valute in root.findall("Valute"):
    char_code = valute.findtext("CharCode")
    nominal = int(valute.findtext("Nominal"))

    currencies[char_code] = nominal

print(currencies)