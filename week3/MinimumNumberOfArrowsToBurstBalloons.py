class Solution: 
    '''
   1---b---6  7--b---12
    2----b-----8
                 10-----b------16
                 
interval limit = 10 
7 not in limit, 12 is in limit  
2 not in limit, 8 not in limit, limit is now 2 
1 not in limit, 6 in limit 

add count when no interval and new balloon is created as interval 
    '''
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(reverse=True)
        count = 0 
        interval = ""
        for balloon in points:
            if interval == "":
                interval = balloon[0]
                count+=1
            else:
                if balloon[0] >= interval or balloon[1]>= interval:
                    pass
                else:
                    interval = balloon[0]
                    count+=1
        return count
        