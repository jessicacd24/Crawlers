<!DOCTYPE html>
<html>
<head>
    <title>
        My Name
    </title>
</head>

<body>
<h1>Get My Name from Facebook</h1>

<?php

use Facebook\Facebook;

require_once 'vendor/autoload.php';

$fb = new Facebook([
    'app_id' => '992039907922991',           //Replace {your-app-id} with your app ID
    'app_secret' => '98f815d8f69f37224cb92405e5967cc4',   //Replace {your-app-secret} with your app secret
    'graph_api_version' => 'v7.0',
]);

try {
    // Returns a `FacebookFacebookResponse` object
    $response = $fb->get(
        '/153823892984243',
        array (
            'fields' => 'birthday','email','hometown'
        ),
        'EAAOGQUpQlC8BAFHbHIxZA3TKCnJ49EzD9RSBZCPaxjN8LlH7QOmU4pCdbCXVlbTcit32pB3wZAOYuWpE3fRji442RfmZCiChAXfsVMgP2bMMdj4orRYpDZBCObDpsxZA9PqFrEARXOp1T3xCitimOxYO57DPeDYGph9ZCdFOvtiEt0p22CZAAZArFZBcxnbZCwJpqnlHrN8notFlEhjGVnb2DN4'
    );
} catch(FacebookExceptionsFacebookResponseException $e) {
    echo 'Graph returned an error: ' . $e->getMessage();
    exit;
} catch(FacebookExceptionsFacebookSDKException $e) {
    echo 'Facebook SDK returned an error: ' . $e->getMessage();
    exit;
}
$graphNode = $response->getGraphNode();

//try {

// Get your UserNode object, replace {access-token} with your token
//    $response = $fb->get('/me', 'EAAOGQUpQlC8BAFHbHIxZA3TKCnJ49EzD9RSBZCPaxjN8LlH7QOmU4pCdbCXVlbTcit32pB3wZAOYuWpE3fRji442RfmZCiChAXfsVMgP2bMMdj4orRYpDZBCObDpsxZA9PqFrEARXOp1T3xCitimOxYO57DPeDYGph9ZCdFOvtiEt0p22CZAAZArFZBcxnbZCwJpqnlHrN8notFlEhjGVnb2DN4');

//} catch(\Facebook\Exceptions\FacebookResponseException $e) {
    // Returns Graph API errors when they occur
//    echo 'Graph returned an error: ' . $e->getMessage();
//    exit;
//} catch(\Facebook\Exceptions\FacebookSDKException $e) {
    // Returns SDK errors when validation fails or other local issues
//    echo 'Facebook SDK returned an error: ' . $e->getMessage();
//    exit;
//}

//$me = $response->getGraphUser();

//All that is returned in the response
//echo 'All the data returned from the Facebook server: ' . $me;

//Print out my name
//echo 'My name is ' . $me->getName();

?>

</body>
</html>