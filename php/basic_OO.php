<?php

include('user.php');

$user1 = new Member('Rodolfo', 'Padilla_r95@Rocketmail.com', 'Sep 6');
echo $user1->getType();

$user2 = new Admin('Nick', 'fssa@gmail.com', 2);
echo $user2->getType();
