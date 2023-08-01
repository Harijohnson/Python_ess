import pymysql


def write_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)


def readBLOB(emp_id, photo):
    print("Reading BLOB data from python_employee table")

    try:
        connection = pymysql.connect(host='localhost',
                                             database='image',
                                             user='root',
                                             password='root')

        cursor = connection.cursor()
        sql_fetch_blob_query = """SELECT * from python_employee where id = %s"""

        cursor.execute(sql_fetch_blob_query, (emp_id,))
        record = cursor.fetchall()
        for row in record:
            print("Id = ", row[0], )
            print("Name = ", row[1])
            image = row[2]
            write_file(image, photo)
        connection.close()

    except pymysql.Error as error:
        print("Failed to read BLOB data from MySQL table {}".format(error))


readBLOB(1, "star.jpg")
readBLOB(2, "star.jpg")
        
# readBLOB(2, "D:\Python\Articles\my_SQL\query_output\scott_photo.png",
#          "D:\Python\Articles\my_SQL\query_output\scott_bioData.txt")
