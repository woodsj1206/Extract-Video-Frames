"""
Program Name: ExtractVideoFrames
Author: woodsj1206 (https://github.com/woodsj1206)
Description: This program extracts frames from a video file based on its FPS and saves them as PNG images. 
Date Created: 4/18/24
Last Modified: 5/2/24
"""

import cv2
import os

def extract_frames(video_path, output_folder):
    # Open the video file
    video = cv2.VideoCapture(video_path)
    
    # Check if the video file is opened successfully
    if not video.isOpened():
        print("Error: Unable to open video file")
        return
    
    # Get the frame rate of the video
    fps = int(video.get(cv2.CAP_PROP_FPS))
    
    # Initialize frame counter and extracted frames counter
    frame_count = 0
    extract_frames_count = 0
    
    print("Extracting frames...")

    # Read and process each frame in the video
    while True:
        # Read a frame from the video
        ret, frame = video.read()
        
        # Check if the frame is read successfully
        if not ret:
            break

        if frame_count % fps == 0:
            # Construct the output file path for the current frame
            output_path = f"{output_folder}/frame_{extract_frames_count:04d}.png"
            
            # Save the frame as a PNG image
            cv2.imwrite(output_path, frame)
             
            print(f"Added: frame_{extract_frames_count:04d}.png")
            
            extract_frames_count += 1
            
        # Increment frame counter
        frame_count += 1
    
    # Release the video object
    video.release()
    print(f"Frames extracted: {extract_frames_count}")

# Prompt the user to input the path of the video file
video_path = input("Enter the path of the video file: ")

if not os.path.exists(video_path):
    print("Error: Input video file not found")
else:
    # Specify the output folder where extracted frames will be saved
    output_folder = "extracted_frames"

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Call the function to extract frames
    extract_frames(video_path, output_folder)