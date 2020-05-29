#Cution:This example is not supported by the officail ImageAI!!!
#This is the examplpe for AIT test "Live window"


from imageai.Detection.Custom import CustomVideoObjectDetection
import os
import cv2
import threading
import time

def mainLoop():
    var=1
    x=0
    while var == 1 :  # This constructs an infinite loop
        x=1
        print(x)
        time.sleep(1)
def videoLoop():
    execution_path = os.getcwd()
    camera = cv2.VideoCapture(0)

    video_detector = CustomVideoObjectDetection()
    video_detector.setModelTypeAsYOLOv3()
    video_detector.setModelPath("detection_model-ex-012--loss-0003.944.h5") #Download the model from "https://github.com/firmamentone/masksDetection/releases/download/20200501_0/detection_model-ex-012--loss-0003.944.h5"
    video_detector.setJsonPath("detection_config_Mask.json")
    video_detector.loadModel(detection_speed='fastest')

    video_detector.detectObjectsFromVideo(camera_input=camera,
                                          output_file_path=os.path.join(execution_path, "holo1-detected3"),
                                          frames_per_second=20,
                                          minimum_percentage_probability=40,
                                          log_progress=True,
                                          save_detected_video=False,
                                          live_window=True) #AIT parameter:live_window
    


thread_video=threading.Thread(target=videoLoop)
thread_Main=threading.Thread(target=mainLoop)

thread_video.start()
thread_Main.start()