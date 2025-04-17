# BreadthFirstSearch

# BFS (Breadth-First Search) Algoritması - Python Uygulaması

Bu projede, **Breadth-First Search (Genişlik Öncelikli Arama)** algoritması Python kullanılarak uygulanmıştır. Kod, algoritmanın temel mantığını göstermek amacıyla hazırlanmıştır.

## 📌 BFS Nedir?

**BFS (Genişlik Öncelikli Arama)**, graf yapılarında kullanılan bir arama algoritmasıdır. Bu algoritma, başlangıç düğümünden (node) başlayarak komşu düğümleri seviyeler halinde dolaşır. İlk olarak en yakın komşular, ardından onların komşuları ziyaret edilir. BFS genellikle:

- En kısa yolun bulunması,
- Düzey düzey (level-order) tarama,
- Dolaşılabilirlik kontrolleri gibi işlemlerde kullanılır.

## 🧠 Algoritmanın Çalışma Mantığı

1. Başlangıç düğümü kuyruğa eklenir.
2. Kuyruk boşalana kadar şu adımlar tekrarlanır:
   - Kuyruktan bir düğüm alınır.
   - Eğer daha önce ziyaret edilmediyse:
     - Ziyaret edilir (işaretlenir),
     - Komşuları kuyruğa eklenir.

## 📁 Proje İçeriği

- `bfs.py`: Python ile yazılmış BFS algoritmasının örnek uygulaması.
- Bu algoritmanın nasıl çalıştığı rapor haline getirilerek detaylı bir şekilde anlatılmıştır.

## 🧪 Kullanım

1. Python 3 yüklü olduğundan emin olun.
2. Terminalden proje klasörüne gidin.
3. Aşağıdaki komutla kodu çalıştırabilirsiniz:

```bash
python .py
