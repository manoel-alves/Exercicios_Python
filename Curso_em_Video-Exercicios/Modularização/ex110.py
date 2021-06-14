from utilidadesCeV import moeda, dados

preco = dados.leiaDinheiro()
f = dados.check()

moeda.resumo(preco, 80, 35, f)