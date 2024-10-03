<?php
function CalcularFactorial($n) : int {
    $f=1;
    if ($n>=0) {
        for ($n; $n >1 ; $n--) { 
            $f*=$n;
        }
    }else {
        throw new Exception("El número tiene que ser mayor que 0");
    }return $f;
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<?php
try {
    echo "<h3> El factorial de 5 es ".CalcularFactorial(5)."<h3/>";
    echo "<h3> El factorial de 10 es ".CalcularFactorial(10)."<h3/>";
    echo "<h3> El factorial de 29 es ".CalcularFactorial(20)."<h3/>";
    echo "<h3> El factorial de -1 es ".CalcularFactorial(-1)."<h3/>";
}
catch(Exception $error) {
   echo "<h3>" .$error->getMessage() ."</h3>";
}

?>
</body>
</html>