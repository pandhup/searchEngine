"""
author rochanaph
October 23 2017"""

import w3,w4,w5, os

def main():
    path = './text files'
    this_path = os.path.split(__file__)[0]
    path = os.path.join(this_path, path)

    # membaca sekaligus pre-processing semua artikel simpan ke dictionary
    articles = {}
    for item in os.listdir(path):
        if item.endswith(".txt"):
            with open(path + "/" + item, 'r') as file:
                articles[item] = w3.prepro_base(file.read())

    # representasi bow
    list_of_bow = [] # membuat list kosong
    for key, value in articles.items(): # iterasi pasangan key, value
        # print key, value
        list_token = value.split() # cari kata2 dengan men-split
        dic = w4.bow(list_token)   # membuat bow
        list_of_bow.append(dic)    # append bow ke list kosong yg di atas

    # membuat matrix
    matrix_akhir = w4.matrix(list_of_bow) # jalankan fungsi matrix ke list_of_bow

    # mencari jarak
    jarak = {}
    for key, vektor in zip(articles.keys(), matrix_akhir):
        jarak[key] = w5.euclidean(matrix_akhir[0], vektor) # simpan nama file sbg key, jarak sbg value
    return jarak

# print main()


# def findSim(pathfile, pathcorpus):
#     """
#     mencari jarak/similarity antara suatu file dengan sekumpulan file/corpus dalam folder.
#     :param pathfile: path tempat artikel yg dicari
#     :param pathcorpus: path tempat folder
#     :return: nama file, jarak terdekat
#     """

#     this_path = os.path.split(__file__)[0]
#     pathcorpus = os.path.join(this_path, pathcorpus)
#     pathfile   = os.path.join(this_path, pathfile)
#     # membaca sekaligus pre-processing semua artikel corpus simpan ke dictionary
#     articles = {}
#     for item in os.listdir(pathcorpus):
#         if item.endswith(".txt"):
#             with open(pathcorpus + "/" + item, 'r') as file:
#                 articles[item] = w3.prepro_base(file.read())

#     # tambahkan artikel yg dicari ke dictionary
#     findname = pathfile.split("/")[-1]
#     try:
#         articles[findname]
#     except:
#         with open(pathfile, 'r') as file:
#             articles[findname] = w3.prepro_base(file.read())

#     # representasi bow
#     list_of_bow = []
#     for key, value in articles.items():
#         list_token = value.split()
#         dic = w4.bow(list_token)
#         list_of_bow.append(dic)

#     # matrix
#     matrix_akhir = w4.matrix(list_of_bow)
#     # jarak
#     id_file = articles.keys().index(findname)    # index findname dalam articles.keys() = index dalam matrix
#     jarak = {}
#     for key, vektor in zip(articles.keys(), matrix_akhir):
#         if key != findname:
#             jarak[key] = w5.cosine(matrix_akhir[id_file], vektor)

#     return w4.sortdic(jarak, descending=True)


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

    # membuat list list_of_bow
    # yang kemudian dimasukan token-token unik di setiap dokumennya
    list_of_bow = []
    for key, value in articles.items():
        list_token = value.split()
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

    return w4.sortdic(presentase, descending=True)

#print findSim('./text files/ot_2.txt','./text files')
