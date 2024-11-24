from transformers import GPTNeoForCausalLM, AutoTokenizer
import torch

# Baixar o modelo GPT-Neo 1.3B e o tokenizer correspondente
model_name = "EleutherAI/gpt-neo-1.3B"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = GPTNeoForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16)
