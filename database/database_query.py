import sqlite3


def get_polarity(uid):
    dbconnection = sqlite3.connect('ChatbotDB.db')
    sqlite_cursor = dbconnection.cursor()

    query = "SELECT SUM(Sentiment), SUM(Counter) FROM PolarityFact WHERE UserID = ?"
    sqlite_cursor.execute(query, (uid,))
    result = sqlite_cursor.fetchall()
    dbconnection.close()

    avg_polarity = result[0][0] / result[0][1]

    return avg_polarity


def get_strikes(uid):
    dbconnection = sqlite3.connect('ChatbotDB.db')
    sqlite_cursor = dbconnection.cursor()

    week_query = "SELECT SUM(Strike) FROM PolarityFact WHERE LogDate > (SELECT DATETIME('now', '-7 day')) and UserID = ?"
    month_query = "SELECT SUM(Strike) FROM PolarityFact WHERE LogDate > (SELECT DATETIME('now', '-30 day')) and UserID = ?"

    sqlite_cursor.execute(week_query, (uid,))
    week_strikes = sqlite_cursor.fetchall()

    sqlite_cursor.execute(month_query, (uid,))
    month_strikes = sqlite_cursor.fetchall()

    strikes = {
        "week": week_strikes[0][0],
        "month": month_strikes[0][0]
    }

    dbconnection.close()

    return strikes

def update_polarity(uid, polarity):
    dbconnection = sqlite3.connect('ChatbotDB.db')
    sqlite_cursor = dbconnection.cursor()
    in_query = "INSERT INTO PolarityFact (UserID, Sentiment, Counter) VALUES (?, ?, 1)"
    sqlite_cursor.execute(in_query, (uid, polarity))
    dbconnection.commit()

    dbconnection.close()

    return get_polarity(uid)


def add_strike(uid):
    dbconnection = sqlite3.connect('ChatbotDB.db')
    sqlite_cursor = dbconnection.cursor()
    in_query = "INSERT INTO PolarityFact (UserID, Strike) VALUES (?, 1)"
    sqlite_cursor.execute(in_query, (uid,))

    dbconnection.commit()
    dbconnection.close()

    return get_strikes(uid)


print(get_strikes("test"))
