from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('books.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/books', methods=['GET'])
def get_books():
    conn = get_db_connection()
    books = conn.execute('SELECT * FROM books').fetchall()
    conn.close()
    return jsonify([dict(book) for book in books])

@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.get_json()
    conn = get_db_connection()
    conn.execute('INSERT INTO books (title, author, year) VALUES (?,?,?)',  (new_book['title'], new_book['author'], new_book['year']))
    
    conn.commit()
    conn.close()
    return jsonify(new_book), 201

@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id): 
    update_book = request.get_json()
    conn = get_db_connection()
    conn.execute('UPDATE books SET title = ?, author = ?, year = ? WHERE id = ?', (update_book['title'], update_book['author'], update_book['year'], id))
    
    conn.commit()
    conn.close()
    return jsonify(update_book)

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM books WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return'', 204

if __name__ == '__main__':
    app.run(debug=True)