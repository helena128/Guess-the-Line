import random
import Utility.soft_string_comparison
f = open('debug.log','a+')

songs = []
lines = [line.rstrip('\n') for line in open('guess-the-line-songs.txt')]
for line in lines:
  words = line.split("|")
  songs.append(words)
random.shuffle(songs)

score=0

songsused=[]
attemptcount=[]
for song in range(len(songs)):
    print("Here are lyrics from the song: ", songs[song][0]) #ввыводим первые 2 значения строки
    songsused.append(songs[song][1])
    print("The song was written/performed by: ", songs[song][2])
    for attempt in range(3):
        if(attempt>0):
            name=input('Try again attempt #' + str(attempt+1) + '> p') 
        else:
            name=input('Enter songs name > ')
        f.write(name.lower().strip()+ ("==" if Utility.soft_string_comparison.SoftStringComparison(name, songs[song][1])
            else "!=") +songs[song][1].lower().strip() + "\n") 
        if Utility.soft_string_comparison.SoftStringComparison(name, songs[song][1]):
            score+=1  #тут надо выйти из цикла
            break
    attemptcount.append(attempt+1)

print( "You got "+str(score)+" correct out of " + str(len(songs)) )
f.close()
#print(list(zip(songsused, attemptcount)))
print(str(songsused))
print(attemptcount)
r=list(map( lambda x, y: print(x,"=", y) , songsused, attemptcount ))
