import string
import random
 
randon_string = ''.join(random.choices(string.ascii_letters, k=5))
 
print("random string : " + str(randon_string))