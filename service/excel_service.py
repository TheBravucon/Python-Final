import time

import pandas as pd

EXCEL_COLUMNS = ['Id', 'Nombre de producto', 'Precio', 'Cantidad']


def crear_ticket(data=()):
    df = pd.DataFrame(data, columns=EXCEL_COLUMNS)
    products_length = len(data)
    df.loc[products_length, 'Total'] = calcular_total(data)
    df.to_excel(f'ticket_{time.time()}.xlsx', index=False, sheet_name='Sheet1')


def calcular_total(data=()):
    total = 0.0
    for product in data:
        total += product[2] * product[3]

    return total
