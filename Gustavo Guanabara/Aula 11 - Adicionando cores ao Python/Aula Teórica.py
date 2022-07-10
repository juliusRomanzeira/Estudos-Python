#        
#                             -- Representação de cores em python --
#                        -- Padrão ANSI padrão de normalização global --
#                    Funciona em várias liguagens - A exemplos de C e Python
#              
#                              Estrutura é: \033[STYLE;TEXT;BACKm
# 
# TEXT - Cor do texto [30(white), 31(red), 32(green), 33(yellow),
#                      34(blue), 35(purple), 36(ciano), 37(gray)]
#
# BACK - Cor do fundo [40(white), 41(red), 42(green), 43(yellow),
#                      44(blue), 45(purple), 46(ciano), 47(gray)]
#
# STYLE - Tipo [0(none), 1(Bold), 4(underline), 7(negative colors)]
# 
# Todos são representados por números inteiros
#
print("\033[0;30mTeste\033[m \033[0;30mTeste\033[m \033[0;37;40m     \033[m")
print("\033[1;30mTeste\033[m \033[0;31mTeste\033[m \033[0;37;41m     \033[m") 
print("\033[4;30mTeste\033[m \033[0;32mTeste\033[m \033[0;37;42m     \033[m")
print("\033[7;30mTeste\033[m \033[0;33mTeste\033[m \033[0;37;43m     \033[m")
print("      \033[0;34mTeste\033[m \033[0;37;44m     \033[m")
print("      \033[0;35mTeste\033[m \033[0;37;45m     \033[m")
print("      \033[0;36mTeste\033[m \033[0;37;46m     \033[m")
print("      \033[0;37mTeste\033[m \033[0;37;47m     \033[m")
