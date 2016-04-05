# Rolodex - Johnathon Kwisses (Kwistech)
import sqlite3
import db_functions


def main():
    """Switch for Rolodex; creates connection and cursor for database."""
    conn = sqlite3.connect("rolodex.db")
    cursor = conn.cursor()
    db_functions.create_db(cursor)

    while True:
        choice = db_functions.menu()

        if choice == "add person":
            db_functions.add_person(cursor)
        elif choice == "delete person":
            db_functions.delete_person(cursor)
        elif choice == "update person":
            db_functions.update_person(cursor)
        elif choice == "list people":
            db_functions.list_people(cursor)
        elif choice == "name lookup":
            db_functions.list_person(cursor)
        elif choice == "letter lookup":
            db_functions.name_lookup(cursor)
        elif choice == "number lookup":
            db_functions.number_lookup(cursor)
        elif choice == "email lookup":
            db_functions.email_lookup(cursor)
        elif choice == "notes lookup":
            db_functions.notes_lookup(cursor)
        elif choice == "quit" or choice == "q":
            print("Goodbye!")
            break
        else:
            print("ERROR: input not valid.")

        conn.commit()  # Commits info every time it loops.

    conn.close()

if __name__ == "__main__":
    main()
