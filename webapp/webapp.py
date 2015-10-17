from flask import Flask, render_template
from PIL import Image
import ParseConnect

app = Flask(__name__)

@app.route('/')
def index():
    campaigns = ParseConnect.getAllCampaigns()
    #photos = ParseConnect.getPhotos()
    path = "../static/images/"
    return render_template('index.html', campaigns=campaigns, path=path, photos="banner.jpg")

@app.route('/stats')
def stats():
    return render_template('stats.html')

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/campaign/<int:cid>')
def campaign(cid):
    data = ParseConnect.getCampaigns(str(cid))
    print data.CampaignName
    return render_template('campaign.html', data=data)

if __name__ == '__main__':

    app.run()
