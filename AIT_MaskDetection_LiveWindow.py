#Cution:This example is not supported by the officail ImageAI!!!
#This is the examplpe for AIT test "Live window"


from imageai.Detection.Custom import CustomVideoObjectDetection
import os
import cv2

execution_path = os.getcwd()
camera = cv2.VideoCapture(0)

video_detector = CustomVideoObjectDetection()
video_detector.setModelTypeAsYOLOv3()
video_detector.setModelPath("detection_model-ex-012--loss-0003.944.h5")
video_detector.setJsonPath("detection_config_Mask.json")
video_detector.loadModel()

video_detector.detectObjectsFromVideo(camera_input=camera,
                                          output_file_path=os.path.join(execution_path, "holo1-detected3"),
                                          frames_per_second=20,
                                          minimum_percentage_probability=40,
                                          log_progress=True,
                                          save_detected_video=False,
                                          live_window=True)#AIT parameter:live_window