#let user input the value of richter
input_richter=input("Please input a Richter scale value: ")
#let the form of richter into float
richter=float(input_richter)
#caculate energy
energy=10**((1.5*richter)+4.8)
# input the value of TNT and lunch
TNT=4.184*(10**9)
Lunch=2930200
# caculate energy to lunch and TNT
equiLunch=energy/Lunch
equiTNT=energy/TNT
#print the result
print("Richter scale value: ",richter)
print("Equivalence in Joules: ",energy)
print("Equivalence in tons of TNT: ",equiTNT)
print("Equivalence in the number of nutritious lunches: "
	,equiLunch)

