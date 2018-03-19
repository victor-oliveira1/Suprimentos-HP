# Tinta-HP
usage: tinta_hp.py [-h] host  

Retorna o nível de tinta das tinta das impressoras em rede da HP  

positional arguments:  
  host        Endereço IP da impressora  

optional arguments:  
  -h, --help  show this help message and exit  
  -t TINTA, --tinta TINTA
                        Número da tinta

### Exemplo de uso:

python3 ./tinta_hp.py 196.1.1.49  
Magenta: 73%  
Cyan: 56%  
Yellow: 33%  
Black: 92%  
