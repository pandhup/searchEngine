"""
author rochanaph
October 23 2017"""

import w3,w4,w5, os

#reload(sys)  
#sys.setdefaultencoding('utf8')

def findSim(keyword, path):

    # membuat dictionary articles
    # membaca semua file .txt yang berada di direktori path(text files)
    # kemudian dimasukan kedalam dictionary articles dengan nama item/index(nama dokumen)
    articles = {}
    for item in os.listdir(path):
        if item.endswith(".txt"):
            with open(path + item, 'r') as file:
                articles[item] = w3.prepro_base(file.read())

    # memasukan kata kunci kedalam dictionary dengan nama item/index(keyword_index)
    # kemudian dimasukan ke dictionary articles dengan value keyword yang dimasukan
    kata_kunci = 'keyword_index'
    articles[kata_kunci] = w3.prepro_base(keyword)
    #menampilkan isi deskripsi sesuai dengan token yang ada 
    isi_doc = {}
    for isi in os.listdir(path):
     if isi.endswith(".txt"):
         with open(path + isi,'r') as file:
             isi_doc[isi] = file.readline()
             

    # membuat list list_of_bow
    # yang kemudian dimasukan token-token unik di setiap dokumennya
    list_of_bow = []
    for key, value in articles.items():
        list_token = value.split(".")
        dic = w4.bow(list_token)
        list_of_bow.append(dic)

    # membuat matrix tiap-tiap dokumen dengan token unik dari semua dokumen
    matrix_akhir = w4.matrix(list_of_bow)

    # mencari id/urutan keyword_index
    # membuat dictionary presentase untuk semua dokumen
    id_keyword = articles.keys().index(kata_kunci)
    presentase = {}
    for key, vektor in zip(articles.keys(), matrix_akhir):
        if key != kata_kunci:
            presentase[key] = w5.cosine(matrix_akhir[id_keyword], vektor)
    

    return w4.sortdic(presentase,baris , descending=True)

path="./text files/"
keyword="JAKARTA"
baris = []
for item in os.listdir(path):
    if item.endswith(".txt"):
        files = open(path + item, 'r', encoding = 'utf-8')
        for line in files:
             if keyword in line: baris.append(line)
print(baris)
    