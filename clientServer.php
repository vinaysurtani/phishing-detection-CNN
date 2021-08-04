<?php
// Purpose - This file acts as a mediator between the client side popup.js and the server side test.py.
// It gets the HTML contents which acts as input to the suite of python files.
function curl_get_contents($url)
{
  $ch = curl_init($url);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
  curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
  curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
  curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0);
  $data = curl_exec($ch);
  curl_close($ch);
  return $data;
}

header("Access-Control-Allow-Origin: *");
$site=$_POST['url'];
$html = curl_get_contents($site);
//echo $html;
$bytes=file_put_contents('markup.txt', $html);

// Can use this if your default interpreter is Python 2.x.
// Has some problem executing 'which python2'. So, absolute path is just simpler.
//$python_path=exec("which python 2>&1 ");
//$decision=exec("$python_path test.py $site 2>&1 ");

// Replace the path with the path of your python2.x installation.
//echo "py test.py $site 2>&1";
$decision=shell_exec("py test.py $site 2>&1");
echo $decision;
?>
