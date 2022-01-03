# CTL_STV
VATSIM Cross The Land - Single Transferable Vote system.
By Amos Ng - 1357854 for VATSIM Cross The Land

The web interface was based on the Buy me a Cookie system:
https://github.com/daveroverts/bmac

This system does not originally come with a voting system inside of it, that part was done from scratch by me.
You can view the fork I made here:
https://github.com/amosngSP/bmac

There are 3 tables used by the voting system:
poll - This is basically the main table that contains the poll name, and the poll description, and the visibility of the poll.
poll_choices - This contains the different poll choices for each poll
votes - This basically contains the votes that each user that casted.

Here are what the tables look like when populated:

![image](https://user-images.githubusercontent.com/40349656/147948719-ba905617-8ec9-4de0-95c1-6662cb48a3e6.png)
![image](https://user-images.githubusercontent.com/40349656/147948751-12c1d8f2-e07b-4039-8691-bbb43e808624.png)
![image](https://user-images.githubusercontent.com/40349656/147948824-c09d5d2f-b575-44e4-98a0-db5d55630ef2.png)

This is the query that is used to extract out the data from mysql. Results were converted to csv files through MySQL Workbench. This is for the poll with id 1. Then I repeated the process for the other 3 polls. 
```
SELECT DISTINCT z.user_id, a.vote_id as "First", b.vote_id as "Second", c.vote_id as "Third" FROM votes z, votes a, votes b, votes c where z.poll_id=1 and a.poll_id=1 and b.poll_id=1 and c.poll_id=1 and z.user_id=a.user_id and z.user_id=b.user_id and z.user_id=c.user_id and a.order=0 and b.order=1 and c.order=2;
```

From there, I used the python module called [pyrankvote](https://github.com/jontingvold/pyrankvote) to tabulate the results.
I then made a python script (filename is stv.py) that reads through each csv file, and organises the data for the module to use.
Thereafter the module calculates the results and shows it to us, as below:
```
==========================EUD LARGE==========================
ROUND 1
Candidate      Votes  Status
-----------  -------  --------
EDDM             230  Hopeful
LFPG             213  Hopeful
LOWW             192  Hopeful
LTFM             114  Rejected

ROUND 2
Candidate      Votes  Status
-----------  -------  --------
EDDM             262  Elected
LOWW             248  Hopeful
LFPG             239  Hopeful
LTFM               0  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
EDDM          249.67  Elected
LOWW          257.37  Elected
LFPG          241.97  Rejected
LTFM            0.00  Rejected

=========================EUD  MEDIUM=========================
ROUND 1
Candidate      Votes  Status
-----------  -------  --------
EBBR             178  Hopeful
LSGG             172  Hopeful
ENGM             157  Hopeful
EPWA             114  Hopeful
LPPT             110  Rejected

ROUND 2
Candidate      Votes  Status
-----------  -------  --------
LSGG             212  Hopeful
EBBR             206  Hopeful
ENGM             186  Hopeful
EPWA             127  Rejected
LPPT               0  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
EBBR             250  Elected
LSGG             246  Elected
ENGM             235  Rejected
EPWA               0  Rejected
LPPT               0  Rejected

==========================EUD SMALL==========================
ROUND 1
Candidate      Votes  Status
-----------  -------  --------
LEMG             168  Hopeful
EVRA             117  Hopeful
EETN             117  Hopeful
LIPE              94  Hopeful
LROP              90  Hopeful
LBSF              76  Hopeful
LZIB              65  Rejected

ROUND 2
Candidate      Votes  Status
-----------  -------  --------
LEMG             178  Hopeful
EVRA             133  Hopeful
EETN             123  Hopeful
LROP             105  Hopeful
LIPE             102  Hopeful
LBSF              86  Rejected
LZIB               0  Rejected

ROUND 3
Candidate      Votes  Status
-----------  -------  --------
LEMG             191  Hopeful
EVRA             154  Hopeful
LROP             143  Hopeful
EETN             129  Hopeful
LIPE             110  Rejected
LBSF               0  Rejected
LZIB               0  Rejected

ROUND 4
Candidate      Votes  Status
-----------  -------  --------
LEMG             240  Hopeful
EVRA             181  Hopeful
LROP             158  Hopeful
EETN             139  Rejected
LIPE               0  Rejected
LBSF               0  Rejected
LZIB               0  Rejected
Blank votes        9  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
LEMG             268  Elected
EVRA             265  Elected
LROP             170  Rejected
EETN               0  Rejected
LIPE               0  Rejected
LBSF               0  Rejected
LZIB               0  Rejected
Blank votes       24  Rejected

=============================MENA============================
ROUND 1
Candidate      Votes  Status
-----------  -------  --------
OMDB             466  Elected
HESH              97  Hopeful
OJAI              52  Hopeful
OKBK              50  Hopeful
OEJN              39  Hopeful
OIIE              39  Hopeful

ROUND 2
Candidate      Votes  Status
-----------  -------  --------
OMDB          123.83  Elected
OKBK          190.98  Elected
HESH          171.16  Elected
OJAI           93.85  Hopeful
OEJN           90.40  Hopeful
OIIE           72.78  Hopeful

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
OMDB          123.83  Elected
OKBK          123.83  Elected
HESH          123.83  Elected
OJAI          121.15  Elected
OEJN          113.56  Elected
OIIE           89.50  Rejected
Blank votes    47.30  Rejected
```
Number of votes casted:
```
VATEUD Large: 749
VATEUD Medium: 731
VATEUD Small: 727
VATMENA: 743
```
