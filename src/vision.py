import cv2

# Muat gambar
image_path = "maudy.jpg"  # Ganti dengan path gambar Anda
image = cv2.imread(image_path)

# Konversi gambar ke grayscale untuk deteksi wajah
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Muat model deteksi wajah dari OpenCV
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Deteksi wajah pada gambar
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Gambar kotak di sekitar wajah yang terdeteksi
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Tampilkan hasil
title = "Face Detection"
cv2.imshow(title, image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Opsional: Simpan gambar hasil
detected_image_path = "detected_faces.jpg"
cv2.imwrite(detected_image_path, image)
