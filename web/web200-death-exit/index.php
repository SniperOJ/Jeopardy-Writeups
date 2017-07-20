<?php
$content = '<?php exit(0); ?>';
$content .= $_POST['code'];
file_put_contents($_POST['filename'], $content);
show_source(__FILE__);
?>

