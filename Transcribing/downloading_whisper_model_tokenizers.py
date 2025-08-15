from transformers import WhisperTokenizer

# Specify the model name for Whisper (small, medium, or large)
model_name = "openai/whisper-small"

# Download the tokenizer
tokenizer = WhisperTokenizer.from_pretrained(model_name)

# Define the local directory where you want to save the tokenizer
local_dir = r"C:\Users\Vivian\PycharmProjects\WHISPER_Finetuning_and_Transcribing\transcribing\checkpoint-5"

# Save the tokenizer locally
tokenizer.save_pretrained(local_dir)

print(f"Tokenizer saved to {local_dir}")
