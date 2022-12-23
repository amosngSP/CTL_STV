import pyrankvote
from pyrankvote import Candidate, Ballot

airports_dict={
    11 : Candidate("HESH"),
    12 : Candidate("OBBI"),
    13 : Candidate("OEJN"),
    14 : Candidate("OIIE"),
    15 : Candidate("OOMS"),
    30 : Candidate("OJAI"),
    16 : Candidate("EDDF"),
    17 : Candidate("EHAM"),
    18 : Candidate("EKCH"),
    19 : Candidate("LPPT"),
    29 : Candidate("LOWW"),
    20 : Candidate("LTFM"),
    21 : Candidate("UUEE"),
    22 : Candidate("LEBL"),
    23 : Candidate("ENBR"),
    24 : Candidate("LHBP"),
    25 : Candidate("LIRN"),
    26 : Candidate("LBSF"),
    27 : Candidate("EVRA"),
    28 : Candidate("GMMN"),
    }

airports_mena = [airports_dict[11],airports_dict[12],airports_dict[13],airports_dict[14],airports_dict[15],airports_dict[30]]
airports_eu_a = [airports_dict[16],airports_dict[17],airports_dict[18],airports_dict[19],airports_dict[29]]
airports_eu_b = [airports_dict[20],airports_dict[21],airports_dict[22],airports_dict[23]]
airports_eu_c = [airports_dict[24],airports_dict[25],airports_dict[26],airports_dict[27],airports_dict[28]]


ballots = []

files = ["departure_airports.csv","arrival_airports_a.csv","arrival_airports_b.csv","arrival_airports_c.csv"]

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

result_mena = pyrankvote.single_transferable_vote(airports_mena, ballots[0], number_of_seats=5)
result_eud_a = pyrankvote.single_transferable_vote(airports_eu_a, ballots[1], number_of_seats=2)
result_eud_b = pyrankvote.single_transferable_vote(airports_eu_b, ballots[2], number_of_seats=3)
result_eud_c = pyrankvote.single_transferable_vote(airports_eu_c, ballots[3], number_of_seats=2)

print("==========================EUD CAT A==========================")
print(result_eud_a)
print("==========================EUD CAT B==========================")
print(result_eud_b)
print("==========================EUD CAT C==========================")
print(result_eud_c)
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
