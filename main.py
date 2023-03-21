import threading

def process_records(records):
    # Kayıtları işleyen fonksiyon
    print(f"kayit alindi  {len(records)} \n" )

def split_records(records, num_threads):
    # Kayıtları eşit olarak bölüp thread'lere dağıtan fonksiyon
    chunk_size = len(records) // num_threads
    chunks = [records[i:i+chunk_size] for i in range(0, len(records), chunk_size)]
    return chunks

def process_with_threads(records, num_threads):
    chunks = split_records(records, num_threads)
    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=process_records, args=(chunks[i],))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()

if __name__ == '__main__':
    records = [i for i in range(5153)] # Kayıt listesi
    num_threads = 5
    process_with_threads(records, num_threads)
