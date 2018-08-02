import scoreboard as sc
import resultsEvaluation as re


h = sc.setWindow()
q = re.addResults(h[0],h[1])
currentRace = h[2][2]
Redhouse,Bluehouse,Greenhouse,Yellowhouse = q[0],q[1],q[2],q[3]
Name1,House1,Grade1,Section1 = h[2][0],h[2][3],h[2][4],h[2][5]
Name2,House2,Grade2,Section2 = h[3][0],h[3][3],h[3][4],h[3][5]
Name3,House3,Grade3,Section3 = h[4][0],h[4][3],h[4][4],h[4][5]
Name4,House4,Grade4,Section4 = h[5][0],h[5][3],h[5][4],h[5][5]
print(" Fixtures")
print()
print(" Redhouse: " + str(Redhouse))
print(" Bluehouse: " + str(Bluehouse))
print(" Greenhouse: " + str(Greenhouse))
print(" Yellowhouse: " + str(Yellowhouse))
print(" -----------------")
print(" Results of the current race")
print()
print(" Race - " + currentRace + " for grade " + Grade1 )
print()
print(" 1st: " + Name1 + "\n House: " + House1 + "\n Class: " + Grade1 + Section1)
print()
print(" 2nd: " + Name2 + "\n House: " + House2 + "\n Class: " + Grade2 + Section2)
print()
print(" 3rd: " + Name3 + "\n House: " + House3 + "\n Class: " + Grade3 + Section3)
print()
print(" 4th: " + Name4 + "\n House: " + House4 + "\n Class: " + Grade4 + Section4)
print()

re.update(q)
