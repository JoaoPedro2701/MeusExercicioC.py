# tem que usar if/elif/else e algum operador de comparação
# fazer que o valor de um seja maior que o outro

primeiro_valor = input('Digite um valor? ')
segundo_valor = input('Digite outro valor? ')

if primeiro_valor > segundo_valor:
    print(
        f'{primeiro_valor=} e maior '
        f'do que {segundo_valor=}'
    )
else:
    print(
        f'{segundo_valor=} e maior '
        f'do que {primeiro_valor}'
    )
