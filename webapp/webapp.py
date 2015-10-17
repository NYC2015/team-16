from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stats')
def stats():
    return render_template('stats.html')

@app.route('/campaign/<int:cid>')
def campaign(cid):
    return render_template('campaign.html')


if __name__ == '__main__':
    app.run()
