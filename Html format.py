# escribe-html-2-windows.py
import webbrowser
import json
import collections

# Data from json
with open('datap.json') as json_file:
    datap = json.load(json_file)

with open('datav.json') as json_file:
    datav = json.load(json_file)

f = open('Material.html','w')

mensaje_init = """<html>
<head></head>
<body>"""
f.write(mensaje_init)

# Main HTML Data

def getTime(total_seconds):     #GetTime function to converse total seconds into hours, minutes and seconds
    hours = total_seconds//3600     
    hourstr = str(hours)+ str(" hrs con ")  #Parse to string so it can be valid on the write()
    minutes = (total_seconds - (hours*3600)) //60   
    minstr = str(minutes) + str(" min y ") 
    seconds = total_seconds % 60  
    secstr = str(seconds) + str(" seg")
    total_time = hourstr + minstr + secstr
    return total_time

vid=[]
total_seconds = 0
for i in range(len(datav)):     #For loop to select and sum the duration of every video of JSON data
    vid.append(datav[i]['duration'])
    total_seconds += vid[i]

f.write(f"<h1 style='color:brown'>Suma total de duracion de videos :</h1>"+getTime(total_seconds)+ f"<hr>") #Display on the HTML 

mexduration = 0
for i in range(len(datav)):    #For loop to select and sum the duration of every video with the 'mexico' tag
    if 'mexico' in datav[i]['tags']:
        mexduration+= datav[i]['duration']

f.write(f"<h1 style='color:brown'>Suma total de los videos con el tag 'mexico':</h1>"+getTime(mexduration)+ f"<hr>") #Display on the HTML 

title_header3 = f"<h1 style='color:brown'>Playlists:</h1>"
f.write(title_header3)

playlist1 = (datav[18]['duration'])
playlist2 = (datav[0]['duration']+ datav[18]['duration'])
playlist3 = (0)                                                 
playlist4 = (datav[18]['duration'])
playlist5 = (0)
playlist6 = (0)
playlist7 = (0)

playlists=[playlist1, playlist2, playlist3, playlist4, playlist5, playlist6, playlist7]

result = dict()
for i in range(len(datap)):
    #playlist_name = key, Time = Playlist Time
    result[datap[i]['name']] = playlists[i]

for playlist_name in sorted(result, key=result.get, reverse=True):
    time = getTime(result[playlist_name])
    f.write(f"{playlist_name}: {time} <br><br>")

# Close HTML tags
mensaje_fin = """</body></html>"""
f.write(mensaje_fin)
f.close()

# Open HTML file in web browser
webbrowser.open_new_tab('Material.html')