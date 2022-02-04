from tweepy import OAuthHandler, API, StreamListener, Stream
from json import loads, dumps
from datetime import datetime
from dotenv import load_dotenv
import os

# Filtros de pesquisa
search = ["Twitter"]
 
# Tokens de acesso a API
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")
CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
 
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = API(auth) 
 
print('Adicionando e salvando os Tweets...')
 
class Output():
    def __init__(self):
        self.tweet_dates = [] # Criando Lista que salva as datas de cada Tweet     
        self.output = [] # Criando Lista que salva os tweets
        self.limit, self.count = 500, 0 # Criando contador e limite para o número de arquivos que devem ser salvos em cada JSON
        self.countname = 0

    def update(self, tweet):
        self.output.append(tweet) # Adicionando um tweet a lista "output"
        self.count += 1
        if self.count == self.limit: # Quando o contador chegar ao limite pré-definido é chamado a função "save"
            self.save()
            
    def save(self): 
        self.count = 0 # Reinicia o contador a uma unidade
        self.countname +=1
        print("Tweet salvo...")
        
    #Salvando os arquivos localmente
        with open(f'{self.countname}.json', 'w') as file:
            file.write(dumps(self.output))
        self.output.clear() # Limpa a lista "Output"
        self.tweet_dates.clear()  # Limpa a lista "tweet_dates"
        
class MyStreamListener(StreamListener):
    output = Output()
    def on_data(self, data):
        self.output.update(loads(data))
        
listener = MyStreamListener()
stream = Stream(auth, listener)
stream.filter(languages=["pt"], track = search)