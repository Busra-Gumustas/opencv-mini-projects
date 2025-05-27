# Projeler

Bu klasör içerisinde iki farklı bilgisayarla görme projesi bulunmaktadır:  
1. **QR Kod Okuma ve Video Akışı**  
2. **El Tespiti ve Parmak Sayma**

---

## 📡 1. QR Kod Okuma ve Video Akışı Projesi

Bu proje, bir cihazdan (Jetson Nano gibi) kamera görüntüsü alınarak QR kodlarının gerçek zamanlı olarak okunmasını ve kod verilerinin ekranda gösterilmesini sağlar.  
Ayrıca, kamera görüntüsü TCP protokolü kullanılarak ağ üzerinden başka bir cihaza aktarılır.

### Proje İçeriği

- **Server Kısmı:**  
  - Kameradan görüntü alır  
  - Görüntüde QR kodlarını tespit eder ve kod verisini ekranda gösterir  
  - Görüntüyü sıkıştırıp TCP üzerinden gönderir  

- **Client Kısmı:**  
  - TCP üzerinden görüntü verisini alır  
  - Gelen görüntüyü çözer ve ekranda gösterir  

### Kullanılan Kütüphaneler

- OpenCV (`cv2`)  
- socket  
- struct  
- pyzbar (QR kod okuma için)  
- numpy  

### Çalıştırma

1. Server tarafında `server.py` dosyasını çalıştırın.  
2. Client tarafında `client.py` dosyasını çalıştırarak görüntüyü alın.  
3. QR kodlar kameraya gösterildiğinde, kod içeriği server konsolunda ve görüntü üzerinde görünecektir.  

---

## ✋ 2. El Tespiti ve Parmak Sayma Projesi

Bu proje, bir kameradan alınan canlı görüntü üzerinde cilt rengini baz alarak el tespiti yapar ve parmakların sayısını gerçek zamanlı olarak tahmini şekilde ekranda gösterir.

### Proje İşleyişi

- Görüntü HSV renk uzayına çevrilir ve cilt rengine uygun bölgeler maskelenir.  
- Maske üzerinde morfolojik işlemler uygulanarak gürültü azaltılır.  
- Maskeden konturlar çıkarılır ve büyük konturlar etrafına dikdörtgen çizilir.  
- Kontur üzerindeki konveksiyet kusurları (defects) analiz edilerek parmak uçları tahmini bulunur.  
- Parmak sayısı hesaplanarak görüntüye yazdırılır.  

### Kullanılan Kütüphaneler

- OpenCV (`cv2`)  
- numpy  

### Çalıştırma

- `hand_detection.py` dosyasını çalıştırın.  
- Kameraya elinizi gösterin, parmak sayısı canlı olarak ekranda görünecektir.  
- Çıkmak için 'q' tuşuna basınız.  




