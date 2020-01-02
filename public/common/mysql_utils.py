# coding=utf-8

import pymysql
from config.basic_config import ConfigInit
from loguru import logger


class MysqlDatabase:
    def __init__(self):
        self.db = self.connect_sql()

    def connect_sql(self):
        # 建立数据库连接
        con = pymysql.connect(host=ConfigInit.mysql_host, port=ConfigInit.mysql_port, user=ConfigInit.mysql_user,
                              password=ConfigInit.mysql_pw, db=ConfigInit.mysql_db, charset='utf8mb4')
        # con.autocommit(False)
        # print('数据库连接成功')
        # return con
        try:
            print('数据库连接成功')
        except Exception as e:
            print('连接数据库失败')
        return con

    # def function(self):
    #     '''---------------------'''
    #     con = self.db
    #     cursor = con.cursor()       # 使用cursor()方法获取操作游标
    #     sql = " DELETE FROM member WHERE member_phone = '---------' "
    #     try:
    #         print("----------SQL执行中")
    #         cursor.execute(sql)     # 使用 execute()方法执行 SQL
    #         con.commit()            # 事务提交
    #         print('成功删除', cursor.rowcount, '条数据')
    #     except Exception as e:
    #         cursor.rollback()       # 如果发生错误则回滚
    #         print('事务处理失败', e)
    #     con.close()                 # 关闭数据库连接
    #     cursor.close()


if __name__ == '__main__':
    print(MysqlDatabase().connect_sql())
