from data.dataPrep import getData
from fastapi import FastAPI, HTTPException, Body

# Initiate App
app = FastAPI()

# Assign variable for data retrieval
# Data is a dictionary data type
data = getData()

# Decorator defines the endpoint 
# Function defined to return data on get request
@app.get('/')
def root():
    '''
    Full data will render when server is run
    
    '''
    return data

#Function defined to return filtered data object based on playlist name
@app.get('/{playlist}')
def playlist(playlist: str):
    '''
    This will retrieve information and filter the data based on the playlist name given
    
    '''
    if playlist in data:
        return data[playlist]
    else:
        # Error response from server
        raise HTTPException(status_code=404, detail="{} not found".format(playlist))
    
# Function defined to add data to a particular playlist
@app.post('/{playlist}')
def playlistAdd(playlist: str, track_data: dict = Body(...)):
    '''
    
    This will allow the user to add new songs/tracks to a playlist

    The Body(...) indicates that a parameter is required
    
    '''
    if playlist in data:
        # Assuming your data structure is a list of dictionaries for each playlist
        data[playlist].append(track_data)
        return {"message": "Track added to {}".format(playlist)}
    else:
        raise HTTPException(status_code=404, detail="{} not found".format(playlist))

