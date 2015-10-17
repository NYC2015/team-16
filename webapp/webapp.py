from flask import Flask, render_template
from PIL import Image
import ParseConnect

app = Flask(__name__)

def convert_keys_to_string(dictionary):
    """Recursively converts dictionary keys to strings."""
    if not isinstance(dictionary, dict):
        return dictionary
    return dict((str(k), convert_keys_to_string(v))
        for k, v in dictionary.items())

@app.route('/')
def index():
    campaigns = ParseConnect.getAllCampaigns()
    photos = ParseConnect.getPhotos()
    #photos =  convert_keys_to_string(photos)
    print photos
    return render_template('index.html', campaigns=campaigns, photos=photos)

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
