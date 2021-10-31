import os

import openpyxl
import config
import game_scrapper as gs
import logging

def data_filling(appids, username):
    logger = logging.getLogger("logger")
    logger.debug(os.getcwd())
    workbook = openpyxl.open('data.xlsx')
    ws = workbook['Main']
    logger.info('Workbook opened')

    appids_existing = []
    for row in range(1, ws.max_row):
        appids_existing.append(int(ws.cell(row=row, column=1).value))
    for appid in appids:
        game = gs.get_game_info(appid)
        if game.get('steam_appid') in appids_existing:
            ws.cell(row=appids_existing.index(game.get('steam_appid')) + 1, column=config.EXCEL_MAPPER.get('username')) \
                .value += username + ', '
            pass
        gs.save_header(appid, game.get('name'))
        current_row = ws.max_row + 1
        for k, v in game.items():
            col_num = config.EXCEL_MAPPER.get(k)
            if col_num is None:
                pass
            ws.cell(row=current_row, column= col_num).value = v
        ws.cell(row=current_row, column= config.EXCEL_MAPPER.get('username')).value = username + ', '

    workbook.save('data.xlsx')
    workbook.close()
