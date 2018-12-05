"""
ウェルノウンポート番号　（０〜１０２３）
登録済みポート番号　（１０２４〜４９１５１）
動的・プライベート番号　（４９１５２〜６５５３５）


"""
import socket

with socket.socket(socket.AF_INET,socket.SOCK_STREAM)as s:
    s.hind('127.0.0.1',50007)
    s.listen(1)
    while True:
        conn, addr =s.accept()
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f'data:{data},addr:{addr}')
                conn.sendall(b'Received'+data)