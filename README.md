# PI-05-IA-Tetris

## Instalação

Para esse PI utilizamos o Python 3.7, pois, segundo a documentação do gym tetris, era a última versão suportada.
### Virtual Enviroment
```
pip install virtualenv
```
Usamos o virtual env para gerenciar os pacotes em um enviroment do Python isolado.  <a href="https://pypi.org/project/virtualenv/1.7.1.2/">Documentação</a>  
\
Para criar o enviroment usamos `virtualenv <NOME> -p "<PATH>"` no terminal, dentro do diretório, para criar.  
No nosso caso:  
* `<NOME>` -> usamos "t" como nome
* `<PATH>` Caminho para o executavel da versao do pyhton a ser usada, para nós Python 3.7  
  
Para ativar, no windows utilizamos o comando `t\Scripts\activate`, onde "t" é o nome do enviroment.

No linux `$ source <NOME>/bin/activate`

Para sair do Vitual Env. o comando é `deactivate`

### Biblioteca
Uma vez ativada, instalamos as bibliotecas a seguir, utilizando o Python 3.7

```
pip3.7 install gym-tetris
pip3.7 install tensorflow
pip3.7 install opencv-python
```

[gym_tetris](https://pypi.org/project/gym-tetris/): "An OpenAI Gym environment for Tetris on The Nintendo Entertainment System (NES) based on the nes-py emulator."

[tensorflow](https://www.tensorflow.org/): "A principal biblioteca de código aberto para desenvolver e criar modelos de ML."  

[opencv-python](https://pypi.org/project/opencv-python/): "Pre-built CPU-only OpenCV packages for Python."  

Depois só executar `py main.py` com o virtualenv ativo para começar o treinamento.  
