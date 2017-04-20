<?php
ini_set("display_errors", "On");
error_reporting(E_ALL | E_STRICT);
$dbhost = "localhost";
$dbuser = "root";
$dbpass = "";
$db = "SniperOJ";
$conn = mysqli_connect($dbhost,$dbuser,$dbpass,$db);
mysqli_set_charset($conn,"utf8");

function   filter($str){
	$filterlist = "/\(|\)|username|password|where|case|when|like|regexp|into|limit|=|for|;/";
	if(preg_match($filterlist,strtolower($str))){
		die("Go away!");
	}
	return $str;
}

$username = isset($_GET['username'])?filter($_GET['username']):die("Please input username!");
$password = isset($_GET['password'])?filter($_GET['password']):die("Please input password!");

$sql = "select * from admin where  username ='$username' and password = '$password'";

$res = $conn -> query($sql);

if($res->num_rows>0){
	$row = $res -> fetch_assoc();
	if($row['id']){
		echo $row['username'];
	}
}else{
	echo "The content in the password column is the flag!";
}

?>


<?php
/*  
    CREATE TABLE `users` (
    `id` int NOT NULL AUTO_INCREMENT,
    `username` varchar(16) NOT NULL,
    `password` varchar(32) NOT NULL,
    PRIMARY KEY (`id`)
    ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
 */
// md5('sniperoj') == '498c67b7c86b01bd68ab5cbafd245b1c'
/*
   INSERT INTO `users` (username, password) values ('admin','SniperOJ{498c67b7c86b01bd68ab5cbafd245b1c}');

 */
?>
