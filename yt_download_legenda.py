# Bibliotecas necessárias ----
#!pip install youtube-transcript-api
#!pip install google-api-python-client
#!pip install pandas

# Importando bibliotecas ----
import os
import pandas as pd
import re
from googleapiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound, CouldNotRetrieveTranscript

# Definindo parâmetros ----

# Defina sua chave de API do YouTube aqui
API_KEY = "SUA_API_KEY_AQUI---LEIA_O_README"
# Insira o ID do canal que deseja obter os vídeos
channel_id = "UCO8t36XjmC6jE2UW7CreQ8w"

# Criando funções ----

# Função para obter o ID de upload do canal
def get_uploads_playlist_id(youtube, channel_id):
    response = youtube.channels().list(
        part="contentDetails",
        id=channel_id
    ).execute()
    
    uploads_playlist_id = response["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]
    return uploads_playlist_id

# Função para obter todos os video IDs e títulos da playlist de uploads
def get_all_video_details(youtube, uploads_playlist_id):
    video_details = []
    next_page_token = None
    
    while True:
        response = youtube.playlistItems().list(
            part="contentDetails,snippet",
            playlistId=uploads_playlist_id,
            maxResults=50,
            pageToken=next_page_token
        ).execute()
        
        for item in response["items"]:
            video_id = item["contentDetails"]["videoId"]
            video_title = item["snippet"]["title"]
            video_details.append({"VideoID": video_id, "Title": video_title})
        
        next_page_token = response.get("nextPageToken")
        if next_page_token is None:
            break
    
    return video_details

# Função para obter legendas de um vídeo
def get_video_captions(video_id):
    try:
        # Tenta obter a legenda em português (ou outra língua disponível)
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=['pt'])
        # Concatena o texto da legenda em uma única string
        captions = " ".join([t["text"] for t in transcript_list])
        return captions
    except (TranscriptsDisabled, NoTranscriptFound, CouldNotRetrieveTranscript):
        # Se não houver legenda disponível, retorna uma string vazia
        return ""
    except Exception as e:
        print(f"Erro inesperado ao obter legenda para o vídeo {video_id}: {str(e)}")
        return ""

def main():
    # Inicializa o cliente da API do YouTube
    youtube = build("youtube", "v3", developerKey=API_KEY)

    # Obtém o ID da playlist de uploads do canal
    uploads_playlist_id = get_uploads_playlist_id(youtube, channel_id)
    
    # Obtém todos os video IDs e títulos
    video_details = get_all_video_details(youtube, uploads_playlist_id)
    
    # Adiciona as legendas a cada vídeo
    for video in video_details:
        video["Captions"] = get_video_captions(video["VideoID"])
    
    # Cria um DataFrame usando os video IDs, títulos e legendas
    df = pd.DataFrame(video_details)
    
    # Salva o DataFrame em um arquivo CSV
    df.to_csv("youtube_video_details_with_captions.csv", index=False)
    
    print("Número total de vídeos encontrados:", len(video_details))
    print("Detalhes dos vídeos foram salvos em 'youtube_video_details_with_captions.csv'")

# Rodando funções ----

if __name__ == "__main__":
    main()