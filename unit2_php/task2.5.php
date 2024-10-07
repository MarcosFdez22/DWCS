<?php
function tripleComprobacion($as) {
    $contador=0;
    $anterior="";

foreach ($as as $a) {
   if($a==$anterior) {
    $contador++;
   }else {
    $contador=0;
   }if ($contador==2) {
        return true;
   }
   $anterior=$a;
}
    return false;
}



function countries(array $c) {
foreach ($c as $x => $y) {
  echo "<br>La capital de $x es $y";
}
    
}






?>


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Task2.5</title>
</head>
<body>
    
<?php
$array1= array(2,2,2,3,4);
echo var_dump(tripleComprobacion($array1));


$array2= array(2,1,2,3,4);
echo var_dump(tripleComprobacion($array2));


$ceu = array( "Italy"=>"Rome", "Luxembourg"=>"Luxembourg", "Belgium"=> "Brussels", "Denmark"=>"Copenhagen", "Finland"=>"Helsinki", "France" => "Paris", "Slovakia"=>"Bratislava", "Slovenia"=>"Ljubljana", "Germany" => "Berlin", "Greece" => "Athens", "Ireland"=>"Dublin", "Netherlands"=>"Amsterdam", "Portugal"=>"Lisbon", "Spain"=>"Madrid", "Sweden"=>"Stockholm", "United Kingdom"=>"London", "Cyprus"=>"Nicosia", "Lithuania"=>"Vilnius", "Czech Republic"=>"Prague", "Estonia"=>"Tallin", "Hungary"=>"Budapest", "Latvia"=>"Riga", "Malta"=>"Valetta", "Austria" => "Vienna", "Poland"=>"Warsaw") ;

countries($ceu);



?>



</body>
</html>