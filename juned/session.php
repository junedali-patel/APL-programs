<html>
<body>
   <form action="<?php echo $_SERVER['PHP_SELF'];?>" method="post">
      <h3>User's ID: <input type="text" name="ID"/></h3>
      <h3>User's Name: <input type="text" name="name"/></h3>
      <h3>User Type: <input type="text" name="type"/></h3>
      <input type="submit" value="Submit" />
   </form>

   <?php
      session_start();
      $id=session_id();
      echo "Session Id: ".$id ;
     
   if( isset( $_SESSION['counter'] ) ) {
      $_SESSION['counter'] += 1;
   } else {
      $_SESSION['counter'] = 1;
   }
   $msg = "Number of visits in this session: ".  $_SESSION['counter'];
    echo "<h3>" . $msg . "</h3>";
      if ($_SERVER["REQUEST_METHOD"] == "POST") {
         $_SESSION['ID'] = $_POST['ID'];
         $_SESSION['Name'] = $_POST['name'];
         $_SESSION['type'] = $_POST['type'];

         echo "<h2>Following Session variables Created</h2>";
         foreach ($_SESSION as $key=>$val) {
            echo "<h3>" . $key . "=>" . $val . "</h3>";
         }
         echo "<a href='formup.html'><b>Click Here</b></a>";
      }

   ?>
</body>
</html>