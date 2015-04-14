#Slope One Demo
#Comp541 - Group 2

def buildAverageDiffs(items, users, averages, writeToCache=True):
    for itemId in items:
        for otherItemId in items:
            average = 0
            userRatingPairCount = 0
            if itemId != otherItemId:
                for userId in users:
                    userRatings = users[userId]
                    if itemId in userRatings and otherItemId in userRatings:
                        userRatingPairCount += 1
                        average += (userRatings[itemId] - userRatings[otherItemId])
                averages[(itemId,otherItemId)] = average / userRatingPairCount

def suggestedRating(users, items, averages, targetUserId, targetItemId):
    runningRatingCount = 0
    weightedRatingTotal = 0.0
    for i in users[targetUserId]:
        ratingCount = usersWhoRatedBoth(users, i, targetItemId)
        weightedRatingTotal += (users[targetUserId][i] + averages[(targetItemId, i)]) * ratingCount
        runningRatingCount += ratingCount
    return weightedRatingTotal / runningRatingCount

def usersWhoRatedBoth(users, itemId1, itemId2):
    count = 0
    for userId in users:
        if itemId1 in users[userId] and itemId2 in users[userId]:
            count += 1
    return count

#-----------------------------------MAIN---------------------------------------
users = {1: {'A':5, 'B':3, 'C':2},
         2: {'A':3, 'B':4},
         3: {'B':2, 'C':5}}
items = {'A': {1:5, 2:3},
         'B': {1:3, 2:4, 3:2},
         'C': {1:2, 3:5}}
averages = {}

buildAverageDiffs(items, users, averages)

print({'ItemCount': len(items), 'UserCount': len(users), 'AverageDiffsCount': len(averages)} )
print(averages)
print("Guess that user A will rate item 3= " + str(suggestedRating(users,items, averages, 3, 'A')))




