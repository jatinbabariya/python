import cv2
import os


video_path = 'video.mp4'
video_name = os.path.splitext(os.path.basename(video_path))[0]
output_dir = os.path.join(os.getcwd(), video_name)

os.makedirs(output_dir, exist_ok=True)

cap = cv2.VideoCapture(video_path)

frame_count = 0

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frame_filename = os.path.join(output_dir,f'frame_{frame_count:07d}.png')
    cv2.imwrite(frame_filename, frame)
    frame_count += 1
cap.release()

print("Process done")