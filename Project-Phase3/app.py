from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

def connect_to_database():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="2489",
        database="project"
    )

@app.route("/")
def index():
    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        # Execute SQL query to fetch table names
        cursor.execute("SHOW TABLES")
        # Fetch all table names
        tables = [table[0] for table in cursor.fetchall()]
        return render_template("index.html", tables=tables)
    except mysql.connector.Error as e:
        # Handle database connection error
        return render_template("error.html", error="Database error: {}".format(e))
    finally:
        cursor.close()
        connection.close()

@app.route("/retrieve", methods=["POST"])
def retrieve_data():
    table_name = request.form["table_name"]
    try:
        connection = connect_to_database()
        cursor = connection.cursor(dictionary=True)
        if table_name == 'procedure':
                table_name = '`procedure`'
        query = "SELECT * FROM {}".format(table_name)
        cursor.execute(query)
        result = cursor.fetchall()
        return render_template("result.html", table_name=table_name, result=result)
    except mysql.connector.Error as e:
        return render_template("error.html", error="Error: {}".format(e))
    finally:
        cursor.close()
        connection.close()

@app.route("/retrieve_all", methods=["POST"])
def retrieve_all_data():
    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES")
        tables = [table[0] for table in cursor.fetchall()]

        all_table_data = {}
        for table in tables:
            cursor = connection.cursor(dictionary=True)
            if table == 'procedure':
                table = '`procedure`'
            cursor.execute("SELECT * FROM {}".format(table))
            table_data = cursor.fetchall()
            all_table_data[table] = table_data
        return render_template("retrieve_all.html", all_table_data=all_table_data)
    except mysql.connector.Error as e:
        return render_template("error.html", error="Database error: {}".format(e))
    finally:
        cursor.close()
        connection.close()

@app.route("/average", methods=["POST"])
def calculate_average():
    table_name = request.form["table_name"]
    if table_name == 'procedure':
                table_name = '`procedure`'
    try:
        connection = connect_to_database()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("DESCRIBE {}".format(table_name))
        columns = []
        for row in cursor.fetchall():
            if row["Type"].startswith("int") or row["Type"].startswith("decimal") or row["Type"].startswith("double"):
                columns.append(row["Field"])
        return render_template("average.html", table_name=table_name, columns=columns)
    except mysql.connector.Error as e:
        return render_template("error.html", error="Error: {}".format(e))
    finally:
        cursor.close()
        connection.close()

@app.route("/insert", methods=["GET","POST"])
def insert_data():
    table_name = request.form["table_name"]
    if table_name == 'procedure':
                table_name = '`procedure`'
    try:
        connection = connect_to_database()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("DESCRIBE {}".format(table_name))
        columns = [row["Field"] for row in cursor.fetchall()]
        return render_template("insert.html", table_name=table_name, columns=columns)
    except mysql.connector.Error as e:
        return render_template("error.html", error="Error: {}".format(e))
    finally:
        cursor.close()
        connection.close()

@app.route("/insert_confirm", methods=["POST"])
def insert_confirm():
    table_name = request.form.get("table_name")
    if table_name == 'procedure':
                table_name = '`procedure`'
    column_names = [col for col in request.form if col != "table_name"]
    values = [request.form[col] for col in column_names]
    try:
        connection = connect_to_database()
        cursor = connection.cursor(dictionary=True)
        query = "INSERT INTO {} ({}) VALUES ({})".format(table_name, ', '.join(column_names), ', '.join(['%s']*len(values)))
        cursor.execute(query, values)
        connection.commit()
        return render_template("success.html", message="Data inserted successfully!", table_name=table_name)
    except mysql.connector.Error as e:
        return render_template("error.html", error="Error: {}".format(e))
    finally:
        cursor.close()
        connection.close()

@app.route("/delete", methods=["GET","POST"])
def delete_data():
    table_name = request.form["table_name"]
    if table_name == 'procedure':
                table_name = '`procedure`'
    try:
        connection = connect_to_database()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("DESCRIBE {}".format(table_name))
        columns = [row["Field"] for row in cursor.fetchall()]
        return render_template("delete.html", table_name=table_name, columns=columns)
    except mysql.connector.Error as e:
        return render_template("error.html", error="Error: {}".format(e))
    finally:
        cursor.close()
        connection.close()

@app.route("/delete_confirm", methods=["POST"])
def delete_confirm():
    table_name = request.form.get("table_name")
    if table_name == 'procedure':
                table_name = '`procedure`'
    column_names = [col for col in request.form if col != "table_name"]
    conditions = ["{}='{}'".format(col, request.form[col]) for col in column_names if request.form[col]]
    try:
        connection = connect_to_database()
        cursor = connection.cursor(dictionary=True)
        if len(conditions) == 1:
            condition_string = ''.join(conditions)
        else:
            condition_string = ' AND '.join(conditions)
        query = "DELETE FROM {} WHERE {}".format(table_name, condition_string)
        cursor.execute(query)
        connection.commit()
        return render_template("success.html", message="Data deleted successfully!", table_name=table_name)
    except mysql.connector.Error as e:
        return render_template("error.html", error="Error: {}".format(e))
    finally:
        cursor.close()
        connection.close()

@app.route("/result_avg", methods=["POST"])
def calculate_avg():
    table_name = request.form["table_name"]
    column_name = request.form["column_name"]
    if table_name == 'procedure':
                table_name = '`procedure`'
    try:
        connection = connect_to_database()
        cursor = connection.cursor(dictionary=True)
        query = "SELECT AVG({}) AS avg FROM {}".format(column_name, table_name)
        cursor.execute(query)
        result = cursor.fetchone()
        average = result["avg"]
        return render_template("result_avg.html", average=average)
    except mysql.connector.Error as e:
        return render_template("error.html", error="Error: {}".format(e))
    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    app.run(debug=True)
