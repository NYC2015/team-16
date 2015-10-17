import datetime
from itertools import chain
from parse_rest.connection import register, ParseBatcher
# Alias the Object type to make clear is not a normal python Object
from parse_rest.datatypes import Object as ParseObject

APPLICATION_ID = "FOFAbDih2YL3jY6ikLz6LVnhMTybzRrITbDhsqIL"
REST_API_KEY = "REWlCz5BOe7cXJEZaNHcu2g6PgGTeR0hxFrk8GQz"

#Keys

class User(ParseObject):
    pass
	
class Campaign(ParseObject):
    pass
	
class UsertoCampaign(ParseObject):
    pass
	
class Photos(ParseObject):
    pass

register(APPLICATION_ID, REST_API_KEY)

def saveToParse(anyObject):
    anyObject.save()
    print "Done!"

def addUser(UserID, Name, Email, HomeAddress, isVolunteer, Occupation):
    user = User(**locals())
    saveToParse(user)
	
#add Campaign
def addCampaign(CampID, CampaignName, StartDate, CampaignURL, DefaultPhoto):
	#if Photo exists, add to Photo
    campaign = Campaign(**locals())
    saveToParse(campaign)

#find users
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

#Get Campaign
def getCampaigns(ID):
	return Campaign.Query.get(CampID = ID)
	
#print getCampaigns("2")

#getPhotos	
def getPhotosOld(campaignID):
	#campid = Campaign.Query.get(CampaignName=CampaignName).CampID
	photoids = UsertoCampaign.Query.all().filter(CampaignID=campaignID)
	photos = []
	
	for photoid in photoids:
		photos = chain(photos, Photos.Query.all().filter(PhotoID=photoid.PhotoID))
		
	return photos
	
#get Photo
def getPhotos():
	photos = {};
	for photo in Photos.Query.all():
		photos[str(photo.PhotoID)] = str(photo.Photo.url)
        #print photo.PhotoID
	return photos
	
def getMinutes(duration):
    seconds = duration.seconds
    minutes = (seconds % 3600) // 60
    return minutes
	
#Return
def getUserCurve():
	Time = ["Date Joined"]
	Users = ["Number of Users"]
	Volunteers = ["Number of Volunteers"]
	for user in User.Query.all().order_by("createdAt"):
		Time = Time + [user.createdAt]
		
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
	return [Time, Users, Volunteers]
	
#print getUserCurve()
	
#print(getPhotos()["1"])
	

	
#for photo in getPhotos("TestCamp"):
#	print(photo.Photo)
	
#count

#addUser("1", "Test", "email", "address", True ,"Lawyer")
#addCampaign("3", "TestCamp", datetime.datetime(2011, 9, 16, 21, 51, 36, 784000) , "URL" ,"4")
