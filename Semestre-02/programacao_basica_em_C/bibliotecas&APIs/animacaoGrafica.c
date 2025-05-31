#include <raylib.h>

int main() {
    int screenWidth = 800;
    int screenHeight = 450;

    InitWindow(screenWidth, screenHeight, "Círculo se movendo");

    int x = 100, y = 200;
    int radius = 30;
    int step = 5;

    SetTargetFPS(60); // Define a taxa de quadros para 60 FPS

    while (!WindowShouldClose()) {
        x += step; // Move o círculo para a direita
        if (x > screenWidth - radius || x < radius) step = -step; // Inverte a direção se atingir as bordas

        BeginDrawing();
        ClearBackground(RAYWHITE);
        DrawCircle(x, y, radius, BLUE); // Desenha o círculo
        EndDrawing();
    }

    CloseWindow(); // Fecha a janela e libera recursos
    return 0;
}