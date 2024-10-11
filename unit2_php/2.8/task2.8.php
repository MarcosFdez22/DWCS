<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Task2.8</title>
</head>
<body>
<h2>Novell Services Login</h2>


<form action="form2.php" method="post">

    Username:<input type="text" name="username" required><span style="color:red;">*</span><br><br> 

    Password:<input type="password" name="paswd" required><span style="color:red;">*</span><br><br> 

    City of <br>Employment:<input type="text" name="city"><br><br>

    Web server:
    <select name="web"> 
        <option value=""> --Choose a server--</option>
        <option value="docker">Docker</option>
        <option value="Nginx">Nginx</option>
    </select>

    <br><br>Role:
        <br><input type="radio" name="role" value="admin">Admin
        <br><input type="radio" name="role" value="engineer">Engineer
        <br><input type="radio" name="role" value="manager">Manager
        <br><input type="radio" name="role" value="guest">Guest
    <br><br>Single sign:
        <br><input type="checkbox" name="option1" value="mail">mail
        <br><input type="checkbox" name="option2" value="payroll">payroll
        <br><input type="checkbox" name="option3" value="self-service">self-service
    
   <br><br><input type="submit"> <input type="reset">

</form>



</body>
</html>