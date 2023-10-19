class UndergroundSystem(object):

    def __init__(self):

        self.time_list = {}
        self.check_in = {}


    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.check_in[id] = [stationName, t]


    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        start_station = self.check_in[id][0]
        start_time = self.check_in[id][1]

        trip = start_station + '>' + stationName
        if not self.time_list.has_key(trip):
            self.time_list[trip] = []
        self.time_list[trip].append(t - start_time)


    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        trip = startStation + '>' + endStation
        if self.time_list.has_key(trip):
            return float(sum(self.time_list[trip])) / len(self.time_list[trip])


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)