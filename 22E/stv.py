import pyrankvote
from pyrankvote import Candidate, Ballot

airports_dict={
    1 : Candidate("HECA"),
    2 : Candidate("OERK"),
    3 : Candidate("OIIE"),
    4 : Candidate("OOMS"),
    5 : Candidate("OTHH"),
    6 : Candidate("LTFM"),
    7 : Candidate("LEMD"),
    8 : Candidate("ULLI"),
    9 : Candidate("LFMN"),
    10 : Candidate("EFHK"),
    11 : Candidate("LKPR"),
    12 : Candidate("LHBP"),
    13 : Candidate("LROP"),
    14 : Candidate("EDDV"),
    15 : Candidate("ELLX"),
    16 : Candidate("LOWS"),
    17 : Candidate("LIML"),
    18 : Candidate("LZIB"),
    19 : Candidate("GMMN"),
    }

airports_eu_large = [airports_dict[6],airports_dict[7],airports_dict[8],airports_dict[9]]
airports_eu_medium = [airports_dict[10],airports_dict[11],airports_dict[12],airports_dict[13],airports_dict[14],airports_dict[19]]
airports_eu_small = [airports_dict[15],airports_dict[16],airports_dict[17],airports_dict[18]]
airports_mena = [airports_dict[1],airports_dict[2],airports_dict[3],airports_dict[4],airports_dict[5]]

ballots = []

ballots_eu_large = []
ballots_eu_medium = []
ballots_eu_small = []
ballots_mena = []

files = ["arrival_airports.csv","departure_large.csv","departure_medium.csv","departure_small.csv"]

i = 1

for file in files:
    f = open(file,"r")
    lines = f.readlines()[1:]
    f.close()
    temp_ballots = []
    for x in lines:
        temp=[]
        x = x.strip()
        x = x.split(",")[1:]
        for y in x:
            temp.append(airports_dict[int(y)])
        temp_ballots.append(Ballot(ranked_candidates=temp))
    ballots.append(temp_ballots)
    
result_eud_large = pyrankvote.single_transferable_vote(airports_eu_large, ballots[1], number_of_seats=2)
result_eud_medium = pyrankvote.single_transferable_vote(airports_eu_medium, ballots[2], number_of_seats=2)
result_eud_small = pyrankvote.single_transferable_vote(airports_eu_small, ballots[3], number_of_seats=2)
result_mena = pyrankvote.single_transferable_vote(airports_mena, ballots[0], number_of_seats=4)
print("==========================EUD LARGE==========================")
print(result_eud_large)
print("=========================EUD  MEDIUM=========================")
print(result_eud_medium)
print("==========================EUD SMALL==========================")
print(result_eud_small)
print("=============================MENA============================")
print(result_mena)
##for x in lines:
##    temp = []
##    x = x.strip()
##    x = x.split(",")
##    for y in x:
##        if y == "1":
##            temp.append(one)
##        elif y == "2":
##            temp.append(two)
##        elif y == "3":
##            temp.append(three)
##        elif y == "4":
##            temp.append(four)
##    ballots.append(Ballot(ranked_candidates=temp))

#election_result = pyrankvote.single_transferable_vote(candidates, ballots, number_of_seats=2)
#print(election_result)
