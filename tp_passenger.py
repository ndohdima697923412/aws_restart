import copy

passenger = {
 "id_passenger" : 0,
 "name" : "<empty>",
 "weigth" : 0.0
}

bus ={
 "id_bus" : 0,
 "number_places" : 0,
 "passage" : []
}

buses=[]

def create_bus():
 idBus=input("Entrer le matricule de votre bus : ")
 numberPlaces=input("Entrer le nombre de place : ")
 newBus=copy.deepcopy(bus)
 newBus["id_bus"]=idBus
 newBus["number_places"]=numberPlaces
 buses.append(newBus)
 print(buses)
 
def create_passenger():
  idPassenger=int(input("Entrer l'identifiant du passager : "))
  name=input("Entrer le nom du passager : ")
  weigth=input("Entrer le poids des bagages du passager : ")
  newPassenger=copy.deepcopy(passenger)
  newPassenger["id_passenger"]=idPassenger
  newPassenger["name"]=name
  newPassenger["weigth"]=weigth
  idBusForPassenger=input("Ajouter le passager a un bus specifique, Veillez preciser a quel bus ce passager est il lié (entrer le matricule du bus: ")
  for bus in buses:
   for key, value in bus.items():
    if key=="id_bus" and value==int(idBusForPassenger):
     if key=="passage"
     bus[key]=newPassenger
  print(bus)
  print(buses)

def check_available_places():
 checkBus=input("Entrer l'identifiant du bus dont on vous voulez verifier la disponibilité des places : ")
 for bus in buses:
  for key, value in bus:
   if key=="id_bus" and value==checkBus:
    available=bus["number_places"]-len(bus["passage"])
    if available>0:
     print(f'il ya encore {available} places disponibles')
    else:
     print("Il y'a plus de places disponible dans ce bus")
 
def check_kg_bus():
 print("connaitre les reservations de kg pour le bus")
 idBusForReserveKg=input("Entrer l'identifiant du Bus dont vous voulez connaitre la capacite en Kg reservee : ")
 for bus in buses:
  for key, value in bus:
   if key=="id_bus" and value==idBusForReserveKg:
    for passage in bus["passage"]:
     reserveKg+=passage["weigth"]
 return reserveKg
  
def remove_passager():
 idBusForRemovePassager=input("Specifiez l'identifiant du bus dans lequel le passager doit être retiré : ")
 idPassageToRemove=input("Spécifiez l'identifiant du passager a retirer : ")
 for bus in buses:
  for key, value in bus:
   if key=="id_bus" and value==idBusForRemovePassager:
    i=0;
    for passage in bus["passage"]:
     if passage["id_passanger"]==idPassageToRemove:
      del passage[i]
     i+=1

create_bus()
create_passenger()
