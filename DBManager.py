import sqlite3, hashlib

def register(id, password):
    encText = hashlib.md5(password.encode()).hexdigest()
    con = sqlite3.connect('./DB/user.db')
    cur = con.cursor()
    cur.execute(f"INSERT INTO user VALUES ('{id}','{encText}')")
    con.commit()
    con.close()

def login(id, password):
    encText = hashlib.md5(password.encode()).hexdigest()
    con = sqlite3.connect('./DB/user.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM User')
    user_list = cur.fetchall()
    id_list = []
    ps_list = []
    code_list = []
    ps_lock = hashlib.md5(password.encode()).hexdigest()

    for row in user_list:
        id_list.append(row[0])
        ps_list.append(row[1])

    if id in id_list:
        index = id_list.index(id)
        if ps_list[index] == ps_lock:
            return "ACCEPT"
        else:
            return "DECLINE"
    else:
        return "NOID"
