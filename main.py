# Rolodex - Johnathon Kwisses (Kwistech)
import sqlite3
import db_functions


def main():
    conn = sqlite3.connect("rolodex.db")
    cursor = conn.cursor()
    db_functions.create_db(cursor)

    while True:
        choice = db_functions.menu()

        if choice == "add person":
            db_functions.add_person(cursor)
        elif choice == "list people":
            db_functions.list_people(cursor)
        elif choice == "delete person":
            db_functions.delete_person(cursor)
        elif choice == "quit" or choice == "q":
            print("Goodbye!")
            break
        else:
            print("ERROR: input not valid.")

        conn.commit()

    conn.close()

if __name__ == "__main__":
    main()
