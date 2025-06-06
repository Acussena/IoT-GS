import cv2
import mediapipe as mp
import pygame

mp_hands = mp.solutions.hands
mp_face = mp.solutions.face_mesh
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
face_mesh = mp_face.FaceMesh(min_detection_confidence=0.7)

pygame.mixer.init()
pygame.mixer.music.load('sons/alerta.mp3')

cap = cv2.VideoCapture(0)

alerta_ativo = False
ultimo_estado_mao = None  

def is_hand_closed(hand_landmarks):
    
    fingers = [
        mp_hands.HandLandmark.INDEX_FINGER_TIP,
        mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
        mp_hands.HandLandmark.RING_FINGER_TIP,
        mp_hands.HandLandmark.PINKY_TIP
    ]
    
    closed_count = 0
    
    for finger_tip in fingers:
        tip = hand_landmarks.landmark[finger_tip]
        pip = hand_landmarks.landmark[finger_tip - 2]  
        
        if tip.y > pip.y:  
            closed_count += 1

    return closed_count >= 3  

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    hand_results = hands.process(img_rgb)
    face_results = face_mesh.process(img_rgb)

    if hand_results.multi_hand_landmarks:
        for hand_landmarks in hand_results.multi_hand_landmarks:
            mao_fechada = is_hand_closed(hand_landmarks)
            estado_atual = 'fechada' if mao_fechada else 'aberta'

            if estado_atual != ultimo_estado_mao:
                print(f"Alerta ativado por mudança de estado da mão: {estado_atual}!")
                pygame.mixer.music.play()
                alerta_ativo = True
                ultimo_estado_mao = estado_atual
            else:
                alerta_ativo = False
    else:
        ultimo_estado_mao = None  

    if face_results.multi_face_landmarks:
        for face_landmarks in face_results.multi_face_landmarks:
            top_lip = face_landmarks.landmark[13]
            bottom_lip = face_landmarks.landmark[14]

            boca_distancia = abs(top_lip.y - bottom_lip.y)

            if boca_distancia > 0.03 and not alerta_ativo:
                print("Alerta ativado por abertura da boca!")
                pygame.mixer.music.play()
                alerta_ativo = True
            elif boca_distancia <= 0.03:
                alerta_ativo = False

    cv2.imshow('Camera', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
