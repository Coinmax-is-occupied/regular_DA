#!/usr/bin/python
# -*- coding: utf-8 -*-

import mysql.connector
import xlwt


def get_conn(**config):
    conn = mysql.connector.connect(**config)
    return conn


def query(cur, sql, args):
    cur.execute(sql, args)
    return cur.fetchall()


def read_mysql_to_xlsx(filename):
    list_table_head = ['roomId', 'profileId', 'en_title', 'city',
                       'room_type_category', 'longitude', 'latitude',
                       'rating', 'room_review_count', 'person_capacity',
                       'bed_count', 'bedroom_count', 'base_fee', 'extra_fee', 'clean_fee']
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet('data', cell_overwrite_ok=True)
    for i in range(len(list_table_head)):
        sheet.write(0, i, list_table_head[i])

    config = {'host': '172.104.94.252',
              'user': 'user216',
              'password': 'funkey520',
              'port': 3306,
              'database': 'airbnb_db',
              'charset': 'utf8'}
    conn = get_conn(**config)
    cur = conn.cursor()
    sql = 'SELECT * FROM airbnb_db.ROOM;'
    results = query(cur, sql, None)
    conn.commit()
    cur.close()
    conn.close()
    row = 1
    for result in results:
        col = 0
        print(type(result))
        print(result)
        for item in result:
            print(item)
            sheet.write(row, col, item)
            col += 1
        row += 1
    workbook.save(filename)


if __name__ == '__main__':
    read_mysql_to_xlsx('export.xls')
