from aiohttp import ClientSession
import numpy as np
from src.core.config import LINK_API_EXTERNAL
from src.core.constanst import LIST_AREA_50


async def get_data_propertys():
    async with ClientSession() as session:
        async with session.get(str(LINK_API_EXTERNAL)) as req:
            resp = req
            if resp.status == 200:
                return await resp.json()


def treating_data(data):
    n_obs = len(data)
    all_mediana = []
    all_area = []
    for _data in data:
        price = _data['pricingInfos']['price']
        area = _data['usableAreas']
        price_per_m2 = float(price) / float(area)
        median = []
        for ar in range(area):
            if ar == 0:
                median.append(price_per_m2)
            else:
                median.append(price_per_m2 + median[-1])

        median = np.median(median)
        all_mediana.append(median)
        all_area.append(area)

    median_all_area = np.median(all_mediana)

    class_per_area = {}
    for key, value in enumerate(LIST_AREA_50):
        if value == 50:
            va = [y for y in data if y['usableAreas'] < value]
            class_per_area[f"ate{value}m2"] = va
        else:
            va = [y for y in data if y['usableAreas'] >= LIST_AREA_50[key - 1] and y['usableAreas'] < LIST_AREA_50[key] and y['usableAreas'] < value]
            if va:
                class_per_area[f"de{value-50}ate{value}m2"] = va

    class_per_area_final = {}
    for k, v in class_per_area.items():
        values_p = [float(va['pricingInfos']['price']) for va in v]
        class_per_area_final[k] = round(np.mean(values_p), 2)

    return n_obs, median_all_area, class_per_area_final
