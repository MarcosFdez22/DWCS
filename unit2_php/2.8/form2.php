<?php
function test_input($data) {
    $data = trim($data);
    $data = stripslashes($data);
    $data = htmlspecialchars($data);
    return $data;
  }

  $userErr="";
  $pswdErr="";

if ($_SERVER["REQUEST_METHOD"] == "POST") {

    if(empty($_POST["username"])){
        $userErr ="se requiere un username";
    }else {
        $username = test_input($_POST["username"]);
    }
    if(empty($_POST["paswd"])){
        $pswdErr ="se requiere una contraseña";
    }else {
        $password = test_input($_POST["paswd"]);
    }

    if(!empty($_POST["role"])){
     $role = test_input($_POST["role"]);
    }else{
        $role=null;
    }

    if(!empty($_POST["option1"])){
        $option1 = test_input($_POST["option1"]);
       }else{
           $option1=null;
       }
       if(!empty($_POST["option2"])){
        $option2 = test_input($_POST["option2"]);
       }else{
           $option2=null;
       }
       if(!empty($_POST["option3"])){
        $option3 = test_input($_POST["option3"]);
       }else{
           $option3=null;
       }

    $city = test_input($_POST["city"]);
    $web = test_input($_POST["web"]);

}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Task2.8</title>
</head>
<body>
<h2>Novell Services Login</h2>

<form action="<?php echo htmlspecialchars(test_input($_SERVER["PHP_SELF"]));?>" method="post">

    Username:<input type="text" name="username" value="<?php echo $username; ?>"><br><br> 

    Password:<input type="password" name="paswd" value=<?php echo $password;?>><br><br> 

    City of <br>Employment:<input type="text" name="city" value=<?php echo $city;?>><br><br>

    Web server:
    <select name="web" value=<?php echo $web;?>>
        <option value=""> --Choose a server--</option>
        <option value="docker" <?php if ($web=="docker") echo "selected";?>>Docker</option>
        <option value="Nginx" <?php if ($web=="Nginx") echo "selected";?>>Nginx</option>
    </select>

    <br><br>Role:
        <br><input type="radio" name="role" value="admin"<?php if ($role=="admin") echo "checked";?> >Admin
        <br><input type="radio" name="role" value="engineer"<?php if ($role=="engineer") echo "checked";?>>Engineer
        <br><input type="radio" name="role" value="manager"<?php if ($role=="manager") echo "checked";?>>Manager
        <br><input type="radio" name="role" value="guest"<?php if ($role=="guest") echo "checked";?>>Guest
    <br><br>Single sign:
        <br><input type="checkbox" name="option1" value="mail"<?php if (isset($option1) && $option1=="mail") echo "checked";?>>mail
        <br><input type="checkbox" name="option2" value="payroll"<?php if (isset($option2) && $option2=="payroll") echo "checked";?>>payroll
        <br><input type="checkbox" name="option3" value="self-service"<?php if (isset($option3) && $option3=="self-service") echo "checked";?>>self-service
    
   <br><br><input type="submit"> <input type="reset">

</form>



</body>
</html>