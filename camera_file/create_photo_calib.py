import cv2

cap = cv2.VideoCapture(0)
i = 1
while(True):
    ret, frame = cap.read()  
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite('camera_file/callib/' + str(i)+'.jpg', frame)
        print('save images ', i)
        i+=1
    elif cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
        
    
  