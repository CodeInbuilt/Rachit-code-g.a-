<?php

$host = "localhost";
$username = "root";
$password = "";
$database = "billing_system";

$conn = new mysqli($host, $username, $password, $database);

if ($conn->connect_error) {
    die("Failed to connect to DB: " . $conn->connect_error);
}

if (isset($_POST['sub'])) {
    $CName = $_POST['CName'];
    $Bno = $_POST['bill'];
    $Add = $_POST['Add'];
    $Bdate = $_POST['bdate'];
    $City = $_POST['cty'];
    $PName = $_POST['PName'];
    $Qty= $_POST['qty'];
    $Rate = $_POST['rate'];
    $Amt = $Qty * $Rate;
    $Total = $Amt;


        $Gst = $_POST['FGst'];
    $NAmt = $Total + ($Total * $Gst / 100);

        $insertQuery = "INSERT INTO dat (Customer, Bill, Adres, BDate, City, Product, Qty, Rate, Amt, Total, Gst, NAmt) 
                        VALUES ('$CName', '$Bno', '$Add', '$Bdate', '$City', '$PName', '$Qty', '$Rate', '$Amt', '$Total', '$Gst', '$NAmt')";

        $run = mysqli_query($conn, $insertQuery);

        if (!$run) {
            echo "Error: " . $insertQuery . "<br>" . $conn->error;
        }
    }

    echo "Data has been submitted";

?>
