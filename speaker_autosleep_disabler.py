import wave
import pyaudio

def play_file(filename: str) -> None:
    # Open the WAV file
    wav_file = wave.open(filename, "rb")

    # Initialize PyAudio
    audio = pyaudio.PyAudio()

    # Open a stream to play the WAV file
    stream = audio.open(
        format=audio.get_format_from_width(wav_file.getsampwidth()),
        channels=wav_file.getnchannels(),
        rate=wav_file.getframerate(),
        output=True
    )

    # Read the WAV file in chunks and write them to the stream
    chunk_size = 1024
    data = wav_file.readframes(chunk_size)
    while data:
        stream.write(data)
        data = wav_file.readframes(chunk_size)

    # Cleanup
    stream.stop_stream()
    stream.close()
    audio.terminate()
    wav_file.close()

while True:
    play_file(filename="WakeupHum.wav")
    # play_file(filename="BabyElephantWalk60.wav")
