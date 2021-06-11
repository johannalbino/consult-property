from src.core.utils import get_data_propertys
from src.validation.validation_propertys import validation_property


async def processing_data(body):
    neighborhood = body['bairro']
    transaction = body['transacao']
    data_external = await get_data_propertys()

    if data_external is False:
        return False

    propertys = []

    for data_e in data_external:
        if data_e['address']['neighborhood'] == neighborhood and data_e['pricingInfos']['businessType'] == transaction:
            propertys.append(data_e)

    data_process = validation_property(propertys)

    return data_process
