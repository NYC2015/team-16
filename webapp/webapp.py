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
    ParseConnect.exportUserExcel('/Users/Alan/Desktop/rocktheearth/webapp/static/data.csv')
    campdata = ParseConnect.campaignUserStat()
    return render_template('stats.html', data=data, campdata=campdata)

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/campaign/<int:cid>')
def campaign(cid):
    data = ParseConnect.getCampaigns(str(cid))
    photos = ParseConnect.getCampPhotos(str(cid))
    photo = ParseConnect.getCampaignPhoto(str(cid))
    return render_template('campaign.html', data=data, photo=photo, photos=photos)

if __name__ == '__main__':
    app.run()
