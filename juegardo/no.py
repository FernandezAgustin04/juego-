import pygame
import random

# Dimensiones de la pantalla
ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Juego de Plataformas")

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.imagen_derecha = pygame.image.load("juego\JUEGO\img\personaje_quieto_1.png")
        self.imagen = [pygame.image.load(f"juego\JUEGO\img\personaje_caminando_{num}.png") for num in range(1, 4)]
        self.indice_imagen = 0
        self.image = self.imagen[self.indice_imagen]
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = ALTO_PANTALLA - self.rect.height
        self.velocidad_x = 0
        self.velocidad_y = 0
        self.en_suelo = False
        self.fotogramas_caminando = 0
        self.direccion = "derecha"  # Dirección inicial del jugador

    def update(self):
        # Actualizar posición en el eje x
        self.rect.x += self.velocidad_x

        # Reflejar imagen horizontalmente si se mueve hacia la izquierda
        if self.velocidad_x < 0:
            self.image = pygame.transform.flip(self.imagen[self.indice_imagen], True, False)
        else:
            self.image = self.imagen[self.indice_imagen]

        # Actualizar posición en el eje y
        self.velocidad_y += 1  # Gravedad
        self.rect.y += self.velocidad_y

        # Verificar colisión con el suelo
        if self.rect.y >= ALTO_PANTALLA - self.rect.height:
            self.rect.y = ALTO_PANTALLA - self.rect.height
            self.velocidad_y = 0
            self.en_suelo = True
        else:
            self.en_suelo = False

        # Verificar colisión con las plataformas
        plataforma_colisionada = pygame.sprite.spritecollideany(self, plataformas)
        if plataforma_colisionada:
            if self.velocidad_y > 0 and self.rect.bottom <= plataforma_colisionada.rect.top + 10:
                self.rect.bottom = plataforma_colisionada.rect.top + 1
                self.velocidad_y = 0
                self.en_suelo = True

        # Comprobar si está en una plataforma
        if not self.en_suelo:
            plataforma_encima = pygame.sprite.spritecollideany(self, plataformas)
            if plataforma_encima:
                if self.velocidad_y < 0 and self.rect.top >= plataforma_encima.rect.bottom - 10:
                    self.rect.top = plataforma_encima.rect.bottom + 1
                    self.velocidad_y = 1

        # Animación de caminata
        self.fotogramas_caminando += 1
        if self.fotogramas_caminando == 10:
            self.indice_imagen += 1
            if self.indice_imagen > 2:
                self.indice_imagen = 0
            self.fotogramas_caminando = 0


