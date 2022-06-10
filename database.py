from sqlite3 import connect
database_d = "users.db"

class Database:
    def get_data(self):
        try:
            connation = connect(database_d)
            cursor = connation.cursor()
            cursor.execute("SELECT (userID) FROM data")
            a = cursor.fetchall()
            return a
        except Exception as e:
            print(e)
    def set(self,name,username,userID,lang="en"):
        try:
            connection = connect(database_d)
            cursor = connection.cursor()
            cursor.execute(f'INSERT INTO data(name,username,userID,language) VALUES("{name}","{username}",{userID},"{lang}")')
            connection.commit()
            connection.close()
        except Exception as e:
            print(e)
    def get_user_50(self):
        try:
            connation = connect(database_d)
            cursor = connation.cursor()
            cursor.execute("SELECT * FROM data")
            a = cursor.fetchall()[-50:]
            return a
        except Exception as e:
            print(e)

    def get_user(self):
        try:
            connation = connect(database_d)
            cursor = connation.cursor()
            cursor.execute("SELECT * FROM data")
            a = cursor.fetchall()
            return a
        except Exception as e:
            print(e)

    def get_user_id(self,id):
        try:
            connation = connect(database_d)
            cursor = connation.cursor()
            cursor.execute(f"SELECT * FROM data WHERE userID = {id}")
            a = cursor.fetchone()
            return a
        except Exception as e:
            print(e)
    def update_user_lang(self,id,lang):
        try:
            connation = connect(database_d)
            cursor = connation.cursor()
            cursor.execute(f"UPDATE data SET language='{lang}' WHERE userID = {id}")
            connation.commit()
            connation.close()
            return True
        except Exception as e:
            print(e)

if __name__ == '__main__':
    db = Database()
    print(db.get_user())
