def dna_5_3_para_rna_5_3(dna):
    '''
    Transforma uma string que representa uma fita de DNA em uma string que representa uma fita de RNA
    
    args:
        dna = string dna simples fita 5'-3'
    
    return:
        rna = uma string rna simples fitas 5'-3'
    '''
    #Coloca os caracteres em maiúsculo e troca timina(T) por uracila(U)
    rna_1 = dna.replace('a', 'A')
    rna_2 = rna_1.replace('t', 'T')
    rna_3 = rna_2.replace('g', 'G')
    rna_4 = rna_3.replace('c', 'C')
    rna = rna_4.replace('T', 'U')
    for c in rna: #Cria um laço para cada base da string 'rna'
        if c not in ['A', 'G', 'C', 'U']: #Se a base não for A G C ou U
            rna = rna.replace(c, '') #Apaga a base
    return rna

def protein_list_to_str(prot):
    '''
    Transforma uma lista de proteína numa string
    
    args:
        prot = uma lista de aminoácidos
        
    return:
        prot_2 = a lista de aminoácidos em string
    '''
    prot_2 = ''.join(prot)
    return prot_2

def rna_to_codon(rna):
    '''
    Transforma uma string de RNA numa lista de aminácidos possíveis
    
    args:
        rna = string de um RNA simples fita 5'-3'
    
    return:
        aa_list = uma lista de aminoácidos
    '''
    codon_dict = {
    'UUU': 'f', 'UUC': 'f', 'UUA': 'l', 'UUG': 'l',  # Fenilalanina (f), Leucina (l)
    'UCU': 's', 'UCC': 's', 'UCA': 's', 'UCG': 's',  # Serina (s)
    'UAU': 'y', 'UAC': 'y', 'UAA': '*', 'UAG': '*',  # Tirosina (y), Códons de terminação (*)
    'UGU': 'c', 'UGC': 'c', 'UGA': '*', 'UGG': 'w',  # Cisteína (c), Triptofano (w)
    'CUU': 'l', 'CUC': 'l', 'CUA': 'l', 'CUG': 'l',  # Leucina (l)
    'CCU': 'p', 'CCC': 'p', 'CCA': 'p', 'CCG': 'p',  # Prolina (p)
    'CAU': 'h', 'CAC': 'h', 'CAA': 'q', 'CAG': 'q',  # Histidina (h), Glutamina (q)
    'CGU': 'r', 'CGC': 'r', 'CGA': 'r', 'CGG': 'r',  # Arginina (r)
    'AUU': 'i', 'AUC': 'i', 'AUA': 'i', 'AUG': 'm',  # Isoleucina (i), Metionina (m, codon de início)
    'ACU': 't', 'ACC': 't', 'ACA': 't', 'ACG': 't',  # Treonina (t)
    'AAU': 'n', 'AAC': 'n', 'AAA': 'k', 'AAG': 'k',  # Asparagina (n), Lisina (k)
    'AGU': 's', 'AGC': 's', 'AGA': 'r', 'AGG': 'r',  # Serina (s), Arginina (r)
    'GUU': 'v', 'GUC': 'v', 'GUA': 'v', 'GUG': 'v',  # Valina (v)
    'GCU': 'a', 'GCC': 'a', 'GCA': 'a', 'GCG': 'a',  # Alanina (a)
    'GAU': 'd', 'GAC': 'd', 'GAA': 'e', 'GAG': 'e',  # Ácido aspártico (d), Ácido glutâmico (e)
    'GGU': 'g', 'GGC': 'g', 'GGA': 'g', 'GGG': 'g'   # Glicina (g)
} #Lista degenerada de códons, ou seja, trincas de bases que são traduzidas em seus respectivos aminoácidos



    codons = [rna[i:i+3] for i in range(0, len(rna), 3)] #Divide a string de RNA de três em três numa lista
    aa_list = []
    for item in codons: #Para cada trinca
        if item in codon_dict:#Se a trinca for uma chave do dicionário
            aa_list.append(codon_dict[item])#Adiciona o valor da chave na lista de aminoácidos
        else:
            aa_list.append('-')#Se não estiver colocar "-"
    return aa_list

def frame1(rna):
    '''
    Gera o frame 1 de aminoácidos
    
    args:
        rna = string de rna
    return:
        frame1str = frame 1 em string
    '''
    frame1 = rna_to_codon(rna) #chama a função rna to codon e gera a lista de aminoácidos
    frame1str = protein_list_to_str(frame1) #transforma em string
    return frame1str
def frame2(rna):
    '''
    Gera o frame 2 de aminoácidos, pulando a primeira base nitrogenada antes de transformar em codon
    
    args:
        rna = string de rna
    return:
        frame2str = frame 2 em string
    '''
    frame2 = rna_to_codon(rna[1:])#pega o rna e pula o primeiro item da lista e transforma em aa
    frame2str = protein_list_to_str(frame2)
    return frame2str
def frame3(rna):
    '''
    Gera o frame 3 de aminoácidos, pulando a segunda base nitrogenada antes de transformar em codon
    
    args:
        rna = string de rna
    return:
        frame3str = frame 3 em string
    '''
    frame3 = rna_to_codon(rna[2:])#pega o rna e pula o segundo item da lista e transforma em aa
    frame3str = protein_list_to_str(frame3)
    return frame3str

import re
def poss_prot(aastring):
    '''
    Transforma sequências de aminoácidos e em uma lista de possíveis proteínas
    
    args:
        aastring = uma string de aminoácidos
        
    return:
        prot_possíveis = Uma lista de strings com sequências de possíveis aminoácidos
        ou seja, que começem com m e terminem no codon de terminação '*'.
    '''
    m_to_codon_f = r"m(.*?)(?=\*)" #cria uma função em regex para achar todas os trechos entre m e *
    prot_possíveis = re.findall(m_to_codon_f, aastring) #aplica essa função do regex na string de aa
    prot_possíveis = ['m' + s for s in prot_possíveis] #coloca m n frente de todas prot pois o regex remove
    return prot_possíveis

def encontra_minimo_string(lista):
    #Retorna o valor minimo de uma lista de valores numéricos
    valor = lista[0]
    for n in lista:
        if len(n) < len(valor):
            valor = n
    return valor

def limpa_imposs(prots):
    '''
    Remove proteínas com menos de 20 aminoácidos.
    
    args:
        prots: uma lista de proteínas
        
    return:
        prots_certas: uma lista de proteínas maiores que 20 aminoácidos
    '''
    prots_certas = []
    for i in prots:
        if len(i) >= 20:
            prots_certas.append(i)
    return prots_certas

def best_prot(fr_1, fr_2, fr_3):
    '''
    Soma os três listas de proteínas em uma e coloca das maiores para as menores.
    
    args:
        fr_1 = Uma lista de (strings) proteínas (geralmente do frame1)
        fr_2 = Uma lista de (strings) proteínas (geralmente do frame2)
        fr_3 = Uma lista de (strings) proteínas (geralmente do frame3)
    return:
        pprotTlist_ord = A lista de proteínas total em ordem decrescente(por tamanho de string)
    '''
    pprot1 = ', '.join(fr_1)
    pprot2 = ', '.join(fr_2)
    pprot3 = ', '.join(fr_3)
    glue = ', '
    pprotT = pprot1 + glue + pprot2 + glue + pprot3
    pprotTlist = pprotT.split(glue)
    pprotTlist_ord = []
    while len(pprotTlist) != 0:
        minimo = encontra_minimo_string(pprotTlist)
        pprotTlist_ord.insert(0, minimo)
        lista.remove(minimo)
    return pprotTlist_ord

