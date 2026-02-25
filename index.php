

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Billing_System_Application</title>
    <!-- For Bootstrap-->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet">

    <!-- jQuery CDN -->
    <script src="https://code.jquery.com/jquery-3.6.2.slim.js"></script>

    <!--For Css-->
    <link rel="stylesheet" href="style.css">


</head>

<body>


    <div class="d-flex justify-content-between ">
     <!-- Logo -->
    
     <img src="logo.png" alt="Your Logo" class="img-fluid" style="height: 55px; width: 70px;">

    <!-- Protofolio Link -->
    <h1 >Billing System Application</h1>

    <span  id="date-time"></span>
   
    <a href="your_protofolio_link_here"  target="_blank">About Developer</a>
    </div>
   
    <form method="POST" action="ct.php">

    <div class="container ">


        <div class="card">
            <div class="card-body ">

                <div class="row">
                    <div class="col-md-8">
                        <div class="input-group mb-3">
                            <span class="input-group-text dark">Customer Name</span>
                            <input type="text" class="form-control" placeholder="Customer Name" name="CName">
                            
                        </div>

                        <div class="input-group mb-3">
                            <span class="input-group-text dark">Address</span>
                            <input type="text" class="form-control " placeholder="Address" name="Add">
                        </div>

                        <div class="input-group mb-3">
                            <span class="input-group-text dark">City</span>
                            <input type="text" class="form-control" placeholder="City" name="cty">
                        </div>
                    </div>
                    <div class="col-md-4">

                        <div class="input-group mb-3">
                            <span class="input-group-text dark">Bill. No</span>
                            <input type="text" class="form-control" placeholder="Bill. No" name="bill">
                        </div>

                        <div class="input-group mb-3">
                            <span class="input-group-text dark">Bill. Date</span>
                            <input type="datetime-local" class="form-control" id="date-time" placeholder="Bill. Date" name="bdate">
                        </div>
                    </div>
                </div>
                <div class="">
                <table class="table table-bordered">
                    <thead class="table-success">

                        <tr>
                            <th scope="col">S.No.</th>
                            <th scope="col" class="text-center">Product Name</th>
                            <th scope="col" class="text-center">Qty</th>
                            <th scope="col" class="text-center">Rate</th>
                            <th scope="col" class="text-center">Amount</th>
                            <th scope="col" class="NoPrint">
                                <button type="button" class="btn btn-sm btn-warning" onclick="BtnAdd()">Add</button>

                            </th>

                        </tr>
                    </thead>
                    <tbody id="TBody">
                        <tr id="TRow" class="d-none">
                            <th scope="row" class="color text-center">1.</th>
                            <td><input type="text" class="form-control text-center" name="PName"></td>
                            <td><input type="number" class="form-control text-center" name="qty"
                                    onchange="Calc(this);">
                            </td>
                            <td><input type="number" class="form-control text-center" name="rate"
                                    onchange="Calc(this);">
                            </td>
                            <td><input type="number" class="form-control text-center" name="amt" value="0"
                                    disabled="">
                            </td>
                            <td class="NoPrint"><button type="button" class="btn btn-sm btn-danger"
                                    onclick="BtnDel(this)">Delete</button></td>
                        </tr>
                    </tbody>
                </table>
                </div>

                <div class="row">
                    <div class="col-md-8 mb-3">

                        <button type="button" class="btn btn-success" onclick="GetPrint()">Print</button>

                        <button type="button" class="btn btn-danger reset" onclick="clearInputs()">All Clear</button>

                        <button type="submit" class="btn btn-success" name="sub" value="submit">Submit</button>

                    </div>

                    <div class="col-md-4 ">
                        <div class="input-group mb-3">
                            <span class="input-group-text dark">Total</span>
                            <input type="number" class="form-control text-end" id="FTotal" name="FTotal"
                                disabled="">
                        </div>
                        <div class="input-group mb-3">
                            <span class="input-group-text dark">GST</span>
                            <input type="number" class="form-control text-end" id="FGST" name="FGst"
                                onchange="GetTotal()" placeholder="%">
                        </div>
                        <div class="input-group mb-3">
                            <span class="input-group-text dark">Net Amt</span>
                            <input type="number" class="form-control text-end " id="FNet" name="FNet" disabled="">
                        </div>


                    </div>
                </div>
            </div>
        </div>
    </div>
    </form>
    <!-- For Invoice  -->
    <script src="bill.js"></script>


</body>

</html>