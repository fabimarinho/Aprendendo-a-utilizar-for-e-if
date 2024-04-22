vendas = [1200, 300, 800, 1500, 1900, 2750, 400, 20, 23, 70, 90, 80, 1100, 999, 900, 880, 870, 50, 1111, 120, 300, 450, 800]
meta = 1000

funcionarios_meta_alcancada = 0
for venda in vendas:
    if venda >= meta:
        funcionarios_meta_alcancada += 1
        
print(funcionarios_meta_alcancada)
