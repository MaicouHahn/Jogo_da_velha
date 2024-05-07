from flask import Flask, render_template, request

app = Flask(__name__)

# Variável para armazenar o estado do tabuleiro
board = [['', '', ''], ['', '', ''], ['', '', '']]
current_player = 'X'

@app.route('/')
def index():
    return render_template('index.html', board=board)

@app.route('/move', methods=['POST'])
def move():
    global current_player
    row = int(request.form['row'])
    col = int(request.form['col'])
    if board[row][col] == '':
        board[row][col] = current_player
        current_player = 'O' if current_player == 'X' else 'X'
        if check_winner() != '':
            reset_board()
    return '', 204

def check_winner():
    for row in board:
        if row[0] == row[1] == row[2] != '':
            return row[0]  # Verifica se há uma linha completa
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '':
            return board[0][col]  # Verifica se há uma coluna completa
    if board[0][0] == board[1][1] == board[2][2] != '':
        return board[0][0]  # Verifica a diagonal principal
    if board[0][2] == board[1][1] == board[2][0] != '':
        return board[0][2]  # Verifica a diagonal secundária
    return ''

def reset_board():
    global board
    board = [['', '', ''], ['', '', ''], ['', '', '']]

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
