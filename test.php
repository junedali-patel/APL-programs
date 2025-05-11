<?php
echo "<h1>Hello from PHP 🎉</h1>";

$date = date("Y-m-d H:i:s");
echo "<p>Current server time is: $date</p>";

$fruits = ["Apple", "Banana", "Mango"];
echo "<p>Fruits List:</p><ul>";
foreach ($fruits as $fruit) {
    echo "<li>$fruit</li>";
}
echo "</ul>";
?>
