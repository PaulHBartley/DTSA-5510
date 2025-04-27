import os
import pandas as pd

metadata_df = pd.read_csv('./data/bird_songs_metadata.csv')

wavfile_path = './data/wavfiles/'
wavfile_list = [f for f in os.listdir(wavfile_path) if f.endswith('.wav')]

metadata_filenames = metadata_df['filename'].tolist()

unmatched_files = [f for f in wavfile_list if f not in metadata_filenames]

print(f"Number of unmatched audio files: {len(unmatched_files)}")

for file in unmatched_files:
    os.remove(os.path.join(wavfile_path, file))
    print(f"Deleted: {file}")