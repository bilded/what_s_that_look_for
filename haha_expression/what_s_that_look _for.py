from imutils
import face_utils 
import matplotlib.pyplot as plt 
import numpy as np 
import argparse 
import imutils 
import dlib 
import cv2 
import face_recognition 
 
known_face_encodings = [] 
known_face_names = []