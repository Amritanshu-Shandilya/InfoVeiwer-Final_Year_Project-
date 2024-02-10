import cv2
from cryptography.fernet import Fernet
import requests


from Marker_detect_decode import DetectAndDecode
from Data_processor import Data_Processor_Module

class Application:
    ''' This is the base of the app. Functions includes : 
        1. Detecting and decoding the marker.
        2. Processing the raw data extracted from the marker
        3. Making a request from the processed data'''
    
    def __init__(self) -> None:
        self.camera = cv2.VideoCapture(1)
        self.qr_detector = cv2.QRCodeDetector()

        self.decoded_data_raw = None
        self.processed_data = ""

        # THIS IP ADDRESS OF THE SERVER SHOULD BE CHANGED AFTER SERVER IS DEPLOYED!
        self.server_ip = '192.168.1.22'
        self.server_port = '5000'

        self.response = None
    
    def detect_decode(self):
        # Handles detection of markers and extracts the infromation from it
        while DetectAndDecode(self, self.camera, self.qr_detector) != True:
            continue
        
        # print("Encoded Data  ->  "+self.decoded_data_raw)

    def data_processing(self):
        # Processes the raw data to convert it into a useable form
        self.processed_data = Data_Processor_Module(self, self.decoded_data_raw)
        # print("Decrypted data  -> "+str(self.processed_data))

    def request_data(self):
        '''This function will take the processed data and will form a request string from it.'''
        self.response = requests.get(f'http://{self.server_ip}:{self.server_port}/get_data/{self.processed_data}')

        if self.response.status_code == 200:
            print('Data received!')
        else:
            print(f'Error : {self.response.status_code}')


        pass


App = Application()
App.detect_decode()
App.data_processing()

App.camera.release()
cv2.destroyAllWindows()