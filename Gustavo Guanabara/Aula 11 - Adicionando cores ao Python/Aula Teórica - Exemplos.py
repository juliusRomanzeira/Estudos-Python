a, b = 3, 5
cores = {"limpa":"\033[m", "vermelho":"\033[31m", "verde":"\033[32m", "azul":"\033[34m"}
print("Os valores são {}{}{} e {}".format(cores["vermelho"], a, cores["limpa"], b))