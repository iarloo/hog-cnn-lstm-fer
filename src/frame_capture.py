import cv2
import numpy

#Código 4.1
def frame_capture(video_path):

    #Contador e buffer zerados.
    frame_count = 0
    captures_buffer = {}

    #Cria objeto do vídeo
    video = cv2.VideoCapture(video_path)

    #Calcula quantos frames tem 1 vídeo.
    total_frames_video = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    print(total_frames_video)

    #Cria um array com os indices que serão guardados.
    selected_index_frames = numpy.linspace(0, total_frames_video - 1, 20, dtype = int)
    print(selected_index_frames)

    #Enquanto o vídeo está aberto e o contador de frames é menor que a quantidade de frames em um vídeo
    while (video.isOpened() and frame_count < total_frames_video):
        
        read_flag, frame = video.read()
        if not read_flag:
            break

        #É o frame desejado ?
        if frame_count in selected_index_frames:
            captures_buffer[frame_count] = frame

        frame_count += 1

    video.release()
    return captures_buffer
        

