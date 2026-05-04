from pygame import image, display

# Carregar uma imagem
img = image.load('imagemoli.png')  # ou .jpg, .bmp
display.init()
tela = display.set_mode((800, 800))
tela.blit(img, (0, 0))
display.flip()

input("Pressione Enter para fechar...")