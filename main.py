import cv2
from cryptography.fernet import Fernet
import requests


from Marker_detect_decode import DetectAndDecode
from Data_processor import Data_Processor_Module
from vizualizer import FileViewerApp

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

        # For storing the response : 
        self.response_path = './received/'

        # THIS IP ADDRESS OF THE SERVER SHOULD BE CHANGED AFTER SERVER IS DEPLOYED!
        self.server_ip = '192.168.1.12'
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

    def request_data(self):
        '''This function will take the processed data and will form a request string from it.'''
        # Gets the file content
        self.response = requests.get(f'http://{self.server_ip}:{self.server_port}/get_data/{self.processed_data}')
        # Gets the marker name
        self.marker_name = requests.get(f'http://{self.server_ip}:{self.server_port}/get_name/{self.processed_data}').text

        if self.response.status_code == 200:
            # store the text received from server into a file
                # Create a file inside received folder and store response inside it
            self.response_path+=str(self.processed_data)+'.txt'
            text_received_from_server = self.response.text
            with open(self.response_path, 'w') as file:
                file.write(text_received_from_server)
            return True
        else:
            print(f'Error : {self.response.status_code}')

    def see_output(self):
        main_win = FileViewerApp()
        main_win.show()
        main_win.init_ui(title=self.marker_name)
        main_win.load_file(self.response_path)
        return True


        

def main():
    App = Application()
    App.detect_decode()
    App.data_processing()
    App.request_data()
    App.see_output()
    App.camera.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()