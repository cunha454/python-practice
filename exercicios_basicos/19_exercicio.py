def calcular_imposto(renda):

    if renda <= 10_000:
        return 0
    elif renda <= 20_000:
        imposto_basico = (renda - 10_000) * 0.1
        return imposto_basico
    else:
        imposto_basico = (20_000 - 10_000) * 0.1
        imposto_extra = (renda - 20_000) * 0.2
        return imposto_basico + imposto_extra


resultado = calcular_imposto(45_000)
print(f"Imposto a ser pago: R$ {resultado:.2f}")