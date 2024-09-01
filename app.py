from flask import Flask,render_template
import backend.database as db

app = Flask(__name__,template_folder='frontend/templates')

@app.route("/api/flights/arrivals", methods =["GET"])
def get_arrivals():
    select_statement = "SELECT * FROM Arrivals"
    cursor.execute(select_statement)
    flights = cursor.fetchall()
    return render_template("table.html",flights=flights)

@app.route("/api/flights/departures", methods =["GET"])
def get_departures():
    select_statement = "SELECT * FROM Departures"
    cursor.execute(select_statement)
    flights = cursor.fetchall()
    return render_template("table.html",flights=flights)

@app.route('/api/flights/departures/<flight_number>', methods=['GET'])
def get_arrivals_flight(flight_number):
    select_statement = "SELECT * FROM Departures WHERE flight_number = %s"
    cursor.execute(select_statement,(flight_number,))
    flights = cursor.fetchall()
    return render_template("table.html",flights=flights)
@app.route('/api/flights/arrivals/<flight_number>', methods=['GET'])
def get_departures_flight(flight_number):
    select_statement = "SELECT * FROM Arrivals WHERE flight_number = %s"

    cursor.execute(select_statement,(flight_number,))
    flights = cursor.fetchall()
    return render_template("table.html",flights=flights)

if __name__ == '__main__':
    db.connect()
    con = db.get_connection()
    cursor = con.get_cursor()
    app.run(host='0.0.0.0', port=5000)

        





