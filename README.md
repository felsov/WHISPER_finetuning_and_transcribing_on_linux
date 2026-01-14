# Finetuning OpenAI's Audio Transcription Model 

Welcome! 
-> This repository provides an outline for fine-tuning OpenAI's Whisper automatic speech recognition (ASR) model **with your own data**. It also provides an outline for running transcriptions with the trained model (or the base models of Whisper.)
-> It is all done **entirely locally** on your machine, making it ideal for those who need to train on person or sensitive audio data and do not want to risk it being leaked.
-> This project was done on a Linux machine, however, with few edits, it remains a similar process for Windows
-> The source of this code came from https://huggingface.co/blog/fine-tune-whisper , a finetuning event for multilingual language training of Whisper

---

## Repository Structure

-> **Finetuning/** – skeleton for preparing data and fine-tuning your own Whisper models
-> **Transcribing/** – skeleton for using trained models (or base Whisper models) to transcribe your own audio files

Each folder contains its own `README.md` with more detailed instructions.

---

## How to Best Train (Results from a Thesis Analysis)

This project stemmed from an internship project at Emory Proton Center and was then fully fledged out later during a senior thesis project at Agnes Scott College. The thesis analysed the best methods of training the system for medical terminology (analyzing different datasets and training parameters.) While the repository does not include example audio, the following outlines the type of datasets used for the analysis.

- **Dataset:** Simulated audio clips representing proton therapy terminology.  
  - Two types: 1-word clips and 1-sentence clips  
  - ~30–40 training examples per dataset  
  - Separate evaluation dataset of ~15-second sections of simulated chart rounds

The results indicate the following (however, it is important to keep in mind datasets have one of the biggest impacts:)

- **Results:**
  - 1-sentence clips outperformed 1-word clips with ~5% lower word-error rate (WER).  
  - Altering the learning rate had a larger impact than the number of steps.
  - Over-training (high learning rate + high steps) reduced performance.


---

