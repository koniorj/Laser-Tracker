import cv2
from my_exceptions import NoCameraFootage

CAMERA_INDEX = 1
KEY_ESC = 27

def main():
    # CAP_DSHOW - DirectShow, it overwrites the standard way of Windows opening
    # camera feed with MSMF, which is incompatible with Iriun
    capture = cv2.VideoCapture(CAMERA_INDEX, cv2.CAP_DSHOW)

    try:
        while True:
            return_value, frame = capture.read()
            if not return_value:
                raise NoCameraFootage()

            cv2.imshow("Live camera", frame)

            if cv2.waitKey(1) & 0xFF == KEY_ESC:
                break
    finally: 
        capture.release()
        cv2.destroyAllWindows()
        print("All resources freed.")


if __name__ == "__main__":
    main()