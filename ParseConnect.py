
import datetime
import csv
from itertools import chain
from parse_rest.connection import register, ParseBatcher
from parse_rest.datatypes import Object as ParseObject

#Keys should be in an encrypted file
APPLICATION_ID = "FOFAbDih2YL3jY6ikLz6LVnhMTybzRrITbDhsqIL"
REST_API_KEY = "REWlCz5BOe7cXJEZaNHcu2g6PgGTeR0hxFrk8GQz"

#User Objects
class User(ParseObject):
    pass
	
class Campaign(ParseObject):
    pass
	
class UsertoCampaign(ParseObject):
    pass
	
class Photos(ParseObject):
    pass

register(APPLICATION_ID, REST_API_KEY)

#Save to Parse
def saveToParse(anyObject):
    anyObject.save()
    print "Done!"

#Add User
def addUser(UserID, Name, Email, HomeAddress, isVolunteer, Occupation):
    user = User(**locals())
    saveToParse(user)
	
#add Campaign
def addCampaign(CampID, CampaignName, StartDate, CampaignURL, DefaultPhoto):
	#if Photo exists, add to Photo
    campaign = Campaign(**locals())
    saveToParse(campaign)

#Find Users
def findUsers(campaignName):
	#campid = Campaign.Query.get(CampaignName=CampaignName).CampID
	userids = UsertoCampaign.Query.all().filter(CampaignID=campaignName)
	users = []
	for userid in userids:
		users = chain(users, User.Query.all().filter(UserID=userid.UserID))
	return users

#Get All Campaigns
def getAllCampaigns():
	return Campaign.Query.all()

#Get Campaign given ID
def getCampaigns(ID):
	return Campaign.Query.get(CampID = ID)

#Get all Photos with corresponding Campaign	
def getCampPhotos(campaignID):
	photoids = UsertoCampaign.Query.all().filter(CampaignID=campaignID)
	photos = []
	
	for photoid in photoids:
		photos = photos + [str(Photos.Query.get(PhotoID=photoid.PhotoID).Photo.url)]	
	return photos
	
#get Photo
def getPhotos():
	photos = {};
	for photo in Photos.Query.all():
		photos[str(photo.PhotoID)] = str(photo.Photo.url)
	return photos
	
#Get Minutes given DateTime Object
def getMinutes(duration):
    seconds = duration.seconds
    minutes = (seconds % 3600) // 60
    return minutes
	
#Users per month
def getUserCurve():
	Time = ["Date Joined"]
	Users = ["Number of Users"]
	Volunteers = ["Number of Volunteers"]
	ArtificialMonth = 3
	
	for user in User.Query.all().order_by("createdAt"):
		#Time = Time + [user.createdAt]
		Time = Time + ["2015-" + str(ArtificialMonth) + "-1"]
		
		count = 0
		for time in User.Query.all():
			if time.createdAt.minute == user.createdAt.minute:
				count = count + 1
		Users = Users + [count]
		
		count = 0
		for time in User.Query.filter(isVolunteer = True):
			if time.createdAt.minute == user.createdAt.minute:
				count = count + 1
		Volunteers = Volunteers + [count]
		ArtificialMonth = ArtificialMonth + 1
	return [Time, Users, Volunteers]
	
print getUserCurve()
	
#Convert User Class data into CSV File
def exportUserExcel(FileLocation):
	#Create CSV File
	csvfile = open(FileLocation, 'wb')
	wr = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
	wr.writerow(["Name","Email" ,"Home Address", "Volunteer" , "Occupation"])
	
	for user in User.Query.all():
		wr.writerow([user.Name,user.Email ,user.HomeAddress ,user.isVolunteer , user.Occupation])
		
	return FileLocation

#Return number of users per campaign
def campaignUserStat():
	campaigns = Campaign.Query.all()
	numUsers = []
	for campaign in campaigns:
		numUsers = numUsers + [[str(campaign.CampaignName), len(list(UsertoCampaign.Query.all().filter(CampaignID = campaign.CampID)))]]

	return numUsers
	
print campaignUserStat()


#addUser("1", "Test", "email", "address", True ,"Lawyer")
#addCampaign("3", "TestCamp", datetime.datetime(2011, 9, 16, 21, 51, 36, 784000) , "URL" ,"4")
