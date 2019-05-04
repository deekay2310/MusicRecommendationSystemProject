
import Recommenders as Recommenders
import Data as Data

def similar_recommender(user_song, user_artist):
    '''
    similarity based recommendations
    '''
    sbr = Recommenders.item_similarity_recommender_py()

    #model created
    sbr.create(Data.train_data, 'user_id', 'song')

    #taking input from user
    user_input = user_song+" - "+user_artist

    #recommendations received as a panda dataframe
    recommendation_frame = sbr.get_similar_items([user_input])

    #dataframe typecasted into a python list
    recommendation_list = list(recommendation_frame['song'])
    print(recommendation_list)
    return recommendation_list
    

def popular_recommender():
    '''
    popularity based recommendations
    '''

    pbr = Recommenders.popularity_recommender_py()
    
    #model created
    pbr.create(Data.train_data, 'user_id', 'song')
    
    #creating a user variable
    user_id_variable = Data.users[69]
    
    #recommendations received as a panda dataframe
    popular_frame = pbr.recommend(user_id_variable)
    
    #dataframe typecasted into a python list
    popular_list = list(popular_frame['song'])
    print(popular_list)
    return popular_list
