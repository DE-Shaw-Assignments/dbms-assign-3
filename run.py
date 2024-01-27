import mysql.connector
import getpass

def connect_to_database(host, username, password):
    try:
        conn = mysql.connector.connect(
            host=host,
            user=username,
            password=password,
            database="airportdb"
        )
        return conn
    except mysql.connector.Error as e:
        print("Error connecting to MySQL:", e)
        return None

def execute_query(choice, query, conn):
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query)
        result = cursor.fetchall()
        if choice == 2:
            print("Seat-wise average prices:")
            for row in result:
                print(f"Seat {row['seat']}: {row['average_price']}")
            num_rows = cursor.rowcount
            print("Total number of seats:", num_rows)
        elif choice == 4:
            print("Flight dates:")
            for row in result:
                print(row['flight_date'])
            num_rows = cursor.rowcount
            print("Total number of flight dates:", num_rows)
        elif choice == 5:
            for row in result:
                print(f"{row['airlinename']}: {row['total_revenue']}")
        elif choice == 3:
            print("Airplane Types:")
            for row in result:
                print(row['airline_type'])
            num_rows = cursor.rowcount
            print("Total number of airplane types:", num_rows)
        elif choice == 1:
            print("Number of flights:", result[0]['num_flights'])
        cursor.close()
    except mysql.connector.Error as e:
        print("Error executing query:", e)

def main():
    host = input("Enter host: ")
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")

    conn = connect_to_database(host, username, password)
    if conn:
        queries = [
            {"description": "Count the number of flights between two airports.",
             "query": "SELECT COUNT(*) AS num_flights FROM flight f JOIN airport a_src ON f.from = a_src.airport_id JOIN airport a_dest ON f.to = a_dest.airport_id WHERE a_src.name = '%s' AND a_dest.name = '%s';"},
            {"description": "Calculate the average price of bookings for a specific flight for every.",
             "query": "SELECT seat,AVG(price) AS average_price FROM booking WHERE flight_id = %s AND seat IS NOT NULL GROUP BY seat;"},
            {"description": "Count the number of airplane types a passenger has traveled in.",
             "query": "SELECT DISTINCT at.identifier AS airline_type FROM booking b JOIN flight f ON b.flight_id = f.flight_id JOIN airplane a ON f.airplane_id = a.airplane_id JOIN airplane_type at ON a.type_id = at.type_id WHERE b.passenger_id = %s;"},
            {"description": "Find the unique dates when it was unsafe to fly.",
             "query": "SELECT DISTINCT DATE(w.log_date) AS flight_date FROM weatherdata w WHERE w.humidity >= 98 AND w.airpressure > 1015;"},
            {"description": "Calculate the total revenue for each airline and print in reverse-sorted order.",
             "query": "SELECT a.airlinename, SUM(b.price) AS total_revenue FROM flight f JOIN booking b ON f.flight_id = b.flight_id JOIN airline a ON f.airline_id = a.airline_id GROUP BY f.airline_id, a.airlinename ORDER BY total_revenue DESC;"}
        ]

        print("Select which query to run:")
        for i, query in enumerate(queries, 1):
            print(f"{i}. {query['description']}")
        choice = int(input("Enter the number of the query: "))

        if 1 <= choice <= len(queries):
            query = queries[choice - 1]['query']
            if choice == 2:
                flight_id = input("Enter flight ID: ")
                execute_query(choice, query % flight_id, conn)
            elif choice == 1:
                src_name = input("Enter source airport name: ")
                dest_name = input("Enter destination airport name: ")
                execute_query(choice, query % (src_name, dest_name), conn)
            elif choice == 3:
                passenger_id = input("Enter passenger ID: ")
                execute_query(choice, query % passenger_id, conn)
            elif choice == 4 or choice == 5:
                execute_query(choice, query, conn)
        else:
            print("Invalid choice. Please select a number between 1 and", len(queries))

        conn.close()

if __name__ == "__main__":
    main()
