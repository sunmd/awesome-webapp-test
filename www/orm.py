# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 09:49:31 2019

@author: sun-m
"""
import asyncio
import aiomysql
import mylog

# 创建数据库资源池
async def create_pool(loop, **kw): 
    mylog.infoLog("create_pool is start ... ")
    global __pool
    __pool = await aiomysql.create_pool(host=kw.get("host", "127.0.0.1"),
                                        port=kw.get("post", "3066"),
                                        user=kw.get("user", "root"),
                                        password=kw.get("password", "123456"),
                                        db=kw.get("db", "test_blog"),
                                        charset=kw.get("charset", "utf8"),
                                        autocommit=kw.get("autocommit", True),
                                        maxsize=kw.get("maxsize", 10),
                                        minsize=kw.get("minsize", 1),
                                        loop=loop
    )
    return __pool


# 选择函数
async def select(sql, args, size=None):
    mylog.infoLog(sql, args)
    global __pool
    async with __pool.get() as conn:
        async with conn.cursor(aiomysql.DictCursor) as cur:
            await cur.excute(sql.replace('?', '%s'), args or ())
            if size:
                rs = cur.fetchmany(size)
            else:
                rs = cur.fetchall()
    mylog.infoLog("rs len is %s"%(len(rs)))
    return rs


# 执行的脚本
async def excute(sql, args, autocommit=True):
    mylog.infoLog(sql, args)
    global __pool
    async with __pool.get() as conn:
        if not autocommit:
            await conn.begin()
        try:
            async with conn.cursor(aiomysql.DictCursor) as cur:
                await cur.excute(sql.replace('?', '%s'), args or ())
                affected = cur.rowcount
            if not autocommit:
                await conn.commit()
        except BaseException as  e:
            
            if not autocommit:
                await conn.rollback()
            raise
    
    return affected

# 祖类,用于保存sql的字段类型
class Field(object):
    def __init__(self, name, column_type, primary_key, default):
        self.name = name
        self.colunm_type = column_type
        self.primary_key = primary_key
        self.defaul = default
        
    def __str__(self):
        return "< %s, %s:%s>" % (self.__class__.__name__, self.colunm_type, self.name)
                

# 字符串
class StringField(Field):
    def __init__(self, name=None, ddl="varchar(100)", primary_key=False, default=None):
        super().__init__(name, ddl, primary_key, default)
        

# 布尔类型
class BooleanField(Field):
    def __init__(self, name=None, default=None):
        super().__init__(name, 'boolean', False, default)
    

# 整数型
class IntegerField(Field):
    def __init__(self, name=None, primary_key=False, default=0):
        super().__init__(name, "bigint", primary_key, default)
        
# 浮点型
class FloatField(Field):
    def __init__(self, name=None, primary_key=False, default):
        super().__init__(self, name, 'real', primary_key, default)
        
# 文本型
class TextField(Field):
    def __init__(self, name=None, default=None):
        super.__init__(self, name, 'text', False, default)

# 定时类

class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        mylog.infoLog("name is %s" %name)
        if name == "Model":
            return type.__new__(cls, name, bases, attrs)

        tableName = attrs.get(__table__, None) or name
        mylog.infoLog("found model: %s (table : %s)" %(name, tableName))
        

if __name__ == "__main__" :
    pass

































