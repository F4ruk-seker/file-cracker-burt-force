import os


class WordList:

    def __init__(self,path) :
        self.__BASE_PATH = path
        self.word_list_file_name = "wordlist.txt"
        self.word_list_path = os.path.join(self.__BASE_PATH,self.word_list_file_name)


    def create_new_word_list(self):
        open(self.word_list_path,"w").close()

    def open_word_list(self):
        os.startfile(self.word_list_path)

    def get_word_list_from_path(self):
        """
        wordlist.txt dosyasını okuyup bir liste halinde döndürmek istiyoruz
        if karşılanır yani word.txt varsa okur ve liste halinde dönüş yapar
        eğer doya yok ise wordlist.txt oluşturup sizden güncellemenizi ister
        :return:
        """
        if os.path.isfile(self.word_list_path):
            with open(self.word_list_path ,'r') as word_list_file:
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


