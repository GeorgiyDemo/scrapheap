<?php 

   $sec = "5";
   $host = "redis";
   $pwd = "pwd";

   $page = $_SERVER['PHP_SELF'];

   $redis = new Redis(); 
   $redis->connect($host, 6379); 
   $redis->auth($pwd);
   $redis->select(6);
   $redis_keys = $redis->keys("*"); 
   
   print('<html>
   <head>
   <meta http-equiv="refresh" content="'.$sec.'";URL='.$page.'">
   <link rel="stylesheet" href="./bootstrap.min.css"/>
   </head>
   <body>
   <table class="table">
   <thead>
     <tr>
       <th scope="col">Номер заказа</th>
       <th scope="col">Напиток</th>
     </tr>
   </thead>
   <tbody>
   </body>
   </html>');

   #Для каждого ключа в таблице 6 Redis получаем значение и ключ
   foreach ($redis_keys as $key){ 
        $value = $redis->get($key);
        print('<tr>
        <td>'.$key.'</td>
        <td>'.$value.'</td>
      </tr>');
    } 

    print('</tbody>
    </table>')

?>

