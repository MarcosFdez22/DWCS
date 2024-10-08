<?php
     $bebidas = array(
        "CocaCola" => array("text"=>"Coca Cola", "precio"=>2.1), 
        "PepsiCola" => array("text"=>"Pepsi Cola", "precio"=>2), 
        "FantaNaranja" => array("text"=>"Fanta Naranja", "precio"=>2.5), 
        "TrinaManzana" => array("text"=>"Trina Manzana", "precio"=>2.3)
    );

    function misBebidas(array $bebidas){
        echo "<select name='opcion'>";
        foreach ($bebidas as $marca => $descripcion){
            echo ("<option value =' " . $marca ." '>" . $descripcion["text"] . " (" . $descripcion["precio"] . "€)</option>");
    }
        echo "</select>";
    }
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Array Dinámico</title>
</head>
<body>
    <?php
        misBebidas($bebidas);
    ?>
</body>
</html>