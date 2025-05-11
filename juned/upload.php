<?php
if (isset($_POST["submit"])) {
    $targetDirectory = "/Applications/XAMPP/xamppfiles/htdocs/juned/";
    $targetFile = $targetDirectory . basename($_FILES["myFile"]["name"]);

    if (move_uploaded_file($_FILES["myFile"]["tmp_name"], $targetFile)) {
        echo "File '" . basename($_FILES["myFile"]["name"]) . "' has been uploaded.";
    } else {
        echo " Upload error. Code: " . $_FILES["myFile"]["error"];
    }
}
?>
