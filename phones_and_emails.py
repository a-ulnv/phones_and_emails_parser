import sys
import re

# Check if running correct version
if sys.version_info.major != 3:
    raise ValueError("You must use Python 3.")
if sys.version_info.minor < 4 :
    raise ValueError("You must use at least Python 3.4")
if sys.version_info.minor < 6:
    print("Recommended Python Version is 3.6")

# Function to parse email addresses
def parse_email(raw_email):
    # prepare the return variable
    result = ''
    
    # STEP 1: define all period characters
    # DESCR: replace 'dot' or '(dot)', preceeded and followed by 1 or more spaces, with '.'
    result = re.sub(r'\s+(dot|\(dot\))\s+', '.', raw_email)
    
    # STEP 2: define all '@' characters
    # DESCR: replace 'at' or '(at)', preceeded and followed by 0 or more spaces, with '@'
    result = re.sub(r'\s*(at|\(at\))\s*', '@', result)
    
    # return the result
    return result

# Function to parse phone numbers
def parse_number(raw_phone_number):
    # prepare the return variable
    result = ''
    
    # STEP 1: filter out all unnecessary characters
    # DESCR: delete anything that is not '+' or a digit
    result = re.sub(r'[^+0-9]', '', raw_phone_number)
    
    # STEP 2: handling the country code
    # DESCR: if the number start with +49, 0049, or 0, change it to +49 with a space
    result = re.sub(r'^(\+49|0049|0)', '+49 ', result)
    
    # STEP 3: if the first digit after +49 is 0, then remove it
    # DESCR: use the look-behind method to check but not select +49
    result = re.sub(r'(?<=^\+49\s)0', '', result)
    
    # STEP 4: if the area code starts with 1, then add a space after 3 digits
    # DESCR: use groups to identify where the space needs to go
    result = re.sub(r'(?<=^\+49\s)(1+\d{2})', r'\1 ', result)
    
    # return the result
    return result

# Input files
rawPhonesFile = "phones.txt"
rawEmailsFile = "emails.txt"

# Parsing telephone numbers
print("Parsed telephone numbers:")
with open(rawPhonesFile) as f:
	for line in f:
		print(parse_number(str(line)))

# Break line
print('\n')

# Parsing email addresses
print("Parsed email addresses:")
with open(rawEmailsFile) as f:
	for line in f:
		print(parse_email(str(line)), end='')
# Break line
print('\n\n')

input("Press Enter to exit ...")