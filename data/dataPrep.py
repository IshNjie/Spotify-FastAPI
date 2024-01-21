import csv

def getData():
    # Assuming your CSV file is named 'playlist_data.csv'
    data_path = 'data/PlaylistListing.csv'

    # Create an empty dictionary to store the playlist data
    playlist_dict = {}

    # Read the CSV file
    with open(data_path, newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)

        # Iterate through each row in the CSV file
        for row in csv_reader:
            # Extract relevant information from the row
            playlist_name = row['PlaylistName']
            track_name = row['TrackName']
            artist_name = row['ArtistName']
            album_name = row['AlbumName']
            date_added = row['DateAdded']

            # Create a dictionary for the current row
            track_info = {'TrackName': track_name, 'ArtistName': artist_name, 'AlbumName': album_name, 'DateAdded': date_added}

            # Check if the playlist name is already a key in the dictionary
            if playlist_name in playlist_dict:
                # Append the current track information track_info) to the existing playlist
                playlist_dict[playlist_name].append(track_info)
            else:
                # Create a new entry for the playlist name with the track information (track_info)
                playlist_dict[playlist_name] = [track_info]

    return playlist_dict
