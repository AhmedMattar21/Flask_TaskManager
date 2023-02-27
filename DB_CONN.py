import sqlite3

class conn:
    'DB Connection Handler with Sqlite3'

    def connect():
        db_conn = sqlite3.connect('app.db')
        return db_conn

    def init_db():
        db = conn.connect()
        cr = db.cursor()

        file = open('init.sql', 'r')
        strc = file.readlines()
        csql = conn.clean_sql(strc)
        cr.execute(csql)
        db.commit()
        

    
    def NonReturnQuery(sql):
        db = conn.connect()
        cr = db.cursor()
        csql = conn.clean_sql(sql)
        cr.execute(csql)
        db.commit()
        

# a methon for removing \n and \t form the sql string
    def clean_sql(sql):
        cleansql = ''
        for line in sql:
            cln = line.split('\n')
            cln[0] = cln[0].replace('\t','')
            cleansql = cleansql + cln[0]
        return cleansql
    
    def get_nextID(table,id):
        db = conn.connect()
        cr = db.cursor()
        try:
            cr.execute(f'SELECT MAX({id}) FROM {table} ')
            maxID = cr.fetchone()
            maxID = maxID[0]
            nextID = maxID + 1
            return nextID
        except:
            return 1
        

    def returnQuery(sql):
        db = conn.connect()
        cr = db.cursor()
        try:
            cr.execute(sql)
            res = cr.fetchall()
            return res
        except:
            return ' - '





        

