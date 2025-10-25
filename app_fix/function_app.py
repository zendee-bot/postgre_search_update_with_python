from cofig_function import get_connetion

def show_data():
    conn = get_connetion()
    curs = conn.cursor()
    curs.execute('SELECT * FROM produk ORDER BY id_produk ASC')
    for record in curs.fetchall():
        print (record)

    curs.close()
    conn.close
    return

def chose(keyword):
    conn = get_connetion()

    curs = conn.cursor()
    # Menggunakan ILIKE untuk case-insensitive search dengan wildcard
    query = "SELECT * FROM produk WHERE nama_produk ILIKE %s ORDER BY id_produk ASC"
    curs.execute(query, (f'%{keyword}%',))
    results = curs.fetchall()
        
    curs.close()
    conn.close()

    return results

def showw_chosen(results):
    if not results:
        print('Produk tidak ditemukan')
        return False
    
    print(f"{'ID':<10} {'Nama Produk':<30} {'Harga':<10} {'Stock':<15}")
    print("-"*70)    

    for record in results :
        # Asumsi struktur: (id, nama_produk, stock, harga, ...)
        print(f"{record[0]:<10} {record[1]:<30} {record[2]:<10} {record[3]:<15}")

    return True

def update_stock(product_id, new_stock):
    """Update stock produk berdasarkan ID"""
    conn = get_connetion()
    if not conn:
        return False
    


    try:
        curs = conn.cursor()
        query = "UPDATE produk SET stok = %s WHERE id_produk = %s"
        curs.execute(query, (new_stock, product_id))
        conn.commit()
        
        if curs.rowcount > 0:
            print(f"\n✓ Stock berhasil diupdate untuk produk ID {product_id}")
            return True
        else:
            print(f"\n✗ Produk dengan ID {product_id} tidak ditemukan")
            return False
    except Exception(eror) as e:
        eror = print(f"Error update stock: {e}")
        conn.rollback()
        return False
    
    finally:
        if curs:
            curs.close()
        if conn:
            conn.close()

