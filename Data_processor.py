'''
Data inside the markers will be encrypted or some additional data might be included before/after them 
to ensure security. This function's job is to deal with all of that and get the actudal data to be used 
to make HTTP requests to the server.
'''

import rsa

def Data_Processor_Module(self, raw_data):

    decoded_data = rsa.decrypt(raw_data, self.private_key).decode()
    return decoded_data
    