from nltk.tokenize import word_tokenize,sent_tokenize
import glob,os

def contarpalavras(frase): 
    
    return frase.count(' ')+1 # retorna a quantidade de espaços na frase



    
def verificasigla(palavra,frase,i):
    veri=0
    teste=1
    vogais = ['a', 'e', 'i', 'o', 'u',"é",'ê','ó','ì','í','ô','á','â','ú','û','m','s','l','r','ã']
            
    
    for letra in palavra:
        if letra.isupper() or letra == '-':#verifica se reconhece Z
            veri=veri+1
    if veri==len(palavra) and veri>1 and palavra!= "--" :#verifica se toda palavra ta em caixa alta
            return 1

    for vogal in vogais:
        if palavra[len(palavra)-1]==vogal:
            teste=0

    if i>0 and i<len(frase)-1:

        if teste==1 and palavra[0].isupper() and len(palavra)>1 and frase[i-1]!='.' and (not(frase[i-1][0].isupper() or frase[i+1][0].isupper())) :
            return 1
    else:
        return 0
        
        

def verificavirguladepois(palavra,token,i):
    tamanho= len (token)# Tamanho da Frase 
    tsigla= len (palavra)# Tamanho da Sigla
    verifica=0
    letras=[]
    
    for letra in palavra:
        if letra != '-':
            letras.append(letra)

    
    if token[i+1] == "," or token[i+1] == ")" or token[i+1] == "-":# verifica se depois da sigla tem ) ou , ou -
        cont=i+2# caminha pra frente na frase
        
        while cont!= tamanho:
            if verificasigla(token[cont],token,cont)or token[cont] ==',' or token[cont]=='.':# se encontar uma , ou . ou outra sigla ele para a verificação.
                break
            p=token[cont]
            if p[0].lower() == letras[0] or p[0].upper() ==letras[0] :# verifica se a palavra começa com letra maiuscula
                letras.remove(letras[0])
                if len(letras)==0:
                    break
            cont=cont+1
        if len(letras)==0:# se o total de palavras começando com letra maiuscula for igual ao total de letras da sigla o significado foi dado
            return 1
        else:
            return 0
    else:
        return 0

    
    

def verificaantes(palavra,token,i):
    tsigla= len (palavra)
    verifica=0
    letras=[]
    
    for letra in palavra:
        if letra != '-':
            letras.append(letra)

            
    if token[i-1] == "," or token[i-1] == "("  or token[i-1] == "-" : # verifica se antes da sigla tem ) ou , ou -
        cont=i-1 # caminha para tras na frase
        
        while cont !=0:
            
            if verificasigla(token[cont],token,cont) or token[cont]==',' or token[cont]=='.': # se encontar uma , ou . ou outra sigla ele para a verificação.
                return 0
                break
            
            p= token[cont]
            
            if p[0].lower() == letras[len(letras)-1] or p[0].upper() ==letras[len(letras)-1] :# verifica se a palavra começa com letra maiuscula
                letras.remove(letras[len(letras)-1])
                if len(letras)==0:
                    return 1
            cont=cont-1
        if len(letras)==0:
            return 1
        else:
            return 0
    else:
        return 0

def verificarmaiusculo(frase,n):#chama os dois metodos de verificaçao 
    palavras =word_tokenize(frase)
    maiusculas=0
    sigla=""
    for i, palavra in enumerate(palavras):
        
        if verificasigla(palavra,palavras,i):
            maiusculas=maiusculas+1
            sigla=sigla+ "\n"+palavra +" Encontrada em S"+str(n+1)            


            sigla=sigla+ '-Erro Acronomo sem explicacao'

            
            if i< len(palavras)-2:
                if verificavirguladepois(palavra,palavras,i):
                    sigla=sigla.replace( '-Erro Acronomo sem explicacao',"")
            if i>2:     
                if verificaantes(palavra,palavras,i):
                    print(sigla)
                    sigla=sigla.replace( '-Erro Acronomo sem explicacao',"")
            
    return (maiusculas,sigla);
                   


        
def saidaDeDados(i):
    i.replace( '.txt'," -Saida")
    nome=i
    arq=open(nome,'w')
    arq.write('Resultado da analise do arquivo' +"\n\n\n")
    Totalp=0
    totalm=0
    siglas=""
    
    
    for i in range(len(txt)):#percorre todas as posiçoes de meu vetor de frases
       
        arq.write('\n S')
        arq.write(str(i+1)+"- ")
        arq.write(txt[i])
        Totalp=Totalp+contarpalavras(txt[i])#conta as palavras
        ax1,ax2=verificarmaiusculo(txt[i],i)
        totalm=totalm+ax1
        siglas= siglas+ax2
    arq.write("\n \n O total de palavras he =")
    arq.write(str(Totalp))
    arq.write("\n \n O total de Siglas he=")
    arq.write(str(totalm))
    arq.write("\n\n As siglas econtrdadas foram"+"\n")
    arq.write(siglas)
    arq.close
cont=1
os.chdir("C:\\Users\\henri\\Documents\IC\\textos")
for i in glob.glob("*.txt"):

    arquivo=open(i,'r');
    
    texto=arquivo.read()#le o aqrquivo todo
    
    
    txt=sent_tokenize(texto)#divide o arquivo em frases
        
    saidaDeDados(i)
    cont+=1
