from math import radians, cos, sin, asin, sqrt


class CloudTravel:
    # Declaring const variable 
    RADIUS = 4000
    MAXINT = 9223372036854775807
    # Initializing private data
    
    def __init__(self):
        self.listOfDistances = [[__class__.MAXINT for i in range(3)] for j in range(3)]  # will contain list of list distances

    def distance(self, latitude1, longitude1, latitude2, longitude2):
        # ========STARTING Calculating travling distance==============
        # convert degrees to radians for every longitude and latitude
        # convert decimal degrees to radians 
        longitude1, latitude1, longitude2, latitude2 = map(radians, [longitude1, latitude1, longitude2, latitude2])

        # =====DEBUGGING==================
        # ======END=======================

        # haversine formula 
        dlon = longitude2 - longitude1 
        dlat = latitude2 - latitude1
        a = sin(dlat/2)**2 + cos(latitude1) * cos(latitude2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a)) 
        # Radius of earth in miles
        return __class__.RADIUS * c
        # ========END OF Calculating travling distance==============

    #Calculate the great circle distance between two points on the earth.   
    def shortestTrip(self, latitude, longitude, canTravel, origin, destination):
       
        # Can't be destination is the same as our point of origin
        if origin == destination:
           return 0.0

        for index in range(len(canTravel)):
            # =====DEBUGGING==================
            # print(int(canTravel[index].replace(" ", "")))
            # ======END=======================
            dest = int(canTravel[index].replace(" ", "")) # getting canTravel from tuple and parsing it to int
            if dest >= 10: # checking if it's two digit number
                while (dest > 0):
                    dest = dest //10 # Calculating distance digit by digit
                    self.listOfDistances[index][dest] = self.distance(latitude[index], longitude[index], latitude[dest], longitude[dest])
            else:
                # Else dest is single digit then simply calculate the distance
                self.listOfDistances[index][dest] = self.distance(latitude[index], longitude[index], latitude[dest], longitude[dest])
        
        # Finding minimum distance for all the available path based on traveling time
        for i in range(len(latitude)):
            for j in range(len(latitude)):
                for k in range(len(latitude)):
                    self.listOfDistances[j][k] = min(self.listOfDistances[j][k], self.listOfDistances[j][i] + self.listOfDistances[i][k])
        
        return self.listOfDistances[origin][destination]
        
if __name__ == '__main__':
    pass