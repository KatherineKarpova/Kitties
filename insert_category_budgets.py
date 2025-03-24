import sqlite3
import sys

def main():

    conn = sqlite3.connect('finances.db')
    c = conn.cursor()

    categories_and_budgets = {
        'fixed_bills': 2940.91,
        'variable_bills': 800,
        'food' : 100,
        'supplements': 200,
        'beauty': 300,
        'needed_misc': 150,
        'optional_misc': 100,
        'business_expenses': None
    }

    # create table for each category
    for category in categories_and_budgets:
        try:
            c.execute(f'''CREATE TABLE IF NOT EXISTS "{category}" (
            item TEXT,
            price FLOAT
            )''')
        except Exception as e:
            print(f'Error creating table for {category}')
            print(e)
    
    # create budgets table
    try:
        c.execute('''CREATE TABLE IF NOT EXISTS "categories_budgets" (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category_name TEXT,
            budgeted_amount FLOAT
            )''')
    except Exception as e:
        print('error creating categories_budgets table')
        print(e)
        sys.exit()

    # insert categories_and_budgets dict into budgets table
    for category, budgeted_amount in categories_and_budgets.items():
        try:
            c.execute('''INSERT INTO categories_budgets (category_name, budgeted_amount)
                        VALUES (?, ?)''', (category, budgeted_amount))
        except Exception as e:
            print(f'Error inserting row for {category} in categories_budgets')
            print(e)
    print(':)')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()