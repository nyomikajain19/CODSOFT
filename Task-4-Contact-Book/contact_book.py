contacts = {}
print("\n Personal Contact Book")
while True:
  print("\nMenu: 1-Add 2-View 3-Search 4-Delete 5-Exit")
  choice = input(" Enter choice: ")
  if choice == "1":
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    contacts[name] = {"phone": phone, "email": email}
    print(" Contact Saved!")
  elif choice == "2":
    if not contacts:
      print(" No contacts found!")
    else:
      print("\nYour Contacts:")
      for name, info in contacts.items():
        print(f"{name} -> {info['phone']} | {info['email']}")
  elif choice == "3":
    name = input("Search name: ")
    if name in contacts:
      info = contacts[name]
      print(f"Found: {info['phone']} | {info['email']}")
    else:
      print(" Not in list!")
  elif choice == "4":
    name = input("Delete which name? ")
    if name in contacts:
      del contacts[name]
      print(" Deleted!")
    else:
      print(" Contact not found!")
  elif choice == "5":
    print(" Goodbye!")
    break
  else:
    print(" Wrong input")
      
    
