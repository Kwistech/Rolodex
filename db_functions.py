# Database Functions
import sqlite3


def create_db(cursor):
    """Attempts to create the table 'people' in database file if not already created.

    Args:
        cursor (sqlite3.Cursor): Cursor in database file.

    """
    try:
        sql = 'create table people (name, number, email, notes)'
        cursor.execute(sql)
    except sqlite3.OperationalError:
        pass


def menu():
    """Main menu for Rolodex.

    Returns:
        str: Command to be used in main().

    """
    welcome = "\n\nWelcome to your Rolodex!\n"
    divider = "-" * len(welcome)
    hint = "\nType 'help' for more info"
    print(welcome + divider + hint)

    cmd = input("> ")
    return cmd.lower()


def add_person(cursor):
    """Adds a person and their information to the database.

    Args:
        cursor (sqlite3.Cursor): Cursor in database file.

    """
    name = input("Person's name: ")
    number = input("Person's number: ")
    email = input("Person's email: ")
    notes = input("Person's notes: ")

    sql = 'insert into people (name, number, email, notes) values ' \
          '("{}", "{}", "{}", "{}")'
    sql = sql.format(name, number, email, notes)
    cursor.execute(sql)


def delete_person(cursor):
    """Deletes a person and their information from the database.

    Args:
        cursor (sqlite3.Cursor): Cursor in database file.

    """
    person = input("Person to delete: ")
    sql = 'delete from people where name="{}"'
    sql = sql.format(person)
    cursor.execute(sql)
    print("Deleted {} from rolodex".format(person))


def update_person(cursor):
    """Updates a person's information in the database.

    Args:
        cursor (sqlite3.Cursor): Cursor in database file.

    """
    person = input("Person to change: ")
    info_type = input("Info to change [name, number, email, notes]: ")
    info_new = input("New info: ")
    sql = 'select * from people order by name'
    results = cursor.execute(sql)
    people = results.fetchall()
    individual = ()

    sql = 'update people set {0}="{1}" where {0}="{2}"'

    for p in people:
        if p[0] == person:
            individual = p

    if info_type.lower() == "name":
        sql = sql.format(info_type, info_new, individual[0])
    elif info_type.lower() == "number":
        sql = sql.format(info_type, info_new, individual[1])
    elif info_type.lower() == "email":
        sql = sql.format(info_type, info_new, individual[2])
    elif info_type.lower() == "notes":
        sql = sql.format(info_type, info_new, individual[3])

    cursor.execute(sql)
    print("Updated info!")


def list_person(cursor):
    """Lists a person and their information.

    Args:
        cursor (sqlite3.Cursor): Cursor in database file.

    """
    person = input("Person to list: ")
    sql = 'select * from people where name="{}"'
    results = cursor.execute(sql.format(person))
    person_out = results.fetchall()

    for p in person_out:
        print(p)


def list_people(cursor):
    """Lists all people and their respective information.

    Args:
        cursor (sqlite3.Cursor): Cursor in database file.

    """
    sql = "select * from people order by name"
    results = cursor.execute(sql)
    people = results.fetchall()
    print("\nYour Rolodex (name, number, email, notes):\n")

    for person in people:
        name = person[0]
        number = person[1]
        email = person[2]
        notes = person[3]

        print_out = "{name}\t{number}\t{email}\t{notes}"
        print(print_out.format(name=name, number=number, email=email, notes=notes))


def name_lookup(cursor):
    """Searches the database for user's input; letters of name(s) to lookup.

    Note: The function will also work with a completed name.

    Args:
        cursor (sqlite3.Cursor): Cursor in database file.

    """
    letter = input("First letter of name(s): ")
    sql = 'select * from people where name like "{}%"'
    results = cursor.execute(sql.format(letter.upper()))
    people = results.fetchall()

    for person in people:
        print(person)


def number_lookup(cursor):
    """Searches the database for user's input; digits of number(s) to lookup.

    Note: The function will also work with a completed number.

    Args:
        cursor (sqlite3.Cursor): Cursor in database file.

    """
    number = input("Number to lookup: ")
    sql = 'select * from people where number like "{}%"'
    results = cursor.execute(sql.format(number))
    people = results.fetchall()

    for person in people:
        print(person)


def email_lookup(cursor):
    """Searches the database for user's input; characters of email(s) to lookup.

    Note: The function will also work with a completed email.

    Args:
        cursor (sqlite3.Cursor): Cursor in database file.

    """
    email = input("Email to lookup: ")
    sql = 'select * from people where email like "%{}%"'
    results = cursor.execute(sql.format(email))
    people = results.fetchall()

    for person in people:
        print(person)


def notes_lookup(cursor):
    """Searches the database for user's input; sample of notes to lookup.

    Note: The function will also work with a completed note.

    Args:
        cursor (sqlite3.Cursor): Cursor in database file.

    """
    notes = input("Sample notes to lookup: ")
    sql = 'select * from people where notes like "%{}%"'
    results = cursor.execute(sql.format(notes))
    people = results.fetchall()

    for person in people:
        print(person)
