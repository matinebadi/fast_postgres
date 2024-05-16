import psycopg2

connected=psycopg2.connect(user='postgres',password=123,host="localhost",port=5432,database="postgres")
cun=connected.cursor()

def add(name, ii):
    cun.execute(f"insert into data_item(name,item_id)values('{name}', {ii})")
    connected.commit()

def update(name, ii,last_id):
    cun.execute(f"update data_item set name='{name}',item_id='{ii}' where item_id='{last_id}' ")
    connected.commit()

def deleted(last_id1):
    cun.execute(f"delete from data_item where item_id='{last_id1}' ")
    connected.commit()

def showed_all():
    try:
        cun.execute(f"SELECT * FROM data_item ")
        res = cun.fetchall()
        l = list()
        for i in res:
            d = dict()
            d['name'] = i[1]
            d['item_id'] = i[2]
            l.append(d)
        return l
    except:
        connected.rollback()

def showed(id):
    try:
        cun.execute(f"SELECT * FROM data_item where item_id={id} ")
        res = cun.fetchone()
        d = dict()
        d['name'] = res[1]
        d['item_id'] = res[2]
        return d
    except:
        connected.rollback()


