#include <glut.h>
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// Dimensões da janela
#define WIDTH 800
#define HEIGHT 600

// Estado do jogo
int playerScore = 0;
int enemyScore = 0;
float ballSpeed = 0.05f;

// Bola
float ballX = 0.0f, ballY = 0.0f, ballZ = 0.0f;
float ballDX = 0.03f, ballDY = 0.02f, ballDZ = 0.0f;
float ballRadius = 0.1f;

// Raquetes
float paddleWidth = 0.2f, paddleHeight = 1.0f;
float playerY = 0.0f;
float enemyY = 0.0f;

bool wPressed = false;
bool sPressed = false;

const float PADDLE_LIMIT_Y = 2.4f;

// Função para desenhar texto
void drawText(float x, float y, char* text) {
    glRasterPos2f(x, y);
    for (char* c = text; *c != '\0'; c++)
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, *c);
}

// Função para desenhar raquete
void drawPaddle(float x, float y) {
    glPushMatrix();
    glColor3f(0.0f, 0.5f, 1.0f); // azul claro
    glTranslatef(x, y, 0);
    glScalef(0.1f, paddleHeight, 0.5f);
    glutSolidCube(1.0);
    glPopMatrix();
}

// Função para desenhar bola
void drawBall() {
    glPushMatrix();
    glColor3f(1.0f, 1.0f, 1.0f); // cor branca
    glTranslatef(ballX, ballY, ballZ);
    glutSolidSphere(ballRadius, 20, 20);
    glPopMatrix();
}

void display() {
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glLoadIdentity();

    gluLookAt(0.0, 0.0, 5.0,   // Câmera
              0.0, 0.0, 0.0,
              0.0, 1.0, 0.0);

    // Desenha os elementos
    drawBall();
    drawPaddle(-3.5f, playerY); // jogador
    drawPaddle(3.5f, enemyY);   // inimigo

    // Placar
    char score[32];
    sprintf(score, "%d x %d", playerScore, enemyScore);
    drawText(-0.3f, 2.5f, score);

    glutSwapBuffers();
}

void updateBall() {
    ballX += ballDX;
    ballY += ballDY;

    // Colisão superior e inferior
    if (ballY > 2.8f || ballY < -2.8f)
        ballDY = -ballDY;

    // Colisão com raquete do jogador
    if (ballX < -3.3f && ballY < playerY + paddleHeight/2 && ballY > playerY - paddleHeight/2) {
        ballDX = -ballDX;
        ballSpeed += 0.005f;  // dificuldade progressiva
    }

    // Colisão com raquete do inimigo
    if (ballX > 3.3f && ballY < enemyY + paddleHeight/2 && ballY > enemyY - paddleHeight/2) {
        ballDX = -ballDX;
    }

    // Pontuação
    if (ballX < -4.0f) {
        enemyScore++;
        ballX = ballY = 0;
        ballSpeed = 0.05f;
    }

    if (ballX > 4.0f) {
        playerScore++;
        ballX = ballY = 0;
        ballSpeed = 0.05f;
    }

    // Movimento da IA (inimigo)
    if (ballY > enemyY)
        enemyY += 0.03f;
    else
        enemyY -= 0.03f;
}

void timer(int v) {
    updateBall();

    if (wPressed && playerY + paddleHeight / 2 < PADDLE_LIMIT_Y)
        playerY += 0.05f;

    if (sPressed && playerY - paddleHeight / 2 > -PADDLE_LIMIT_Y)
        playerY -= 0.05f;

    glutPostRedisplay();
    glutTimerFunc(16, timer, 0); // ~60 FPS
}

void keyboard(unsigned char key, int x, int y) {
    switch (key) {
        case 'w': wPressed = true; break;
        case 's': sPressed = true; break;
        case 27: exit(0); // ESC
    }
}

void keyboardUp(unsigned char key, int x, int y) {
    switch (key) {
        case 'w': wPressed = false; break;
        case 's': sPressed = false; break;
    }
}


void init() {
    glEnable(GL_DEPTH_TEST);
    glClearColor(0, 0, 0, 1);

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(60.0, (float)WIDTH / (float)HEIGHT, 1.0, 100.0);
    glMatrixMode(GL_MODELVIEW);

}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
    glutInitWindowSize(WIDTH, HEIGHT);
    glutCreateWindow("Pong 3D");

    init();
    glutDisplayFunc(display);
    glutKeyboardFunc(keyboard);
    glutTimerFunc(16, timer, 0);
    glutKeyboardUpFunc(keyboardUp);


    glutMainLoop();
    return 0;
}