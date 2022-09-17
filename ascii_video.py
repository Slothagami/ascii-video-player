import ascii_image, cv2, os, time
from PIL import Image
from playsound import playsound

# needs to be run from cmd so it has its own window

# todo
    # get audio from video file instead of seperate mp3
        # sync video with audio track progress

def process_frame(frame, width, map):
    frame = Image.fromarray(frame)
    frame = ascii_image.convert(frame, width, map)
    os.system("cls")
    print(frame)

def display(video, delay=24, width=130, map=" .*a@"):
    """
    Video: Filepath or camera (0 = camera)
    Width: Width (in characters) of output display
    Map:   Characters to map brightnesses to
    """
    # setup the window size
    height = int(width * ascii_image.char_ratio)
    os.system(f"mode con lines={height+1} cols={width}")

    cap = cv2.VideoCapture(video)
    fps = cap.get(cv2.CAP_PROP_FPS)

    seconds_per_frame = 1 / fps
    frames_used = 0

    frame_step = 2

    time.sleep(delay * seconds_per_frame)

    start_time = time.time()

    while(cap.isOpened()):
        time_since_start = time.time() - start_time
        frames_since_start = time_since_start / seconds_per_frame # how many frames should have passed

        if frames_since_start >= frames_used:
            frames_used += frame_step

            for _ in range(frame_step):
                sucess, frame = cap.read()

            if not sucess: break

            process_frame(frame, width, map)

    cap.release()
    cv2.destroyAllWindows()