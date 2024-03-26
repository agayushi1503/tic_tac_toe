
from flask import Flask, request, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tictactoe.db'
app.config['SECRET_KEY'] = 'secretkey'
db = SQLAlchemy(app)

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    board = db.Column(db.String(9))
    winner = db.Column(db.String(1))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_move', methods=['POST'])
def process_move():
    move = request.form['move']
    game = Game.query.first()
    board = game.board
    if board[int(move)] == '-':
        if game.winner == '-':
            if game.turn == 'X':
                board = board[:int(move)] + 'X' + board[int(move)+1:]
                game.turn = 'O'
            else:
                board = board[:int(move)] + 'O' + board[int(move)+1:]
                game.turn = 'X'
            game.board = board
            db.session.commit()
            flash('Move successful')
        else:
            flash('Game over')
    else:
        flash('Invalid move')
    return redirect(url_for('index'))

if __name__ == '__main__':
    db.create_all()
    game = Game(board='---------', winner='-', turn='X')
    db.session.add(game)
    db.session.commit()
    app.run(debug=True)
