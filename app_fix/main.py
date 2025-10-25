from function_app import chose, showw_chosen, show_data, update_stock

def main():
    """Fungsi utama aplikasi"""
    print("\n" + "="*70)
    print("APLIKASI MANAJEMEN STOCK PRODUK")
    print("="*70)
    
    while True:
        print("\n1. Cari dan Update Stock Produk")
        print("2. Tampilkan Semua Produk")
        print("3. Keluar")
        
        pilihan = input("\nPilih menu (1-3): ").strip()
        
        if pilihan == '1':
            # Step 1: Input keyword pencarian
            keyword = input("\nMasukkan kata kunci pencarian (nama produk): ").strip()
            
            if not keyword:
                print("Keyword tidak boleh kosong!")
                continue
            
            # Step 2: Cari dan tampilkan hasil
            results = chose(keyword)
            
            if not  showw_chosen(results):
                continue
            
            # Step 3: Pilih produk dan update stock
            try:
                pilih = input("\nPilih nomor produk yang ingin diupdate (atau 0 untuk batal): ").strip()
                pilih_num = int(pilih)
                
                if pilih_num == 0:
                    print("Batal update.")
                    continue
                
            # Cari produk berdasarkan ID database yang diinput
                selected_product = None
                for record in results:
                    if record[0] == pilih_num:  # record[0] adalah ID dari database
                        selected_product = record
                        break

                if selected_product is None:
                    print(f"\n✗ ID {pilih_num} tidak ditemukan dalam hasil pencarian!")
                    print("Silakan pilih ID yang tersedia di tabel di atas.")
                    return pilih
                
                product_id = selected_product[0]
                product_name = selected_product[1]
                current_stock = selected_product[3]
                
                print(f"\nProduk terpilih: {product_name}")
                print(f"Stock saat ini: {current_stock}")
                
                new_stock = input("Masukkan stock baru: ").strip()
                new_stock_int = int(new_stock)
                
                if new_stock_int < 0:
                    print("Stock tidak boleh negatif!")
                    continue
                
                # Konfirmasi
                konfirmasi = input(f"\nUpdate stock dari {current_stock} menjadi {new_stock_int}? (y/n): ").strip().lower()
                
                if konfirmasi == 'y':
                    update_stock(product_id, new_stock_int)
                else:
                    print("Update dibatalkan.")
                    
            except ValueError:
                print("Input tidak valid! Masukkan angka.")
            except Exception as e:
                print(f"Error: {e}")
        
        elif pilihan == '2':
            show_data()
        
        elif pilihan == '3':
            print("\nTerima kasih! Program selesai.")
            break
        
        else:
            print("\nPilihan tidak valid! Pilih 1-3.")

if __name__ == "__main__":
    main()