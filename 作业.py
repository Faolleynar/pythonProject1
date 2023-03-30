songs=["以父之名","夜的第七章","止战之殇"]
for song in songs:
    print("i like "+song+".")
new_songs=songs[:]
songs.pop()
print("删除一首太肃穆的吧："+"\t")
print(songs)
print("原列表，战歌起："+"\t")
new_songs.insert(0,"夜曲")
print(new_songs)




