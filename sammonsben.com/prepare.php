<?php
//if no permission redirect to denied

//else work some magic
$conn = mysql_connect('localhost:3306','devrec5','godCh3ck!');
echo ($conn);
if ($conn) {
	$result = mysql_query('SELECT * FROM dbo.blogs;',$conn);
	if (!$result) die('uh oh:'.mysql_error());
	$result = mysql_fetch_array($result);
}
?>