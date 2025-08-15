# Transcribing Instructions

### A) Setup Steps
(everything should be done through project terminal except step 3)
1. Update pip
````
python.exe -m pip install --upgrade pip
````
2. Install transcribing requirements (cd to transcribing directory)
````
pip install -r requirements_transcribing.txt
````
3. Download ffmpeg (add ffmpeg ffplay and ffprobe .exe files to  transcribing directory)
4. Check project is running on GPU (in console)
````
torch.__version__ # '2.3.1+cu121'
torch.cuda.is_available() #True
````

### B) Transcribing Steps
1. Copy paste the checkpoint directory in outputted_trained_model to transcribing directory
2. Set model_id equal to r"full path to checkpoint directory" in transcribing.py
2. Add r"full path to checkpoint directory" to downloading_whisper_model_tokenizers.py in order to add tokenizers 
3. Change whisper model to right one (small, medium, or large) in downloading_whisper_model_tokenizers.py
4. Run downloading_whisper_model_tokenizers.py
6. Upload desired audio to transcribing directory 
7. Replace audiofile.mp3 with desired audio file in line 30 of transcribing.py: result = pipe("audiofile.mp3", generate_kwargs={"language": "english"})
8. Run transcribing.py for transcription
