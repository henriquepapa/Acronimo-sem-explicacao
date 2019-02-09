def saidaDeDados(i):
    i.replace( '.txt',"")
    nome=i
    arq=open(nome,'w')
    Totalp=0
    totalm=0
    siglas=[]
    
    
    for i in range(len(txt)):#percorre todas as posiçoes de meu vetor de frases
       
        Totalp=Totalp+contarpalavras(txt[i])#conta as palavras
        ax1,ax2=verificarmaiusculo(txt[i],i)
        totalm=totalm+ax1
        siglas.append(ax2)


    for i in imp:
        arq.write(i+' ')
    arq.close
