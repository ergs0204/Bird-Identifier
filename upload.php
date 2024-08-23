
<?php
if(isset($_FILES['file'])){
        $file =$_FILES['file'];
        //print_r($file);
        $fileName= $_FILES['file']['name'];
        $fileext=strtolower(end(explode('.',$_FILES['file']['name'])));

        $allowed= array('jpg','jpeg','png','jfif');
        if(in_array($fileext,$allowed)){
                if($_FILES['file']['error']===0){
                        if($_FILES['file']['size']<1000000){
                                $filenewname=uniqid('',true).".".$fileext;
                                $filedes='uploads/'.$filenewname;
                                move_uploaded_file($_FILES['file']['tmp_name'],$filedes);
				//echo "<br>upload success</br>";
				$command="python3 predict.py ".$filedes;
				//echo "<br>".$filedes."</br>";
				//print("<br>".$command."</br>");
				//exec("python3 num.py",$output1);
				//echo "<br>The random number is ".$output1[0]."</br>";
				exec("python3 predict.py ".$filedes,$output2);
				echo "<br>Prediction : ".$output2[2]."</br>";
				if(count($output2)===4){
					echo "<br>相似度 : ".$output2[3]."%</br>";}
                                unlink($filedes);
				//header("Location: birds/".end($output2).".html");
                        }else{echo "The file was too big";}
                }else{echo "An error occur";}
        }else{echo "Only image is avliable.";}




}
?>
