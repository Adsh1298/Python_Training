from typing import final

import pymysql

#Class the abstracts the mysql code from your flask application.
class MySqlDatabase:
    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.password = 'cdacacts'
        self.database = 'sampledb'
        self.connection = None

    def connect(self):
        try:
            self.connection = pymysql.connect(host = self.host, user = self.user, password =
            self.password, database = self.database)
            print('Connected to the Database')
        except Exception as ex:
            print('Exception: ', ex)

    def disconnect(self):
        if self.connection:
            #self.connection.cursor.close()
            self.connection.close()
            print('Disconnected from the Databas')

    def get_all_users(self):
        try:
            self.connect()
            with self.connection.cursor() as cursor:
                query = 'SELECT * FROM userinfo'
                cursor.execute(query)
                users = cursor.fetchall()

        except Exception as ex:
            print('Exception: ', ex)
        else:
            return users
        finally:
            self.disconnect()

    def get_user_by_id(self, id):
        try:
            self.connect()
            with self.connection.cursor() as cursor:
                query = 'SELECT * FROM userinfo WHERE id = %s'
                cursor.execute(query, id)
                selected_user = cursor.fetchone()
        except Exception as ex:
            print('Exception: ', ex)
        else:
            return selected_user
        finally:
            self.disconnect()
    def update_user(self, id, name, pwd, email):
        try:
            self.connect()
            with self.connection.cursor() as cursor:
                query = 'UPDATE USERINFO SET username=%s, password=%s, emailaddress=%s WHERE id = %s'
                cursor.execute(query, (name, pwd, email, id))
                self.connection.commit()
        except Exception as ex:
            print(f'Exception: {ex}')
        finally:
            self.disconnect()

    def add_user(self, name, pwd, email):
        try:
            self.connect()
            with self.connection.cursor() as cursor:
                query = (
                    f"INSERT INTO USERINFO (username, password, emailaddress) values (%s, %s, %s)")
                cursor.execute(query, (name, pwd, email))
                self.connection.commit()
        except Exception as ex:
            print("Exception while inserting: ", ex)
        finally:
            self.disconnect()
