import csv

def load_database():
  database = {
    'DOMAIN_CATEGORIES': {},
    'COMMON_PROVIDERS': {},
    'ORG_TYPES': {}
  }
  
  try:
    with open('database.csv', mode='r', encoding='utf-8-sig') as file:
      reader = csv.DictReader(file)
      for row in reader:
        if row['TYPE'] == 'DOMAIN_CATEGORY':
          database['DOMAIN_CATEGORIES'][row['KEY']] = row['VALUE']
        elif row['TYPE'] == 'COMMON_PROVIDER':
          database['COMMON_PROVIDERS'][row['KEY']] = row['VALUE']
        elif row['TYPE'] == 'ORG_TYPE':
          database['ORG_TYPES'][row['KEY']] = row['VALUE']
  except FileNotFoundError:
    raise FileNotFoundError("Database file 'database.csv' not found")
  except Exception as e:
    raise Exception(f"Error loading database: {str(e)}")
  
  return database

def get_domain_info(domain, database):
  domain_parts = domain.split('.')
  tld = domain_parts[-1] if domain_parts else ''
  
  info = {
    'provider': database['COMMON_PROVIDERS'].get(domain, None),
    'tld_description': database['DOMAIN_CATEGORIES'].get(tld, 'Unknown TLD'),
    'org_type': None,
    'country': None
  }
  
  if tld in database['DOMAIN_CATEGORIES'] and len(tld) == 2:
    info['country'] = database['DOMAIN_CATEGORIES'][tld]
  
  for part in domain_parts:
    if part in database['ORG_TYPES']:
      info['org_type'] = database['ORG_TYPES'][part]
      break

  return info

def main():
  try:
    database = load_database()
  except Exception as e:
    print(f"Error: {e}")
    return

  while True:
    email = input("Input the email address you want to analyze. Leave blank to exit.\nEmail Address: ").strip().lower()

    if not email:
      print("Goodbye!")
      break

    if "@" not in email:
      print("Incorrect Email format\n")
      continue

    try:
      username, domain = email.split("@")
    except ValueError:
      print("Invalid email format\n")
      continue

    print(f"\n{' Email Analysis ':=^50}\n")
    print(f"Username: {username}")
    print(f"Domain: {domain}")
    
    domain_info = get_domain_info(domain, database)

    if domain_info['provider']:
      print(f"\nProvider: {domain_info['provider']} (personal email)")
    else:
      print(f"\nTop-Level Domain: {domain_info['tld_description']}")
      
      if domain_info['org_type']:
        print(f"Organization Type: {domain_info['org_type']}")
      
      if domain_info['country']:
        print(f"Country: {domain_info['country']}")
      elif domain.split('.')[-1] in ['com', 'org', 'net']:
        print("Global domain (no specific country)")
  
    print("\n" + "="*50)

if __name__ == "__main__":
    main()
