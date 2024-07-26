import sqlite3

con = sqlite3.connect("detectivebot.db")

cursor = con.cursor()

# cursor.execute("""CREATE TABLE suspected
#                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 # name TEXT)
#             """)
#
# cursor.execute("""CREATE TABLE hint
#                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 description TEXT
#             """)


def show_hint_by_id(hint_id):
    cursor.execute("SELECT description FROM hint WHERE id = ?", (hint_id,))
    result = cursor.fetchone()
    return result

def show_suspected_by_id(suspected_id):
    cursor.execute("SELECT name FROM suspected WHERE id = ?", (suspected_id,))
    result = cursor.fetchone()
    return result




con.commit()

