import cv2

def DetectAndDecode(self, camera, qrdetector):
    '''
    This functions abstracts the process of detection and decoding of the marker

    Function: 
        it returns the data extracted from the marker
    '''
    
    #check if camera is opened
    if not camera.isOpened():
        exit()

    # Capture frames
    while True:
        ret, frame = camera.read()

        if not ret:
            # print("Error in capturing the frame")
            break
        else:
            # Detection and Decoding is done
            ret_qr, decoded_info, points, _ = qrdetector.detectAndDecodeMulti(frame)
            if ret_qr:
                for s, p in zip(decoded_info, points):
                    if s:
                        self.decoded_data_raw = s
                        return True

            cv2.imshow('camera_feed', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break