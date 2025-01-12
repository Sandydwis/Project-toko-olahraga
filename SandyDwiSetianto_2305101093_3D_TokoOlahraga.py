class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

class Barang:
    def __init__(self, kode, nama, stok):
        self.kode = kode
        self.nama = nama
        self.stok = stok
    def __lt__(self, other):
        return self.kode < other.kode

    def __eq__(self, other):
        return self.kode == other.kode

class LinkedList:
    def __init__(self):
        self.head = None
        
    def add_to_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def find(self, kode):
        current = self.head
        while current:
            if current.data.kode == kode:
                return current.data
            current = current.next
        return None

    def update_stock(self, kode, jumlah):
        barang = self.find(kode)
        if barang:
            barang.stok += jumlah
            print("Stok barang berhasil diperbarui.")
        else:
            print("Barang tidak ditemukan.")

    def display(self):
        current = self.head
        while current:
            print(f"Kode: {current.data.kode}, Nama: {current.data.nama}, Stok: {current.data.stok}")
            current = current.next

    def sort(self):
        if self.head is None:
            return
        
        sorted = False
        while not sorted:
            sorted = True
            current = self.head
            while current.next:
                if current.data.kode > current.next.data.kode:
                    current.data, current.next.data = current.next.data, current.data
                    sorted = False
                current = current.next

class Stack:
    def __init__(self):
        self.items = []


    def add_to_stack(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def is_empty(self):
        return len(self.items) == 0

class TreeNode:
    def __init__(self, barang):
        self.barang = barang
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def add_to_tree(self, barang):
        if not self.root:
            self.root = TreeNode(barang)
        else:
            self._insert_recursively(self.root, barang)

    def _insert_recursively(self, current_node, barang):
        if barang < current_node.barang:
            if current_node.left is None:
                current_node.left = TreeNode(barang)
            else:
                self._insert_recursively(current_node.left, barang)
        elif barang > current_node.barang:
            if current_node.right is None:
                current_node.right = TreeNode(barang)
            else:
                self._insert_recursively(current_node.right, barang)

    def search(self, kode):
        return self._search_recursively(self.root, kode)

    def _search_recursively(self, node, kode):
        if node is None or node.barang.kode == kode:
            return node.barang if node else None
        if kode < node.barang.kode:
            return self._search_recursively(node.left, kode)
        return self._search_recursively(node.right, kode)

    def inorder_traversal(self):
        return self._inorder(self.root)

    def _inorder(self, node):
        if node is None:
            return []
        return self._inorder(node.left) + [node.barang] + self._inorder(node.right)

class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, barang):
        if barang.kode not in self.graph:
            self.graph[barang.kode] = []

    def add_edge(self, barang1, barang2):
        if barang1.kode in self.graph and barang2.kode in self.graph:
            self.graph[barang1.kode].append(barang2.kode)
            self.graph[barang2.kode].append(barang1.kode)

    def get_neighbors(self, kode):
        return self.graph.get(kode, [])

    def display(self):
        for node, neighbors in self.graph.items():
            print(f"Barang Kode {node} memiliki hubungan dengan barang: {', '.join(neighbors)}")

data_barang = LinkedList()
binary_tree = BinaryTree()
graph = Graph()

def tambah_data_barang_nama():
    nama_barang = [
        Barang("K1", "Sepatu", 100),
        Barang("K2", "Bola", 50),
        Barang("K3", "Jersey", 75),
        Barang("K4", "Raket", 30),
        Barang("K5", "Celana", 20),
        Barang("K6", "Topi", 15),
        Barang("K7", "Dekker", 40),
        Barang("K8", "Tas", 60),
        Barang("K9", "Kacamata", 25),
        Barang("K10", "Sandal", 80)
    ]
    
    for barang in nama_barang:
        data_barang.add_to_end(barang)
        binary_tree.add_to_tree(barang)
        graph.add_node(barang)

tambah_data_barang_nama()

def metode_pembayaran():
    print("Pilih metode pembayaran:")
    print("1. Tunai")
    print("2. Debit card")
    print("3. Qris")
    pilihan_pembayaran = input("Masukkan pilihan Anda: ")

    if pilihan_pembayaran == '1':
        metode = "Tunai"
    elif pilihan_pembayaran == '2':
        metode = "Debit card"
        print("Pilih jenis pembayaran debit:")
        print("1. Bank Central Indonesia (BCA)")
        print("2. Bank Nasional Indonesia (BNI)")
        print("3. Livin Mandiri")
        print("4. Bank Rakyat Indonesia (BRI)")
        print("5. Bank Syariah Indonesia (BSI)")
        print("6. Bank Jatim")
        print("7. Bank Danamon Indonesia")
        pilihan_debit = input("Masukkan pilihan jenis pembayaran debit: ")

        if pilihan_debit == '1':
            metode = "Bank Central Indonesia (BCA)"
        elif pilihan_debit == '2':
            metode = "Bank Nasional Indonesia (BNI)"
        elif pilihan_debit == '3':
            metode = "Livin Mandiri"
        elif pilihan_debit == '4':
            metode = "Bank Rakyat Indonesia (BRI)"
        elif pilihan_debit == '5':
            metode = "Bank Syariah Indonesia (BSI)"
        elif pilihan_debit == '6':
            metode = "Bank Jatim"
        elif pilihan_debit == '7':
            metode = "Bank Danamon Indonesia"
        else:
            print("Pilihan tidak valid.")
            return
    elif pilihan_pembayaran == '3':
        metode = "Qris"
    else:
        print("Pilihan tidak valid.")
        return

    jumlah_bayar = int(input("Masukkan jumlah pembayaran: "))
    print(f"Pembayaran dengan metode {metode} sebesar {jumlah_bayar} berhasil diproses.")

