import pygame
import time
import random

# Inicializar o pygame
pygame.init()

# Dimensões da tela
largura = 600
altura = 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo da Cobrinha")

# Cores
BRANCO = (255, 255, 255)
VERDE = (0, 255, 0)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)

# Relógio e velocidade
clock = pygame.time.Clock()
velocidade = 15

# Tamanho do bloco da cobra
tamanho_bloco = 20

# Fonte
fonte = pygame.font.SysFont(None, 35)

# Função para mostrar a pontuação


def mostrar_pontuacao(pontos):
    valor = fonte.render(f"Pontos: {pontos}", True, PRETO)
    tela.blit(valor, [10, 10])

# Função principal do jogo


def jogo():
    x = largura // 2
    y = altura // 2
    x_mudanca = 0
    y_mudanca = 0

    cobra = []
    comprimento_cobra = 1

    # Posição inicial da comida
    comida_x = round(random.randrange(0, largura - tamanho_bloco) / 20) * 20
    comida_y = round(random.randrange(0, altura - tamanho_bloco) / 20) * 20

    fim_de_jogo = False

    while not fim_de_jogo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_de_jogo = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x_mudanca = -tamanho_bloco
                    y_mudanca = 0
                elif evento.key == pygame.K_RIGHT:
                    x_mudanca = tamanho_bloco
                    y_mudanca = 0
                elif evento.key == pygame.K_UP:
                    y_mudanca = -tamanho_bloco
                    x_mudanca = 0
                elif evento.key == pygame.K_DOWN:
                    y_mudanca = tamanho_bloco
                    x_mudanca = 0

        # Atualizar posição da cobra
        x += x_mudanca
        y += y_mudanca

        # Verificar colisão com borda
        if x >= largura or x < 0 or y >= altura or y < 0:
            fim_de_jogo = True

        tela.fill(BRANCO)

        # Desenhar comida
        pygame.draw.rect(tela, VERMELHO, [
                         comida_x, comida_y, tamanho_bloco, tamanho_bloco])

        # Atualizar lista da cobra
        cabeca = [x, y]
        cobra.append(cabeca)

        if len(cobra) > comprimento_cobra:
            del cobra[0]

        # Verificar colisão com a própria cobra
        for bloco in cobra[:-1]:
            if bloco == cabeca:
                fim_de_jogo = True

        # Desenhar a cobra
        for bloco in cobra:
            pygame.draw.rect(
                tela, VERDE, [bloco[0], bloco[1], tamanho_bloco, tamanho_bloco])

        # Mostrar pontuação
        mostrar_pontuacao(comprimento_cobra - 1)

        pygame.display.update()

        # Verificar se a cobra comeu a comida
        if x == comida_x and y == comida_y:
            comida_x = round(random.randrange(
                0, largura - tamanho_bloco) / 20) * 20
            comida_y = round(random.randrange(
                0, altura - tamanho_bloco) / 20) * 20
            comprimento_cobra += 1

        clock.tick(velocidade)

    # Tela de Game Over
    tela.fill(BRANCO)
    mensagem = fonte.render(
        f"GAME OVER, PONTUAÇÃO: {comprimento_cobra - 1}", True, VERMELHO)
    tela.blit(mensagem, [largura / 6, altura / 3])
    pygame.display.update()
    time.sleep(3)
    pygame.quit()


# Iniciar o jogo
jogo()

