def proxy():
    try:
        response = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt")
        response.raise_for_status()  # cek misal ana sing salah
        proxy_list = response.text.splitlines()  # gawe siji siji 
        random_proxy = random.choice(proxy_list)  # pilih siji rndom
        print(random_proxy)
    except requests.RequestException as e:
        print(f"Gagal mengambil data: {e}")