class Enemigo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.imagen_derecha = pygame.image.load("juego\JUEGO\img\imagen.png")
        self.imagen_izquierda = pygame.transform.flip(self.imagen_derecha, True, False)  # Reflejar imagen horizontalmente
        self.image = self.imagen_derecha
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, ANCHO_PANTALLA - self.rect.width)
        self.rect.y = random.randint(0, ALTO_PANTALLA - self.rect.height)
        self.velocidad_x = random.choice([-1, 1])
        self.direccion = "izquierda" if self.velocidad_x < 0 else "derecha"
        self.disparar_probabilidad = 0.02  # Probabilidad de disparar en cada iteración

    def disparar(self):
        if random.random() < self.disparar_probabilidad:
            proyectil = ProyectilEnemigo(self.rect.x + self.rect.width // 2, self.rect.y + self.rect.height // 2, 5, self.direccion)
            proyectiles_enemigos.add(proyectil)
            todos_los_sprites.add(proyectil)

    def update(self):
        self.rect.x += self.velocidad_x

        if self.rect.left < 0 or self.rect.right > ANCHO_PANTALLA:
            self.velocidad_x *= -1

        if self.velocidad_x > 0:
            self.image = self.imagen_derecha
            self.direccion = "derecha"
        elif self.velocidad_x < 0:
            self.image = self.imagen_izquierda
            self.direccion = "izquierda"


class Plataforma(pygame.sprite.Sprite):
    def __init__(self, x, y, ancho, alto):
        super().__init__()
        self.image = pygame.image.load("juego\JUEGO\img\intentoplat.png")
        self.image = pygame.transform.scale(self.image, (200, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.width = 150  # Ajustar el ancho del rectángulo de colisión
        self.rect.height = 10  # Ajustar el alto del rectángulo de colisión


class Moneda(pygame.sprite.Sprite):
    def __init__(self, x, y, ancho, alto):
        super().__init__()
        self.image = pygame.image.load("juego\JUEGO\img\Snowball-PNG-Clipart.png")
        self.image = pygame.transform.scale(self.image, (ancho, alto))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Proyectil(pygame.sprite.Sprite):
    def __init__(self, x, y, velocidad_x, direccion):
        super().__init__()
        self.image = pygame.image.load("juego\JUEGO\img\projectileperso.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocidad_x = velocidad_x
        self.direccion = direccion

    def update(self):
        if self.direccion == "izquierda":
            self.rect.x -= self.velocidad_x
        elif self.direccion == "derecha":
            self.rect.x += self.velocidad_x


class ProyectilEnemigo(pygame.sprite.Sprite):
    def __init__(self, x, y, velocidad_x, direccion):
        super().__init__()
        self.image = pygame.image.load("juego\JUEGO\img\projectileperso.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocidad_x = velocidad_x
        self.direccion = direccion

    def update(self):
        if self.direccion == "izquierda":
            self.rect.x -= self.velocidad_x
        elif self.direccion == "derecha":
            self.rect.x += self.velocidad_x


# Inicialización
pygame.init()

# Crear la pantalla
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Mario Bros")

reloj = pygame.time.Clock()

# Cargar imágenes
fondo_imagen = pygame.image.load("juego\JUEGO\img\plats.jpg")

# Escalar imágenes
fondo_imagen = pygame.transform.scale(fondo_imagen, (ANCHO_PANTALLA, ALTO_PANTALLA))

# Crear jugador
jugador = Jugador()

# Grupos de sprites
todos_los_sprites = pygame.sprite.Group()
plataformas = pygame.sprite.Group()
proyectiles_jugador = pygame.sprite.Group()
proyectiles_enemigos = pygame.sprite.Group()
monedas = pygame.sprite.Group()
enemigos = pygame.sprite.Group()
proyectiles_enemigos = pygame.sprite.Group()
todos_los_sprites.add(jugador)

# Crear suelo y plataformas
suelo = Plataforma(0, ALTO_PANTALLA - 108, ANCHO_PANTALLA, 800)
plataformas.add(suelo)
todos_los_sprites.add(suelo)

platform1 = Plataforma(200, 400, 200, 80)
platform2 = Plataforma(500, 500, 200, 80)
platform3 = Plataforma(100, 300, 200, 80)
plataformas.add(platform1)
plataformas.add(platform2)
plataformas.add(platform3)
todos_los_sprites.add(platform1)
todos_los_sprites.add(platform2)
todos_los_sprites.add(platform3)

moneda1 = Moneda(250, 370, 30, 30)  # Posición de la moneda en la plataforma
moneda2 = Moneda(600, 470, 30, 30)  # Posición de la segunda moneda en la plataforma
moneda3 = Moneda(150, 270, 30, 30)  # Posición de la tercera moneda en la plataforma
monedas.add(moneda1)
monedas.add(moneda2)
monedas.add(moneda3)
todos_los_sprites.add(moneda1)
todos_los_sprites.add(moneda2)
todos_los_sprites.add(moneda3)

# Crear enemigos
for _ in range(5):
    enemigo = Enemigo()
    enemigos.add(enemigo)
    todos_los_sprites.add(enemigo)

juego_terminado = False
enemigos_disparando_evento = pygame.USEREVENT + 1
pygame.time.set_timer(enemigos_disparando_evento, 100) 
# Bucle principal del juego  
# Bucle principal del juego
# Bucle principal del juego
juego_terminado = False
while not juego_terminado:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador.velocidad_x = -5
                jugador.direccion = "izquierda"
            elif evento.key == pygame.K_RIGHT:
                jugador.velocidad_x = 5
                jugador.direccion = "derecha"
            elif evento.key == pygame.K_SPACE:
                if jugador.direccion == "derecha":
                    proyectil = Proyectil(jugador.rect.x + jugador.rect.width, jugador.rect.y + jugador.rect.height // 2, 5, "derecha")
                else:
                    proyectil = Proyectil(jugador.rect.x, jugador.rect.y + jugador.rect.height // 2, -5, "izquierda")
                proyectiles_jugador.add(proyectil)
                todos_los_sprites.add(proyectil)
        elif evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador.velocidad_x = 0

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador.velocidad_x = 0

        # Generar evento para que los enemigos disparen proyectiles
        if evento.type == enemigos_disparando_evento:
            for enemigo in enemigos:
                enemigo.disparar()


    # Actualizar
    todos_los_sprites.update()

    for proyectil in proyectiles_jugador:
        enemigos_colisionados = pygame.sprite.spritecollide(proyectil, enemigos, True)
        if proyectil.rect.x > ANCHO_PANTALLA or proyectil.rect.x < 0:
            proyectiles_jugador.remove(proyectil)
            todos_los_sprites.remove(proyectil)

    for proyectil in proyectiles_enemigos:
        if proyectil.rect.x > ANCHO_PANTALLA or proyectil.rect.x < 0:
            proyectiles_enemigos.remove(proyectil)
            todos_los_sprites.remove(proyectil)
        
    jugador_golpeado = False
    for proyectil in proyectiles_enemigos:
        if pygame.sprite.collide_rect(proyectil, jugador) and not jugador_golpeado:
            print("¡El jugador ha sido golpeado!")
            jugador_golpeado = True

    # Reiniciar el estado del jugador si está en el suelo
    if jugador.en_suelo:
        jugador_golpeado = False

    monedas_colisionadas = pygame.sprite.spritecollide(jugador, monedas, True)
    if monedas_colisionadas:
        print("¡Has recolectado una moneda!")

    # Renderizar
    pantalla.blit(fondo_imagen, (0, 0))
    todos_los_sprites.draw(pantalla)

    # Refrescar pantalla
    pygame.display.flip()
    reloj.tick(60)

# Cerrar juego
pygame.quit()
