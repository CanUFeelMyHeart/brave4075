import pymysql
from config import host, password, user, db_name

try:
    connection = pymysql.connect(
        host = host, # localhost
        port = 3306,
        user = user, # "root"
        password = password, # "1234"
        database = db_name, #lesson_2
        cursorclass = pymysql.cursors.DictCursor
    )
    print("Connected successfully")
    try:
        cursor = connection.cursor()

        # create table
        create_query = "CREATE TABLE IF NOT EXISTS users" \
                       "( id INT PRIMARY KEY AUTO_INCREMENT," \
                       "firstname VARCHAR(45));"
        cursor.execute(create_query)
        print("Table created successfully")

        # insert data
        insert_query = "INSERT users(firstname) VALUES ('Алина'), " \
                       "('Test');"
        cursor.execute(insert_query)
        connection.commit()
        print("Insert successfully")

        # update
        cursor.execute("UPDATE users SET firstname = 'Mikle'"
                       "WHERE id = 4")

        # delete
        cursor.execute("DELETE FROM users WHERE id = 2")
        connection.commit()

        #  select-ы
        cursor.execute("SELECT * FROM users;")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    finally:
        connection.close()

except Exception as ex:
    print("Disconnected")
    print(ex)