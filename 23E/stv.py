import pyrankvote
from pyrankvote import Candidate, Ballot

airports_dict={
    31 : Candidate("OEJN"),
    32 : Candidate("OMDB"),
    33 : Candidate("OLBA"),
    34 : Candidate("OIIE"),
    35 : Candidate("OJAI"),
    36 : Candidate("HEGN"),
    37 : Candidate("EHAM"),
    38 : Candidate("LTFM"),
    39 : Candidate("UUEE"),
    40 : Candidate("LOWW"),
    41 : Candidate("ESGG"),
    42 : Candidate("LFMN"),
    43 : Candidate("EDDB"),
    44 : Candidate("UKBB"),
    45 : Candidate("GCTS"),
    46 : Candidate("LBSF"),
    47 : Candidate("LIRN"),
    48 : Candidate("LJLJ"),
    }

airports_mena = [airports_dict[31],airports_dict[32],airports_dict[33],airports_dict[34],airports_dict[35],airports_dict[36]]
airports_eu_a = [airports_dict[37],airports_dict[38],airports_dict[39],airports_dict[40]]
airports_eu_b = [airports_dict[41],airports_dict[42],airports_dict[43],airports_dict[44]]
airports_eu_c = [airports_dict[45],airports_dict[46],airports_dict[47],airports_dict[48]]


ballots = []

files = ["MENA.csv","DEP_A.csv","DEP_B.csv","DEP_C.csv"]

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
result_eud_b = pyrankvote.single_transferable_vote(airports_eu_b, ballots[2], number_of_seats=2)
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
