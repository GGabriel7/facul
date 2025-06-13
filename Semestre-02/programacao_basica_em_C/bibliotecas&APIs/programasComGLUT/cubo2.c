#include <glut.h>

//variaveis globais
float rotX = 20.0f, rotY = 30.0f;
int lastMouseX, lastMouseY;
int isDragging = 0;

// Desenhar eixo X, Y e Z
void drawAxes() {
    glDisable(GL_LIGHTING); // Eixos sem iluminação

    glBegin(GL_LINES);
        // Eixo X (vermelho)
        glColor3f(1, 0, 0);
        glVertex3f(0, 0, 0);
        glVertex3f(2, 0, 0);

        // Eixo Y (verde)
        glColor3f(0, 1, 0);
        glVertex3f(0, 0, 0);
        glVertex3f(0, 2, 0);

        // Eixo Z (azul)
        glColor3f(0, 0, 1);
        glVertex3f(0, 0, 0);
        glVertex3f(0, 0, 2);
    glEnd();

    glEnable(GL_LIGHTING);
}

// Função chamada para desenhar
void display() {
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glLoadIdentity();

    gluLookAt(3.0, 3.0, 3.0,
              0.0, 0.0, 0.0,
              0.0, 1.0, 0.0);

    glRotatef(rotX, 1.0, 0.0, 0.0);
    glRotatef(rotY, 0.0, 1.0, 0.0);

    drawAxes(); // Mostra os eixos

    glColor3f(0.7f, 0.7f, 1.0f); // Cor do cubo
    glutSolidCube(1.5);

    glutSwapBuffers();
}

// Tecla WASD para girar
void handleKeys(unsigned char key, int x, int y) {
    switch (key) {
        case 'a': rotY -= 5; break;
        case 'd': rotY += 5; break;
        case 'w': rotX -= 5; break;
        case 's': rotX += 5; break;
        case 27: exit(0); // Esc para sair
    }
    glutPostRedisplay();
}

// Mouse para rotação
void mouseButton(int button, int state, int x, int y) {
    if (button == GLUT_LEFT_BUTTON) {
        if (state == GLUT_DOWN) {
            isDragging = 1;
            lastMouseX = x;
            lastMouseY = y;
        } else {
            isDragging = 0;
        }
    }
}

void mouseMotion(int x, int y) {
    if (isDragging) {
        rotY += (x - lastMouseX);
        rotX += (y - lastMouseY);
        lastMouseX = x;
        lastMouseY = y;
        glutPostRedisplay();
    }
}

// Inicializa parametros de renderização
void initRendering() {
    glEnable(GL_DEPTH_TEST); // Habilita o teste de profundidade
    glEnable(GL_LIGHTING);   // Habilita iluminação
    glEnable(GL_LIGHT0);     // Habilita a luz 0
    glEnable(GL_COLOR_MATERIAL); // Habilita material de cor
    glEnable(GL_NORMALIZE); // Normaliza os vetores normais

    glClearColor(0.1, 0.1, 0.1, 1.0); // Cor de fundo

    GLfloat light_position[] = { 1.0, 1.0, 1.0, 0.0 };
    glLightfv(GL_LIGHT0, GL_POSITION, light_position); // Define a posição da luz
}

// Chamada quando a janela é redimensionada
void handleResize(int w, int h) {
    glViewport(0, 0, w, h); // Define a viewport
    glMatrixMode(GL_PROJECTION); // Muda para a matriz de projeção
    glLoadIdentity();
    gluPerspective(45.0, (double)w / (double)h, 1.0, 200.0); // Define a perspectiva
    glMatrixMode(GL_MODELVIEW); // Volta para a matriz de modelo/visualização
    glLoadIdentity();
}

int main(int argc, char** argv) {
    // Inicializa o GLUT e cria uma janela
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);

    // Define a posição e tamanho da janela
    glutInitWindowSize(800, 600);
    glutInitWindowPosition(100, 100);

    // Cria a janela
    glutCreateWindow("Cubo 3D com OpenGL");

    // Inicializa a renderização e registra as funções de callback
    initRendering();

    glutDisplayFunc(display); // Registra a função de exibição
    glutIdleFunc(display); // Registra a função de exibição para o modo ocioso
    glutReshapeFunc(handleResize); // Registra a função de redimensionamento
    glutKeyboardFunc(handleKeys);       // Teclado
    glutMouseFunc(mouseButton);         // Botões do mouse
    glutMotionFunc(mouseMotion);        // Movimento com botão pressionado


    glutMainLoop(); // Inicia o loop principal do GLUT
    return 0;
}