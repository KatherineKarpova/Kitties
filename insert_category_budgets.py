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
        'business_expenses': None,
        'app_subscriptions': 100
    }

    # create table for categories
    try:
        c.execute('''CREATE TABLE IF NOT EXISTS categories (
                  id INTEGER PRIMARY KEY,
                  category_name TEXT
                  )''')
    except Exception as e:
        print(e)
        sys.exit()
    
    # create budgets table
    try:
        c.execute('''CREATE TABLE IF NOT EXISTS budgets (
            category_id INTEGER,
            budgeted_amount FLOAT,
            FOREIGN KEY (category_id) REFERENCES categories(id)
            )''')
    except Exception as e:
        print(e)
        sys.exit()

    category_id = 1
    # insert categories_and_budgets dict into budgets table
    for category, budgeted_amount in categories_and_budgets.items():
        try:
            # create table for each category
            c.execute(f'''CREATE TABLE IF NOT EXISTS "{category}" (
            item TEXT,
            price FLOAT
            )''')
            # insert each category as a row in categories table
            c.execute('''INSERT INTO categories (id, category_name) VALUES (?, ?)''', (category_id, category,))
            # insert categories_and_budgets dict into budgets table with category as id num
            c.execute('''INSERT INTO budgets (category_id, budgeted_amount)
                        VALUES (?, ?)''', (category_id, budgeted_amount,))
            category_id += 1
        except Exception as e:
            print(e)
            sys.exit()
    print(':)')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()