#Program To Calculate Amount Of Particular Blood Type Taken As Input(Litres)
def blood_bank(litres,bloodtype):
  #conversion of bloodtype from litres to mililitres
    mililitres=litres*1000
  #dictionary
    charges={"O-ve":98,"O+ve":127,"A+ve":82,"A-ve":176,"B+ve":176,"B-ve":241,"AB+ve":241,"AB-ve":280}
    charge_ml=charges[bloodtype]
  #formula to calculate amount charged per litre
    total_amount=mililitres*(charge_ml/1000)
  #conditional statements
    if bloodtype=="O-ve":
       print(f"Amount to be Paid is Rs. {total_amount} for {litres} litres.")
    elif bloodtype=="O+ve":
      print(f"Amount to be Paid is Rs. {total_amount} for {litres} litres.")
    elif bloodtype=="A+ve":
      print(f"Amount to be Paid is Rs. {total_amount} for {litres} litres.")
    elif bloodtype=="A-ve": 
      print(f"Amount to be Paid is Rs. {total_amount} for {litres} litres.")
    elif bloodtype=="B+ve":
     print(f"Amount to be Paid is Rs. {total_amount} for {litres} litres.")
    elif bloodtype=="B-ve":
      print(f"Amount to be Paid is Rs. {total_amount} for {litres} litres.") 
    elif bloodtype=="AB+ve":
      print(f"Amount to be Paid is Rs. {total_amount} for {litres} litres.")
    elif bloodtype=="AB-ve":
      print(f"Amount to be Paid is Rs. {total_amount} for {litres} litres.")
try:
    litres=float(input("Enter the Blood Group in Litres:"))
    bloodtype=input("Enter the blood type(format AB+ve or AB-ve:):")
    #function call
    blood_bank(litres,bloodtype)
except ValueError:
    print("Enter the Litres in Numeric Form!")

        
        
    