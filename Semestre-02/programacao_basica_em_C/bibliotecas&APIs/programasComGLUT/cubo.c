#include <glut.h>

// Função chamada para desenhar
void display() {
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glLoadIdentity();
    
    // Posição da câmera
    gluLookAt(3.0, 3.0, 3.0,  // Eye position
              0.0, 0.0, 0.0,  // Look at point
              0.0, 1.0, 0.0); // Up vector

    // Rotação ao redor do eixo
    static float angle = 0.0;
    glRotatef(angle, 0.0, 1.0, 0.0);

    // Draw a cube
    glutSolidCube(1.5);

    angle += 0.2; // incrementa o ângulo de rotação
    if (angle > 360) angle = 0;

    glutSwapBuffers();
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

    glutMainLoop(); // Inicia o loop principal do GLUT
    return 0;
}