import cv2
from cryptography.fernet import Fernet
import requests
import datetime
import sys
import os
from PyQt6.QtWidgets import QApplication

from Marker_detect_decode import DetectAndDecode
from Data_processor import Data_Processor_Module
from vizualizer import FileViewerApp
from text_to_speech import text_to_speech   

class Application:
    ''' This is the base of the app. Functions includes : 
        1. Detecting and decoding the marker.
        2. Processing the raw data extracted from the marker
        3. Making a request from the processed data'''
    
    def __init__(self) -> None:

        self.user_id = 'amrit_sandy02'

        self.camera = cv2.VideoCapture(1)
        self.qr_detector = cv2.QRCodeDetector()

        self.decoded_data_raw = None
        self.processed_data = ""

        # For storing the response : 
        self.response_path = r'C:\Users\Shiv\dev\InfoVeiwer-Final_Year_Project-\received'
        self.file_path = ''
        self.audio_name = ''

        # THIS IP ADDRESS OF THE SERVER SHOULD BE CHANGED AFTER SERVER IS DEPLOYED!
        self.server_ip = '192.168.1.21'
        self.server_port = '5000'

        self.response = None
        self.marker_name = None
    
    def detect_decode(self):
        # Handles detection of markers and extracts the infromation from it
        while DetectAndDecode(self, self.camera, self.qr_detector) != True:
            continue
        # print("Encoded Data  ->  "+self.decoded_data_raw)

    def data_processing(self):
        # Processes the raw data to convert it into a useable form
        self.processed_data = Data_Processor_Module(self, self.decoded_data_raw)
        # print("Decrypted data  -> "+str(self.processed_data))

    def get_time(self):
        '''This function is used to get the cyrrent time and date and format it to send it o the server for maintaining a history.'''
        current_datetime = datetime.datetime.now()
        # print(current_datetime) 
        return current_datetime

    def request_data(self):
        '''This function will take the processed data and will form a request string from it.'''
        # Gets the file content
        time_stamp = self.get_time()
        
        self.response = requests.get(f'http://{self.server_ip}:{self.server_port}/get_data/{self.user_id}/{self.processed_data}/{time_stamp}')
        
        # Gets the marker name
        # self.marker_name = requests.get(f'http://{self.server_ip}:{self.server_port}/get_name/{self.processed_data}').text

        if self.response.status_code == 200:
            # store the text received from server into a file
                # Create a file inside received folder and store response inside it
        
            text_received_from_server = self.response.text
            self.file_path = self.response_path+'\\'+str(self.processed_data)+'.txt'
            self.audio_name = str(self.processed_data)+'.mp3'
            
            # print('file path : '+self.file_path)
            # print('audio name : '+self.audio_name)
            
            with open(self.file_path, 'w') as file:
                file.write(text_received_from_server)
            
            # Create the audio file for that file
            text_to_speech(text=text_received_from_server, filename= self.audio_name)

            return True
        else:
            print(f'Error gxh : {self.response.status_code}')
            return False


    def see_output(self):
        app = QApplication(sys.argv)
        visualizer = FileViewerApp( self.audio_name )
        visualizer.init_ui(title=self.marker_name)
        visualizer.load_file(self.file_path)

        # Connect the windowClosed signal to the delete_file method
        visualizer.window_closed.connect(self.delete_file)

        visualizer.show()
        sys.exit(app.exec())

    def delete_file(self):
        # Delete the file when the window is closed
        if os.path.exists(self.response_path):
            os.remove(self.response_path)


App = Application()
App.detect_decode()
App.data_processing()
App.request_data()
App.see_output()
App.camera.release()
cv2.destroyAllWindows()

