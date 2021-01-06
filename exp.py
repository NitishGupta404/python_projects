import requests
import json
import webbrowser






print("Enter the name of the movie/series")
name=input()

r=requests.get(f"http://www.omdbapi.com/?t={name}&plot=full&apikey=a98c33eb").text

moviedata=json.loads(r)
print(moviedata)
try:
    m_name=moviedata['Title']
    print(m_name)
except:
    print("Please check the spelling")
try:
    m_release=moviedata['Released']
    print(m_release)
except:
    print("N/A")
try:
    m_length=moviedata['Runtime']
    int_m_len = m_length.replace(" min", "")
    int_m_len = int(int_m_len)
    int_m_len = int_m_len / 60
    print(int_m_len, "hr")

except:
    print("N/A")
try:
    m_genre=moviedata['Genre']
    print(m_genre)
except:
    print("N/A")
try:
    m_cast=moviedata['Actors']
    print(m_cast)
except:
    print("N/A")
try:
    m_plot=moviedata['Plot']
    print(m_plot)
except:
    print("N/A")

try:
    m_rating=moviedata['imdbRating']
    print(m_rating)
except:
    print("N/A")







try:
    pass
except Exception as e:
    print("no data found")



