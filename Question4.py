from decimal import Decimal, getcontext


getcontext().prec = 8

def calcular_aproximacoes(calc_exato):
    # Realizar calculos com truncamento de 3 digitos
    resultado_truncado_3 = Decimal(calc_exato).quantize(Decimal('0.000'), rounding='ROUND_DOWN')
    
    # Realizar calculos com truncamento de 4 digitos
    resultado_truncado_4 = Decimal(calc_exato).quantize(Decimal('0.0000'), rounding='ROUND_DOWN')
    
    # Realizar calculos com arredondamento de 3 digitos
    resultado_arredondado_3 = Decimal(calc_exato).quantize(Decimal('0.000'), rounding='ROUND_HALF_UP')
    
    # Realizar calculos com arredondamento de 4 digitos
    resultado_arredondado_4 = Decimal(calc_exato).quantize(Decimal('0.0000'), rounding='ROUND_HALF_UP')
    
    erros_3 = {
        'truncado_absoluto': float(abs(calc_exato - resultado_truncado_3)),
        'arredondado_absoluto': float(abs(calc_exato - resultado_arredondado_3)),
        'truncado_relativo': float(abs(calc_exato - resultado_truncado_3) / abs(calc_exato)),
        'arredondado_relativo': float(abs(calc_exato - resultado_arredondado_3) / abs(calc_exato))
    }
    erros_4 = {
        'truncado_absoluto': float(abs(calc_exato - resultado_truncado_4)),
        'arredondado_absoluto': float(abs(calc_exato - resultado_arredondado_4)),
        'truncado_relativo': float(abs(calc_exato - resultado_truncado_4) / abs(calc_exato)),
        'arredondado_relativo': float(abs(calc_exato - resultado_arredondado_4) / abs(calc_exato))
    }
    
    return {
        'truncado_3': resultado_truncado_3,
        'truncado_4': resultado_truncado_4,
        'arredondado_3': resultado_arredondado_3,
        'arredondado_4': resultado_arredondado_4,
        'erros_3': erros_3,
        'erros_4': erros_4
    }

def imprimir_resultados(titulo, calc_exato, resultados):
    print(f'{titulo}\n Calculo exato: {calc_exato}\n')
    for k, v in resultados.items():
        print(f'{k}: {v}')
    print('\n')

    
    

def main():
    # Exemplo a) 133 - 0.499
    calc_exato_a = Decimal('133') - Decimal('0.499')
    resultados_a = calcular_aproximacoes(calc_exato_a)
    imprimir_resultados('Exemplo a) 133 - 0.499', calc_exato_a, resultados_a)
    
    # Exemplo b) x, tal que (1/3)*x**2 - (123/4)*x + (1/6) = 0
    calc_exato_b =  Decimal('1') / Decimal('3')
    resultados_b = calcular_aproximacoes(calc_exato_b)
    imprimir_resultados('Exemplo b) x, tal que (1/3)*x**2 - (123/4)*x + (1/6) = 0', calc_exato_b, resultados_b)
    
    # Exemplo c) ((13/4) - (6/7)) / (2e - 5.4)
    e = Decimal('2.7182818284590452353602874713527')
    calc_exato_c = (Decimal(13) / Decimal(4) - Decimal(6) / Decimal(7)) / ((Decimal('2') * Decimal(e)) - Decimal('5.4'))
    imprimir_resultados('Exemplo c) ((13/4) - (6/7)) / (2e - 5.4)', calc_exato_c, calcular_aproximacoes(calc_exato_c))
main()