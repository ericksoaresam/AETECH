def descarte():
    while True:
        escolha = int(input("-----==========-----\nQual você deseja descartar?\n1- Plástico\n2- Papel\n3- Vidro\n4- Metal\n5- Madeira\n6- Orgânico\n7- Hospitalar\n0- Voltar ao menu\n-----==========-----\nEscolha uma opção: "))
        
        if escolha == 1:
            print("A melhor opção para o descarte de plástico é colocá-los em sacos biodegradáveis e deixá-los em aterros sanitários. Também é possível procurar um posto de coleta.")
        elif escolha == 2:
            print("A forma correta de descartar o papel é separá-lo do lixo comum e reciclá-lo. Afinal, o papel é um material reciclável, o que significa que pode ser transformado em novos produtos, como papelão, sacolas, papéis ondulados e até mesmo em papel para jornais.")
        elif escolha == 3:
            print("O ideal é embrulhá-lo em jornais e, depois disso, guardar em caixas de leite ou de papelão. Com isso, é praticamente impossível que o vidro fique para fora da embalagem e machuque alguém. Mas o descarte correto não termina aqui. Depois desse processo, você ainda deve depositar o material no local correto.")
        elif escolha == 4:
            print("Descarte as latinhas de cerveja, refrigerante e sucos, esquadrias e molduras de quadros, sempre prensadas ou amassadas para otimizar o armazenamento até o processo de reciclagem.")
        elif escolha == 5:
            print("Assim como entulho e móveis velhos não são considerados lixo domiciliar e devem ser encaminhados às Unidades de Recebimento de Pequenos Volumes (URPVs).")
        elif escolha == 6:
            print("O destino ideal para resíduos orgânicos é ser reciclado por meio de processos como a compostagem ou a biodigestão, que praticamente eliminam os problemas encontrados em lixões e aterros sanitários e devolvem aos resíduos orgânicos seu papel natural de fertilizar os solos.")
        elif escolha == 7:
            print("Os órgãos, tecidos, fluidos ou outro tipo de resíduo deve ser posto em dois sacos vermelhos (um dentro de outro) onde tenha o símbolo de risco infectante. Por fim, devem ser encaminhados para empresa especializada realizar a incineração.")
        elif escolha == 0:
            print("Voltando ao menu principal...")
            break
        else:
            print("Opção inválida. Por favor, escolha um número de 0 a 7.")

def calculo():
    num_dias = int(input("Quantos dias você deseja calcular a poluição? "))
    
    total_lixo = 0
    for i in range(num_dias):
        lixo_dia = float(input(f"Quantos gramas de lixo você descartou no dia {i+1}? "))
        total_lixo += lixo_dia
    
    media_lixo = total_lixo / num_dias
    
    print(f"Total de lixo descartado em {num_dias} dias: {total_lixo:.2f} gramas")
    print(f"Média de lixo descartado por dia: {media_lixo:.2f} gramas")
    if media_lixo > 1100:
        print("Você está acima da média da população e deve diminuir a quantidade de lixo produzida.")
    else:
        print("Parabéns! O seu uso está abaixo da média da população, continue assim!")


while True:
    menu = int(input("-----==========-----\n1- Descarte de lixo\n2- Calculo de poluição\n3- Outra opção\n0- Sair\n-----==========-----\nEscolha uma opção: "))
    
    if menu == 1:
        descarte()
    elif menu == 2:
        calculo()
    elif menu == 3:
        print("Outra opção em processo...")
    elif menu == 0:
        print("Saindo...")
        break
    else:
        print("Escolha uma opção válida.")
    
