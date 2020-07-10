import cv2


class Video(object):

    def __init__(self, path, width, height, qsize=10, loop=True, codec='h264'):
        self.path = path
        self.width = width
        self.height = height
        self.qsize = qsize
        self.loop = loop
        self.codec = codec
        self.reset()

    def reset(self):
        if hasattr(self, 'cap'):
            del self.cap
        self.cap = cv2.VideoCapture('/dev/video0')

    def read(self):
        re, img = self.cap.read()
        if re:
            return img
        else:
            return None

    def destroy(self):
        self.cap.release()

    def destroy_window(self):
        cv2.destroyAllWindows()

    def show_frame(self, frame):
        cv2.imshow('Test', frame)
        key = cv2.waitKey(10)
        if key == 27 or key == ord('q') or key == ord('Q'):
            return -1
        else:
            return 0
