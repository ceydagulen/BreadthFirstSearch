# Genişlik Öncelikli Arama (Breadth-First Search - BFS) algoritmasını Python'da bir graf için uygular ve her satırı açıklar.

def bfs(graph, start):
    """
    Bir graf için BFS algoritması.
    Parametreler:
        graph (dict): Düğümden düğüme olan bağlantıları temsil eden bir sözlük.
        start (str): Aramanın başlayacağı düğüm.
    """
    # Ziyaret edilen düğümleri tutmak için bir liste oluşturuyoruz.
    visited = []  # BFS sırasıyla düğümleri ekleriz.

    # Ziyaret edilmesi gereken düğümleri bir kuyrukta tutuyoruz.
    queue = []  # Kuyruk veri yapısı, FIFO (First In, First Out) mantığıyla çalışır.

    # Başlangıç düğümünü kuyruğa ekliyoruz.
    queue.append(start)

    # Kuyruk boş olmadığı sürece döngü devam eder.
    while queue:
        # Kuyruğun ilk elemanını çekip alıyoruz (FIFO).
        node = queue.pop(0)

        # Eğer bu düğüm daha önce ziyaret edilmediyse:
        if node not in visited:
            # Düğümü "visited" listesine ekliyoruz.
            visited.append(node)

            # Mevcut düğüme komşularını kuyruğa ekliyoruz.
            # (Eğer daha önce ziyaret edilmedilerse.)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    # Ziyaret edilen düğümleri döndürüyoruz.
    return visited

# Bir graf tanımlıyoruz.
# Sözlük yapısı: Anahtarlar düğümler, değerler komşuları temsil eder.
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# BFS algoritmasını çağırarak arama yapıyoruz.
visited_nodes = bfs(graph, 'A')

# Ziyaret sırasıyla tüm düğümleri yazdırıyoruz.
print("Ziyaret Edilen Düğümler Sırası: ", visited_nodes)
