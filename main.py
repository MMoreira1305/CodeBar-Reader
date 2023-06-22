import cv2
from pyzbar import pyzbar

def barcode_reader():
    # Inicializa a câmera
    cap = cv2.VideoCapture(0)

    while True:
        # Captura o frame da câmera
        ret, frame = cap.read()
        list_codebar = ["8949461894984", "6515648916", "6548964631668"]
        confirmation = False

        # Detecta e decodifica os códigos de barras
        barcodes = pyzbar.decode(frame)

        # Itera sobre os códigos de barras encontrados
        for barcode in barcodes:
            # Extrai as coordenadas do retângulo que contém o código de barras
            (x, y, w, h) = barcode.rect

            # Desenha o retângulo ao redor do código de barras
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            # Extrai o valor do código de barras
            barcode_data = barcode.data.decode("utf-8")
            barcode_type = barcode.type

            # Exibe o valor do código de barras
            cv2.putText(frame, barcode_data, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            
            # Verifica se o código de barras está na lista (essa lista pode mudar para um database por exemplo)
            for code_bar in list_codebar:
                if code_bar == barcode_data:
                    confirmation = True
                    print(code_bar, "O Valor está inserido na database")
                    break

        # Se estiver, o sistema para      
        if confirmation:
            break


        # Exibe o frame capturado
        cv2.imshow("Barcode Reader", frame)

        # Verifica se a tecla 'q' foi pressionada para sair do loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Libera a câmera e fecha a janela
    cap.release()
    cv2.destroyAllWindows()

barcode_reader()