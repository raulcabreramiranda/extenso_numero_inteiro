from pprint import pprint
from flask_restful import Resource

class extenso(Resource):
    palavras_extenso=()
  
    def __init__(self):
        self.palavras_extenso=(
                ("cero", "um","dois","três","quatro","cinco","seis","sete","oito","nove"),
                ("dez","onze","doze","treze","quatorze","quinze","dezesseis","dezessete","dezoito","dezenove"),
                ("vinte","trinta","quarenta","cinquenta","sessenta","setenta","oitenta","noventa"),
                ("cento","duzentos","trezentos","quatrocentos", "quinhentos","seiscentos","setecentos","oitocentos","novecentos")
            )

    def to_extenso(self, trio):
        """
        Retorna um trio por extenso.

        """
        extenso=[]
  
        if trio == '100':
            return 'cem'
        elif trio == '000':
            return 'zero'
        else:
            c, d, u = trio
            c, d, u = int(c), int(d), int(u)
  
            if c != 0:
                extenso.append(self.palavras_extenso[3][c-1])
            if d == 1:
                extenso.append(self.palavras_extenso[1][u])
            else:
                if d != 0:
                    extenso.append(self.palavras_extenso[2][d-2])
                if u != 0:
                    extenso.append(self.palavras_extenso[0][u])
        return ' e '.join(extenso)
  
    def get(self, num):
        """
        Algoritmo principal. Recebe um número na forma de
        string e retorna sua escrita em extenso.  
 
        """
  
        # Remove os zeros iniciais e faz padding
        # para números com quantidade de algarismos
        # não múltipla de 3

        menos_string = "";
        if num[0] == "-": 
          menos_string = "menos " 
          num = num.lstrip('-')
        if not(num.isdigit()):  return {"error": "O valor entrado nao e um numero valido"}, 500
        if(num == "0"): return {"extenso": self.palavras_extenso[0][0]}, 200

        num = num.lstrip('0')
        pad = 3 - len(num) % 3
        if pad < 3: num = '0'*pad + num

        if int(num) > 99999: return {"error": 'Número fora do intervalo. Os números podem estar no intervalo [-99999, 99999]'}, 500
        if int(num) < -99999: return {"error": 'Número fora do intervalo. Os números podem estar no intervalo [-99999, 99999]'}, 500


        it = iter(num)
        trioLista = [ ''.join([a,b,c]) for a, b, c in zip(it, it, it)]


  
        contador=0
        extensofinal=''
  
        for trio in reversed(trioLista):         
            if int(trio) > 0:
                extenso = self.to_extenso(trio)
                if contador > 0: extenso = extenso + ' ' + "mil"      
                if contador < (len(trioLista) - 1): extenso = ' e ' + extenso
     
                extensofinal = extenso + extensofinal
            contador = contador + 1
        return {"extenso": menos_string + extensofinal.rstrip('\n')}, 200