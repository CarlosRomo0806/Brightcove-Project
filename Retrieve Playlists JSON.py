from rauth import OAuth2Session
import requests, json, base64

# Clientid y clientsecret hardcodeados
client_id = "0a217c59-efa8-455b-9cce-e072d205511c"
client_secret = "nhm5ky9faYcaz8Ok3mEDxJW6OLKEsCEdfTKY5IibFNvBPS7kGNfg0-Vne4buBrbxfWOho1tw-x8L9fBnVPjWZg"


def getToken(client_id, client_secret):
    string = client_id + ":" + client_secret  
    #Se codifica el string para codificarlo en base 64
    authString = base64.b64encode(string.encode("utf-8"))
    headersMap = {
        "Content-Type": "application/x-www-form-urlencoded",
        #Se debe decodificar para que sea un string
        "Authorization": "Basic " + authString.decode()
    }
    params = {"grant_type": "client_credentials"}

    r = requests.post('https://oauth.brightcove.com/v4/access_token',
                      headers=headersMap, params=params).json()  #Se hace una petición POST para conseguir el token

    return r['access_token']  #Se regresa solamente el token


def getAllVideos(session):
    r = session.get('https://cms.api.brightcove.com/v1/accounts/6044537239001/playlists',
                    params={'format': 'json'})  # Se hace un HTTP GET en la sesion ya autorizada del url y params se formatea en json
    with open('datap.json', 'w') as f:
        #Paso el json conseguido(r) a un archivo llamado data.json
        json.dump(r.json(), f)


#se consigue el token
token = getToken(client_id, client_secret)

#La session se inicializa con los datos anteriores
session = OAuth2Session(client_id, client_secret, token)

getAllVideos(session=session)
