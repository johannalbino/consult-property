from src.core.utils import get_data_propertys


async def processing_data(body):
    neighborhood = body['neighborhood']
    transaction = body['transaction']
    data_external = await get_data_propertys()

    if data_external is False:
        return False

    propertys = []

    for data_e in data_external:
        if data_e['address']['neighborhood'] == neighborhood and data_e['pricingInfos']['businessType'] == transaction:
            propertys.append(data_e)
    return propertys
