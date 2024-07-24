import os
import wave

import pyaudio


class AudioRecorder:
    def __init__(self):
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100
        self.CHUNK = 1024
        self.audio = pyaudio.PyAudio()
        self.stream = None
        self.is_recording = False
        self.frames = []

    def start_recording(self):
        if self.stream is None:
            self.stream = self.audio.open(format=self.FORMAT,
                                          channels=self.CHANNELS,
                                          rate=self.RATE,
                                          input=True,
                                          frames_per_buffer=self.CHUNK)
            print("Recording...")
            self.is_recording = True
            self.frames = []
            
    def stop_recording(self):
        if self.stream is not None:
            self.stream.stop_stream()
            self.stream.close()
            self.is_recording = False
            print("Recording stopped.")
            self.save_recording()

    def save_recording(self):
        if not os.path.exists("recordings"):
            os.makedirs("recordings")

        wf = wave.open(f"recordings/recording.wav", 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(self.audio.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(self.frames))
        wf.close()
        print("Recording saved.")

    def playback_recording(self):
        if os.path.exists("recordings/recording.wav"):
            wf = wave.open("recordings/recording.wav", 'rb')
            stream = self.audio.open(format=self.audio.get_format_from_width(wf.getsampwidth()),
                                     channels=wf.getnchannels(),
                                     rate=wf.getframerate(),
                                     output=True)
            data = wf.readframes(self.CHUNK)

            while data:
                stream.write(data)
                data = wf.readframes(self.CHUNK)

            stream.stop_stream()
            stream.close()
        else:
            print("No recording found.")

if __name__ == "__main__":
    recorder = AudioRecorder()

    while True:
        print("\n1. Start Recording")
        print("2. Stop Recording")
        print("3. Playback Recording")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            if not recorder.is_recording:
                recorder.start_recording()
            else:
                print("Already recording.")
        elif choice == '2':
            if recorder.is_recording:
                recorder.stop_recording()
            else:
                print("Not currently recording.")
        elif choice == '3':
            recorder.playback_recording()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
