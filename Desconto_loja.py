# Programa de cálculo de desconto progressivo
#Suellen Campos

# ===================== FUNÇÕES (no topo!) =====================
# DICA 2 IA:
# Pelas suas diretrizes, funções devem ficar no topo do script, antes de qualquer variável ou execução. 
# No seu código, a variável Valor_compra aparece antes da função.

def calcular_desconto(valor_compra):
    """Retorna a taxa de desconto conforme o valor da compra."""
    if valor_compra < 200:
        desconto = 0.05
    elif valor_compra < 500:
        desconto = 0.10
    else:
        desconto = 0.15
    return desconto


# ===================== PROGRAMA PRINCIPAL =====================

# Dados de Entrada:
valor_compra = float(input("Digite o Valor da Compra: R$ "))

## DICA IA SOBRE A FUNÇÃO calcular_desconto():
## Cada vez que você escreve calcular_desconto(Valor_compra), o Python roda a função inteira de novo. Isso é desperdício e pode causar bugs se a função tiver efeitos colaterais.
# Solução: Guarde o resultado em uma variável e use essa variável depois.

# Processamento:
taxa_desconto = calcular_desconto(valor_compra)  # ← chama 1x e guarda
valor_desconto = valor_compra * taxa_desconto    # ← calcula o valor em R$
valor_final = valor_compra - valor_desconto

# Saída:
print(f"\nValor da compra:      R$ {valor_compra:.2f}")
print(f"Desconto aplicado:    {taxa_desconto * 100:.0f}%")
print(f"Valor do desconto:    R$ {valor_desconto:.2f}")
print(f"Valor final da compra: R$ {valor_final:.2f}")