from flask import Flask, render_template
import ParseConnect

app = Flask(__name__)

@app.route('/')
def index():
    campaigns = ParseConnect.getAllCampaigns()
    return render_template('index.html', campaigns=campaigns)

@app.route('/stats')
def stats():
    return render_template('stats.html')

@app.route('/campaign/<int:cid>')
def campaign(cid):
    data = ParseConnect.getCampaign(str(cid))
    print data.CampaignName
    return render_template('campaign.html', data=data)

if __name__ == '__main__':
    app.run()
