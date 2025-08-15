# Local Whisper ASR Fine-Tuning & Transcription

Welcome! This repository provides a framework for fine-tuning OpenAI's Whisper automatic speech recognition (ASR) model and running transcriptions **entirely locally**.  
It is designed for users who want to train on personal or sensitive audio data while keeping all models and processing on their own machine.

---

## Overview

This project allows users to:

- Fine-tune Whisper on their own datasets.  
- Run transcription using either a fine-tuned model or the base Whisper models.  

All processing is local, making this suitable for privacy-sensitive audio data. Evaluation of transcription performance (e.g., WER) is left to the user and can be done externally with preferred tools.

---

## Repository Structure

- **Finetuning/** – Scripts and instructions for preparing data and fine-tuning Whisper models.  
- **Transcribing/** – Scripts for using trained models (or base models) to transcribe audio files.  

Each folder contains its own `README.md` with detailed instructions.

---

## Key Features

- **Flexible Dataset Preparation:** Users provide a CSV with `file_name` (audio paths) and `transcription` columns.  
- **Preprocessing:** Audio resampling, feature extraction, and tokenization using Hugging Face `WhisperProcessor`.  
- **Fine-Tuning:** Adjustable model size, learning rate, batch size, and training steps.  
- **Local Execution:** All audio, models, and results stay on the user’s machine.  

---

## Results from Thesis Analysis

While the repository does not include example audio, research performed for the senior thesis explored how different fine-tuning strategies impact Whisper’s transcription accuracy in a medical domain:

- **Dataset:** Simulated audio clips representing proton therapy terminology.  
  - Two types: 1-word clips and 1-sentence clips  
  - ~30–40 training examples per dataset  
  - Separate evaluation dataset of ~15-second sections of simulated chart rounds  

- **Research Question 1:** Which type of training data performs better?  
  - **Result:** 1-sentence clips outperformed 1-word clips with ~5% lower word-error rate (WER).  
  - Insight: Training on full sentences allows the model to learn context and phrase structure.

- **Research Question 2:** Optimal training parameters (learning rate, number of steps)  
  - **Result:** Learning rate ~1e-7 performed best; number of steps had smaller effect.  
  - Over-training (high learning rate + high steps) reduced performance.  
  - Several fine-tuned models achieved better WER than the pre-trained Whisper baseline.

**Takeaway:** Fine-tuning Whisper on a small, domain-specific dataset with complete sentences and optimized parameters improves transcription accuracy, demonstrating a feasible approach for privacy-sensitive domains.

---

