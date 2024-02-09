'''
Data inside the markers will be encrypted or some additional data might be included before/after them 
to ensure security. This function's job is to deal with all of that and get the actudal data to be used 
to make HTTP requests to the server.
'''
from cryptography.fernet import Fernet



def Data_Processor_Module(self, raw_data):

    with open('fernet.key', 'rb') as key_file:
        key = key_file.read()

    
    fernet = Fernet(key)

    decoded_data = fernet.decrypt(raw_data)

    return decoded_data.decode('utf-8')
    

if __name__ == '__main__':
    Data_Processor_Module('gAAAAABlxmLSm5mhc9_Iq2VUjrZuZfHwNA7Bz0X3F1z6IHPaytooHa2wCzmrHiBjL5__ozSw1neqsUuTGd9ZzZNFRVHeJ57IVZEzwTAWJnsi8f4kNW0W-H8=')