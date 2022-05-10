def main():
  import json  # For writing the data to a JSON file
  import re  # For verifying the e-mail

  email = None # The email
  email_data = { 'username': '', 'domain': '', 'tld': '' }  # The parts of the e-mail
  email_re = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'  # Regex for identifying emails
  valid = False 

  # Getting the input and doing a regular expression check
  while not valid:
    email = input('Enter the e-mail address you would like to add to the database: ')
    valid = re.fullmatch(email_re, email)

  # Getting the e-mail data => re.split() returns username, domain name and top-level domain
  email_data['username'], email_data['domain'], email_data['tld'] = re.split(r'@|\.', email)

  try:
    with open('data/data.json', 'r+t') as data_file:
      # Getting the data
      data = json.load(data_file)

      # Getting the number of records
      index = str(len(data) + 1)

      # Updating the data
      data[index] = email_data

      # Writing the data to the file 
      data_file.seek(0)
      json.dump(data, data_file, indent=2)

  except FileNotFoundError:
    import os # For making the directory

    print('Creating json file...')

    # Making the directory
    os.mkdir('data')

    with open('data/data.json', 'wt') as data_file:
      # Getting the data
      data = { '1': email_data }

      # Writing the data to the file 
      data_file.seek(0)
      json.dump(data, data_file, indent=2)


if __name__=='__main__':
  main()