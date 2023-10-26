import cv2
import time
import math

# Abra o vídeo e verifique se a abertura foi bem-sucedida
video = cv2.VideoCapture("bb3.mp4")
if not video.isOpened():
    print("Erro ao abrir o vídeo")
    exit()

# Inicialize o tracker (rastreador)
tracker = cv2.TrackerCSRT_create()

# Leia o primeiro quadro do vídeo
returned, img = video.read()

# Selecione a região de interesse (ROI) na imagem
bbox = cv2.selectROI("Rastreamento", img, False)

# Inicialize o tracker na imagem e na região de interesse
tracker.init(img, bbox)

print("BBox (região de interesse):", bbox)

# Função para desenhar a caixa delimitadora (bounding box) e texto
def drawBox(img, bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])

    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 3, 1)
    cv2.putText(img, "Rastreando", (75, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

# Função para realizar o rastreamento do objetivo
def goal_track(img, bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])


# Loop principal
while True:
    check, img = video.read()

    # Atualize o tracker na imagem e na região de interesse
    success, bbox = tracker.update(img)

    if success:
        drawBox(img, bbox)
    else:
        cv2.putText(img, "Perdido", (75, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.imshow("Resultado", img)

    key = cv2.waitKey(25)
    if key == 32:  # Tecla de espaço para parar
        print("Parado")
        break

# Libere o vídeo e feche todas as janelas
video.release()
cv2.destroyAllWindows()  # "destroyALLwindows" corrigido para "destroyAllWindows"
