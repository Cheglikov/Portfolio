import pymysql.cursors

from config import host, user, password, db_name


try:
    connection = pymysql.connect(host=host,
                                 port=3306,
                                 user=user,
                                 password=password,
                                 database=db_name,
                                 cursorclass=pymysql.cursors.DictCursor)
    print("Successfully connected...")
    print("=="*20)

    try:
        #with connection.cursor() as cursor:
            # create table
            #create_table = "CREATE TABLE `users` (`id` int(11) AUTO_INCREMENT," \
            #               "email varchar(255) COLLATE utf8_bin NOT NULL," \
            #               "password varchar(255) COLLATE utf8_bin NOT NULL," \
            #               "PRIMARY KEY (`id`));"
            #cursor.execute(create_table)
            #print("Table created")

            # Create a new record
        #with connection.cursor() as cursor:
            #insert_sql = "INSERT INTO `students` (`Name`, `SurName`, Age, GroupId) VALUES ('Сірко', 'Козак', 27, 13)"
            #cursor.execute(insert_sql)
            #connection.commit()

            # Select
        with connection.cursor() as cursor:
            select_all = "SELECT * FROM `students` WHERE Name='Іван'"
            cursor.execute(select_all)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            print("*" * 20)

       #with connection.cursor() as cursor:
            # Update data
            #update_data = "UPDATE `students` SET Age = 22 WHERE Name='Іван';"
            #cursor.execute(update_data)
            #connection.commit()

       #with connection.cursor() as cursor:
            #Delete data
            #delete_data = "DELETE FROM `students` WHERE Id=8"
            #cursor.execute(delete_data)
            #connection.commit()

       #with connection.cursor() as cursor:
            #Drop table
            #drop_table = "DROP TABLE `users`"
            #cursor.execute(drop_table)


    finally:
        connection.close()


except Exception as ex:
    print("Connection refused...")
    print(ex)

