<html>
    <body>
        <?php
            $notas=[8, 6, 9, 7, 5];

            foreach($notas as $nota){
                $soma += $nota;
            }

            $media = $soma / count($notas);

            if ($media >= 7) {
                echo "Aprovado com média: " . $media;
            } else if ($media >= 5) {
                echo "Recuperação com média: " . $media;
            } else {
                echo "Reprovado com média: " . $media;
            }
        ?>
    </body>
</html>