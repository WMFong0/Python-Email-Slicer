# no import required

while True:
  email = input("Input the email address you wanna slice. Leave Blank to exit.\nEmail Address: ")
  if(email == "" or email.lower() == "exit"):
    print(f"Exit!")
    break

  slice_index = email.find("@")
  if (slice_index == -1):
    print(f"Incorrect Email format")

  username = email[ : slice_index]
  domain = email[slice_index + 1 : ]

  print(f"Username: {username} \nDomain Name: {domain}\n")

  Analysis_bool = input("Would you like a simplified analysis? (y/n): ")

  if (Analysis_bool.lower()) == 'y':
    print(f"{username}'s email is registered with {domain}.")

    if domain.lower() in ["gmail.com", "yahoo.com", "outlook.com"]:
      print("This looks like a personal email account.")

    elif domain.lower().endswith(".edu"):
      print("This appears to be an educational institution email.")

    else:
      print("This seems to be a professional/work email address.")
  
  print("\n")
