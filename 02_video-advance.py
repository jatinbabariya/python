import cv2
import os


video_path = 'video.mp4'
video_name = os.path.splitext(os.path.basename(video_path))[0]
output_dir = os.path.join(os.getcwd(), video_name)

os.makedirs(output_dir, exist_ok=True)

cap = cv2.VideoCapture(video_path)
original_fps = cap.get(cv2.CAP_PROP_FPS)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
desired_fps = 3
frame_interval = int(round(original_fps / desired_fps))

print(f"Original FPS: {original_fps}")
print(f"Total frames in video: {total_frames}")

expected_images = total_frames // frame_interval
print(f"Expected number of images to be generated: {expected_images}")


frame_count = 0
image_count = 0
while True:
    ret, frame = cap.read()

    if not ret:
        break
    if frame_count % frame_interval == 0:
        frame_filename = os.path.join(output_dir,f'frame_{image_count:07d}.jpeg')
        cv2.imwrite(frame_filename, frame)
        image_count += 1

    frame_count += 1
cap.release()

print(f"Extracted {image_count} frames at {desired_fps} fps.")