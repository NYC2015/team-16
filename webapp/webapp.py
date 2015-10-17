from flask import Flask, render_template
import ParseConnect

app = Flask(__name__)

@app.route('/')
def index():
    campaigns = ParseConnect.getAllCampaigns()
    photos = ParseConnect.getPhotos()
    return render_template('index.html', campaigns=campaigns, photos=photos)

@app.route('/stats')
def stats():
    data = ParseConnect.getUserCurve()
    return render_template('stats.html', data=data)

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/campaign/<int:cid>')
def campaign(cid):
    data = ParseConnect.getCampaigns(str(cid))
    photos = ParseConnect.getPhotos1(str(cid))
    return render_template('campaign.html', data=data, photos=photos)

if __name__ == '__main__':

    app.run()
