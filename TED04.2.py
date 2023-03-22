''''2. Problema: As maçãs custam R$ 1,30 cada, se forem compradas menos de uma dúzia, e R$ 1,00 se
forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas,
calcule e escreva o custo total da compra.
Aluno: Paulo Renan P1B'''

maça_comprada = int(input('Digite a quantidade de maçãs que deseja comprar:  '))

normal = float(maça_comprada * 1.30)
promo = float(maça_comprada * 1.00)

if maça_comprada <= 12:
    print(f'Valor da compra: R${normal}')
elif maça_comprada > 12:
    print(f'Valor da compra: R${promo}')