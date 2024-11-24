from transformers import GPTNeoForCausalLM, AutoTokenizer
from optimum.intel.neural_compressor import INCQuantizer
from neural_compressor.config import PostTrainingQuantConfig, AccuracyCriterion, TuningCriterion
import torch

# Nome do modelo pré-treinado
model_name = "EleutherAI/gpt-neo-1.3B"

# Carregar o tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Carregar o modelo
model = GPTNeoForCausalLM.from_pretrained(model_name)

# Configuração de critério de precisão
accuracy_criterion = AccuracyCriterion(
    higher_is_better=True,
    criterion='relative',
    tolerable_loss=0.05  # Permitir perda relativa de até 5%
)

# Configuração de critério de tuning
tuning_criterion = TuningCriterion(
    strategy="basic",
    timeout=300,       # 5 minutos de timeout
    max_trials=500     # Até 500 tentativas
)

# Configuração de quantização
quantization_config = PostTrainingQuantConfig(
    approach="dynamic",
    accuracy_criterion=accuracy_criterion,
    tuning_criterion=tuning_criterion
)

# Inicializar o quantizador
quantizer = INCQuantizer.from_pretrained(model)

# Diretório para salvar o modelo quantizado
quantized_model_dir = "./quantized_model"

# Função de avaliação (opcional)
def evaluation_function(model):
    return 0.99  # Simula uma avaliação com alta precisão

# Aplicar quantização com save_directory
quantized_model = quantizer.quantize(
    quantization_config=quantization_config,
    save_directory=quantized_model_dir,
    eval_func=evaluation_function  # Avaliação opcional
)

# Salvar o tokenizer no mesmo diretório
tokenizer.save_pretrained(quantized_model_dir)

print("Modelo quantizado salvo com sucesso em:", quantized_model_dir)
