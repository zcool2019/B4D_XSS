<html>
<head><title>
demo xss
</title></head>
<body>
<?php
if(isset($_COOKIE['admin'])) {
  echo "logged in as Admin";
  echo "<h1>FLAG</h1>";
  echo "{B4Db0TS3Cr3T}";
} else {
  echo "Access denied";
}
?>
</body>
</html>