#include <glut.h>
#include <math.h>
#include <time.h>
#include <stdio.h>

#define PI 3.14159265358979323846

// declarando funções
void display();
void timer(int);
void drawClockFace();
void drawHand(float length, float width);
void drawClock();

int width = 500;
int height = 500;

// Função para desenhar o relógio
void display() {
    glClear(GL_COLOR_BUFFER_BIT);
    drawClock();
    glutSwapBuffers();
}

void drawClock() {
    time_t rawTime;
    struct tm* currentTime;
    time(&rawTime);
    currentTime = localtime(&rawTime);

    float seconds = currentTime->tm_sec;
    float minutes = currentTime->tm_min + seconds / 60.0f;
    float hours = currentTime->tm_hour % 12 + minutes / 60.0f;

    glPushMatrix();
    drawClockFace();

    // Ponteiro das horas
    glPushMatrix();
    glRotatef(-30.0f * hours, 0.0f, 0.0f, 1.0f);  // 360/12 = 30
    glColor3f(0.2f, 0.2f, 0.8f);
    drawHand(0.4f, 6.0f);
    glPopMatrix();

    // Ponteiro dos minutos
    glPushMatrix();
    glRotatef(-6.0f * minutes, 0.0f, 0.0f, 1.0f);  // 360/60 = 6
    glColor3f(0.2f, 0.8f, 0.2f);
    drawHand(0.6f, 4.0f);
    glPopMatrix();

    // Ponteiro dos segundos
    glPushMatrix();
    glRotatef(-6.0f * seconds, 0.0f, 0.0f, 1.0f);
    glColor3f(0.9f, 0.1f, 0.1f);
    drawHand(0.7f, 2.0f);
    glPopMatrix();

    glPopMatrix();
}

void drawClockFace() {
    int i;
    glColor3f(0.0f, 0.0f, 0.0f);

    glBegin(GL_LINE_LOOP);
    for (i = 0; i < 360; i++) {
        float theta = i * PI / 180.0f;
        glVertex2f(cos(theta), sin(theta));
    }
    glEnd();

    // Marcas das horas
    for (i = 0; i < 12; i++) {
        float angle = i * 2 * PI / 12;
        float x1 = 0.9f * cos(angle);
        float y1 = 0.9f * sin(angle);
        float x2 = 1.0f * cos(angle);
        float y2 = 1.0f * sin(angle);
        glBegin(GL_LINES);
        glVertex2f(x1, y1);
        glVertex2f(x2, y2);
        glEnd();
    }

    // Números
    for (i = 1; i <= 12; i++) {
        float angle = -(i - 3) * PI / 6.0;  // (i - 3) para ajustar a rotação
        float x = 0.78f * cos(angle);
        float y = 0.78f * sin(angle);

        char number[3];
        sprintf(number, "%d", i);

        glRasterPos2f(x - 0.03f, y - 0.03f); // ajuste fino para centralizar
        for (char* c = number; *c != '\0'; c++) {
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, *c);
        }
    }

    for (i = 1; i <= 60; i++) {
        float angle = -(i - 15) * PI / 30.0;  // ajuste do ângulo para minutos/segundos
        float x = 0.92f * cos(angle);
        float y = 0.92f * sin(angle);

        char number[3];
        sprintf(number, "%d", i);

        glColor3f(0.5f, 0.5f, 0.5f);  // cinza claro para diferenciar
        glRasterPos2f(x - 0.015f, y - 0.015f); // ajuste para centralizar números pequenos
        for (char* c = number; *c != '\0'; c++) {
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_10, *c);
        }
    }
}

void drawHand(float length, float width) {
    glLineWidth(width);
    glBegin(GL_LINES);
    glVertex2f(0.0f, 0.0f);
    glVertex2f(0.0f, length);
    glEnd();
    glLineWidth(1.0f); // Reset
}

void timer(int value) {
    glutPostRedisplay();
    glutTimerFunc(1000, timer, 0); // Atualiza a cada segundo
}

void reshape(int w, int h) {
    width = w;
    height = h;
    glViewport(0, 0, w, h);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(-1, 1, -1, 1);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
    glutInitWindowSize(width, height);
    glutCreateWindow("Relógio Analógico com GLUT");

    glClearColor(1.0, 1.0, 1.0, 1.0);

    glutDisplayFunc(display);
    glutReshapeFunc(reshape);
    glutTimerFunc(0, timer, 0);

    glutMainLoop();
    return 0;
}