import pickle
from exception import CustomException
import sys


try:
    with open('src/df_cleaned.pkl', 'rb') as f:
        df = pickle.load(f)

    with open('src/tfidf_matrix.pkl', 'rb') as f:
        tfidf_matrix = pickle.load(f)

    with open('src/consin_sim.pkl', 'rb') as f:
        consin_sim = pickle.load(f)

except Exception as ex:
    raise CustomException(ex,sys)

def recommand_song(song_name,top_n=5):
    #find the index of the song 
    idx = df[df['song'].str.lower() == song_name.lower()].index
    if len(idx) == 0 :
        return "Song not found in the dataset"
    idx = idx[0]

    #get simalarity scores
    sim_scores = list(enumerate(consin_sim[idx]))
    sim_scores = sorted(sim_scores,key=lambda x:x[1],reverse=True)
    sim_scores = sim_scores[1:top_n+1]

    #get song indices
    song_indices = [i[0] for i in sim_scores]

    # Return top n similar songs
    result = df[['artist', 'song']].iloc[song_indices].reset_index(drop=True)
    result.index = result.index + 1
    result.index.name = "S.NO."


    return result   
