import sqlite3

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

def insertBLOB(empId, name, resumeFile):
    try:
        sqliteConnection = sqlite3.connect('ms.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sqlite_insert_blob_query = """ INSERT INTO cbse
                                  (id, name, resume) VALUES (?, ?, ?)"""

        resume = convertToBinaryData(resumeFile)
        # Convert data into tuple format
        data_tuple = (empId, name, resume)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        sqliteConnection.commit()
        print("Image and file inserted successfully as a BLOB into a table")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("the sqlite connection is closed")

insertBLOB(1, "Smith", "C:/Users/Ajith P/PycharmProjects/pythonProject/edit1.txt")
insertBLOB(2, "David", "C:/Users/Ajith P/PycharmProjects/pythonProject/edit2.txt")

