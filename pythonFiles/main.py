from datetime import date

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
        # piecesResult = cursor.fetchone()
        #
        # for x in range(2000):
        #     #base
        #     base = "INSERT INTO pieces (piecelength, genre, artist, piecename) VALUES "
        #     base += "("
        #
        #     #append length
        #     base += str(random.randint(100, 45000))
        #     base += ", "
        #
        #     #append foreign key
        #     count = "SELECT COUNT(*) FROM genres"
        #     cursor.execute(count)
        #     result = cursor.fetchone()
        #     help = "SELECT * FROM genres WHERE genrename='genre"
        #     help += str(random.randint(0, result[0] - 1))
        #     help += "'"
        #     cursor.execute(help)
        #     result = cursor.fetchone()
        #     base += str(result[0])
        #     base += ", "
        #
        #     # append foreign key
        #     count = "SELECT COUNT(*) FROM artists"
        #     cursor.execute(count)
        #     result = cursor.fetchone()
        #     print(result[0])
        #     help = "SELECT * FROM artists WHERE artistname='artistname"
        #     help += str(random.randint(0, result[0] - 1))
        #     help += "'"
        #     print(help)
        #     cursor.execute(help)
        #     result = cursor.fetchone()
        #     base += str(result[0])
        #
        #     #append piecename
        #     base += ", 'piecename"
        #     base += str(x + piecesResult[0])
        #     base += "')"
        #     print(base)
        #     cursor.execute(base)
        #     connection.commit()

        # PROFESSIONS
        # count = "SELECT COUNT(*) FROM professions"
        # cursor.execute(count)
        # professionsResult = cursor.fetchone()
        #
        # for x in range(6):
        #     base = "INSERT INTO professions (professionName) VALUES "
        #     base += "('profession"
        #     base += str(x + professionsResult[0])
        #     base += "')"
        #     print(base)
        #     cursor.execute(base)
        #     connection.commit()

        # ARTISTS-PROFESSIONS
        # for x in range(700):
        #     while True:
        #         # base
        #         base = "INSERT INTO artistsprofessions (artist, profession) VALUES "
        #         base += "("
        #
        #         # append foreign key
        #         count = "SELECT COUNT(*) FROM artists"
        #         cursor.execute(count)
        #         artistResult = cursor.fetchone()
        #         help = "SELECT * FROM artists WHERE artistname='artistname"
        #         artistId = random.randint(0, artistResult[0] - 1)
        #         help += str(artistId)
        #         help += "'"
        #         cursor.execute(help)
        #         aResult = cursor.fetchone()
        #         base += str(aResult[0])
        #         base += ', '
        #
        #         # append foreign key
        #         count = "SELECT COUNT(*) FROM professions"
        #         cursor.execute(count)
        #         proffesionsResult = cursor.fetchone()
        #         help = "SELECT * FROM professions WHERE professionname='profession"
        #         professionId = random.randint(0, proffesionsResult[0] - 1)
        #         help += str(professionId)
        #         help += "'"
        #         cursor.execute(help)
        #         pResult = cursor.fetchone()
        #         base += str(pResult[0])
        #         base += ")"
        #
        #         check = "SELECT COUNT(*) FROM artistsprofessions WHERE artist="
        #         check += str(aResult[0])
        #         check += " AND profession="
        #         check += str(pResult[0])
        #
        #         cursor.execute(check)
        #
        #         resultTwice = cursor.fetchone()[0]
        #
        #         if resultTwice == 0:
        #             cursor.execute(base)
        #             break
        #         else:
        #             print("continue")
        #
        #     connection.commit()

        #FESTIVALS
        # count = "SELECT COUNT(*) FROM festivals"
        # cursor.execute(count)
        # result = cursor.fetchone()
        #
        # for x in range(100):
        #     base = "INSERT INTO festivals (festivalName, festivalstartingdate, festivalendingdate) VALUES(%s, %s, %s)"
        #     randDate1 = fake.date()
        #     randDate2 = fake.date_between(randDate1, date.fromisoformat('2025-12-04'))
        #     cursor.execute(base, ("festival" + str(x + result[0]), randDate1, randDate2))
        #     connection.commit()

        #ORGANIZERS
        # count = "SELECT COUNT(*) FROM organizers"
        # cursor.execute(count)
        # organisersResult = cursor.fetchone()
        #
        # for x in range(100):
        #     base = "INSERT INTO organizers (organizerName, organizerPage) VALUES "
        #     base += "('organizerName"
        #     base += str(x + organisersResult[0])
        #     base += "', "
        #     base += "'organizerPage"
        #     base += str(x)
        #     base += "')"
        #     print(base)
        #     cursor.execute(base)
        #     connection.commit()

        # COUNTRIES
        # count = "SELECT COUNT(*) FROM countries"
        # cursor.execute(count)
        # result = cursor.fetchone()
        #
        # for x in range(50):
        #     base = "INSERT INTO countries (countryname) VALUES "
        #     base += "('country"
        #     base += str(x + result[0])
        #     base += "')"
        #     print(base)
        #     cursor.execute(base)
        #     connection.commit()

        # CITIES
        # count = "SELECT COUNT(*) FROM cities"
        # cursor.execute(count)
        # citiesResult = cursor.fetchone()
        #
        # for x in range(500):
        #     base = "INSERT INTO cities (cityname, country) VALUES "
        #     base += "('cityname"
        #     base += str(x + citiesResult[0])
        #     base += "', "
        #
        #     # append foreign key
        #     count = "SELECT COUNT(*) FROM countries"
        #     cursor.execute(count)
        #     result = cursor.fetchone()
        #     help = "SELECT * FROM countries WHERE countryname='country"
        #     help += str(random.randint(2, result[0] - 3))
        #     help += "'"
        #     cursor.execute(help)
        #     result = cursor.fetchone()
        #     base += str(result[0])
        #     base += ")"
        #     print(base)
        #     cursor.execute(base)
        #     connection.commit()

        # USERS
        # count = "SELECT COUNT(*) FROM users"
        # cursor.execute(count)
        # usersResult = cursor.fetchone()
        #
        # for x in range(5000):
        #     base = "INSERT INTO users (username, password, email, role, city) VALUES "
        #     base += "('username"
        #     base += str(x + usersResult[0])
        #     base += "', "
        #     base += "'password"
        #     base += str(x + usersResult[0])
        #     base += "', "
        #     base += "'email"
        #     base += str(x + usersResult[0])
        #     base += "', '"
        #
        #     print("sss")
        #     # randomise role
        #     random_ = random.randrange(10)
        #     role = "user"
        #
        #     if random_ == 9:
        #         role = "admin"
        #     elif random_ == 8 or random_ == 7:
        #         role = "moderator"
        #
        #     base += role
        #     base += "', "
        #     print("sss")
        #
        #     # append foreign key
        #     count = "SELECT COUNT(*) FROM cities"
        #     cursor.execute(count)
        #     result = cursor.fetchone()
        #     help = "SELECT * FROM cities WHERE cityname='cityname"
        #     help += str(random.randint(0, result[0] - 1))
        #     print(help)
        #     help += "'"
        #     cursor.execute(help)
        #     result = cursor.fetchone()
        #     print(result)
        #     base += str(result[0])
        #     print("sss")
        #     base += ")"
        #     print(base)
        #     cursor.execute(base)
        #     connection.commit()

        #LOCALIZATIONS
        # count = "SELECT COUNT(*) FROM localizations"
        # cursor.execute(count)
        # localizationsResult = cursor.fetchone()
        #
        # for x in range(1000):
        #     base = "INSERT INTO localizations (localizationname, postcode, adress, city) VALUES "
        #     base += "('localizationname"
        #     base += str(x + localizationsResult[0])
        #     base += "', '"
        #     base += str(random.randint(10, 99))
        #     base += "-"
        #     base += str(random.randint(100, 999))
        #     base += "', 'address"
        #     base += str(x + localizationsResult[0])
        #
        #     # append foreign key
        #     count = "SELECT COUNT(*) FROM cities"
        #     cursor.execute(count)
        #     result = cursor.fetchone()
        #     help = "SELECT * FROM cities WHERE cityname='cityname"
        #     help += str(random.randint(0, result[0] - 1))
        #     help += "'"
        #     cursor.execute(help)
        #     result = cursor.fetchone()
        #     base += "', "
        #     base += str(result[0])
        #     base += ")"
        #     print(base)
        #
        #     cursor.execute(base)
        #     connection.commit()

        #EVENTS
        for x in range(6):
            print(x)

        #PERFORMANCES
        for x in range(6):
            print(x)

        #TICKET VENDORS
        # count = "SELECT COUNT(*) FROM ticketvendors"
        # cursor.execute(count)
        # ticketsVendorsResult = cursor.fetchone()
        #
        # for x in range(50):
        #     base = "INSERT INTO ticketvendors (ticketvendorName, ticketvendorPage) VALUES "
        #     base += "('ticketvendorName"
        #     base += str(x + ticketsVendorsResult[0])
        #     base += "', "
        #     base += "'ticketvendorPage"
        #     base += str(x)
        #     base += "')"
        #     cursor.execute(base)
        #     connection.commit()

        #TICKETS
        # count = "SELECT COUNT(*) FROM tickets"
        # cursor.execute(count)
        # ticketsResult = cursor.fetchone()
        #
        # for x in range(2500):
        #     base = "INSERT INTO cities (sellingpage, place, price, event, ticketvendor) VALUES "
        #     base += "('sellingpage"
        #     base += str(x + ticketsResult[0])
        #     base += "', "
        #     base += "'place"
        #     base += str(x + ticketsResult[0])
        #     base += "', '"
        #     base += str(random.randint(0, 1000))
        #     base += "', "
        #
        #     # append foreign key
        #     count = "SELECT COUNT() FROM events"
        #     cursor.execute(count)
        #     result = cursor.fetchone()
        #     help = "SELECT * FROM events WHERE eventname='eventName"
        #     help += str(random.randint(0, result[0] - 1))
        #     help += "'"
        #     cursor.execute(help)
        #     result = cursor.fetchone()
        #     base += str(result[0])
        #
        #     # append foreign key
        #     count = "SELECT COUNT(*) FROM ticketvendors"
        #     cursor.execute(count)
        #     result = cursor.fetchone()
        #     help = "SELECT * FROM ticketvendors WHERE ticketvendorname='ticketvendorName"
        #     help += str(random.randint(0, result[0] - 1))
        #     help += "'"
        #     cursor.execute(help)
        #     result = cursor.fetchone()
        #     base += str(result[0])
        #     base += ")"
        #     print(base)
        #     cursor.execute(base)
        #     connection.commit()

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
