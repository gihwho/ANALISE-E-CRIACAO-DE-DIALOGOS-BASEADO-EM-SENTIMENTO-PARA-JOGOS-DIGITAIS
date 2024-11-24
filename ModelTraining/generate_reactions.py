from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Carregar o modelo e o tokenizer
model_name = "huggingface/llama-7b"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Lê a entrada do jogo
with open("reaction_input.txt", "r") as file:
    context = file.read()

# Configurar o prompt
prompt = (
    f"Imagine que unidades próximas testemunharam este evento: {context}.\n"
    "Escreva reações curtas e impactantes para cada unidade:\n"
    "1. "
)

# Gerar texto com o modelo
inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(
    inputs["input_ids"],
    max_length=100,
    num_return_sequences=5,  # Número de reações a gerar
    temperature=0.7,  # Controle da aleatoriedade
)

# Decodificar e salvar as falas geradas
with open("reaction_output.txt", "w") as file:
    for i, output in enumerate(outputs):
        reaction = tokenizer.decode(output, skip_special_tokens=True).strip()
        file.write(f"{reaction}\n")
