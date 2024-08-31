# YouTube Video Captions Downloader

Este projeto permite baixar as legendas de todos os vídeos de um canal do YouTube e salvá-las em um arquivo CSV. Cada linha no CSV contém o ID do vídeo, o título do vídeo e as legendas (se disponíveis).

## Requisitos

- Python 3.6 ou superior
- Bibliotecas Python:
  - `pandas`
  - `google-auth`
  - `google-auth-oauthlib`
  - `google-auth-httplib2`
  - `google-api-python-client`
  - `youtube-transcript-api`

Você pode instalar as dependências com o seguinte comando:

```bash
pip install pandas google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client youtube-transcript-api
```

## Passos para Obter a API Key e o ID do Canal

### 1. Obter uma API Key do YouTube Data API

1. Acesse o [Google Cloud Console](https://console.cloud.google.com/).
2. Crie um novo projeto.
3. No menu do lado esquerdo, vá em **APIs & Services > Library**.
4. Pesquise por "YouTube Data API v3" e ative-a.
5. Vá para **APIs & Services > Credentials**.
6. Clique em **Create Credentials** e selecione **API Key**.
7. Salve a API Key gerada, pois ela será usada no código.

### 2. Encontrar o ID do Canal do YouTube

1. [Acesse este site](https://www.streamweasels.com/tools/youtube-channel-id-and-user-id-convertor/)

## Como Usar

1. Clone este repositório para a sua máquina local.

2. Substitua `API_KEY` pela sua API Key do YouTube no código.

3. Substitua `channel_id` pelo ID do canal do YouTube no código.

4. Execute o script para baixar as legendas dos vídeos e salvá-las em um arquivo CSV.

### Verificação de Vídeos Sem Legendas:

Depois de rodar o código acima e gerar o CSV, você pode verificar quais vídeos não possuem legendas:

```python
import pandas as pd

# Carregar o DataFrame do arquivo CSV
df = pd.read_csv("youtube_video_details_with_captions.csv")

# Filtrar os vídeos que não possuem legendas (coluna 'Captions' vazia)
videos_sem_legendas = df[df["Captions"].isna()]

# Exibir a quantidade de vídeos sem legendas
num_videos_sem_legendas = videos_sem_legendas.shape[0]
print(f"Número total de vídeos sem legendas: {num_videos_sem_legendas}")

# Exibir os títulos dos vídeos sem legendas
print("Títulos dos vídeos sem legendas:")
print(videos_sem_legendas["Title"].tolist())
```

## Considerações Finais

- Certifique-se de ter configurado corretamente o ambiente com todas as dependências.
- A API Key do YouTube tem limites de uso, então você pode precisar ajustá-los caso o número de vídeos seja grande.
- Caso o vídeo não tenha legendas ou elas estejam desativadas, o campo "Captions" no CSV será preenchido com "No captions available".

## Contato

 - rtheodoro@usp.br

## Ver também

 - [https://github.com/sillasgonzaga/foodcaptions-saas](https://github.com/sillasgonzaga/foodcaptions-saas)
 - [https://thepythoncode.com/article/using-youtube-api-in-python](https://thepythoncode.com/article/using-youtube-api-in-python)

## TO-DO List

 - [] Alguns vídeos estão vindo sem legenda, não porque, estou tentando resolver (precisa fazer uma busca novamente)
 - [] Adicionar função que encontre o Id do Canal pela URL (minha autenticação do google não estava funcionando para isso, depois tento novamente)
