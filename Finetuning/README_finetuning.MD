# Finetuning Instructions

### A) Setup Steps
(everything should be done through project terminal except step 7)
1. Update pip
````
python.exe -m pip install --upgrade pip
````
2. Install requirements
````
pip install --upgrade datasets[audio] transformers accelerate evaluate jiwer tensorboard gradio
````
3. Check transformers:
````
python -c "from transformers import pipeline; print(pipeline('sentiment-analysis')('we love you'))"
#should return: [{'label': 'POSITIVE', 'score': 0.9998704791069031}]
````
4. Clone HuggingFace community events 
````
git clone https://github.com/huggingface/community-events.git
````
5. Install HuggingFace community events' requirements
````
pip install -r community-events/whisper-fine-tuning-event/requirements.txt
````
6. Install torch (from pytorch.org)

````
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
````

7. Check project is running on GPU (in console)
````
import torch
torch.__version__ # '2.3.1+cu121'
torch.cuda.is_available() #True
````

### B) Training Steps
1. Create a CSV with first column "file_name" with full path to audio files and a column "transcription" with the transcription of the corresponding audio file
2. Set metadata_path equal to r"fullpathtoCSV" in training.py
3. Edit training parameters such as whisper model (small, medium, or large) and training steps
4. Run training.py to get trained model
5. Follow README_transcribing.md to use the outputted trained model
