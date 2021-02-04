<?php

//Inspired by https://developers.facebook.com/docs/php/FacebookRequest/5.0.0

// Execute this file on root project : /vagrant
require_once 'vendor/autoload.php';

use Facebook\Facebook;
use Facebook\FacebookClient;
use Facebook\FacebookRequest;
use Facebook\Authentication\AccessToken;
use Facebook\GraphNodes\GraphEdge;

// TODO launch this php script with parameters to secure apps & token
$fb = new Facebook([
    'app_id' => '992039907922991',
    'app_secret' => '98f815d8f69f37224cb92405e5967cc4',
    'default_graph_version' => 'v7.0',
    'default_access_token' => 'EAAOGQUpQlC8BAFHbHIxZA3TKCnJ49EzD9RSBZCPaxjN8LlH7QOmU4pCdbCXVlbTcit32pB3wZAOYuWpE3fRji442RfmZCiChAXfsVMgP2bMMdj4orRYpDZBCObDpsxZA9PqFrEARXOp1T3xCitimOxYO57DPeDYGph9ZCdFOvtiEt0p22CZAAZArFZBcxnbZCwJpqnlHrN8notFlEhjGVnb2DN4', // optional
]);

$request = $fb->request(
    'GET',
    '/GROUP_ID/feed',
    array(
        'fields' => 'message,created_time,from,permalink_url,shares,attachments{media,type,url},likes.limit(1).summary(true),comments.limit(1).summary(true)',
        'since' => 'SINCE_DATE',
        'until' => 'UNTIL_DATE'
    )
);

// Send the request to Graph
try {
    $response = $fb->getClient()->sendRequest($request);
    $graphEdge = $response->getGraphEdge();
    $posts_metadata = array("message","date","from","permalink_url","shares","type","source","comments","likes");

    $file='data/<file>.json';
    $fp = fopen($file, 'a');
    //fputcsv($fp, $posts_metadata);

    $i=0;
    while(! is_null($graphEdge)){

        /* we have choosen to store posts by bucket of 25 in csv
        to avoid too much space usage (9500 for one month), so this solution
        is more scalable */
        $posts= array();
        //array_push($posts,$posts_metadata);

        foreach ($graphEdge as $graphNode) {

            $comment_metadata= $graphNode->getField('comments')->getMetaData();
            $likes_metadata= $graphNode->getField('likes')->getMetaData();

            // some attachments media value are null ( album or just text in post)
            $attachments=$graphNode->getField('attachments')[0];
            if(isset ($attachments["media"])) {
                $attachments_media=$attachments["media"]["image"]["src"];
            }else{
                $attachments_media="null";
            }

            // DateTime php RFC supported : http://php.net/manual/fr/class.datetime.php
            $date=$graphNode->getField('created_time')->format('Y-m-d-H-i-s');

            $post=array("message" => $graphNode->getField('message'),
                "date" => $date,
                "from" => "https://www.facebook.com/".$graphNode->getField('from')["id"],
                "permalink_url" => $graphNode->getField('permalink_url'),
                "shares" => $graphNode->getField('shares')["count"],
                "type" => $attachments["type"],
                "source" => $attachments_media,
                "comments" => $comment_metadata['summary']['total_count'],
                "likes" => $likes_metadata['summary']['total_count'],
            );

            // http://php.net/manual/fr/function.array-push.php
            array_push($posts,$post);
        }

        /* store results in a CSV File */
        foreach ($posts as $fields) {
            fputs($fp, json_encode($fields).PHP_EOL);
        }

        $graphEdge = $fb->next($graphEdge);
        print($i++);
    }

    echo "nombre de pages traitées".$i;
    fclose($fp);

} catch(Facebook\Exceptions\FacebookResponseException $e) {
    // When Graph returns an error
    echo 'Graph returned an error: ' . $e->getMessage();
    exit;
} catch(Facebook\Exceptions\FacebookSDKException $e) {
    // When validation fails or other local issues
    echo 'Facebook SDK returned an error: ' . $e->getMessage();
    exit;
}catch(Facebook\Exceptions\FacebookAuthenticationException $e) {
    // When token is invalidate ( duration 1 hour)
    echo 'Facebook SDK returned an error: ' . $e->getMessage();
    fclose($fp);
    echo "nombre de pages traitées".$i;
    exit;
}

?>