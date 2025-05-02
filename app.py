from flask import Flask, request, render_template, redirect
from blockchain import Blockchain

app = Flask(__name__)
blockchain = Blockchain()

@app.route('/')
def index():
    chain = blockchain.get_chain()
    return render_template('index.html', chain=chain)

@app.route('/add', methods=['POST'])
def add_block():
    product = request.form['product']
    location = request.form['location']
    actor = request.form['actor']
    blockchain.create_block(product, location, actor)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
