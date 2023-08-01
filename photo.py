import pymysql

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData


def insertBLOB(emp_id, name, photo):
    print("Inserting BLOB into python_employee table")
    try:
        connection = pymysql.connect(host='localhost',
                                             database='image',
                                             user='root',
                                             password='root')

        cursor = connection.cursor()
        sql_insert_blob_query = """ INSERT INTO python_employee
                          (id, name, photo) VALUES (%s,%s,%s)"""

        empPicture = convertToBinaryData(photo)

        # Convert data into tuple format
        insert_blob_tuple = (emp_id, name, empPicture)
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        connection.commit()
        connection.close()
        print("Image and file inserted successfully as a BLOB into python_employee table", result)


    except pymysql.Error as error:
        print("Failed inserting BLOB data into MySQL table {}".format(error))


insertBLOB(1, "sea_animal", "sea.jpg")
insertBLOB(2, "hari_balck", "hari_black.jpg")
# insertBLOB(2, "Scott", "D:\Python\Articles\my_SQL\images\scott_photo.png",
#            "D:\Python\Articles\my_SQL\images\scott_bioData.txt")
