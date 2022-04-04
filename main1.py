import sqlite3
from flask import *
from flask import Flask, render_template, request
from difflib import SequenceMatcher

app = Flask(__name__)


def writeTofile(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)
    print("Stored blob data into: ", filename, "\n")


headings = ("Id", "Name", "Accuracy")

data = []


@app.route('/')
def index():
    return render_template("base.html")


@app.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    # if(uploaded_file.filename.endswith('.pdf')==False):
    #     return 'redirect(request.url)'

    if uploaded_file.filename != '':
        fo = uploaded_file.read()
        print(fo)
    else:
        return redirect(request.url)
    my_file = "m1.txt"
    with open(my_file, 'wb') as f:
        f.write(fo)
    conn = sqlite3.connect("ms.db")
    cursor = conn.cursor()
    print("IN DATABASE FUNCTION ")
    c = cursor.execute(""" SELECT * FROM  cbse """)

    for x in c.fetchall():
        index_v = x[0]
        name_v = x[1]
        data_v = x[2]
        print(index_v)

        print(name_v)
        my_file1 = "m2.txt"
        with open(my_file1, 'wb') as f1:
            f1.write(data_v)
        with open(my_file) as file1, open(my_file1) as file2:
            file1data = file1.read()
            file2data = file2.read()
            similarity = SequenceMatcher(None, file1data, file2data).ratio()
            res = similarity * 100
            print("ACCURACY:", res)
        data1 = []
        data1.append(str(index_v))
        data1.append(name_v)
        data1.append(str(res))
        data.append(tuple(data1))
    rest=tuple(data)
    print(rest)
    return render_template("base.html", headings=headings, data=rest, asq="output :")

    return fo
    conn.commit()
    cursor.close()
    conn.close()


if __name__ == '__main__':
    app.run(debug=True)
