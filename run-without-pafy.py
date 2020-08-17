import json 
import pandas as pd
import json
from time import sleep
import asyncio


f = open("../PLAYLIST/'YOUR JSON FILE'",encoding="utf8")
data = json.load(f)


#print(data[0]["contentDetails"]["videoId"])
#print(data[0]["snippet"]["title"])

video_urls=[]
video_title = []
merged_list ={'Video Title' :[],'Video URLs': []}
video_count =0
for i in range(video_count):
  video_id = data[i]["contentDetails"]["videoId"]
  y_title = data[i]["snippet"]["title"]
  y_url = "https://www.youtube.com/watch?v={}".format(video_id)
  print("{}--------------------------------------------------------".format(i))
  print("[+]LINK: {}".format(y_url))
  print("[+]TITLE: {}".format(y_title).encode('utf8'))
  video_urls.append(y_url)
  video_title.append(y_title)
  

merged_list['Video Title'].extend(video_title)
merged_list['Video URLs'].extend(video_urls)
df = pd.DataFrame(merged_list, columns=['Video Title','Video URLs'])
print(df)
df.to_excel("../PLAYLIST/list.xlsx",index=False,header=True)