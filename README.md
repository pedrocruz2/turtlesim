Instruções:

- Clone o Repositório utilizando o comando git ``` git clone git@github.com:pedrocruz2/turtlesim.git```
- rode o comando ``` cd turtlesim ``` para entrar na diretória raiz do workspace
- rode o comando ```colcon build ``` para compilar o pacote
- rode o comando ```ros2 run turtlesim turtlesim_node``` para iniciar o turtlesim


EM OUTRO TERMINAL:
- rode o comando ```source install/local_setup.bash``` para rodar os pacotes do diretório local
- rode o comando ```ros2 pkg executables desenhador``` para garantir que a instalação foi bem-sucedida, o output deve ser o seguinte:
```desenhador desenho
desenhador teste
desenhador teste2
desenhador desenho
```

- rode o comando ```ros2 run desenhador desenho``` e você verá uma tartaruga desenhando um círculo e ficará espantado com tamanha criatividade no desenvolvimento desse pacote ^^

NÃO FOI POSSÍVEL PROVIDENCIAR UM VÍDEO POIS NÃO CONSEGUI CONFIGURAR O GRAVADOR DE TELA NO UBUNTU <3
