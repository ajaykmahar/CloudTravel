"""
Constraints
 • latitude, longitude, and canTravel will contain between 1 and 20 elements, inclusive.
 •latitude, longitude, and canTravel will each contain the same number of elements.
 •Each element of latitude will be between -89 and 89, inclusive.
 •Each element of longitude will be between -179 and 179, inclusive.
 •Each element of canTravel will be a space-delimited list of integers, with no leading zeroes.

•Each integer represented in each element of canTravel will be between 0 and n - 1, where n is the number of elements in latitude.
•origin and destination will be between 0 and n - 1, inclusive, where n is the number of elements in latitude.
•No two airports will reside at the same latitude and longitude.

 Examples
  0)
    {0, 0, 70}
    {90, 0, 45}
    {"2", "0 2", "0 1"}
    0
    1
    Returns: 10612.237799994255
    Here, we are looking to travel from airport 0 to airport 1.
    Using the given formula, we calculate that the distance from 0 to 1 is 6283, from 0 to 2 is 5306, and from 1 to 2 is 5306.
    A direct route from airport 0 to 1 would be fastest, if such a route were allowed.
    Since it is not, we have to travel through airport 2.
  
   1)
    {0, 0, 70}
    {90, 0, 45}
    {"1 2", "0 2", "0 1"}
    0
    1
    Returns: 6283.185307179586
    Here, we have the same three airports, and there is a safe route between any two.
    Thus, we take the direct route, which is quickest.
    
    2)
     {0, 30, 60}
     {25, -130, 78}
     {"1 2", "0 2", "1 2"}
     0 
     0
     Returns: 0.0
     We are free to travel as we wish, but since our destination is the same as our point of origin,
     we don't have much travel to do.
     
     3)
     {0, 20, 55}
     {-20, 85, 42}
     {"1", "0", "0"}
     0
     2
     Returns:
     Notice here that we could go from airport 2 to airport 0, but not from 0 to 2.
     Given the available routes, there is no way we can get from airport 0 to airpor
"""

import Solution.CloudTravel as cloud

list_of_latitude = [
                    (0, 0, 70),
                    (0, 0, 70),
                    (0, 30, 60),
                    (0, 20, 55),
                    ]
lsit_of_longitude = [
                    (90, 0, 45),
                    (90, 0, 45),
                    (25, -130, 78),
                    (-20, 85, 42),
                    ]
list_of_canTravel = [
                    ("2", "0 2", "0 1"),
                    ("1 2", "0 2", "0 1"),
                    ("1 2", "0 2", "1 2"),
                    ("1", "0", "0"),
                    ]
list_of_origin = [0, 0, 0, 0, ]
list_of_destination = [1, 1, 0, 2]
expected_output = [
                    10612.237799994255,
                    6283.185307179585,
                    0.0,
                    5306.118899997127,
                    ]

obj = cloud.CloudTravel()


def test_shortestTrip():
    for index in range(len(list_of_latitude) - 1):
        assert obj.shortestTrip(list_of_latitude[index], lsit_of_longitude[index], list_of_canTravel[index],list_of_origin[index], list_of_destination[index]) == expected_output[index]
