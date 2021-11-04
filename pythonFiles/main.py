import psycopg2
from psycopg2 import Error
import random

from faker import Faker
fake = Faker()

def generateString(length):

    return length

def magic():
    try:
        # Connect to an existing database
        connection = psycopg2.connect(user="postgres",
                                      password="Maciek009",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="BazyTest")

        # Create a cursor to perform database operations
        cursor = connection.cursor()
        # Print PostgreSQL details
        print("PostgreSQL server information")
        print(connection.get_dsn_parameters(), "\n")

        test = "SELECT * FROM genres"
        cursor.execute(test)
        res = cursor.fetchone()
        print(res)

        # GENRES

        # count = "SELECT COUNT(*) FROM artists"
        # cursor.execute(count)
        # result = cursor.fetchone()

        # for x in range(20):
        #     base = "INSERT INTO genres (genreName) VALUES "
        #     base += "('genre"
        #     base += str(x + result[0])
        #     base += "')"
        #     print(base)
        #     cursor.execute(base)
        #     connection.commit()

        #ARTISTS
        # count = "SELECT COUNT(*) FROM artists"
        # cursor.execute(count)
        # result = cursor.fetchone()

        # for x in range(500):
        #     base = "INSERT INTO artists (artistname, foundationyear, description) VALUES "
        #     base += "('artistname"
        #     print(x)
        #     base += str(x + result[0])
        #     base += "', "
        #     base += str(random.randint(1000, 2999))
        #     base += ", 'description"
        #     base += str(x)
        #     base += "')"
        #     print(base)
        #     cursor.execute(base)
        #     connection.commit()


        #PIECES
        # count = "SELECT COUNT(*) FROM pieces"
        # cursor.execute(count)
        # result = cursor.fetchone()

        for x in range(2000):
            #dobra jest gitara

            #base
            base = "INSERT INTO pieces (piecelength, genre, artist, piecename) VALUES "
            base += "("
            #append length
            base += str(random.randint(100, 45000))
            base += ", "
            print("aaa")
            #append foreign key
            count = "SELECT COUNT(*) FROM genres"
            cursor.execute(count)
            result = cursor.fetchone()
            help = "SELECT * FROM genres WHERE genrename='genre"
            help += str(random.randint(0, result[0] - 1))
            help += "'"
            cursor.execute(help)
            result = cursor.fetchone()
            base += str(result[0])

            # append foreign key
            count = "SELECT COUNT(*) FROM artists"
            cursor.execute(count)
            result = cursor.fetchone()
            print(result[0])
            help = "SELECT * FROM artists WHERE artistname='artistname"
            help += str(random.randint(0, result[0] - 1))
            help += "'"
            print(help)
            cursor.execute(help)
            result = cursor.fetchone()
            base += str(result[0])
            print("aaa")
            base += ")"
            print(base)
            # cursor.execute(base)
            # cursor.fetchone()

        #PROFFESIONS
        for x in range(6):
            print(x)
            # cursor.execute(base)
            # cursor.fetchall()

        #ARTISTS-PROFFESIONS
        for x in range(6):
            print(x)

        #FESTIVALS
        for x in range(6):
            print(x)

        #ORGANIZERS
        for x in range(6):
            print(x)

        #COUNTRIES
        for x in range(6):
            print(x)

        #USERS
        for x in range(6):
            print(x)

        #CITIES
        for x in range(6):
            print(x)

        #LOCALIZATIONS
        for x in range(6):
            print(x)

        #EVENTS
        for x in range(6):
            print(x)

        #PERFORMANCES
        for x in range(6):
            print(x)

        #TICKET VENDORS
        for x in range(6):
            print(x)

        #TICKETS
        for x in range(6):
            print(x)

        # Fetch result
        record = cursor.fetchall()

        cursor.close()
        connection.close()

        print("You are connected to - ", record, "\n")

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
    print()

if __name__ == '__main__':
    magic()
