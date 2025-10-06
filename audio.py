
import librosa
import soundfile as sf

# Load audio
y, sr = librosa.load("song.mp3")

# Change speed (e.g., 1.5x faster)
y_speed = librosa.effects.time_stretch(y, rate=1.5)

# Change pitch (e.g., up 4 semitones)
y_pitch = librosa.effects.pitch_shift(y_speed, sr=sr, n_steps=4)

# Save the modified audio
sf.write("song_modified.wav", y_pitch, sr)


# The code below processes the audio and saves it as a new file for download.
print("Audio processed and saved as song_modified.wav. You can now download this file.")
