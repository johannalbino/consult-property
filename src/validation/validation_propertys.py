import json
from jsonschema import validate


def validation_property(data):
    propertys = list()
    with open('src/validation/validation_json.json', 'rb') as file:
        validation = file.read()
        validation = json.loads(validation)
    for property in data:
        try:
            property_valid = validate(property, validation)
        except:
            continue
        if property_valid is None:
            if property["pricingInfos"]["businessType"] == "SALE" and int(property["pricingInfos"]["price"]) <= 700000:
                propertys.append(property)
            elif property["pricingInfos"]["businessType"] == "RENTAL" and int(property["pricingInfos"]["price"]) <= 10000:
                propertys.append(property)
    return propertys