
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
        echo ("<option value = " . $marca ." >" . $descripcion["text"] . " (" . $descripcion["precio"] . "€)</option>");
}
    echo "</select>";
}

$numeroerr="";
$numero=0;


function test_input($data) {
    $data = trim($data);
    $data = stripslashes($data);
    $data = htmlspecialchars($data);
    return $data;
}

if ($_SERVER["REQUEST_METHOD"]=="POST"){
    $opcion=test_input($_POST['opcion']);
    if (empty($_POST["cantidad"])||$_POST["cantidad"]<=0) {
        $numeroerr="<br>Introduce un valor mayor a 0";
    }else {
        $numero = test_input($_POST["cantidad"]);
    }

    $nombrebebida= $bebidas[$opcion]["text"];
    $preciobebida = $bebidas[$opcion]["precio"]*$numero;

}

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TAsk2.7</title>
</head>
<body>

<form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>" method="post"><?php
misBebidas($bebidas);
?>
<br><input type="number" name="cantidad">

<input type="submit" name="enviar">

<?php
 if ($numero > 0) {
    echo "<br>Has pedido $numero botellas de $nombrebebida. Precio total a pagar: $preciobebida";
}else{
    echo $numeroerr;

}
?>
</body>
</html>