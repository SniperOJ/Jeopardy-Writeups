<?php
$c = $_GET[c];
if(strlen($c) < 8){
    echo shell_exec($c);
}else{
    echo "too long!";
}
highlight_file(__FILE__);
?>
<?php echo "The web root directory will be emptied every two minutes.";?>
