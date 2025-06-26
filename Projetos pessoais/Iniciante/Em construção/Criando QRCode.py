import qrcode

imagem = qrcode.make("https://i.pinimg.com/736x/9b/8d/26/9b8d26cd70f09a90e118d901de35fc06.jpg")
imagem.save("qrcode.png")