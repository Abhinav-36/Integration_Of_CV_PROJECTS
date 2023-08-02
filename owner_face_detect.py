import cv2

def face_detector():
    face_classifier = cv2.CascadeClassifier('myhaarcascade_frontalface_default.xml')
    loaded_model = cv2.face.LBPHFaceRecognizer_create()
    model_file_path = './face_detector.h5'  # Replace with the actual file path you used to save the model
    loaded_model.read(model_file_path)

    def face_detector(img, size=0.5):
        
        # Convert image to grayscale
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray, 1.3, 2)
        if faces is ():
            return img, [] , 0
        
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
            roi = img[y:y+h, x:x+w]
            roi = cv2.resize(roi, (200, 200))
            
        return img, roi, (x,y-20)


    cap = cv2.VideoCapture(0)


    while True:
        ret, frame = cap.read()
        cv2.imwrite("pic.jpg", frame)
        
        image, face, dim = face_detector(frame)
        try:
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
            
            results = loaded_model.predict(face)
            
            if results[1] < 500:
                confidence = int( 100 * (1 - (results[1])/400) )
                #display_string = str(confidence) + "%" 

            if confidence > 85:
                cv2.putText(image, "Hey Abhinav: {}%".format(confidence), dim, cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
                cv2.imshow('Face Recognition', image )
                
        
            else:
                cv2.putText(image, "Wrong Face Detected", (220,80), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
                cv2.imshow('Face Recognition', image )

        except:
            cv2.putText(image, "No Face Found", (220, 80) , cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
            cv2.putText(image, "looking for face", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
            cv2.imshow('Face Recognition', image )
            pass
            
        if cv2.waitKey(1) == 13: #13 is the Enter Key
            break
            
    cap.release()
    cv2.destroyAllWindows()