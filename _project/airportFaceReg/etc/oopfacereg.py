import cv2
import mysql.connector

cnx = mysql.connector.connect(  host='localhost',
                                user='earth',
                                password='kikuanone1234',
                                database='project'  )
cursor = cnx.cursor()
query = ("SELECT firstname, lastname, gate, terminal, seat FROM info")
cursor.execute(query)
face = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
clf = cv2.face.LBPHFaceRecognizer_create()
clf.read("D:/__PROJ/_WORK/coding/python/_project/x.xml")
_fname, _lname, _gate, _terminal, _seat = ([] for i in range(5))

for fname, lname, gate, terminal, seat in cursor:
    _fname.append(fname)
    _lname.append(lname)
    _gate.append(gate)
    _terminal.append(terminal)
    _seat.append(seat)
print(_fname)

class eiei():
    def __init__(self):
        self.cap = cv2.VideoCapture(1)
        print('Opening camera.')

    def get_frame(self):
        ret, frame = self.cap.read()
        if ret:
            pass
        return frame
    
    def cam_release(self):
        self.cap.release()

    def draw(self, img, cascade, scaleFactor, minNeighbors, color, clf):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        features = face.detectMultiScale(gray, scaleFactor, minNeighbors)
        treshold = 70

        for x,y,w,h in features:
            #cv2.rectangle(img, (x,y), (x+w, y+h), color, 2)
            id, con = clf.predict(gray[y:y+h,x:x+h])
            print(id)
            if con <= treshold:
                    cv2.putText(img, f"{_fname[id-1]} {_lname[id-1]}",
                                (x+170,y),
                                cv2.FONT_ITALIC,
                                0.8, color, 2)
                    cv2.putText(img, f"gate: {_gate[id-1]} terminal: {_terminal[id-1]} seat: {_seat[id-1]}",
                                (x+170,y+40),
                                cv2.FONT_ITALIC,
                                0.8, color, 2)
            else:
                cv2.putText(img, "Unknown",(x,y-4), cv2.FONT_ITALIC, 0.8, color, 2)
        return img

    def detect(frame, cascade, clf):
        frame = draw(frame, cascade, 1.1, 10, (0,0,255), clf)
        return frame

def main():
    while True:
        cam = eiei().get_frame()
        #frame = eiei.detect(cam, face, clf)
        frame = eiei().draw(cam, face, 1.1, 10, (0,0,255), clf)
        cv2.imshow('lol', frame)
        if (cv2.waitKey(30) & 0xFF == ord('q')):
            break
    eiei().cam_release()
    cv2.destroyAllWindows()

if '__main__' == __name__:
    main()

