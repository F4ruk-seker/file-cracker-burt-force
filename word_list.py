import os
import time


class WordList:

    def __init__(self,path):
        """
        init func kurulumdan sonra sınıfa tanımlama yaparken kullanılır
        base dir dışardan verilemez
        documents in içine aktarılması tavsiye edilir
        :param path:
        """
        self.__BASE_PATH = path
        self.word_list_file_name = "wordlist.txt"
        self.word_list_path = os.path.join(self.__BASE_PATH,self.word_list_file_name)

    def create_new_word_list(self):
        """
        yeni bit wordlist.txt dosyası oluşturur
        :return:
        """
        open(self.word_list_path,"w").close()

    def open_word_list(self):
        """
        wordlist.txt dosyasını notpad ile açar
        :return:
        """
        os.startfile(self.word_list_path)

    def get_word_list_from_path(self):
        """
        wordlist.txt dosyasını okuyup bir liste halinde döndürmek istiyoruz
        if karşılanır yani word.txt varsa okur ve liste halinde dönüş yapar
        eğer doya yok ise wordlist.txt oluşturup sizden güncellemenizi ister
        :return:
        """
        if os.path.isfile(self.word_list_path):
            with open(self.word_list_path,'r',encoding='utf-8') as word_list_file:
                return word_list_file.read().split("\n")
        else:
            self.create_new_word_list()
            self.open_word_list()
            self.update_tracker()
            self.get_word_list_from_path()

    def update_tracker(self):
        """
        wordlist.txt dosyasının son güncelleme tarihini alıp güncellenmesini bekliyoruz
        :return: none (hiç bir şey void)
        """
        last_update_time = os.path.getmtime(self.word_list_path)
        while True:
            if os.path.getmtime(self.word_list_path) > last_update_time:
                break
            time.sleep(1)

