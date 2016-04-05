# Database Functions
import sqlite3


def create_db(cursor):
    try:
        sql = 'create table people (name, number, email, notes)'
        cursor.execute(sql)
    except sqlite3.OperationalError:
        pass


def menu():
    welcome = "\n\nWelcome to your Rolodex!\n"
    divider = "-" * len(welcome)
    hint = "\nType 'help' for more info"
    print(welcome + divider + hint)

    cmd = input("> ")
    return cmd.lower()


def add_person(cursor):
    name = input("Person's name: ")
    number = input("Person's number: ")
    email = input("Person's email: ")
    notes = input("Person's notes: ")

    sql = 'insert into people (name, number, email, notes) values ' \
          '("{}", "{}", "{}", "{}")'
    sql = sql.format(name, number, email, notes)
    cursor.execute(sql)


def delete_person(cursor):
    person = input("Person to delete: ")
    sql = 'delete from people where name="{}"'
    sql = sql.format(person)
    cursor.execute(sql)
    print("Deleted {} from rolodex".format(person))


def list_people(cursor):
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
