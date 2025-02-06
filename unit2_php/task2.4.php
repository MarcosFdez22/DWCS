<?php declare(strict_types=1);
function Cadena(?string $nombre, int $edad, string $apellido="apelido") {
echo "<h2>".$nombre ." " . $apellido . " tiene " .$edad. " años </h2> ";
    
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Task2.4</title>
</head>
<body>
    <?php

    Cadena("marcos",21,"fdez");
    Cadena("marcos",21);
    Cadena(null,21);
    ?>



</body>
</html>