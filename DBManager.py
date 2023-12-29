import sqlite3, hashlib

def register(id, password):
    encText = hashlib.md5(password.encode()).hexdigest()
    con = sqlite3.connect('./DB/user.db')
    cur = con.cursor()
    cur.execute(f"INSERT INTO user VALUES ('{id}','{encText}','NONE')")
    con.commit()
    con.close()
