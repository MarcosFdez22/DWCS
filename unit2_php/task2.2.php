<?php 
   function Potencia($b,$e=2) : int {
    if (is_int($b)&&is_int($e)) {
        $t=1;
        for ($e; $e>0 ; $e--) { 
            $t*=$b; 
        }

        return $t;
    }else {
       throw new Exception("ERROR");
    }

   } 
    

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Task 2.2</title>
</head>
<body>
    
<?php

try {
    echo "<h3> 5 elevado al cuadrado es = " . Potencia(5) . "</h3>";
    echo "<h3> 20 elevado al cuadrado es = " . Potencia(20) . "</h3>";
    echo "<h3> 3 elevado a 4 es = " . Potencia(3,4) . "</h3>";
} catch (Exception $error) {
    $error->getMessage();
}

?>


</body>
</html>