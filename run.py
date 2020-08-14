
import pafy
import pandas as pd
import json 

video_url=[]
video_title = []
merged_list = {'Video Title' :[],'Video URLs': []}
video_count = 5
list_url ="PLAYLIST URL"
for i in range(1,video_count):
    playlist = pafy.get_playlist(list_url)
    items = playlist["items"]
    item = items[i]
    i_pafy = item['pafy']
    y_url = i_pafy.watchv_url
    y_title = i_pafy.title
    y_author = i_pafy.author
    y_thumbnail= i_pafy.thumb

    print("{}--------------------------------------------------------".format(i))
    print("[+]LINK: {}".format(y_url))
    print("[+]TITLE: {}".format(y_title))
    print("[+]THUMB: {}".format(y_thumbnail))
    video_url.append(y_url)
    video_title.append(y_title)

merged_list['Video Title'].extend(video_title)
merged_list['Video URLs'].extend(video_url)
df = pd.DataFrame(merged_list, columns=['Video Title','Video URLs'])
print(df)
df.to_excel("../YoutubeList/list.xlsx",index=False,header=True)