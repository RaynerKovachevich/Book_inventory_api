import sqlite3

def create_database():
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            year INTEGER NOT NULL
            )           
        ''')
    
    conn.commit()
    conn.close()
    
if __name__ == "__main__":
    create_database()    