import cv2
import mysql.connector

def queryDB():
    global _fname, _lname, _gate, _terminal, _seat
    cnx = mysql.connector.connect(  host='localhost',
                                user='earth',
                                password='kikuanone1234',
                                database='project'  )
    cursor = cnx.cursor()
    query = ("SELECT firstname, lastname, gate, terminal, seat FROM info")
    cursor.execute(query)
    _fname, _lname, _gate, _terminal, _seat = ([] for i in range(5))

    for fname, lname, gate, terminal, seat in cursor:
        _fname.append(fname)
        _lname.append(lname)
        _gate.append(gate)
        _terminal.append(terminal)
        _seat.append(seat)
    print(_fname)
  
def draw(img, cascade, scaleFactor, minNeighbors, color, clf):
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
    global face
    face = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(1)
    clf = cv2.face.LBPHFaceRecognizer_create()
    clf.read("D:/__PROJ/_WORK/coding/python/_project/x.xml")
    while cap.isOpened():
        ret,frame = cap.read()
        if ret:
            frame = detect(frame, face, clf)
            img = cv2.imread(r"D:\__PROJ\_WORK\coding\python\_project\qr.png")
            img = cv2.resize(img, (256, 256))
            cv2.imshow('qr', img)
            cv2.imshow('Real', frame)
            if (cv2.waitKey(1) & 0xFF == ord('q')):
                break
    cap.release()
    cv2.destroyAllWindows()

if '__main__' == __name__:
    queryDB()
    main()


"""info = {
    '_fname' : [],
    '_lname' : [],
    '_gate' : [],
    '_terminal' : [],
    '_seat' : []
}
for _ in info:
    for fname, lname, gate, terminal, seat in cursor:
        info[_].append(__)"""