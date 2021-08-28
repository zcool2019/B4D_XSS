<html>
<head><title>
demo xss
</title></head>
<body>
<?php
if(isset($_COOKIE['admin'])) {
  echo "logged in as Admin";
  echo "<a href='admin.php'>secret flag</a>";
} else {
  echo "logged in as Guest";
}
?>
<center>
<h1>XSS demo</h1>
<form name="search" action="#" method="GET">
<input type="text" name="kw">
<br>
<button type="submit" value="search">Search</button>
</form>

<?php if (isset($_GET['kw'])){
    echo '<h2>Search Keyword </h2><b>'. $_GET['kw'].'';
}
?>
</center>
</body>
</html>