def tampilkan_menu():
    print("\nPilihan Menu:")
    print("1. Tambah Data Barang")
    print("2. Cari Data Barang")
    print("3. Update Stok Barang")
    print("4. Tampilkan List Barang")
    print("5. Metode Pembayaran")
    print("6. Gunakan Stack")
    print("7. Gunakan Queue")
    print("8. Gunakan Tree")
    print("9. Gunakan Graph")
    print("10. Keluar")

stack_barang = Stack()
queue_barang = Queue()

while True:
    tampilkan_menu()
    pilihan = input("Masukkan pilihan Anda: ")

    if pilihan == '1':
        kode = input("Masukkan kode barang: ")
        nama = input("Masukkan nama barang: ")
        stok = int(input("Masukkan stok barang: "))
        data_barang.add_to_end(Barang(kode, nama, stok))
        binary_tree.add_to_tree(Barang(kode, nama, stok))
        graph.add_node(Barang(kode, nama, stok))
        print("Data barang berhasil ditambahkan.")
    elif pilihan == '2':
        kode_cari = input("Masukkan kode barang yang ingin dicari: ")
        barang_ditemukan = data_barang.find(kode_cari)
        if barang_ditemukan:
            print("Data barang ditemukan:")
            print("Kode:", barang_ditemukan.kode)
            print("Nama:", barang_ditemukan.nama)
            print("Stok:", barang_ditemukan.stok)
        else:
            print("Data barang tidak ditemukan.")
    elif pilihan == '3':
        kode_barang = input("Masukkan kode barang yang ingin diupdate stok: ")
        jumlah = int(input("Masukkan jumlah stok baru: "))
        data_barang.update_stock(kode_barang, jumlah)
    elif pilihan == '4':
        print("List Barang:")
        data_barang.display()
    elif pilihan == '5':
        metode_pembayaran()
    elif pilihan == '6':  
        print("1. Add to Stack")
        print("2. Pop from Stack")
        sub_pilihan = input("Masukkan pilihan Stack: ")
        if sub_pilihan == '1':
            kode = input("Masukkan kode barang: ")
            nama = input("Masukkan nama barang: ")
            stok = int(input("Masukkan stok barang: "))
            stack_barang.add_to_stack(Barang(kode, nama, stok))
            print("Barang ditambahkan ke Stack.")
        elif sub_pilihan == '2':
            barang = stack_barang.pop()
            if barang:
                print(f"Barang diambil dari Stack: {barang.nama}, Stok: {barang.stok}")
            else:
                print("Stack kosong.")
    elif pilihan == '7': 
        print("1. Enqueue ke Queue")
        print("2. Dequeue dari Queue")
        sub_pilihan = input("Masukkan pilihan Queue: ")
        if sub_pilihan == '1':
            kode = input("Masukkan kode barang: ")
            nama = input("Masukkan nama barang: ")
            stok = int(input("Masukkan stok barang: "))
            queue_barang.enqueue(Barang(kode, nama, stok))
            print("Barang ditambahkan ke Queue.")
        elif sub_pilihan == '2':
            barang = queue_barang.dequeue()
            if barang:
                print(f"Barang diambil dari Queue: {barang.nama}, Stok: {barang.stok}")
            else:
                print("Queue kosong.")
    elif pilihan == '8': 
        print("Gunakan Tree:")
        print("1. Inorder Traversal")
        print("2. Cari Barang (Search)")
        sub_pilihan = input("Masukkan pilihan Tree: ")
        if sub_pilihan == '1':
            print("Inorder Traversal dari Tree:")
            barang_list = binary_tree.inorder_traversal()
            for barang in barang_list:
                print(f"Kode: {barang.kode}, Nama: {barang.nama}, Stok: {barang.stok}")
        elif sub_pilihan == '2':
            kode = input("Masukkan kode barang yang ingin dicari: ")
            barang = binary_tree.search(kode)
            if barang:
                print(f"Barang ditemukan: Kode: {barang.kode}, Nama: {barang.nama}, Stok: {barang.stok}")
            else:
                print("Barang tidak ditemukan di Tree.")
    elif pilihan == '9': 
        print("Gunakan Graph:")
        print("1. Tambah hubungan barang")
        print("2. Tampilkan hubungan barang")
        sub_pilihan = input("Masukkan pilihan Graph: ")
        if sub_pilihan == '1':
            kode1 = input("Masukkan kode barang pertama: ")
            kode2 = input("Masukkan kode barang kedua: ")
            barang1 = data_barang.find(kode1)
            barang2 = data_barang.find(kode2)
            if barang1 and barang2:
                graph.add_edge(barang1, barang2)
                print(f"Hubungan antara {barang1.nama} dan {barang2.nama} berhasil ditambahkan.")
            else:
                print("Salah satu barang tidak ditemukan.")
        elif sub_pilihan == '2':
            graph.display()
    elif pilihan == '10':
        break

