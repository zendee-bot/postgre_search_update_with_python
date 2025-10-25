from cofig_function import get_connetion
from typing import List, Tuple, Optional

def show_data():
    conn = get_connetion()
    curs = conn.cursor()

    query = """ 
        SELECT 
            p.id_produk,
            p.nama_produk,
            p.harga,
            p.stok,
            p.kategori,
            v.nama_vendor,
            v.kota
        FROM produk p
        INNER JOIN vendor v ON p.id_vendor = v.id_vendor
        ORDER BY p.id_produk ASC
"""
    curs.execute(query)

    print(f"{'ID':<5} {'Nama Produk':<25} {'Harga':<15} {'Stock':<15}{'Jenis':<15}{'Vendor':<20}{'kota'}")  
    for record in curs.fetchall():
        print (f'{record[0]:<5}{record[1]:<25}{record[2]:<20}{record[3]:<10}{record[4]:<15}{record[5]:<20}{record[6]}')

    curs.close()
    conn.close
    return

def chose(keyword):
    conn = get_connetion()

    curs = conn.cursor()
    # Menggunakan ILIKE untuk case-insensitive search dengan wildcard
    query = """
        SELECT 
            p.id_produk,
            p.nama_produk,
            p.harga,
            p.stok,
            p.kategori,
            v.nama_vendor,
            v.kota
        FROM produk p
        INNER JOIN vendor v ON p.id_vendor = v.id_vendor
        WHERE p.nama_produk ILIKE %s 
            OR v.nama_vendor ILIKE %s
            OR p.kategori ILIKE %s
        ORDER BY p.id_produk ASC
    """
    search_parameter = f'%{keyword}%'
    curs.execute(query, (search_parameter, search_parameter, search_parameter))
    results = curs.fetchall()
        
    curs.close()
    conn.close()

    return results

def showw_chosen(results):
    if not results:
        print('Produk tidak ditemukan')
        return False
    
    print(f"{'ID':<5} {'Nama Produk':<25} {'Harga':<15} {'Stock':<15}{'Jenis':<15}{'Vendor':<20}{'kota'}")  
    for record in results:
        print (f'{record[0]:<5}{record[1]:<25}{record[2]:<20}{record[3]:<10}{record[4]:<15}{record[5]:<20}{record[6]}')

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

