from flask import Flask, request, jsonify
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

app = Flask(__name__)

# Carregar o modelo treinado
model_name = "./quantized_model"  # Certifique-se de que este caminho está correto
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
model.to("cpu")  # Use "cuda" se estiver disponível

@app.route('/generate', methods=['POST'])
def generate():
    try:
        # Capturar os dados recebidos
        data = request.json
        prompt = data.get('prompt', '')  # Use um valor padrão vazio
        
        if not prompt:  # Verificar se o prompt foi fornecido
            return jsonify({"error": "O campo 'prompt' está vazio ou ausente."}), 400

        # Gerar a resposta usando o modelo
        inputs = tokenizer(prompt, return_tensors="pt")
        outputs = model.generate(inputs["input_ids"], max_length=50, temperature=0.7)
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)
