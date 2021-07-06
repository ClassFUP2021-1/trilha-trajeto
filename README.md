# k-vezesDigito
### Objetivo do algoritmo: Verifica quantas vezes um dígito aparece em um determinado número de telefone (celular ou fixo). 
O algoritmo deverá receber dois números inteiros, o primeiro será o número que deve ser verificado e o segundo será o número do telefone. 

### Objetivos do exercicio:
- A partir do código base dentro de **exercicio.py**, você deverá validar o que já está escrito, realizando as modificações necessárias para a execução correta do algoritmo.
- Desenvolver a capacidade de detectar os casos de teste de um algoritmo

### Entrada
- Número inteiro X entre 0 e 9.
- String Y com 8 dígitos ou 9 dígitos. 

### Saída
- Quantidade de vezes que o primeiro número (X) aparece no segundo número (Y) ou string "entrada invalida".

### Observações
**Obs1.:** O número do telefone Y (fixo ou celular) não deve iniciar por 0 ou uma sequência de 0s, caso seja, informar ao usuário ‘entrada invalida’. Tratar outros casos inválidos conforme descrição de entrada do problema, nesse caso informar também ‘entrada invalida’.

**Obs2.:** Não é permitido manipular os dados de entrada como listas e não se deve usar funções de contagem e de pesquisa como o count(), find(), ou outras funções de listas/strings. Caso seja utilizado, a resolução não será corrigida e não será atribuída pontuação.

**Obs3.:** Podem manipular como Strings, por exemplo, a entrada do telefone. O envio máximo permitido desta questão é até 2 vezes.

### Exemplos
| Numero inteiro X | String Y | Saida |
| ------ | ------ | ------ |
| 1 | 656789110 | 2 |
| 0 | 00000000 | entrada invalida |

### Instruções gerais
- Escreva seu código dentro do arquivo **exercicio.py**
- Escreva os casos de teste do algoritmo dentro do arquivo **casosDeTeste.py**
- Dentro do arquivo **exercicio.py** existe um código que resolve parcialmente o problema. Vocé deverá validar o que está escrito, realizando as modificações necessárias para a execução correta do algoritmo.
- Dentro do arquivo **casosDeTeste.py** existe uma estrutura no formato: { "X-Y": "saida" }, onde X e Y são as entradas já descritas e devem ser separadas po hífen. Você deverá inserir seus casos de teste nele. Por exemplo, {"1-656781111" : "4"} significa que as entradas serão **X = 1**, **Y = 656781111** e a saida será **4**. Para inserir um novo caso de teste como, por exemplo,{"0-00000000" : "entrada invalida"}, basta inserir uma virgula e adicionar os novos dados, como no exemplo abaixo:
```sh
{"1-656781111" : "4",
"0-00000000" : "entrada invalida"}
```
- Após a codificação do algoritmo não esqueça de **commitar as mudanças** clicando no botão commit **changes**.
- Dentro do arquivo **exercicio.py** existem duas variáveis: **num1** e **num2** que representam **X** e **Y** respectivamente. Ou seja, você deverá usa-las como entradas do seu algoritmo. Note, que esse algoritmo não recebe as entradas através do ``` input()``` e sim através de ``` sys.argv[1]``` e ``` sys.argv[2]```. Para a codificação do algoritmo na sua máquina, você poderá ``` input()``` normalmente, mas não se esqueça de altera-lo para ``` sys.argv[1]``` e ``` sys.argv[2]``` no momento de submeter seu código.
- Em hipótese alguma você deverá alterar o código do arquivo exercicio_test.py, caso seja detectada alguma alteração, sua resolução será desconsiderada.

