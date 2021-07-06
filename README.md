# k-vezesDigito
### Objetivo do algoritmo: Calcula o menor esforço para que um atleta percorra um determinado trajeto. 
Um atleta que faz caminhada deseja saber o esforço para subir ou descer um determinado trajeto do seu percurso. Dado que este percurso pode ter aclive e declive, um trajeto pode ser representado por vários pontos de alturas (Hi) e pode ser percorrido em dois sentidos: indo ou voltando. Faça um programa que receba a quantidade de pontos que um trajeto deverá conter e, em seguida, seu programa deverá receber as alturas que compõem aquele trajeto.

O algoritmo deverá receber um ou mais números inteiros, o primeiro será o número de pontos e os seguintes serão a altura de cada um. 

### Objetivos do exercicio:
- A partir do código base dentro de **exercicio.py**, você deverá validar o que já está escrito, realizando as modificações necessárias para a execução correta do algoritmo.
- Desenvolver a capacidade de detectar os casos de teste de um algoritmo

### Entrada
- Número inteiro tamanho de valor mínimo 2 e máximo 1000.
- Numeros inteiros de valor maior que 0 (quantidade de números definida pelo valor da variável tamanho). 

### Saída
- Valor do menor esforço possível para percorrer o trajeto ou string "entrada invalida".

### Observações
**Obs1.:** Seu programa deve calcular o esforço apenas quando há subidas e, portanto, não deve levar em conta que há esforço para descidas. 

**Obs2.:** O percurso pode ser percorrido em dois sentidos: da esquerda para direita (ponto inicial é a primeira altura do trecho e ponto final é a última altura do trecho) ou o contrário (ponto inicial é a última altura do trecho e o ponto final é a primeira altura do trecho).

**Obs3.:** As entradas deverão ser números inteiros, onde a quantidade de pontos do trajeto deverá ser no mínimo 2 e no máximo 1000.  As alturas deverão ser valores maiores que 0.

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

